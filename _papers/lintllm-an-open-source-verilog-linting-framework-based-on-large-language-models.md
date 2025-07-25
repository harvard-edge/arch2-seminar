---
layout: paper_detail
title: "LintLLM: An Open-Source Verilog Linting Framework Based on Large Language Models"
date: 2025-02-15
arxiv_url: http://arxiv.org/abs/2502.10815v1
---

Code Linting tools are vital for detecting potential defects in Verilog code. However, the limitations of traditional Linting tools are evident in frequent false positives and redundant defect reports. Recent advancements in large language models (LLM) have introduced new possibilities in this area. In this paper, we propose LintLLM, an open-source Linting framework that utilizes LLMs to detect defects in Verilog code via Prompt of Logic-Tree and Defect Tracker. Furthermore, we create an open-source benchmark using the mutation-based defect injection technique to evaluate LLM's ability in detecting Verilog defects. Experimental results show that o1-mini improves the correct rate by 18.89\% and reduces the false-positive rate by 15.56\% compared with the best-performing EDA tool. Simultaneously, LintLLM operates at less than one-tenth of the cost of commercial EDA tools. This study demonstrates the potential of LLM as an efficient and cost-effective Linting tool for hardware design. The benchmark and experimental results are open-source at URL: https://github.com/fangzhigang32/Static-Verilog-Analysis
