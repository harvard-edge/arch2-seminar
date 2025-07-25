---
layout: paper_detail
title: "SPICEAssistant: LLM using SPICE Simulation Tools for Schematic Design of Switched-Mode Power Supplies"
date: 2025-07-14
arxiv_url: http://arxiv.org/abs/2507.10639v1
---

State-of-the-art large language models (LLMs) show high performance across a wide range of tasks in many domains of science. In the field of electronic design automation (EDA), it is yet to be determined to what extent they are capable to understand, adapt, and dimension electronic circuits. This paper focuses on the application of LLMs to switched-mode power supply (SMPS) design on printed circuit boards (PCBs). Particular challenges for LLMs in this context include their limited ability to interpret results from key simulation tools like SPICE and the multi-step design process. To address these challenges, we suggest SPICEAssistant, a framework that provides a broad selection of tools to an LLM. The tools serve as an interface to SPICE, allowing the LLM to interact flexibly with the simulator to estimate the impact of its modifications to the circuit. To evaluate the performance of SPICEAssistant, we defined a benchmark consisting of 256 questions testing the ability to adapt circuit netlists to fulfil different SMPS design tasks. The benchmarking results show that simulation feedback effectively improves SMPS design capabilities of LLMs. An increasing number of simulation iterations leads to enhanced performance. The SPICEAssistant framework significantly outperforms the standalone LLM GPT-4o on the benchmark by approximately 38%.
