---
layout: paper_detail
title: "Evaluating LLMs for Hardware Design and Test"
date: 2024-04-23
arxiv_url: http://arxiv.org/abs/2405.02326v2
---

Large Language Models (LLMs) have demonstrated capabilities for producing code in Hardware Description Languages (HDLs). However, most of the focus remains on their abilities to write functional code, not test code. The hardware design process consists of both design and test, and so eschewing validation and verification leaves considerable potential benefit unexplored, given that a design and test framework may allow for progress towards full automation of the digital design pipeline. In this work, we perform one of the first studies exploring how a LLM can both design and test hardware modules from provided specifications. Using a suite of 8 representative benchmarks, we examined the capabilities and limitations of the state-of-the-art conversational LLMs when producing Verilog for functional and verification purposes. We taped out the benchmarks on a Skywater 130nm shuttle and received the functional chip.
