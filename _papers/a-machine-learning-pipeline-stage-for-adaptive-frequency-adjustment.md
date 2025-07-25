---
layout: paper_detail
title: "A Machine Learning Pipeline Stage for Adaptive Frequency Adjustment"
date: 2020-07-02
arxiv_url: http://arxiv.org/abs/2007.01820v1
---

A machine learning (ML) design framework is proposed for adaptively adjusting clock frequency based on propagation delay of individual instructions. A random forest model is trained to classify propagation delays in real time, utilizing current operation type, current operands, and computation history as ML features. The trained model is implemented in Verilog as an additional pipeline stage within a baseline processor. The modified system is experimentally tested at the gate level in 45 nm CMOS technology, exhibiting a speedup of 70% and energy reduction of 30% with coarse-grained ML classification. A speedup of 89% is demonstrated with finer granularities with 15.5% reduction in energy consumption.
