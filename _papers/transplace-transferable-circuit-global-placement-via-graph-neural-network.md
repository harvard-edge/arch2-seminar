---
layout: paper_detail
title: "TransPlace: Transferable Circuit Global Placement via Graph Neural Network"
date: 2025-01-10
arxiv_url: http://arxiv.org/abs/2501.05667v2
---

Global placement, a critical step in designing the physical layout of computer chips, is essential to optimize chip performance. Prior global placement methods optimize each circuit design individually from scratch. Their neglect of transferable knowledge limits solution efficiency and chip performance as circuit complexity drastically increases. This study presents TransPlace, a global placement framework that learns to place millions of mixed-size cells in continuous space. TransPlace introduces i) Netlist Graph to efficiently model netlist topology, ii) Cell-flow and relative position encoding to learn SE(2)-invariant representation, iii) a tailored graph neural network architecture for informed parameterization of placement knowledge, and iv) a two-stage strategy for coarse-to-fine placement. Compared to state-of-the-art placement methods, TransPlace-trained on a few high-quality placements-can place unseen circuits with 1.2x speedup while reducing congestion by 30%, timing by 9%, and wirelength by 5%.
