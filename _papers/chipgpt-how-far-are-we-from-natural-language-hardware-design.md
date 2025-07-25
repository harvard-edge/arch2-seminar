---
layout: paper_detail
title: "ChipGPT: How far are we from natural language hardware design"
date: 2023-05-23
arxiv_url: http://arxiv.org/abs/2305.14019v3
---

As large language models (LLMs) like ChatGPT exhibited unprecedented machine intelligence, it also shows great performance in assisting hardware engineers to realize higher-efficiency logic design via natural language interaction. To estimate the potential of the hardware design process assisted by LLMs, this work attempts to demonstrate an automated design environment that explores LLMs to generate hardware logic designs from natural language specifications. To realize a more accessible and efficient chip development flow, we present a scalable four-stage zero-code logic design framework based on LLMs without retraining or finetuning. At first, the demo, ChipGPT, begins by generating prompts for the LLM, which then produces initial Verilog programs. Second, an output manager corrects and optimizes these programs before collecting them into the final design space. Eventually, ChipGPT will search through this space to select the optimal design under the target metrics. The evaluation sheds some light on whether LLMs can generate correct and complete hardware logic designs described by natural language for some specifications. It is shown that ChipGPT improves programmability, and controllability, and shows broader design optimization space compared to prior work and native LLMs alone.
