---
layout: paper_detail
title: "ILILT: Implicit Learning of Inverse Lithography Technologies"
date: 2024-05-06
arxiv_url: http://arxiv.org/abs/2405.03574v1
---

Lithography, transferring chip design masks to the silicon wafer, is the most important phase in modern semiconductor manufacturing flow. Due to the limitations of lithography systems, Extensive design optimizations are required to tackle the design and silicon mismatch. Inverse lithography technology (ILT) is one of the promising solutions to perform pre-fabrication optimization, termed mask optimization. Because of mask optimization problems' constrained non-convexity, numerical ILT solvers rely heavily on good initialization to avoid getting stuck on sub-optimal solutions. Machine learning (ML) techniques are hence proposed to generate mask initialization for ILT solvers with one-shot inference, targeting faster and better convergence during ILT. This paper addresses the question of \textit{whether ML models can directly generate high-quality optimized masks without engaging ILT solvers in the loop}. We propose an implicit learning ILT framework: ILILT, which leverages the implicit layer learning method and lithography-conditioned inputs to ground the model. Trained to understand the ILT optimization procedure, ILILT can outperform the state-of-the-art machine learning solutions, significantly improving efficiency and quality.
