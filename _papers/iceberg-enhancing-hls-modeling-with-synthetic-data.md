---
layout: paper_detail
title: "Iceberg: Enhancing HLS Modeling with Synthetic Data"
date: 2025-07-14
arxiv_url: http://arxiv.org/abs/2507.09948v2
---

Deep learning-based prediction models for High-Level Synthesis (HLS) of hardware designs often struggle to generalize. In this paper, we study how to close the generalizability gap of these models through pretraining on synthetic data and introduce Iceberg, a synthetic data augmentation approach that expands both large language model (LLM)-generated programs and weak labels of unseen design configurations. Our weak label generation method is integrated with an in-context model architecture, enabling meta-learning from actual and proximate labels. Iceberg improves the geometric mean modeling accuracy by $86.4\%$ when adapt to six real-world applications with few-shot examples and achieves a $2.47\times$ and a $1.12\times$ better offline DSE performance when adapting to two different test datasets. Our open-sourced code is here: https://github.com/UCLA-VAST/iceberg
