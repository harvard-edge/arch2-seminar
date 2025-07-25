---
layout: paper_detail
title: "Towards Optimal Circuit Generation: Multi-Agent Collaboration Meets Collective Intelligence"
date: 2025-04-20
arxiv_url: http://arxiv.org/abs/2504.14625v3
---

Large language models (LLMs) have transformed code generation, yet their application in hardware design produces gate counts 38\%--1075\% higher than human designs. We present CircuitMind, a multi-agent framework that achieves human-competitive efficiency through three key innovations: syntax locking (constraining generation to basic logic gates), retrieval-augmented generation (enabling knowledge-driven design), and dual-reward optimization (balancing correctness with efficiency). To evaluate our approach, we introduce TC-Bench, the first gate-level benchmark harnessing collective intelligence from the TuringComplete ecosystem -- a competitive circuit design platform with hundreds of thousands of players. Experiments show CircuitMind enables 55.6\% of model implementations to match or exceed top-tier human experts in composite efficiency metrics. Most remarkably, our framework elevates the 14B Phi-4 model to outperform both GPT-4o mini and Gemini 2.0 Flash, achieving efficiency comparable to the top 25\% of human experts without requiring specialized training. These innovations establish a new paradigm for hardware optimization where collaborative AI systems leverage collective human expertise to achieve optimal circuit designs. Our model, data, and code are open-source at https://github.com/BUAA-CLab/CircuitMind.
