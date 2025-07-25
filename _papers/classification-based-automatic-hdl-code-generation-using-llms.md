---
layout: paper_detail
title: "Classification-Based Automatic HDL Code Generation Using LLMs"
date: 2024-07-04
arxiv_url: http://arxiv.org/abs/2407.18326v1
---

While large language models (LLMs) have demonstrated the ability to generate hardware description language (HDL) code for digital circuits, they still suffer from the hallucination problem, which leads to the generation of incorrect HDL code or misunderstanding of specifications. In this work, we introduce a human-expert-inspired method to mitigate the hallucination of LLMs and improve the performance in HDL code generation. We first let LLMs classify the type of the circuit based on the specifications. Then, according to the type of the circuit, we split the tasks into several sub-procedures, including information extraction and human-like design flow using Electronic Design Automation (EDA) tools. Besides, we also use a search method to mitigate the variation in code generation. Experimental results show that our method can significantly improve the functional correctness of the generated Verilog and reduce the hallucination of LLMs.
