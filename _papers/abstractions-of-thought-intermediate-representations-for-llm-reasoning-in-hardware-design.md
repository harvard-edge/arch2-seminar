---
layout: paper_detail
title: "Abstractions-of-Thought: Intermediate Representations for LLM Reasoning in Hardware Design"
date: 2025-05-21
arxiv_url: http://arxiv.org/abs/2505.15873v2
---

Large language models (LLMs) have achieved impressive proficiency on logic and programming tasks, often rivaling expert-level performance. However, generating functionally correct hardware description language (HDL) code from natural language specifications remains challenging, primarily in data-scarce domains.   Therefore, we present Abstractions-of-Thought (AoT) - a training-free, inference-only prompting framework to mitigate misinterpretations and reasoning pitfalls of LLMs through a series of task-based abstractions within the prompting procedure, assisting in the transition from high-level to low-level representations of hardware. Furthermore, AoT consists of the following stages: (1) an LLM-based classification of hardware design patterns, (2) a structured intermediate representation (IR) to separate functional decomposition from code syntax, and (3) a line-by-line pseudocode solution enabling a more direct mapping to the final Verilog implementation. Experimental results on the VerilogEval benchmark depict that AoT demonstrates improvements in functionality when applied to large non-reasoning models (such as GPT-4o, outperforming all baseline techniques (including 1-shot, Chain-of-Thought, and Tree-of-Thought) while significantly reducing the generated tokens by 1.8-5.2x compared to popular Tree-of-Thought prompting.
