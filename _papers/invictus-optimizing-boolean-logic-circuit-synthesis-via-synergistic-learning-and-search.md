---
layout: paper_detail
title: "INVICTUS: Optimizing Boolean Logic Circuit Synthesis via Synergistic Learning and Search"
date: 2023-05-22
arxiv_url: http://arxiv.org/abs/2305.13164v3
---

Logic synthesis is the first and most vital step in chip design. This steps converts a chip specification written in a hardware description language (such as Verilog) into an optimized implementation using Boolean logic gates. State-of-the-art logic synthesis algorithms have a large number of logic minimization heuristics, typically applied sequentially based on human experience and intuition. The choice of the order greatly impacts the quality (e.g., area and delay) of the synthesized circuit. In this paper, we propose INVICTUS, a model-based offline reinforcement learning (RL) solution that automatically generates a sequence of logic minimization heuristics ("synthesis recipe") based on a training dataset of previously seen designs. A key challenge is that new designs can range from being very similar to past designs (e.g., adders and multipliers) to being completely novel (e.g., new processor instructions). %Compared to prior work, INVICTUS is the first solution that uses a mix of RL and search methods joint with an online out-of-distribution detector to generate synthesis recipes over a wide range of benchmarks. Our results demonstrate significant improvement in area-delay product (ADP) of synthesized circuits with up to 30\% improvement over state-of-the-art techniques. Moreover, INVICTUS achieves up to $6.3\times$ runtime reduction (iso-ADP) compared to the state-of-the-art.
