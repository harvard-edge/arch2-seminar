---
layout: paper_detail
title: "ML-based AIG Timing Prediction to Enhance Logic Optimization"
date: 2024-12-03
arxiv_url: http://arxiv.org/abs/2412.02268v1
---

As circuit designs become more intricate, obtaining accurate performance estimation in early stages, for effective design space exploration, becomes more time-consuming. Traditional logic optimization approaches often rely on proxy metrics to approximate post-mapping performance and area. However, these proxies do not always correlate well with actual post-mapping delay and area, resulting in suboptimal designs. To address this issue, we explore a ground-truth-based optimization flow that directly incorporates the exact post-mapping delay and area during optimization. While this approach improves design quality, it also significantly increases computational costs, particularly for large-scale designs. To overcome the runtime challenge, we apply machine learning models to predict post-mapping delay and area using the features extracted from AIGs. Our experimental results show that the model has high prediction accuracy with good generalization to unseen designs. Furthermore, the ML-enhanced logic optimization flow significantly reduces runtime while maintaining comparable performance and area outcomes.
