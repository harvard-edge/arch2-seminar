---
layout: paper_detail
title: "MORPH: Design Co-optimization with Reinforcement Learning via a Differentiable Hardware Model Proxy"
date: 2023-09-29
arxiv_url: http://arxiv.org/abs/2309.17227v1
---

We introduce MORPH, a method for co-optimization of hardware design parameters and control policies in simulation using reinforcement learning. Like most co-optimization methods, MORPH relies on a model of the hardware being optimized, usually simulated based on the laws of physics. However, such a model is often difficult to integrate into an effective optimization routine. To address this, we introduce a proxy hardware model, which is always differentiable and enables efficient co-optimization alongside a long-horizon control policy using RL. MORPH is designed to ensure that the optimized hardware proxy remains as close as possible to its realistic counterpart, while still enabling task completion. We demonstrate our approach on simulated 2D reaching and 3D multi-fingered manipulation tasks.
