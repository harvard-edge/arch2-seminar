---
layout: paper_detail
title: "A Unified Learning Platform for Dynamic Frequency Scaling in Pipelined Processors"
date: 2020-06-12
arxiv_url: http://arxiv.org/abs/2006.07450v1
---

A machine learning (ML) design framework is proposed for dynamically adjusting clock frequency based on propagation delay of individual instructions. A Random Forest model is trained to classify propagation delays in real-time, utilizing current operation type, current operands, and computation history as ML features. The trained model is implemented in Verilog as an additional pipeline stage within a baseline processor. The modified system is simulated at the gate-level in 45 nm CMOS technology, exhibiting a speed-up of 68% and energy reduction of 37% with coarse-grained ML classification. A speed-up of 95% is demonstrated with finer granularities at additional energy costs.
