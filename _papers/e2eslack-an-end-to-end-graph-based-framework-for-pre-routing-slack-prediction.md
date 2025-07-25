---
layout: paper_detail
title: "E2ESlack: An End-to-End Graph-Based Framework for Pre-Routing Slack Prediction"
date: 2025-01-13
arxiv_url: http://arxiv.org/abs/2501.07564v2
---

Pre-routing slack prediction remains a critical area of research in Electronic Design Automation (EDA). Despite numerous machine learning-based approaches targeting this task, there is still a lack of a truly end-to-end framework that engineers can use to obtain TNS/WNS metrics from raw circuit data at the placement stage. Existing works have demonstrated effectiveness in Arrival Time (AT) prediction but lack a mechanism for Required Arrival Time (RAT) prediction, which is essential for slack prediction and obtaining TNS/WNS metrics. In this work, we propose E2ESlack, an end-to-end graph-based framework for pre-routing slack prediction. The framework includes a TimingParser that supports DEF, SDF and LIB files for feature extraction and graph construction, an arrival time prediction model and a fast RAT estimation module. To the best of our knowledge, this is the first work capable of predicting path-level slacks at the pre-routing stage. We perform extensive experiments and demonstrate that our proposed RAT estimation method outperforms the SOTA ML-based prediction method and also pre-routing STA tool. Additionally, the proposed E2ESlack framework achieves TNS/WNS values comparable to post-routing STA results while saving up to 23x runtime.
