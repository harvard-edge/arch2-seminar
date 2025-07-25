---
layout: paper_detail
title: "Fixing Hardware Security Bugs with Large Language Models"
date: 2023-02-02
arxiv_url: http://arxiv.org/abs/2302.01215v1
---

Novel AI-based code-writing Large Language Models (LLMs) such as OpenAI's Codex have demonstrated capabilities in many coding-adjacent domains. In this work we consider how LLMs maybe leveraged to automatically repair security relevant bugs present in hardware designs. We focus on bug repair in code written in the Hardware Description Language Verilog. For this study we build a corpus of domain-representative hardware security bugs. We then design and implement a framework to quantitatively evaluate the performance of any LLM tasked with fixing the specified bugs. The framework supports design space exploration of prompts (i.e., prompt engineering) and identifying the best parameters for the LLM. We show that an ensemble of LLMs can repair all ten of our benchmarks. This ensemble outperforms the state-of-the-art Cirfix hardware bug repair tool on its own suite of bugs. These results show that LLMs can repair hardware security bugs and the framework is an important step towards the ultimate goal of an automated end-to-end bug repair framework.
