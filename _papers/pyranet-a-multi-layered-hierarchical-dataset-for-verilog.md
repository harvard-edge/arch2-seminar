---
layout: paper_detail
title: "PyraNet: A Multi-Layered Hierarchical Dataset for Verilog"
date: 2024-12-09
arxiv_url: http://arxiv.org/abs/2412.06947v3
---

Recently, there has been a growing interest in leveraging Large Language Models for Verilog code generation. However, the current quality of the generated Verilog code remains suboptimal. This is largely due to the absence of well-defined, well-organized datasets with high-quality samples, as well as a lack of innovative fine-tuning methods and models specifically trained on Verilog. In this paper, we introduce a novel open-source dataset and a corresponding fine-tuning technique, which utilizes a multi-layered structure that we refer to as PyraNet. Our experiments demonstrate that employing the proposed dataset and fine-tuning approach leads to a more accurate fine-tuned model, producing syntactically and functionally correct Verilog code. The evaluation results show improvements by up-to $32.6\%$ in comparison to the CodeLlama-7B baseline model and up-to $16.7\%$ in comparison to the state-of-the-art models using VerilogEval evaluation platform.
