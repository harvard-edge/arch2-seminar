---
layout: paper_detail
title: "VerilogCoder: Autonomous Verilog Coding Agents with Graph-based Planning and Abstract Syntax Tree (AST)-based Waveform Tracing Tool"
date: 2024-08-15
arxiv_url: http://arxiv.org/abs/2408.08927v2
---

Due to the growing complexity of modern Integrated Circuits (ICs), automating hardware design can prevent a significant amount of human error from the engineering process and result in less errors. Verilog is a popular hardware description language for designing and modeling digital systems; thus, Verilog generation is one of the emerging areas of research to facilitate the design process. In this work, we propose VerilogCoder, a system of multiple Artificial Intelligence (AI) agents for Verilog code generation, to autonomously write Verilog code and fix syntax and functional errors using collaborative Verilog tools (i.e., syntax checker, simulator, and waveform tracer). Firstly, we propose a task planner that utilizes a novel Task and Circuit Relation Graph retrieval method to construct a holistic plan based on module descriptions. To debug and fix functional errors, we develop a novel and efficient abstract syntax tree (AST)-based waveform tracing tool, which is integrated within the autonomous Verilog completion flow. The proposed methodology successfully generates 94.2% syntactically and functionally correct Verilog code, surpassing the state-of-the-art methods by 33.9% on the VerilogEval-Human v2 benchmark.
