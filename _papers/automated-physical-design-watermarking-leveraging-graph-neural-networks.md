---
layout: paper_detail
title: "Automated Physical Design Watermarking Leveraging Graph Neural Networks"
date: 2024-07-30
arxiv_url: http://arxiv.org/abs/2407.20544v1
---

This paper presents AutoMarks, an automated and transferable watermarking framework that leverages graph neural networks to reduce the watermark search overheads during the placement stage. AutoMarks's novel automated watermark search is accomplished by (i) constructing novel graph and node features with physical, semantic, and design constraint-aware representation; (ii) designing a data-efficient sampling strategy for watermarking fidelity label collection; and (iii) leveraging a graph neural network to learn the connectivity between cells and predict the watermarking fidelity on unseen layouts. Extensive evaluations on ISPD'15 and ISPD'19 benchmarks demonstrate that our proposed automated methodology: (i) is capable of finding quality-preserving watermarks in a short time; and (ii) is transferable across various designs, i.e., AutoMarks trained on one layout is generalizable to other benchmark circuits. AutoMarks is also resilient against potential watermark removal and forging attacks
