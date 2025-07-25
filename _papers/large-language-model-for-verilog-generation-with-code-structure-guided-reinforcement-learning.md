---
layout: paper_detail
title: "Large Language Model for Verilog Generation with Code-Structure-Guided Reinforcement Learning"
date: 2024-07-21
arxiv_url: http://arxiv.org/abs/2407.18271v4
---

Recent advancements in large language models (LLMs) have sparked significant interest in the automatic generation of Register Transfer Level (RTL) designs, particularly using Verilog. Current research on this topic primarily focuses on pre-training and instruction tuning, but the effectiveness of these methods is constrained by the limited availability of training data, as public Verilog code is far less abundant than software code. In particular, these methods struggle to effectively capture Verilog parallel code structures, which fundamentally differ from the imperative, sequential control flow typical in most software programming languages. This paper introduces VeriSeek, an LLM enhanced by reinforcement learning using a limited amount of high-quality training data to achieve high Verilog code generation performance. Our reinforcement learning approach employs code structure information as feedback signals to refine the pre-trained model, enabling it to effectively learn important patterns from Verilog code with parallel structures. Experiments show that VeriSeek outperforms state-of-the-art methods across multiple benchmarks.
