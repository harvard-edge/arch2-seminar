---
layout: paper_detail
title: "Paradigm-Based Automatic HDL Code Generation Using LLMs"
date: 2025-01-22
arxiv_url: http://arxiv.org/abs/2501.12702v1
---

While large language models (LLMs) have demonstrated the ability to generate hardware description language (HDL) code for digital circuits, they still face the hallucination problem, which can result in the generation of incorrect HDL code or misinterpretation of specifications. In this work, we introduce a human-expert-inspired method to mitigate the hallucination of LLMs and enhance their performance in HDL code generation. We begin by constructing specialized paradigm blocks that consist of several steps designed to divide and conquer generation tasks, mirroring the design methodology of human experts. These steps include information extraction, human-like design flows, and the integration of external tools. LLMs are then instructed to classify the type of circuit in order to match it with the appropriate paradigm block and execute the block to generate the HDL codes. Additionally, we propose a two-phase workflow for multi-round generation, aimed at effectively improving the testbench pass rate of the generated HDL codes within a limited number of generation and verification rounds. Experimental results demonstrate that our method significantly enhances the functional correctness of the generated Verilog code
