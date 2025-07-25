---
layout: paper_detail
title: "Evaluating Large Language Models for Automatic Register Transfer Logic Generation via High-Level Synthesis"
date: 2024-08-05
arxiv_url: http://arxiv.org/abs/2408.02793v1
---

The ever-growing popularity of large language models (LLMs) has resulted in their increasing adoption for hardware design and verification. Prior research has attempted to assess the capability of LLMs to automate digital hardware design by producing superior-quality Register Transfer Logic (RTL) descriptions, particularly in Verilog. However, these tests have revealed that Verilog code production using LLMs at current state-of-the-art lack sufficient functional correctness to be practically viable, compared to automatic generation of programs in general-purpose programming languages such as C, C++, Python, etc. With this as the key insight, in this paper we assess the performance of a two-stage software pipeline for automated Verilog RTL generation: LLM based automatic generation of annotated C++ code suitable for high-level synthesis (HLS), followed by HLS to generate Verilog RTL. We have benchmarked the performance of our proposed scheme using the open-source VerilogEval dataset, for four different industry-scale LLMs, and the Vitis HLS tool. Our experimental results demonstrate that our two-step technique substantially outperforms previous proposed techniques of direct Verilog RTL generation by LLMs in terms of average functional correctness rates, reaching score of 0.86 in pass@1 metric.
