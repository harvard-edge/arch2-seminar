---
layout: paper_detail
title: "Accelerating Exact Combinatorial Optimization via RL-based Initialization -- A Case Study in Scheduling"
date: 2023-08-19
arxiv_url: http://arxiv.org/abs/2308.11652v1
---

Scheduling on dataflow graphs (also known as computation graphs) is an NP-hard problem. The traditional exact methods are limited by runtime complexity, while reinforcement learning (RL) and heuristic-based approaches struggle with determinism and solution quality. This research aims to develop an innovative approach that employs machine learning (ML) for addressing combinatorial optimization problems, using scheduling as a case study. The goal is to provide guarantees in optimality and determinism while maintaining the runtime cost of heuristic methods. Specifically, we introduce a novel two-phase RL-to-ILP scheduling framework, which includes three steps: 1) RL solver acts as coarse-grain scheduler, 2) solution relaxation and 3) exact solving via ILP. Our framework demonstrates the same scheduling performance compared with using exact scheduling methods while achieving up to 128 $\times$ speed improvements. This was conducted on actual EdgeTPU platforms, utilizing ImageNet DNN computation graphs as input. Additionally, the framework offers improved on-chip inference runtime and acceleration compared to the commercially available EdgeTPU compiler.
