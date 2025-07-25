---
layout: paper_detail
title: "CoopetitiveV: Leveraging LLM-powered Coopetitive Multi-Agent Prompting for High-quality Verilog Generation"
date: 2024-12-15
arxiv_url: http://arxiv.org/abs/2412.11014v2
---

Recent advances in agentic LLMs have demonstrated great capabilities in Verilog code generation. However, existing approaches either use LLM-assisted single-agent prompting or cooperation-only multi-agent learning, which will lead to: (i) Degeneration issue for single-agent learning: characterized by diminished error detection and correction capabilities; (ii) Error propagation in cooperation-only multi-agent learning: erroneous information from the former agent will be propagated to the latter through prompts, which can make the latter agents generate buggy code. In this paper, we propose an LLM-based coopetitive multi-agent prompting framework, in which the agents cannot collaborate with each other to form the generation pipeline, but also create a healthy competitive mechanism to improve the generating quality. Our experimental results show that the coopetitive multi-agent framework can effectively mitigate the degeneration risk and reduce the error propagation while improving code error correction capabilities, resulting in higher quality Verilog code generation. The effectiveness of our approach is validated through extensive experiments. On VerilogEval Machine and Human dataset, CoopetitiveV+GPT-4 achieves 99.2% and 99.1% pass@10 scores, respectively. While on RTLLM, CoopetitiveV+GPT-4 obtains 100% syntax and 99.9% functionality pass@5 scores.
