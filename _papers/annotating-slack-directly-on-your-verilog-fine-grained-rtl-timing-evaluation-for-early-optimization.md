---
layout: paper_detail
title: "Annotating Slack Directly on Your Verilog: Fine-Grained RTL Timing Evaluation for Early Optimization"
date: 2024-03-27
arxiv_url: http://arxiv.org/abs/2403.18453v2
---

In digital IC design, compared with post-synthesis netlists or layouts, the early register-transfer level (RTL) stage offers greater optimization flexibility for both designers and EDA tools. However, timing information is typically unavailable at this early stage. Some recent machine learning (ML) solutions propose to predict the total negative slack (TNS) and worst negative slack (WNS) of an entire design at the RTL stage, but the fine-grained timing information of individual registers remains unavailable. In this work, we address the unique challenges of RTL timing prediction and introduce our solution named RTL-Timer. To the best of our knowledge, this is the first fine-grained general timing estimator applicable to any given design. RTL-Timer explores multiple promising RTL representations and proposes customized loss functions to capture the maximum arrival time at register endpoints. RTL-Timer's fine-grained predictions are further applied to guide optimization in a standard synthesis flow. The average results on unknown test designs demonstrate a correlation above 0.89, contributing around 3% WNS and 10% TNS improvement after optimization.
