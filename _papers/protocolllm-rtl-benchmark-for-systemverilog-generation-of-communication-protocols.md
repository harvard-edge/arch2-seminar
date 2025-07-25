---
layout: paper_detail
title: "ProtocolLLM: RTL Benchmark for SystemVerilog Generation of Communication Protocols"
date: 2025-06-09
arxiv_url: http://arxiv.org/abs/2506.07945v2
---

Recent advances in large language models (LLMs) have demonstrated strong performance in generating code for general-purpose programming languages. However, their potential for hardware description languages (HDLs), such as SystemVerilog, remains largely unexplored. HDL code generation poses unique challenges due to strict timing semantics, concurrency, and synthesizability constraints essential for correct hardware functionality. Further, HDL-based design flows encompass a broad set of tasks beyond structural code generation, including testbench development, assertion-based verification, timing closure, and protocol-level integration for on-chip communication. In this work, we evaluate the capabilities of both open-source and state-of-the-art LLMs in generating synthesizable and functionally accurate SystemVerilog implementations of widely used communication protocols that are critical components of embedded and System-on-Chip (SoC) systems. We introduce ProtocolLLM, the first benchmark suite specifically targeting these protocols with tasks spanning multiple design abstraction levels and varying prompt specificity. Our evaluation method also focuses on timing correctness in addition to synthesizability and syntactic correctness. We observe that most of the models fail to generate SystemVerilog code for communication protocols that follow timing constrains.
