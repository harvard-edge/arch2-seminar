---
layout: paper_detail
title: "ForgeHLS: A Large-Scale, Open-Source Dataset for High-Level Synthesis"
date: 2025-07-04
arxiv_url: http://arxiv.org/abs/2507.03255v2
---

High-Level Synthesis (HLS) plays a crucial role in modern hardware design by transforming high-level code into optimized hardware implementations. However, progress in applying machine learning (ML) to HLS optimization has been hindered by a shortage of sufficiently large and diverse datasets. To bridge this gap, we introduce ForgeHLS, a large-scale, open-source dataset explicitly designed for ML-driven HLS research. ForgeHLS comprises over 400,000 diverse designs generated from 536 kernels covering a broad range of application domains. Each kernel includes systematically automated pragma insertions (loop unrolling, pipelining, array partitioning), combined with extensive design space exploration using Bayesian optimization. Compared to existing datasets, ForgeHLS significantly enhances scale, diversity, and design coverage. We further define and evaluate representative downstream tasks, such as Quality of Result (QoR) prediction and automated pragma exploration, clearly demonstrating ForgeHLS's utility for developing and improving ML-based HLS optimization methodologies.
