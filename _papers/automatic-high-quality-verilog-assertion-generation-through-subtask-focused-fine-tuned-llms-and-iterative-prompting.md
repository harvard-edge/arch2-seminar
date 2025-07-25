---
layout: paper_detail
title: "Automatic High-quality Verilog Assertion Generation through Subtask-Focused Fine-Tuned LLMs and Iterative Prompting"
date: 2024-11-23
arxiv_url: http://arxiv.org/abs/2411.15442v1
---

Formal Property Verification (FPV), using SystemVerilog Assertions (SVA), is crucial for ensuring the completeness of design with respect to the specification. However, writing SVA is a laborious task and has a steep learning curve. In this work, we present a large language model (LLM) -based flow to automatically generate high-quality SVA from the design specification documents, named \ToolName. We introduce a novel sub-task-focused fine-tuning approach that effectively addresses functionally incorrect assertions produced by baseline LLMs, leading to a remarkable 7.3-fold increase in the number of functionally correct assertions. Recognizing the prevalence of syntax and semantic errors, we also developed an iterative refinement method that enhances the LLM's initial outputs by systematically re-prompting it to correct identified issues. This process is further strengthened by a custom compiler that generates meaningful error messages, guiding the LLM towards improved accuracy. The experiments demonstrate a 26\% increase in the number of assertions free from syntax errors using this approach, showcasing its potential to streamline the FPV process.
