---
layout: paper_detail
title: "Learning-driven Physically-aware Large-scale Circuit Gate Sizing"
date: 2024-03-13
arxiv_url: http://arxiv.org/abs/2403.08193v1
---

Gate sizing plays an important role in timing optimization after physical design. Existing machine learning-based gate sizing works cannot optimize timing on multiple timing paths simultaneously and neglect the physical constraint on layouts. They cause sub-optimal sizing solutions and low-efficiency issues when compared with commercial gate sizing tools. In this work, we propose a learning-driven physically-aware gate sizing framework to optimize timing performance on large-scale circuits efficiently. In our gradient descent optimization-based work, for obtaining accurate gradients, a multi-modal gate sizing-aware timing model is achieved via learning timing information on multiple timing paths and physical information on multiple-scaled layouts jointly. Then, gradient generation based on the sizing-oriented estimator and adaptive back-propagation are developed to update gate sizes. Our results demonstrate that our work achieves higher timing performance improvements in a faster way compared with the commercial gate sizing tool.
