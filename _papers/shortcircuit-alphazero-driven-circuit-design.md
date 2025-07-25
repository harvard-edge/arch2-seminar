---
layout: paper_detail
title: "ShortCircuit: AlphaZero-Driven Circuit Design"
date: 2024-08-19
arxiv_url: http://arxiv.org/abs/2408.09858v2
---

Chip design relies heavily on generating Boolean circuits, such as AND-Inverter Graphs (AIGs), from functional descriptions like truth tables. This generation operation is a key process in logic synthesis, a primary chip design stage. While recent advances in deep learning have aimed to accelerate circuit design, these efforts have mostly focused on tasks other than synthesis, and traditional heuristic methods have plateaued. In this paper, we introduce ShortCircuit, a novel transformer-based architecture that leverages the structural properties of AIGs and performs efficient space exploration. Contrary to prior approaches attempting end-to-end generation of logic circuits using deep networks, ShortCircuit employs a two-phase process combining supervised with reinforcement learning to enhance generalization to unseen truth tables. We also propose an AlphaZero variant to handle the double exponentially large state space and the reward sparsity, enabling the discovery of near-optimal designs. To evaluate the generative performance of our model , we extract 500 truth tables from a set of 20 real-world circuits. ShortCircuit successfully generates AIGs for $98\%$ of the 8-input test truth tables, and outperforms the state-of-the-art logic synthesis tool, ABC, by $18.62\%$ in terms of circuits size.
