---
layout: paper_detail
title: "Encoder-Decoder Networks for Analyzing Thermal and Power Delivery Networks"
date: 2021-10-27
arxiv_url: http://arxiv.org/abs/2110.14197v1
---

Power delivery network (PDN) analysis and thermal analysis are computationally expensive tasks that are essential for successful IC design. Algorithmically, both these analyses have similar computational structure and complexity as they involve the solution to a partial differential equation of the same form. This paper converts these analyses into image-to-image and sequence-to-sequence translation tasks, which allows leveraging a class of machine learning models with an encoder-decoder-based generative (EDGe) architecture to address the time-intensive nature of these tasks. For PDN analysis, we propose two networks: (i) IREDGe: a full-chip static and dynamic IR drop predictor and (ii) EMEDGe: electromigration (EM) hotspot classifier based on input power, power grid distribution, and power pad distribution patterns. For thermal analysis, we propose ThermEDGe, a full-chip static and dynamic temperature estimator based on input power distribution patterns for thermal analysis. These networks are transferable across designs synthesized within the same technology and packing solution. The networks predict on-chip IR drop, EM hotspot locations, and temperature in milliseconds with negligibly small errors against commercial tools requiring several hours.
