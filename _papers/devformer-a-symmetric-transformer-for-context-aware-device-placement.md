---
layout: paper_detail
title: "DevFormer: A Symmetric Transformer for Context-Aware Device Placement"
date: 2022-05-26
arxiv_url: http://arxiv.org/abs/2205.13225v3
---

In this paper, we present DevFormer, a novel transformer-based architecture for addressing the complex and computationally demanding problem of hardware design optimization. Despite the demonstrated efficacy of transformers in domains including natural language processing and computer vision, their use in hardware design has been limited by the scarcity of offline data. Our approach addresses this limitation by introducing strong inductive biases such as relative positional embeddings and action-permutation symmetricity that effectively capture the hardware context and enable efficient design optimization with limited offline data. We apply DevFoemer to the problem of decoupling capacitor placement and show that it outperforms state-of-the-art methods in both simulated and real hardware, leading to improved performances while reducing the number of components by more than $30\%$. Finally, we show that our approach achieves promising results in other offline contextual learning-based combinatorial optimization tasks.
