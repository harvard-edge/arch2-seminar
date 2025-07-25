---
layout: paper_detail
title: "MetRex: A Benchmark for Verilog Code Metric Reasoning Using LLMs"
date: 2024-11-05
arxiv_url: http://arxiv.org/abs/2411.03471v2
---

Large Language Models (LLMs) have been applied to various hardware design tasks, including Verilog code generation, EDA tool scripting, and RTL bug fixing. Despite this extensive exploration, LLMs are yet to be used for the task of post-synthesis metric reasoning and estimation of HDL designs. In this paper, we assess the ability of LLMs to reason about post-synthesis metrics of Verilog designs. We introduce MetRex, a large-scale dataset comprising 25,868 Verilog HDL designs and their corresponding post-synthesis metrics, namely area, delay, and static power. MetRex incorporates a Chain of Thought (CoT) template to enhance LLMs' reasoning about these metrics. Extensive experiments show that Supervised Fine-Tuning (SFT) boosts the LLM's reasoning capabilities on average by 37.0\%, 25.3\%, and 25.7\% on the area, delay, and static power, respectively. While SFT improves performance on our benchmark, it remains far from achieving optimal results, especially on complex problems. Comparing to state-of-the-art regression models, our approach delivers accurate post-synthesis predictions for 17.4\% more designs (within a 5\% error margin), in addition to offering a 1.7x speedup by eliminating the need for pre-processing. This work lays the groundwork for advancing LLM-based Verilog code metric reasoning.
