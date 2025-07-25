---
layout: paper_detail
title: "Deep Inverse Design for High-Level Synthesis"
date: 2024-07-11
arxiv_url: http://arxiv.org/abs/2407.08797v3
---

High-level synthesis (HLS) has significantly advanced the automation of digital circuits design, yet the need for expertise and time in pragma tuning remains challenging. Existing solutions for the design space exploration (DSE) adopt either heuristic methods, lacking essential information for further optimization potential, or predictive models, missing sufficient generalization due to the time-consuming nature of HLS and the exponential growth of the design space. To address these challenges, we propose Deep Inverse Design for HLS (DID4HLS), a novel approach that integrates graph neural networks and generative models. DID4HLS iteratively optimizes hardware designs aimed at compute-intensive algorithms by learning conditional distributions of design features from post-HLS data. Compared to four state-of-the-art DSE baselines, our method achieved an average improvement of 42.8% on average distance to reference set (ADRS) compared to the best-performing baselines across six benchmarks, while demonstrating high robustness and efficiency. The code is available at https://github.com/PingChang818/DID4HLS.
