---
layout: default
title: Community Papers
---
<div class="community-page">
  <h1>Community Papers</h1>
  <p>Total papers: <span id="total-papers">{{ site.data.tagged_papers | size }}</span></p>

  <div id="tag-filters">
    <button class="tag-filter-btn active" data-tag="all">All Topics</button>
    {% assign all_tags_str = site.data.tagged_papers | map: "tags" | join: "," %}
    {% assign tags = all_tags_str | split: "," | uniq | sort %}
    {% for tag in tags %}
      {% if tag != "" %}
        <button class="tag-filter-btn" data-tag="{{ tag | downcase }}">{{ tag }}</button>
      {% endif %}
    {% endfor %}
  </div>

  <input type="text" id="paper-search" placeholder="Search papers by title or abstract...">

  <div class="talk-list" id="papers-list">
      {% assign papers = site.data.tagged_papers %}
      {% for paper in papers %}
        <div class="talk list-group-item paper-item" data-tags="{{ paper.tags | join: ',' | downcase }}" data-date="{{ paper.date }}">
          <div class="paper-header">
            <div class="paper-title">{{ paper.title }}</div>
            <div class="paper-tags">
              {% for tag in paper.tags %}
                <span class="paper-tag">{{ tag }}</span>
              {% endfor %}
            </div>
          </div>
          <div class="paper-date" style="display:none;">{{ paper.date | date: '%B %Y' }}</div>
          <div>
            <a class="talk-title-link" href="{{ paper.url }}">Details <i class="bi bi-box-arrow-up-right"></i></a>
            <span class="like-widget" data-paper-id="{{ paper.title | slugify }}">
              <button class="like-button"><i class="bi bi-heart"></i></button>
              <span class="likes-count">0</span>
            </span>
          </div>
          <details>
            <summary>Abstract</summary>
            <div class="paper-abstract">
              {{ paper.abstract }}
            </div>
          </details>
        </div>
      {% endfor %}
  </div>
</div>

