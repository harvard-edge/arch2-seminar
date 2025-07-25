---
layout: paper_detail
title: "Cross-Timeslot Optimization for Distributed GPU Inference Using Reinforcement Learning"
date: 2025-07-14
arxiv_url: http://arxiv.org/abs/2507.10259v1
---

The rapid growth of large language model (LLM) services imposes increasing demands on distributed GPU inference infrastructure. Most existing scheduling systems rely on the current system state to make decisions, without considering how task demand and resource availability evolve over time. This lack of temporal awareness leads to inefficient GPU utilization, high task migration overhead, and poor system responsiveness under dynamic workloads. In this work, we identify the fundamental limitations of these instantaneous-state-only scheduling approaches and propose Temporal Optimal Resource scheduling via Two-layer Architecture (TORTA). TORTA introduces a spatiotemporal scheduling framework that captures both long-term workload patterns and short-term execution constraints. It adopts a two-layer design: a macro-level scheduler leverages reinforcement learning and optimal transport to coordinate inter-region task distribution, while a micro-level allocator refines task-to-server assignments within each region to reduce latency and switching costs. Experimental results across multiple network topologies show that TORTA reduces average inference response time by up to 15\%, improves load balance by approximately 4-5\%, and cuts total operational cost by 10-20\% compared to state-of-the-art baseline methods.
