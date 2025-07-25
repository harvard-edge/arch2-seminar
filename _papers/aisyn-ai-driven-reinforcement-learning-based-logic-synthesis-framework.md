---
layout: paper_detail
title: "AISYN: AI-driven Reinforcement Learning-Based Logic Synthesis Framework"
date: 2023-02-08
arxiv_url: http://arxiv.org/abs/2302.06415v1
---

Logic synthesis is one of the most important steps in design and implementation of digital chips with a big impact on final Quality of Results (QoR). For a most general input circuit modeled by a Directed Acyclic Graph (DAG), many logic synthesis problems such as delay or area minimization are NP-Complete, hence, no optimal solution is available. This is why many classical logic optimization functions tend to follow greedy approaches that are easily trapped in local minima that does not allow improving QoR as much as needed. We believe that Artificial Intelligence (AI) and more specifically Reinforcement Learning (RL) algorithms can help in solving this problem. This is because AI and RL can help minimizing QoR further by exiting from local minima. Our experiments on both open source and industrial benchmark circuits show that significant improvements on important metrics such as area, delay, and power can be achieved by making logic synthesis optimization functions AI-driven. For example, our RL-based rewriting algorithm could improve total cell area post-synthesis by up to 69.3% when compared to a classical rewriting algorithm with no AI awareness.
