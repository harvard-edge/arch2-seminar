---
layout: paper_detail
title: "Veritas: Deterministic Verilog Code Synthesis from LLM-Generated Conjunctive Normal Form"
date: 2025-05-07
arxiv_url: http://arxiv.org/abs/2506.00005v1
---

Automated Verilog code synthesis poses significant challenges and typically demands expert oversight. Traditional high-level synthesis (HLS) methods often fail to scale for real-world designs. While large language models (LLMs) have enhanced scalability, they often introduce syntactical and logical errors requiring extensive post-generation verification. Here, we introduce a novel conjunctive normal form (CNF)-guided synthesis methodology. The idea is to have an LLM generate CNF clauses, a format widely used for formal verification and synthesis validation in hardware design, but here it is used to formally describe the desired circuit functionality. These CNF specifications are then deterministically converted into Verilog, ensuring correctness by construction. Our approach fine-tunes an open-source and lightweight LLM, namely the CPU-deployable LLama-3.2-3B-Instruct model (parameters < 4B), on a dataset of standard RTL components. Experimental results demonstrate that our approach reliably produces functionally correct Verilog code on the first attempt, compared to other lightweight open-source SoTA works such as Verigen (2B parameters) and RTLCoder (4-bit quantized with around 7B parameters). We will release our method and data in full post peer-review.
