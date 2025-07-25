---
layout: paper_detail
title: "Bayesian Optimization over Permutation Spaces"
date: 2021-12-02
arxiv_url: http://arxiv.org/abs/2112.01049v1
---

Optimizing expensive to evaluate black-box functions over an input space consisting of all permutations of d objects is an important problem with many real-world applications. For example, placement of functional blocks in hardware design to optimize performance via simulations. The overall goal is to minimize the number of function evaluations to find high-performing permutations. The key challenge in solving this problem using the Bayesian optimization (BO) framework is to trade-off the complexity of statistical model and tractability of acquisition function optimization. In this paper, we propose and evaluate two algorithms for BO over Permutation Spaces (BOPS). First, BOPS-T employs Gaussian process (GP) surrogate model with Kendall kernels and a Tractable acquisition function optimization approach based on Thompson sampling to select the sequence of permutations for evaluation. Second, BOPS-H employs GP surrogate model with Mallow kernels and a Heuristic search approach to optimize expected improvement acquisition function. We theoretically analyze the performance of BOPS-T to show that their regret grows sub-linearly. Our experiments on multiple synthetic and real-world benchmarks show that both BOPS-T and BOPS-H perform better than the state-of-the-art BO algorithm for combinatorial spaces. To drive future research on this important problem, we make new resources and real-world benchmarks available to the community.
