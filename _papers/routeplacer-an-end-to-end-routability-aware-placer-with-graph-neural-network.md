---
layout: paper_detail
title: "RoutePlacer: An End-to-End Routability-Aware Placer with Graph Neural Network"
date: 2024-06-04
arxiv_url: http://arxiv.org/abs/2406.02651v1
---

Placement is a critical and challenging step of modern chip design, with routability being an essential indicator of placement quality. Current routability-oriented placers typically apply an iterative two-stage approach, wherein the first stage generates a placement solution, and the second stage provides non-differentiable routing results to heuristically improve the solution quality. This method hinders jointly optimizing the routability aspect during placement. To address this problem, this work introduces RoutePlacer, an end-to-end routability-aware placement method. It trains RouteGNN, a customized graph neural network, to efficiently and accurately predict routability by capturing and fusing geometric and topological representations of placements. Well-trained RouteGNN then serves as a differentiable approximation of routability, enabling end-to-end gradient-based routability optimization. In addition, RouteGNN can improve two-stage placers as a plug-and-play alternative to external routers. Our experiments on DREAMPlace, an open-source AI4EDA platform, show that RoutePlacer can reduce Total Overflow by up to 16% while maintaining routed wirelength, compared to the state-of-the-art; integrating RouteGNN within two-stage placers leads to a 44% reduction in Total Overflow without compromising wirelength.
