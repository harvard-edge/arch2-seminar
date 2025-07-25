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
.likes-count {
  margin-left: 10px;
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
