---
layout: default
meta-description: "Seminar series on AI×Systems."
---

<div markdown="1">
<div class="slogan">Discussing the Future of Computer Architecture</div>

## About

With the rapid rise of large language models and generative AI, modern computer systems are facing unprecedented challenges and opportunities. The scale and complexity of today’s computing workloads—from cloud infrastructures to edge devices—are pushing existing design methodologies to their limits.

This is what we call Architecture 2.0: a new paradigm where machine learning is used not just as a workload, but as a tool for designing, optimizing, and even generating computer systems themselves. From learned heuristics to fully automated design loops, AI is beginning to reshape the entire hardware-software co-design stack.

We want to bring the community together to discuss the future of computer systems and architecture. We plan for each seminar to last one hour and take place every two weeks. Each session will include a 20-minute invited speaker talk, followed by a 10-minute Q&A session, and the remaining time will be used for open discussion.

### Topics we'll cover include:

- AI-driven system architecture design, verification and performance optimization
- AI algorithms tailored for hardware design and AI model self-improvement
- Ensuring reliability and validation of ML-driven systems
- Industry perspectives on needs and practical deployments
- Building academic infrastructure for the {{ site.archsys_name }} community: datasets, benchmarks, opensource tools
</div>

To understand why these discussions are vital, explore these insightful pieces on Architecture 2.0: the [blog post](https://www.sigarch.org/architecture-2-0-why-computer-architects-need-a-data-centric-ai-gymnasium/) and [this related paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10857820).

<div class="card" style="margin: 2em 0; padding: 1em; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9; text-align: center;">
    <h3 style="margin-top: 0;">Have a topic idea or want to be a speaker?</h3>
    <p>We are always looking for new ideas and speakers for our seminar series. <br>Let us know what you'd like to hear about or apply to be a speaker!</p>
    <a href="https://docs.google.com/forms/d/e/1FAIpQLSf2Y9h-B74eIiRfFhDxnWPgSVlou_4uXULEAczkBjGhsXfI6A/viewform?usp=dialog" class="btn btn-primary" style="margin-right: 1em;">Suggest a Topic</a>
    <a href="https://docs.google.com/forms/d/e/1FAIpQLSeCBYzO0PSNhpRnuy7MpR4zJ8MtW2zIqGU-8-TQF0PWGpnBCA/viewform?usp=dialog" class="btn btn-secondary">Become a Speaker</a>
</div>

<div markdown="1" id="community-papers">
## Community Papers
</div>
<p>We have a collection of {{ site.papers | size }} papers from the community. <a href="{{ site.baseurl }}/community/">View all papers</a>.</p>
<input type="text" id="paper-search-home" placeholder="Search papers by title or abstract...">
<div class="talk-list" id="home-papers-list">
  {% assign sorted_papers = site.data.tagged_papers | sort: 'published' | reverse %}
  {% for paper in sorted_papers %}
    <div class="talk list-group-item paper-item-home" data-date="{{ paper.published }}">
      <div class="paper-title">
        {{ paper.title }}
        {% if paper.highlight %}
          <span class="badge bg-success">High-rated paper</span>
        {% endif %}
      </div>
      <div>
        <a class="talk-title-link" href="{{ paper.url }}">Details <i class="bi bi-box-arrow-up-right"></i></a>
        <span class="like-widget" data-paper-id="{{ paper.title | slugify }}">
          <button class="like-button"><i class="bi bi-heart"></i></button>
          <span class="likes-count">0</span>
        </span>
      </div>
      <details>
        <summary>Abstract</summary>
        {{ paper.abstract | strip_html | truncatewords: 50 }}
      </details>
    </div>
  {% endfor %}
</div>


<!-- The rest of the page content remains unchanged -->
<!-- -------------------------------------------------- -->

{% for category in site.data.talks_229s %}
### {{ category.type }}
<div class="talk-list">
  {% for talk in category.members %}
  <div class="talk list-group-item">
  <div class="talk-date">{{ talk.date }}</div>
  <div class="talk-presenter">{{ talk.speaker }}{% if talk.affiliation %} ({{ talk.affiliation }}){% endif %}</div>
  {% if talk.title %}
  <div>
    {% if talk.recording %}
      <span><a class="talk-title-link" href="{{ talk.recording }}">{{ talk.title }} <i class="bi bi-box-arrow-up-right"></i></a></span>
    {% elsif talk.livestream %}
      <span><a class="talk-title-link" href="{{ talk.livestream }}">{{ talk.title }} <i class="bi bi-box-arrow-up-right"></i></a></span>
    {% else %}
      <span>{{ talk.title }}</span>
    {% endif %}
  </div>
  {% endif %}
  {% if talk.abstract %}
    <details>
    <summary>Abstract</summary>
    {{ talk.abstract }}
    
    {% if talk.bio %}
    <br><br>
    <strong>Bio: </strong> {{ talk.bio }}
    {% endif %}

    {% if talk.recording %}
      <br><br>
      <strong><a href="{{ talk.recording }}">Video Link</a></strong>
    {% elsif talk.livestream %}
      <br><br>
      <strong><a href="{{ talk.livestream }}">Livestream Link</a></strong>
    {% endif %}
    </details>
  {% endif %}
  </div>
  {% endfor %}
</div>
{% endfor %}

<!-- Read our blog post on our [why we're running this seminar]({{ site.baseurl }}/about). -->

{% for category in site.data.talks %}
## {{ category.type }}
<div class="talk-list">
  {% for talk in category.members %}
  <div class="talk list-group-item">
  <div class="talk-date">{{ talk.date }}</div>
  <div class="talk-presenter">{{ talk.speaker }}{% if talk.affiliation %} ({{ talk.affiliation }}){% endif %}</div>
  {% if talk.title %}
  <div>
    {% if talk.recording %}
      <span><a class="talk-title-link" href="{{ talk.recording }}">{{ talk.title }} <i class="bi bi-box-arrow-up-right"></i></a></span>
    {% elsif talk.livestream %}
      <span><a class="talk-title-link" href="{{ talk.livestream }}">{{ talk.title }} <i class="bi bi-box-arrow-up-right"></i></a></span>
    {% else %}
      <span>{{ talk.title }}</span>
    {% endif %}
  </div>
  {% endif %}
  {% if talk.abstract %}
    <details>
    <summary>Abstract</summary>
    {{ talk.abstract }}
    
    {% if talk.bio %}
    <br><br>
    <strong>Bio: </strong> {{ talk.bio }}
    {% endif %}

    {% if talk.recording %}
      <br><br>
      <strong><a href="{{ talk.recording }}">Video Link</a></strong>
    {% elsif talk.livestream %}
      <br><br>
      <strong><a href="{{ talk.livestream }}">Livestream Link</a></strong>
    {% endif %}
    </details>
  {% endif %}
  </div>
  {% endfor %}
</div>
{% endfor %}

{% for category in site.data.past_talks %}
## {{ category.type }}
<div class="talk-list">
  {% for talk in category.members %}
  <div class="talk list-group-item">
  <div class="talk-date">{{ talk.date }}</div>
  <div class="talk-presenter">{{ talk.speaker }}{% if talk.affiliation %} ({{ talk.affiliation }}){% endif %}</div>
  {% if talk.title %}
  <div>
    {% if talk.recording %}
      <span><a class="talk-title-link" href="{{ talk.recording }}">{{ talk.title }} <i class="bi bi-box-arrow-up-right"></i></a></span>
    {% elsif talk.livestream %}
      <span><a class="talk-title-link" href="{{ talk.livestream }}">{{ talk.title }} <i class="bi bi-box-arrow-up-right"></i></a></span>
    {% else %}
      <span>{{ talk.title }}</span>
    {% endif %}
  </div>
  {% endif %}
  {% if talk.abstract %}
    <details>
    <summary>Abstract</summary>
    {{ talk.abstract }}
    
    {% if talk.bio %}
    <br><br>
    <strong>Bio: </strong> {{ talk.bio }}
    {% endif %}

    {% if talk.recording %}
      <br><br>
      <strong><a href="{{ talk.recording }}">Video Link</a></strong>
    {% elsif talk.livestream %}
      <br><br>
      <strong><a href="{{ talk.livestream }}">Livestream Link</a></strong>
    {% endif %}
    </details>
  {% endif %}
  </div>
  {% endfor %}
</div>
{% endfor %}

<small>Website template adapted from the <a href="https://github.com/stanford-sysml-seminar/stanford-sysml-seminar.github.io">Stanford SysML Seminar</a> site, and enhanced by <a href="https://www.cursor.sh">Cursor</a>.</small>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('paper-search-home');
    const papersList = document.getElementById('home-papers-list');
    const allPaperElements = Array.from(papersList.getElementsByClassName('paper-item-home'));

    function filterPapers() {
        const searchTerm = searchInput.value.toLowerCase();
        
        allPaperElements.forEach(el => {
            const title = el.querySelector('.paper-title').textContent.toLowerCase();
            const abstract = el.querySelector('details').textContent.toLowerCase();
            const isVisible = title.includes(searchTerm) || abstract.includes(searchTerm);
            el.style.display = isVisible ? 'block' : 'none';
        });
    }

    searchInput.addEventListener('input', filterPapers);

    // --- Like functionality ---

    const API_GATEWAY_URL = 'https://your-api-gateway-url.execute-api.us-east-1.amazonaws.com/prod'; // Placeholder
    const WEBSOCKET_URL = 'wss://your-websocket-url.execute-api.us-east-1.amazonaws.com/prod'; // Placeholder

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

    async function fetchLikes(paperId) {
        // MOCK: In a real implementation, this would fetch from the backend.
        // const response = await fetch(`${API_GATEWAY_URL}/papers/${paperId}/likes`);
        // const data = await response.json();
        // return data.likes;
        return 0;
    }

    async function postLike(paperId) {
        // MOCK: In a real implementation, this would post to the backend.
        // const response = await fetch(`${API_GATEWAY_URL}/papers/${paperId}/like`, { method: 'POST' });
        // const data = await response.json();
        // return data.likes;
        const countEl = document.querySelector(`.like-widget[data-paper-id="${paperId}"] .likes-count`);
        const currentLikes = parseInt(countEl.textContent, 10);
        return currentLikes + 1;
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

    document.querySelectorAll('.like-widget').forEach(async (widget) => {
        const paperId = widget.dataset.paperId;
        const button = widget.querySelector('.like-button');
        const countEl = widget.querySelector('.likes-count');

        const initialLikes = await fetchLikes(paperId);
        countEl.textContent = initialLikes;
        
        updateLikeButtonUI(button, paperId);

        button.addEventListener('click', async () => {
            if (isPaperLiked(paperId)) {
                console.log('Already liked:', paperId);
                return;
            }
            
            const newLikes = await postLike(paperId);
            countEl.textContent = newLikes;
            setPaperLiked(paperId);
            updateLikeButtonUI(button, paperId);
        });
    });

    // Mock WebSocket for real-time updates
    function connectWebSocket() {
        // In a real implementation, you would connect to your WebSocket endpoint:
        // const socket = new WebSocket(WEBSOCKET_URL);
        // socket.onmessage = function(event) {
        //     const data = JSON.parse(event.data);
        //     if (data.paperId && data.likes) {
        //         const countEl = document.querySelector(`.like-widget[data-paper-id="${data.paperId}"] .likes-count`);
        //         if (countEl) {
        //             countEl.textContent = data.likes;
        //         }
        //     }
        // };

        // This is a mock to simulate another user liking a paper every few seconds
        setInterval(() => {
            const allWidgets = Array.from(document.querySelectorAll('.like-widget'));
            if (allWidgets.length === 0) return;
            
            const randomWidget = allWidgets[Math.floor(Math.random() * allWidgets.length)];
            const countEl = randomWidget.querySelector('.likes-count');
            
            const currentLikes = parseInt(countEl.textContent, 10);
            countEl.textContent = currentLikes + 1;
        }, 5000);
    }
    
    connectWebSocket();
});
</script>

<style>
#home-papers-list {
  max-height: 400px;
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
#paper-search-home {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    font-size: 1em;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
}
</style>