<script src="https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/8.10.1/firebase-database.js"></script>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('paper-search');
    const papersList = document.getElementById('papers-list');
    const totalPapersSpan = document.getElementById('total-papers');
    const tagFilterButtons = document.querySelectorAll('.tag-filter-btn');

    const allPaperElements = Array.from(papersList.getElementsByClassName('paper-item'));
    const papersData = allPaperElements.map(el => {
        return {
            element: el,
            title: el.querySelector('.paper-title').textContent.toLowerCase(),
            abstract: el.querySelector('.paper-abstract').textContent.toLowerCase(),
            tags: (el.dataset.tags || '').split(','),
            date: el.dataset.date
        };
    });

    // Sort papers by date, newest first
    papersData.sort((a, b) => new Date(b.date) - new Date(a.date));

    let filteredPapers = papersData;
    let currentTag = 'all';

    function displayPapers() {
        // Filter by tag first
        let papersToShow = papersData;
        if (currentTag !== 'all') {
            papersToShow = papersData.filter(paper => paper.tags.includes(currentTag));
        }

        // Then, filter by search term
        const searchTerm = searchInput.value.toLowerCase();
        filteredPapers = papersToShow.filter(paper => {
            return paper.title.includes(searchTerm) || paper.abstract.includes(searchTerm);
        });

        totalPapersSpan.textContent = filteredPapers.length;

        // Hide all papers first
        allPaperElements.forEach(el => el.style.display = 'none');

        // Show filtered papers
        filteredPapers.forEach(paper => paper.element.style.display = 'block');
    }

    searchInput.addEventListener('input', () => {
        displayPapers();
    });

    tagFilterButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentTag = button.dataset.tag;
            
            tagFilterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            displayPapers();
        });
    });

    // Initial display - show all papers sorted by date
    allPaperElements.forEach(p => papersList.appendChild(p));
    displayPapers();

    // --- Like functionality using Firebase ---

    // =================================================================================
    // TODO: PASTE YOUR FIREBASE CONFIGURATION HERE
    //
    // 1. Go to the Firebase console (https://console.firebase.google.com/).
    // 2. Create a new project.
    // 3. In your project, create a "Realtime Database".
    //    - Start in "test mode" for now (allows public read/write).
    // 4. Go to Project Settings > General, and find your web app's configuration object.
    // 5. Paste that configuration object here.
    // =================================================================================
    const firebaseConfig = {
      apiKey: "AIzaSyC7JxyxwsOxiDI3jVSz1Du7fXVNYhKuDyM",
      authDomain: "my-awesome-seminar-likes.firebaseapp.com",
      databaseURL: "https://my-awesome-seminar-likes-default-rtdb.firebaseio.com",
      projectId: "my-awesome-seminar-likes",
      storageBucket: "my-awesome-seminar-likes.firebasestorage.app",
      messagingSenderId: "1064951229888",
      appId: "1:1064951229888:web:c8234ad6cd99df348e6c25"
    };
 
     function getLikedPapers() {
         return JSON.parse(localStorage.getItem('likedPapers') || '{}');
     }
 
     function isPaperLiked(paperId) {
         return !!getLikedPapers()[paperId];
     }
 
     function setPaperLiked(paperId) {
         const likedPapers = getLikedPapers();
         likedPapers[paperId] = true;
         localStorage.setItem('likedPapers', JSON.stringify(likedPapers));
     }
 
    function updateLikeButtonUI(button, paperId) {
        const icon = button.querySelector('i');
        if (isPaperLiked(paperId)) {
            button.classList.add('liked');
            icon.className = 'bi bi-heart-fill';
        } else {
            button.classList.remove('liked');
            icon.className = 'bi bi-heart';
        }
    }

    function initializeLikeButtons(database) {
        const likesRef = database.ref('likes');

        // This function will be called once with the initial state,
        // and then again every time the data changes.
        likesRef.on('value', (snapshot) => {
            const allLikes = snapshot.val() || {};
            document.querySelectorAll('.like-widget').forEach(widget => {
                const paperId = widget.dataset.paperId;
                const countEl = widget.querySelector('.likes-count');
                countEl.textContent = allLikes[paperId] || 0;
            });
        });

        document.querySelectorAll('.like-widget').forEach(widget => {
            const paperId = widget.dataset.paperId;
            const button = widget.querySelector('.like-button');
            const paperLikesRef = database.ref(`likes/${paperId}`);

            updateLikeButtonUI(button, paperId);

            button.addEventListener('click', () => {
                if (isPaperLiked(paperId)) {
                    console.log('Already liked:', paperId);
                    return;
                }

                // Use a transaction to safely increment the like count.
                // This prevents race conditions if multiple people like at the same time.
                paperLikesRef.transaction((currentLikes) => {
                    return (currentLikes || 0) + 1;
                }).then(() => {
                     setPaperLiked(paperId);
                     updateLikeButtonUI(button, paperId);
                });
            });
        });
    }

    // Initialize Firebase, but only if the config has been filled out.
    if (firebaseConfig.apiKey !== "YOUR_API_KEY") {
        firebase.initializeApp(firebaseConfig);
        const database = firebase.database();
        initializeLikeButtons(database);
    } else {
        console.warn("Firebase is not configured. Please add your project credentials to index.md. Like functionality will be disabled.");
        document.querySelectorAll('.like-widget').forEach(widget => widget.style.display = 'none');
    }
});
</script>

<style>
.talk-list {
  max-height: 800px; /* Or any height you prefer */
  overflow-y: auto;
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 4px;
}
.like-widget {
  display: inline-flex;
  align-items: center;
  margin-left: 1em;
  color: #dc3545;
}
.like-button {
  border: none;
  background: transparent;
  cursor: pointer;
  color: inherit;
  padding: 0 5px 0 0;
  font-size: 1.1em;
}
.like-button .bi-heart-fill {
  display: none;
}
.like-button.liked .bi-heart {
  display: none;
}
.like-button.liked .bi-heart-fill {
  display: inline-block;
}
.likes-count {
  margin-left: 0.25em;
  min-width: 1em;
  text-align: left;
}
#paper-search {
    width: 100%;
    padding: 10px;
    margin: 20px 0;
    font-size: 1em;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
}
.paper-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}
.paper-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  justify-content: flex-end;
  max-width: 30%;
}
.paper-tag {
  background-color: #eee;
  color: #333;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 0.8em;
  white-space: nowrap;
}
#tag-filters {
  margin-bottom: 20px;
  display: flex;
  flex-wrap: wrap;
}
#tag-filters .tag-filter-btn {
  margin-right: 10px;
  margin-bottom: 10px;
  padding: 8px 12px;
  cursor: pointer;
  border: 1px solid #ddd;
  background-color: #fff;
  border-radius: 16px;
}
#tag-filters .tag-filter-btn.active {
  background-color: #007bff;
  color: white;
  border-color: #007bff;
}
</style> 