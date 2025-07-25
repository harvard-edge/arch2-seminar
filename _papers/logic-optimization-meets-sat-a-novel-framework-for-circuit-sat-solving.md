---
layout: paper_detail
title: "Logic Optimization Meets SAT: A Novel Framework for Circuit-SAT Solving"
date: 2024-03-28
arxiv_url: http://arxiv.org/abs/2403.19446v2
---

The Circuit Satisfiability (CSAT) problem, a variant of the Boolean Satisfiability (SAT) problem, plays a critical role in integrated circuit design and verification. However, existing SAT solvers, optimized for Conjunctive Normal Form (CNF), often struggle with the intrinsic complexity of circuit structures when directly applied to CSAT instances. To address this challenge, we propose a novel preprocessing framework that leverages advanced logic synthesis techniques and a reinforcement learning (RL) agent to optimize CSAT problem instances. The framework introduces a cost-customized Look-Up Table (LUT) mapping strategy that prioritizes solving efficiency, effectively transforming circuits into simplified forms tailored for SAT solvers. Our method achieves significant runtime reductions across diverse industrial-scale CSAT benchmarks, seamlessly integrating with state-of-the-art SAT solvers. Extensive experimental evaluations demonstrate up to 63\% reduction in solving time compared to conventional approaches, highlighting the potential of EDA-driven innovations to advance SAT-solving capabilities.
