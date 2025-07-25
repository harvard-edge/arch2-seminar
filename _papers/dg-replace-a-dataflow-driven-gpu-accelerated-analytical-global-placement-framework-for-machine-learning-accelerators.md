---
layout: paper_detail
title: "DG-RePlAce: A Dataflow-Driven GPU-Accelerated Analytical Global Placement Framework for Machine Learning Accelerators"
date: 2024-03-16
arxiv_url: http://arxiv.org/abs/2404.13049v2
---

Global placement is a fundamental step in VLSI physical design. The wide use of 2D processing element (PE) arrays in machine learning accelerators poses new challenges of scalability and Quality of Results (QoR) for state-of-the-art academic global placers. In this work, we develop DG-RePlAce, a new and fast GPU-accelerated global placement framework built on top of the OpenROAD infrastructure, which exploits the inherent dataflow and datapath structures of machine learning accelerators. Experimental results with a variety of machine learning accelerators using a commercial 12nm enablement show that, compared with RePlAce (DREAMPlace), our approach achieves an average reduction in routed wirelength by 10% (7%) and total negative slack (TNS) by 31% (34%), with faster global placement and on-par total runtimes relative to DREAMPlace. Empirical studies on the TILOS MacroPlacement Benchmarks further demonstrate that post-route improvements over RePlAce and DREAMPlace may reach beyond the motivating application to machine learning accelerators.
