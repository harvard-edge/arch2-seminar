---
layout: paper_detail
title: "ASCENT: Amplifying Power Side-Channel Resilience via Learning & Monte-Carlo Tree Search"
date: 2024-06-27
arxiv_url: http://arxiv.org/abs/2406.19549v2
---

Power side-channel (PSC) analysis is pivotal for securing cryptographic hardware. Prior art focused on securing gate-level netlists obtained as-is from chip design automation, neglecting all the complexities and potential side-effects for security arising from the design automation process. That is, automation traditionally prioritizes power, performance, and area (PPA), sidelining security. We propose a "security-first" approach, refining the logic synthesis stage to enhance the overall resilience of PSC countermeasures. We introduce ASCENT, a learning-and-search-based framework that (i) drastically reduces the time for post-design PSC evaluation and (ii) explores the security-vs-PPA design space. Thus, ASCENT enables an efficient exploration of a large number of candidate netlists, leading to an improvement in PSC resilience compared to regular PPA-optimized netlists. ASCENT is up to 120x faster than traditional PSC analysis and yields a 3.11x improvement for PSC resilience of state-of-the-art PSC countermeasures
