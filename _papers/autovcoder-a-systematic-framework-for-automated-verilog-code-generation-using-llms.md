---
layout: paper_detail
title: "AutoVCoder: A Systematic Framework for Automated Verilog Code Generation using LLMs"
date: 2024-07-21
arxiv_url: http://arxiv.org/abs/2407.18333v1
---

Recently, the use of large language models (LLMs) for software code generation, e.g., C/C++ and Python, has proven a great success. However, LLMs still suffer from low syntactic and functional correctness when it comes to the generation of register-transfer level (RTL) code, such as Verilog. To address this issue, in this paper, we develop AutoVCoder, a systematic open-source framework that significantly improves the LLMs' correctness of generating Verilog code and enhances the quality of its output at the same time. Our framework integrates three novel techniques, including a high-quality hardware dataset generation approach, a two-round LLM fine-tuning method and a domain-specific retrieval-augmented generation (RAG) mechanism. Experimental results demonstrate that AutoVCoder outperforms both industrial and academic LLMs in Verilog code generation. Specifically, AutoVCoder shows a 0.5% and 2.2% improvement in functional correctness on the EvalMachine and EvalHuman benchmarks compared with BetterV, and also achieves a 3.4% increase in syntax correctness and a 3.4% increase in functional correctness on the RTLLM benchmark compared with RTLCoder.
