---
layout: paper_detail
title: "Online Adaptive Learning for Runtime Resource Management of Heterogeneous SoCs"
date: 2020-08-22
arxiv_url: http://arxiv.org/abs/2008.09728v1
---

Dynamic resource management has become one of the major areas of research in modern computer and communication system design due to lower power consumption and higher performance demands. The number of integrated cores, level of heterogeneity and amount of control knobs increase steadily. As a result, the system complexity is increasing faster than our ability to optimize and dynamically manage the resources. Moreover, offline approaches are sub-optimal due to workload variations and large volume of new applications unknown at design time. This paper first reviews recent online learning techniques for predicting system performance, power, and temperature. Then, we describe the use of predictive models for online control using two modern approaches: imitation learning (IL) and an explicit nonlinear model predictive control (NMPC). Evaluations on a commercial mobile platform with 16 benchmarks show that the IL approach successfully adapts the control policy to unknown applications. The explicit NMPC provides 25% energy savings compared to a state-of-the-art algorithm for multi-variable power management of modern GPU sub-systems.
