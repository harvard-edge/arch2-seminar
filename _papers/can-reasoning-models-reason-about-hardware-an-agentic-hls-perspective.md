---
layout: paper_detail
title: "Can Reasoning Models Reason about Hardware? An Agentic HLS Perspective"
date: 2025-03-17
arxiv_url: http://arxiv.org/abs/2503.12721v2
---

Recent Large Language Models (LLMs) such as OpenAI o3-mini and DeepSeek-R1 use enhanced reasoning through Chain-of-Thought (CoT). Their potential in hardware design, which relies on expert-driven iterative optimization, remains unexplored. This paper investigates whether reasoning LLMs can address challenges in High-Level Synthesis (HLS) design space exploration and optimization. During HLS, engineers manually define pragmas/directives to balance performance and resource constraints. We propose an LLM-based optimization agentic framework that automatically restructures code, inserts pragmas, and identifies optimal design points via feedback from HLs tools and access to integer-linear programming (ILP) solvers. Experiments compare reasoning models against conventional LLMs on benchmarks using success rate, efficiency, and design quality (area/latency) metrics, and provide the first-ever glimpse into the CoTs produced by a powerful open-source reasoning model like DeepSeek-R1.
