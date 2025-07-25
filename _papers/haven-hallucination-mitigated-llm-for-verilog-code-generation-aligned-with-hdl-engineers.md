---
layout: paper_detail
title: "HaVen: Hallucination-Mitigated LLM for Verilog Code Generation Aligned with HDL Engineers"
date: 2025-01-09
arxiv_url: http://arxiv.org/abs/2501.04908v1
---

Recently, the use of large language models (LLMs) for Verilog code generation has attracted great research interest to enable hardware design automation. However, previous works have shown a gap between the ability of LLMs and the practical demands of hardware description language (HDL) engineering. This gap includes differences in how engineers phrase questions and hallucinations in the code generated. To address these challenges, we introduce HaVen, a novel LLM framework designed to mitigate hallucinations and align Verilog code generation with the practices of HDL engineers. HaVen tackles hallucination issues by proposing a comprehensive taxonomy and employing a chain-of-thought (CoT) mechanism to translate symbolic modalities (e.g. truth tables, state diagrams, etc.) into accurate natural language descriptions. Furthermore, HaVen bridges this gap by using a data augmentation strategy. It synthesizes high-quality instruction-code pairs that match real HDL engineering practices. Our experiments demonstrate that HaVen significantly improves the correctness of Verilog code generation, outperforming state-of-the-art LLM-based Verilog generation methods on VerilogEval and RTLLM benchmark. HaVen is publicly available at https://github.com/Intelligent-Computing-Research-Group/HaVen.
