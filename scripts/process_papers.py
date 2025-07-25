import json
import os
from datetime import datetime

# Function to create a slug from a title
def create_slug(title):
    return "".join(c for c in title if c.isalnum() or c in " -").rstrip().replace(" ", "-").lower()

# Load the filtered papers data
with open('_data/filter_papers.json', 'r') as f:
    papers = json.load(f)

# Create the output directory if it doesn't exist
output_dir = '_papers'
os.makedirs(output_dir, exist_ok=True)

# Process each paper
for paper in papers:
    title = paper.get('title', 'No Title').replace('"', '\\"')
    slug = create_slug(title)
    
    # Format the date
    published_date = paper.get('published')
    if published_date:
        date_obj = datetime.fromisoformat(published_date.replace('Z', '+00:00'))
        formatted_date = date_obj.strftime('%Y-%m-%d')
    else:
        formatted_date = 'N/A'

    # Create the content for the Markdown file
    content = f"""---
layout: paper_detail
title: "{title}"
date: {formatted_date}
arxiv_url: {paper.get('url', '')}
---

{paper.get('abstract', 'No abstract available.')}
"""

    # Write the content to a file
    with open(os.path.join(output_dir, f'{slug}.md'), 'w') as f:
        f.write(content)

print(f"Processed {len(papers)} papers into {output_dir}") 