---
layout: paper_detail
title: "GNN4IP: Graph Neural Network for Hardware Intellectual Property Piracy Detection"
date: 2021-07-19
arxiv_url: http://arxiv.org/abs/2107.09130v1
---

Aggressive time-to-market constraints and enormous hardware design and fabrication costs have pushed the semiconductor industry toward hardware Intellectual Properties (IP) core design. However, the globalization of the integrated circuits (IC) supply chain exposes IP providers to theft and illegal redistribution of IPs. Watermarking and fingerprinting are proposed to detect IP piracy. Nevertheless, they come with additional hardware overhead and cannot guarantee IP security as advanced attacks are reported to remove the watermark, forge, or bypass it. In this work, we propose a novel methodology, GNN4IP, to assess similarities between circuits and detect IP piracy. We model the hardware design as a graph and construct a graph neural network model to learn its behavior using the comprehensive dataset of register transfer level codes and gate-level netlists that we have gathered. GNN4IP detects IP piracy with 96% accuracy in our dataset and recognizes the original IP in its obfuscated version with 100% accuracy.
