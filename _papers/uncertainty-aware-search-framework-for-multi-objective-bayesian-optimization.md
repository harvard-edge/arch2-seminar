---
layout: paper_detail
title: "Uncertainty-Aware Search Framework for Multi-Objective Bayesian Optimization"
date: 2022-04-12
arxiv_url: http://arxiv.org/abs/2204.05944v1
---

We consider the problem of multi-objective (MO) blackbox optimization using expensive function evaluations, where the goal is to approximate the true Pareto set of solutions while minimizing the number of function evaluations. For example, in hardware design optimization, we need to find the designs that trade-off performance, energy, and area overhead using expensive simulations. We propose a novel uncertainty-aware search framework referred to as USeMO to efficiently select the sequence of inputs for evaluation to solve this problem. The selection method of USeMO consists of solving a cheap MO optimization problem via surrogate models of the true functions to identify the most promising candidates and picking the best candidate based on a measure of uncertainty. We also provide theoretical analysis to characterize the efficacy of our approach. Our experiments on several synthetic and six diverse real-world benchmark problems show that USeMO consistently outperforms the state-of-the-art algorithms.
