---
layout: paper_detail
title: "LIMCA: LLM for Automating Analog In-Memory Computing Architecture Design Exploration"
date: 2025-03-17
arxiv_url: http://arxiv.org/abs/2503.13301v1
---

Resistive crossbars enabling analog In-Memory Computing (IMC) have emerged as a promising architecture for Deep Neural Network (DNN) acceleration, offering high memory bandwidth and in-situ computation. However, the manual, knowledge-intensive design process and the lack of high-quality circuit netlists have significantly constrained design space exploration and optimization to behavioral system-level tools. In this work, we introduce LIMCA, a novel fine-tune-free Large Language Model (LLM)-driven framework for automating the design and evaluation of IMC crossbar architectures. Unlike traditional approaches, LIMCA employs a No-Human-In-Loop (NHIL) automated pipeline to generate and validate circuit netlists for SPICE simulations, eliminating manual intervention. LIMCA systematically explores the IMC design space by leveraging a structured dataset and LLM-based performance evaluation. Our experimental results on MNIST classification demonstrate that LIMCA successfully generates crossbar designs achieving $\geq$96% accuracy while maintaining a power consumption $\leq$3W, making this the first work in LLM-assisted IMC design space exploration. Compared to existing frameworks, LIMCA provides an automated, scalable, and hardware-aware solution, reducing design exploration time while ensuring user-constrained performance trade-offs.
