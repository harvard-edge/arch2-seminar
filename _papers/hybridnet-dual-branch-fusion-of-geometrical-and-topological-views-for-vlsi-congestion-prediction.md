---
layout: paper_detail
title: "HybridNet: Dual-Branch Fusion of Geometrical and Topological Views for VLSI Congestion Prediction"
date: 2023-05-07
arxiv_url: http://arxiv.org/abs/2305.05374v2
---

Accurate early congestion prediction can prevent unpleasant surprises at the routing stage, playing a crucial character in assisting designers to iterate faster in VLSI design cycles. In this paper, we introduce a novel strategy to fully incorporate topological and geometrical features of circuits by making several key designs in our network architecture. To be more specific, we construct two individual graphs (geometry-graph, topology-graph) with distinct edge construction schemes according to their unique properties. We then propose a dual-branch network with different encoder layers in each pathway and aggregate representations with a sophisticated fusion strategy. Our network, named HybridNet, not only provides a simple yet effective way to capture the geometric interactions of cells, but also preserves the original topological relationships in the netlist. Experimental results on the ISPD2015 benchmarks show that we achieve an improvement of 10.9% compared to previous methods.
