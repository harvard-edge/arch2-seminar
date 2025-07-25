---
layout: paper_detail
title: "AutoChip: Automating HDL Generation Using LLM Feedback"
date: 2023-11-08
arxiv_url: http://arxiv.org/abs/2311.04887v2
---

Traditionally, designs are written in Verilog hardware description language (HDL) and debugged by hardware engineers. While this approach is effective, it is time-consuming and error-prone for complex designs. Large language models (LLMs) are promising in automating HDL code generation. LLMs are trained on massive datasets of text and code, and they can learn to generate code that compiles and is functionally accurate. We aim to evaluate the ability of LLMs to generate functionally correct HDL models. We build AutoChip by combining the interactive capabilities of LLMs and the output from Verilog simulations to generate Verilog modules. We start with a design prompt for a module and the context from compilation errors and debugging messages, which highlight differences between the expected and actual outputs. This ensures that accurate Verilog code can be generated without human intervention. We evaluate AutoChip using problem sets from HDLBits. We conduct a comprehensive analysis of the AutoChip using several LLMs and problem categories. The results show that incorporating context from compiler tools, such as Icarus Verilog, improves the effectiveness, yielding 24.20% more accurate Verilog. We release our evaluation scripts and datasets as open-source contributions at the following link https://github.com/shailja-thakur/AutoChip.
