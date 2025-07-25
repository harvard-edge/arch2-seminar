---
layout: paper_detail
title: "HL-Pow: A Learning-Based Power Modeling Framework for High-Level Synthesis"
date: 2020-09-02
arxiv_url: http://arxiv.org/abs/2009.00871v1
---

High-level synthesis (HLS) enables designers to customize hardware designs efficiently. However, it is still challenging to foresee the correlation between power consumption and HLS-based applications at an early design stage. To overcome this problem, we introduce HL-Pow, a power modeling framework for FPGA HLS based on state-of-the-art machine learning techniques. HL-Pow incorporates an automated feature construction flow to efficiently identify and extract features that exert a major influence on power consumption, simply based upon HLS results, and a modeling flow that can build an accurate and generic power model applicable to a variety of designs with HLS. By using HL-Pow, the power evaluation process for FPGA designs can be significantly expedited because the power inference of HL-Pow is established on HLS instead of the time-consuming register-transfer level (RTL) implementation flow. Experimental results demonstrate that HL-Pow can achieve accurate power modeling that is only 4.67% (24.02 mW) away from onboard power measurement. To further facilitate power-oriented optimizations, we describe a novel design space exploration (DSE) algorithm built on top of HL-Pow to trade off between latency and power consumption. This algorithm can reach a close approximation of the real Pareto frontier while only requiring running HLS flow for 20% of design points in the entire design space.
