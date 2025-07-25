---
layout: paper_detail
title: "RTLFixer: Automatically Fixing RTL Syntax Errors with Large Language Models"
date: 2023-11-28
arxiv_url: http://arxiv.org/abs/2311.16543v3
---

This paper presents RTLFixer, a novel framework enabling automatic syntax errors fixing for Verilog code with Large Language Models (LLMs). Despite LLM's promising capabilities, our analysis indicates that approximately 55% of errors in LLM-generated Verilog are syntax-related, leading to compilation failures. To tackle this issue, we introduce a novel debugging framework that employs Retrieval-Augmented Generation (RAG) and ReAct prompting, enabling LLMs to act as autonomous agents in interactively debugging the code with feedback. This framework demonstrates exceptional proficiency in resolving syntax errors, successfully correcting about 98.5% of compilation errors in our debugging dataset, comprising 212 erroneous implementations derived from the VerilogEval benchmark. Our method leads to 32.3% and 10.1% increase in pass@1 success rates in the VerilogEval-Machine and VerilogEval-Human benchmarks, respectively.
