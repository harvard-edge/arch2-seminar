---
layout: paper_detail
title: "Fast Machine Learning for Quantum Control of Microwave Qudits on Edge Hardware"
date: 2025-06-03
arxiv_url: http://arxiv.org/abs/2506.03323v1
---

Quantum optimal control is a promising approach to improve the accuracy of quantum gates, but it relies on complex algorithms to determine the best control settings. CPU or GPU-based approaches often have delays that are too long to be applied in practice. It is paramount to have systems with extremely low delays to quickly and with high fidelity adjust quantum hardware settings, where fidelity is defined as overlap with a target quantum state. Here, we utilize machine learning (ML) models to determine control-pulse parameters for preparing Selective Number-dependent Arbitrary Phase (SNAP) gates in microwave cavity qudits, which are multi-level quantum systems that serve as elementary computation units for quantum computing. The methodology involves data generation using classical optimization techniques, ML model development, design space exploration, and quantization for hardware implementation. Our results demonstrate the efficacy of the proposed approach, with optimized models achieving low gate trace infidelity near $10^{-3}$ and efficient utilization of programmable logic resources.
