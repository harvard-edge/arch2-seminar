---
layout: paper_detail
title: "AUTOCIRCUIT-RL: Reinforcement Learning-Driven LLM for Automated Circuit Topology Generation"
date: 2025-06-03
arxiv_url: http://arxiv.org/abs/2506.03122v1
---

Analog circuit topology synthesis is integral to Electronic Design Automation (EDA), enabling the automated creation of circuit structures tailored to specific design requirements. However, the vast design search space and strict constraint adherence make efficient synthesis challenging. Leveraging the versatility of Large Language Models (LLMs), we propose AUTOCIRCUIT-RL,a novel reinforcement learning (RL)-based framework for automated analog circuit synthesis. The framework operates in two phases: instruction tuning, where an LLM learns to generate circuit topologies from structured prompts encoding design constraints, and RL refinement, which further improves the instruction-tuned model using reward models that evaluate validity, efficiency, and output voltage. The refined model is then used directly to generate topologies that satisfy the design constraints. Empirical results show that AUTOCIRCUIT-RL generates ~12% more valid circuits and improves efficiency by ~14% compared to the best baselines, while reducing duplicate generation rates by ~38%. It achieves over 60% success in synthesizing valid circuits with limited training data, demonstrating strong generalization. These findings highlight the framework's effectiveness in scaling to complex circuits while maintaining efficiency and constraint adherence, marking a significant advancement in AI-driven circuit design.
