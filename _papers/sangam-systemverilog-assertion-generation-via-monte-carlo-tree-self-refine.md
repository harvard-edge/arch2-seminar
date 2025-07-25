---
layout: paper_detail
title: "SANGAM: SystemVerilog Assertion Generation via Monte Carlo Tree Self-Refine"
date: 2025-06-11
arxiv_url: http://arxiv.org/abs/2506.13983v1
---

Recent advancements in the field of reasoning using Large Language Models (LLMs) have created new possibilities for more complex and automatic Hardware Assertion Generation techniques. This paper introduces SANGAM, a SystemVerilog Assertion Generation framework using LLM-guided Monte Carlo Tree Search for the automatic generation of SVAs from industry-level specifications. The proposed framework utilizes a three-stage approach: Stage 1 consists of multi-modal Specification Processing using Signal Mapper, SPEC Analyzer, and Waveform Analyzer LLM Agents. Stage 2 consists of using the Monte Carlo Tree Self-Refine (MCTSr) algorithm for automatic reasoning about SVAs for each signal, and finally, Stage 3 combines the MCTSr-generated reasoning traces to generate SVA assertions for each signal. The results demonstrated that our framework, SANGAM, can generate a robust set of SVAs, performing better in the evaluation process in comparison to the recent methods.
