---
layout: paper_detail
title: "Inverse Design in Distributed Circuits Using Single-Step Reinforcement Learning"
date: 2025-06-02
arxiv_url: http://arxiv.org/abs/2506.08029v1
---

The goal of inverse design in distributed circuits is to generate near-optimal designs that meet a desirable transfer function specification. Existing design exploration methods use some combination of strategies involving artificial grids, differentiable evaluation procedures, and specific template topologies. However, real-world design practices often require non-differentiable evaluation procedures, varying topologies, and near-continuous placement spaces. In this paper, we propose DCIDA, a design exploration framework that learns a near-optimal design sampling policy for a target transfer function. DCIDA decides all design factors in a compound single-step action by sampling from a set of jointly-trained conditional distributions generated by the policy. Utilizing an injective interdependent ``map", DCIDA transforms raw sampled design ``actions" into uniquely equivalent physical representations, enabling the framework to learn the conditional dependencies among joint ``raw'' design decisions. Our experiments demonstrate DCIDA's Transformer-based policy network achieves significant reductions in design error compared to state-of-the-art approaches, with significantly better fit in cases involving more complex transfer functions.
