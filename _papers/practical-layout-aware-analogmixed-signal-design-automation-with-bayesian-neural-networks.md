---
layout: paper_detail
title: "Practical Layout-Aware Analog/Mixed-Signal Design Automation with Bayesian Neural Networks"
date: 2023-11-27
arxiv_url: http://arxiv.org/abs/2311.17073v1
---

The high simulation cost has been a bottleneck of practical analog/mixed-signal design automation. Many learning-based algorithms require thousands of simulated data points, which is impractical for expensive to simulate circuits. We propose a learning-based algorithm that can be trained using a small amount of data and, therefore, scalable to tasks with expensive simulations. Our efficient algorithm solves the post-layout performance optimization problem where simulations are known to be expensive. Our comprehensive study also solves the schematic-level sizing problem. For efficient optimization, we utilize Bayesian Neural Networks as a regression model to approximate circuit performance. For layout-aware optimization, we handle the problem as a multi-fidelity optimization problem and improve efficiency by exploiting the correlations from cheaper evaluations. We present three test cases to demonstrate the efficiency of our algorithms. Our tests prove that the proposed approach is more efficient than conventional baselines and state-of-the-art algorithms.
