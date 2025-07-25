---
layout: paper_detail
title: "That Chip Has Sailed: A Critique of Unfounded Skepticism Around AI for Chip Design"
date: 2024-11-15
arxiv_url: http://arxiv.org/abs/2411.10053v1
---

In 2020, we introduced a deep reinforcement learning method capable of generating superhuman chip layouts, which we then published in Nature and open-sourced on GitHub. AlphaChip has inspired an explosion of work on AI for chip design, and has been deployed in state-of-the-art chips across Alphabet and extended by external chipmakers. Even so, a non-peer-reviewed invited paper at ISPD 2023 questioned its performance claims, despite failing to run our method as described in Nature. For example, it did not pre-train the RL method (removing its ability to learn from prior experience), used substantially fewer compute resources (20x fewer RL experience collectors and half as many GPUs), did not train to convergence (standard practice in machine learning), and evaluated on test cases that are not representative of modern chips. Recently, Igor Markov published a meta-analysis of three papers: our peer-reviewed Nature paper, the non-peer-reviewed ISPD paper, and Markov's own unpublished paper (though he does not disclose that he co-authored it). Although AlphaChip has already achieved widespread adoption and impact, we publish this response to ensure that no one is wrongly discouraged from innovating in this impactful area.
