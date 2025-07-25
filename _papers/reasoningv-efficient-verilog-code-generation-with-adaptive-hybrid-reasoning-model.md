---
layout: paper_detail
title: "ReasoningV: Efficient Verilog Code Generation with Adaptive Hybrid Reasoning Model"
date: 2025-04-20
arxiv_url: http://arxiv.org/abs/2504.14560v3
---

Large Language Models (LLMs) have advanced Verilog code generation significantly, yet face challenges in data quality, reasoning capabilities, and computational efficiency. This paper presents ReasoningV, a novel model employing a hybrid reasoning strategy that integrates trained intrinsic capabilities with dynamic inference adaptation for Verilog code generation. Our framework introduces three complementary innovations: (1) ReasoningV-5K, a high-quality dataset of 5,000 functionally verified instances with reasoning paths created through multi-dimensional filtering of PyraNet samples; (2) a two-stage training approach combining parameter-efficient fine-tuning for foundational knowledge with full-parameter optimization for enhanced reasoning; and (3) an adaptive reasoning mechanism that dynamically adjusts reasoning depth based on problem complexity, reducing token consumption by up to 75\% while preserving performance. Experimental results demonstrate ReasoningV's effectiveness with a pass@1 accuracy of 57.8\% on VerilogEval-human, achieving performance competitive with leading commercial models like Gemini-2.0-flash (59.5\%) and exceeding the previous best open-source model by 10.4 percentage points. ReasoningV offers a more reliable and accessible pathway for advancing AI-driven hardware design automation, with our model, data, and code available at https://github.com/BUAA-CLab/ReasoningV.
