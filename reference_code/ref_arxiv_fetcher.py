import arxiv
import json
import os
import re
import requests
import argparse
from datetime import datetime, timezone

# --- Configuration ---
# Query terms: require "LLM" plus at least one hardware-related term.
# Using explicit `all:` field specifiers matches what the web UI does when you simply type the words.
# DEFAULT_QUERY = 'all:LLM AND (all:"hardware design" OR all:hardware OR all:EDA OR all:chip OR all:FPGA OR all:ASIC OR all:VLSI)'

DEFAULT_QUERY = 'all:LLM AND (all:"chip design" OR all:chip OR all:EDA)'

# Default behaviours (overridden via CLI)
DEFAULT_MAX_NEW = 10        # default to fetch 10 new papers; set 0 to fetch all
DEFAULT_MAX_AGE_DAYS = 1000  # only keep papers within past year; 0 to disable

# When max is specified (non-zero), we fetch in excess to allow filtering.
API_FETCH_MULTIPLIER = 8

PAPER_DOWNLOAD_DIR = "downloaded_papers"
DATABASE_FILE = "processed_articles.json"
LLM_KEYWORDS = [
    'llm', 'large language model', 'language model', 'gpt', 'bert', 'transformer'
]
HARDWARE_KEYWORDS = [
    'hardware design', 'hardware', 'chip', 'eda', 'vlsi', 'fpga', 'asic',
    'circuit', 'rtl', 'verilog', 'silicon', 'architecture'
]
# --- End Configuration ---

def load_processed_articles(db_file=DATABASE_FILE):
    """Loads the set of processed article IDs from the database file."""
    if os.path.exists(db_file):
        try:
            with open(db_file, 'r') as f:
                return set(json.load(f))
        except json.JSONDecodeError:
            print(f"Warning: Database file {db_file} is corrupted. Starting with an empty database.")
            return set()
    return set()

def save_processed_articles(processed_ids, db_file=DATABASE_FILE):
    """Saves the set of processed article IDs to the database file."""
    with open(db_file, 'w') as f:
        json.dump(list(processed_ids), f, indent=4)

def sanitize_filename(title):
    """Sanitizes a string to be a valid filename."""
    title = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', title)  # Remove/replace invalid characters
    title = re.sub(r'\s+', ' ', title).strip() # Normalize whitespace
    return title[:200]  # Limit length to avoid issues with long filenames

def download_pdf(paper, download_dir):
    """Downloads the PDF for a given paper."""
    pdf_url = paper.pdf_url
    if not pdf_url:
        print(f"No PDF URL found for '{paper.title}'. Skipping.")
        return None

    # Ensure .pdf extension if not present
    if not pdf_url.endswith('.pdf'):
        pdf_url += '.pdf' 

    sanitized_title = sanitize_filename(paper.title)
    filename = os.path.join(download_dir, f"{sanitized_title}.pdf")

    try:
        print(f"Downloading: '{paper.title}' from {pdf_url}")
        response = requests.get(pdf_url, stream=True, timeout=30) # Added timeout
        response.raise_for_status()  # Raise an exception for bad status codes
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded to '{filename}'")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Error downloading '{paper.title}' from {pdf_url}. Error: {e}")
        if os.path.exists(filename): # Clean up partially downloaded file
            os.remove(filename)
        return None
    except Exception as e:
        print(f"An unexpected error occurred while downloading '{paper.title}'. Error: {e}")
        if os.path.exists(filename): # Clean up partially downloaded file
            os.remove(filename)
        return None

def is_relevant(paper):
    """Checks whether a paper is relevant (mentions at least one LLM keyword *and* one hardware keyword)."""
    text = f"{paper.title} {paper.summary}".lower()
    has_llm = any(k in text for k in LLM_KEYWORDS)
    has_hw  = any(k in text for k in HARDWARE_KEYWORDS)
    return has_llm and has_hw

def parse_args():
    parser = argparse.ArgumentParser(description="Download LLM-for-Hardware papers from arXiv.")
    parser.add_argument("--query", default=DEFAULT_QUERY, help="arXiv query string")
    parser.add_argument("--max", type=int, default=DEFAULT_MAX_NEW, help="Maximum number of NEW papers to download this run (0 = no limit / download all)")
    parser.add_argument("--max_age_days", type=int, default=DEFAULT_MAX_AGE_DAYS, help="Only consider papers published in the last N days (0 = no limit)")
    parser.add_argument("--fetch_limit", type=int, default=None, help="Override the internal max_results sent to arXiv (advanced usage)")
    return parser.parse_args()

def main():
    """Main function to search arXiv, download new papers, and update the database."""
    args = parse_args()

    # Ensure download directory exists
    if not os.path.exists(PAPER_DOWNLOAD_DIR):
        os.makedirs(PAPER_DOWNLOAD_DIR)
        print(f"Created directory: {PAPER_DOWNLOAD_DIR}")

    processed_article_ids = load_processed_articles()
    print(f"Loaded {len(processed_article_ids)} processed article IDs from database.")

    print(
        f"Searching arXiv for '{args.query}' (max_new={args.max if args.max else 'ALL'}, max_age_days={args.max_age_days})..."
    )

    # Decide how many to fetch from API (upper bound)
    if args.fetch_limit is not None:
        api_limit = args.fetch_limit
    else:
        if args.max:
            api_limit = args.max * API_FETCH_MULTIPLIER
        else:
            api_limit = 5000  # arbitrary large number; change if needed

    search = arxiv.Search(
        query=args.query,
        max_results=api_limit,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    try:
        results_iter = search.results()
    except Exception as e:
        print(f"Error during arXiv search: {e}")
        return

    new_papers_found = 0
    downloaded_this_session = 0

    for paper in results_iter:
        # Respect --max (0 = unlimited)
        if args.max and downloaded_this_session >= args.max:
            break

        # Filter by recency
        if args.max_age_days and (datetime.now(timezone.utc) - paper.published).days > args.max_age_days:
            continue  # too old

        # Ensure relevance (LLM & hardware)
        if not is_relevant(paper):
            continue

        article_id = paper.entry_id.split('/')[-1] # Use the short ID (e.g., 2303.10130v1 -> 2303.10130)
        # Sometimes IDs have version numbers (e.g., v1, v2). We consider the base ID.
        base_article_id = article_id.split('v')[0]

        if base_article_id not in processed_article_ids:
            print(f"\nFound new paper: '{paper.title}' (ID: {base_article_id})")
            pdf_filepath = download_pdf(paper, PAPER_DOWNLOAD_DIR)
            if pdf_filepath:
                processed_article_ids.add(base_article_id)
                save_processed_articles(processed_article_ids)
                downloaded_this_session += 1
                new_papers_found +=1 # This was missing
            else:
                print(f"Failed to download or skipped PDF for '{paper.title}'. It will not be marked as processed.")
            
            # If we hit the requested max, stop further processing
            if args.max and downloaded_this_session >= args.max:
                print(f"\nReached the target of {args.max} new papers for this session.")
                break
        else:
            print(f"Paper '{paper.title}' (ID: {base_article_id}) already processed. Skipping.")

    print(f"\n--- Session Summary ---")
    if new_papers_found > 0:
        print(f"Successfully downloaded {new_papers_found} new paper(s).")
    else:
        print("No new papers were found in this session.")

    if args.max and new_papers_found < args.max and new_papers_found > 0:
        print(f"Note: Only {new_papers_found} new papers found (requested {args.max}).")

if __name__ == "__main__":
    main() 