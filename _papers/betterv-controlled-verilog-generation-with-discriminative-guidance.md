---
layout: paper_detail
title: "BetterV: Controlled Verilog Generation with Discriminative Guidance"
date: 2024-02-03
arxiv_url: http://arxiv.org/abs/2402.03375v3
---

Due to the growing complexity of modern Integrated Circuits (ICs), there is a need for automated circuit design methods. Recent years have seen rising research in hardware design language generation to facilitate the design process. In this work, we propose a Verilog generation framework, BetterV, which fine-tunes the large language models (LLMs) on processed domain-specific datasets and incorporates generative discriminators for guidance on particular design demands. The Verilog modules are collected, filtered and processed from internet to form a clean and abundant dataset. Instruct-tuning methods are specially designed to fine-tune the LLMs to understand the knowledge about Verilog. Furthermore, data are augmented to enrich the training set and also used to train a generative discriminator on particular downstream task, which leads a guidance for the LLMs to optimize the Verilog implementation. BetterV has the ability to generate syntactically and functionally correct Verilog, which can outperform GPT-4 on the VerilogEval benchmark. With the help of task-specific generative discriminator, BetterV can achieve remarkable improvement on various electronic design automation (EDA) downstream tasks, including the netlist node reduction for synthesis and verification runtime reduction with Boolean Satisfiability (SAT) solving.
