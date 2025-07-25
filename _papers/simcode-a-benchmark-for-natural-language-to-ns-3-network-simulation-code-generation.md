---
layout: paper_detail
title: "SIMCODE: A Benchmark for Natural Language to ns-3 Network Simulation Code Generation"
date: 2025-07-15
arxiv_url: http://arxiv.org/abs/2507.11014v1
---

Large language models (LLMs) have demonstrated remarkable capabilities in code generation across various domains. However, their effectiveness in generating simulation scripts for domain-specific environments like ns-3 remains underexplored. Despite the growing interest in automating network simulations, existing tools primarily focus on interactive automation over rigorous evaluation. To facilitate systematic evaluation, we introduce SIMCODE, the first benchmark to evaluate LLMs' ability to generate ns-3 simulation code from natural language. SIMCODE includes 400 tasks across introductory, intermediate, and advanced levels, with solutions and test cases. Using SIMCODE, we evaluate three prominent LLMs, Gemini-2.0, GPT-4.1, and Qwen-3, across six prompt techniques. Furthermore, investigating task-specific fine-tuning's impact reveals that while GPT-4.1 outperforms others, execution accuracy remains modest, with substantial room for improvement. Error analysis identifies missing headers and API mismatches as dominant failures. Nevertheless, SIMCODE provides a foundational step toward evaluating LLMs and research in domain-aware generative systems.
