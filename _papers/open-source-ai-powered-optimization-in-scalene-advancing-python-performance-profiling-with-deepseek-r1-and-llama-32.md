---
layout: paper_detail
title: "Open-Source AI-Powered Optimization in Scalene: Advancing Python Performance Profiling with DeepSeek-R1 and LLaMA 3.2"
date: 2025-02-14
arxiv_url: http://arxiv.org/abs/2502.10299v1
---

Python's flexibility and ease of use come at the cost of performance inefficiencies, requiring developers to rely on profilers to optimize execution. SCALENE, a high-performance CPU, GPU, and memory profiler, provides fine-grained insights into Python applications while running significantly faster than traditional profilers. Originally, SCALENE integrated OpenAI's API to generate AI-powered optimization suggestions, but its reliance on a proprietary API limited accessibility. This study explores the feasibility of using opensource large language models (LLMs), such as DeepSeek-R1 and Llama 3.2, to generate optimization recommendations within SCALENE. Our evaluation reveals that DeepSeek-R1 provides effective code optimizations comparable to proprietary models. We integrate DeepSeek-R1 into SCALENE to automatically analyze performance bottlenecks and suggest improvements, enhancing SCALENE's utility while maintaining its open-source nature. This study demonstrates that open-source LLMs can be viable alternatives for AI-driven code optimization, paving the way for more accessible and cost-effective performance analysis tools.
