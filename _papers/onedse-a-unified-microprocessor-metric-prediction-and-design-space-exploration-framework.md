---
layout: paper_detail
title: "OneDSE: A Unified Microprocessor Metric Prediction and Design Space Exploration Framework"
date: 2025-04-29
arxiv_url: http://arxiv.org/abs/2505.03771v1
---

With the diminishing returns of Moore Law scaling and as power constraints become more impactful, processor designs rely on architectural innovation to achieve differentiating performance. Innovation complexity has increased the design space of modern high-performance processors. This work offers an efficient and novel design space exploration (DSE) solution to these challenges of modern CPU design. We identify three key challenges in past DSE approaches: (a) Metric prediction is slow and inaccurate for unseen workloads, microarchitectures, (b) Search is slow and inaccurate in CPU parameter space, and (c) A Single model is unable to learn the huge design space. We present OneDSE, a unified metric predictor and CPU parameter explorer to mitigate these challenges with three key techniques: (a) Transformer-based workload-Aware CPU DSE (TrACE) predictor that outperforms state-of-the-art ANN-based prediction methods by 2.75x and 6.12x with and without fine-tuning, respectively, on several benchmarks; (b) a novel metric space search approach that outperforms optimized metaheuristics by 1.19x while reducing search time by an order of magnitude; (c) MARL-based multi-agent framework that achieves a 10.6% reduction in prediction error compared to its non-MARL counterpart, enabling more accurate and efficient exploration of the CPU design space.
