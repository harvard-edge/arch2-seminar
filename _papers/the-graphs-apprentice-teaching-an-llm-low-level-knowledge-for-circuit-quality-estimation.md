---
layout: paper_detail
title: "The Graph's Apprentice: Teaching an LLM Low Level Knowledge for Circuit Quality Estimation"
date: 2024-10-30
arxiv_url: http://arxiv.org/abs/2411.00843v2
---

Logic synthesis is a crucial phase in the circuit design process, responsible for transforming hardware description language (HDL) designs into optimized netlists. However, traditional logic synthesis methods are computationally intensive, restricting their iterative use in refining chip designs. Recent advancements in large language models (LLMs), particularly those fine-tuned on programming languages, present a promising alternative. This work proposes augmenting LLMs with predictor networks trained to estimate circuit quality directly from HDL code. To enhance performance, the model is regularized using embeddings from graph neural networks (GNNs) trained on Look-Up Table (LUT) graphs, thereby incorporating lower-level circuit insights. The proposed method demonstrates superior performance compared to existing graph-based RTL-level estimation techniques on the established benchmark OpenABCD, while providing instant feedback on HDL code quality.
