---
layout: paper_detail
title: "IR-Aware ECO Timing Optimization Using Reinforcement Learning"
date: 2024-02-12
arxiv_url: http://arxiv.org/abs/2402.07781v2
---

Engineering change orders (ECOs) in late stages make minimal design fixes to recover from timing shifts due to excessive IR drops. This paper integrates IR-drop-aware timing analysis and ECO timing optimization using reinforcement learning (RL). The method operates after physical design and power grid synthesis, and rectifies IR-drop-induced timing degradation through gate sizing. It incorporates the Lagrangian relaxation (LR) technique into a novel RL framework, which trains a relational graph convolutional network (R-GCN) agent to sequentially size gates to fix timing violations. The R-GCN agent outperforms a classical LR-only algorithm: in an open 45nm technology, it (a) moves the Pareto front of the delay-power tradeoff curve to the left (b) saves runtime over the prior approaches by running fast inference using trained models, and (c) reduces the perturbation to placement by sizing fewer cells. The RL model is transferable across timing specifications and to unseen designs with fine tuning.
