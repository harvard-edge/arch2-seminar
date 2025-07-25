---
layout: paper_detail
title: "VFlow: Discovering Optimal Agentic Workflows for Verilog Generation"
date: 2025-03-30
arxiv_url: http://arxiv.org/abs/2504.03723v2
---

Hardware design automation faces challenges in generating high-quality Verilog code efficiently. This paper introduces VFlow, an automated framework that optimizes agentic workflows for Verilog code generation. Unlike traditional approaches relying on fixed prompts or manually designed flows, VFlow treats workflow discovery as a search over graph-structured LLM invocation sequences. It introduces a multi-population cooperative evolution (CEPE-MCTS) algorithm that balances multiple hardware objectives -- functional correctness, area, power, timing and token cost -- while sharing successful patterns and avoiding repeated failures. Integrated multi-level verification ensures syntactic correctness, functional behavior, and synthesizability. Experiments on VerilogEval and RTLLM2.0 show VFlow improves pass@1 by 20--30\% over prompting baselines and closely matches designer-level area/power. Remarkably, VFlow enables small LLMs to outperform larger models with up to 10.9$\times$ ROI, offering a cost-effective solution for RTL design. This work paves the way for intelligent, automated hardware development, advancing LLM applications in EDA.
