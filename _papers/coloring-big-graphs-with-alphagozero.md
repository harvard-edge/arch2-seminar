---
layout: paper_detail
title: "Coloring Big Graphs with AlphaGoZero"
date: 2019-02-26
arxiv_url: http://arxiv.org/abs/1902.10162v3
---

We show that recent innovations in deep reinforcement learning can effectively color very large graphs -- a well-known NP-hard problem with clear commercial applications. Because the Monte Carlo Tree Search with Upper Confidence Bound algorithm used in AlphaGoZero can improve the performance of a given heuristic, our approach allows deep neural networks trained using high performance computing (HPC) technologies to transform computation into improved heuristics with zero prior knowledge. Key to our approach is the introduction of a novel deep neural network architecture (FastColorNet) that has access to the full graph context and requires $O(V)$ time and space to color a graph with $V$ vertices, which enables scaling to very large graphs that arise in real applications like parallel computing, compilers, numerical solvers, and design automation, among others. As a result, we are able to learn new state of the art heuristics for graph coloring.
