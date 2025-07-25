---
layout: paper_detail
title: "Masala-CHAI: A Large-Scale SPICE Netlist Dataset for Analog Circuits by Harnessing AI"
date: 2024-11-21
arxiv_url: http://arxiv.org/abs/2411.14299v5
---

Masala-CHAI is a fully automated framework leveraging large language models (LLMs) to generate Simulation Programs with Integrated Circuit Emphasis (SPICE) netlists. It addresses a long-standing challenge in circuit design automation: automating netlist generation for analog circuits. Automating this workflow could accelerate the creation of fine-tuned LLMs for analog circuit design and verification. In this work, we identify key challenges in automated netlist generation and evaluate multimodal capabilities of state-of-the-art LLMs, particularly GPT-4, in addressing them. We propose a three-step workflow to overcome existing limitations: labeling analog circuits, prompt tuning, and netlist verification. This approach enables end-to-end SPICE netlist generation from circuit schematic images, tackling the persistent challenge of accurate netlist generation. We utilize Masala-CHAI to collect a corpus of 7,500 schematics that span varying complexities in 10 textbooks and benchmark various open source and proprietary LLMs. Models fine-tuned on Masala-CHAI when used in LLM-agentic frameworks such as AnalogCoder achieve a notable 46% improvement in Pass@1 scores. We open-source our dataset and code for community-driven development.
