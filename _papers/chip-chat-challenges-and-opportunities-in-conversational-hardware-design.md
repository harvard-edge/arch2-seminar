---
layout: paper_detail
title: "Chip-Chat: Challenges and Opportunities in Conversational Hardware Design"
date: 2023-05-22
arxiv_url: http://arxiv.org/abs/2305.13243v2
---

Modern hardware design starts with specifications provided in natural language. These are then translated by hardware engineers into appropriate Hardware Description Languages (HDLs) such as Verilog before synthesizing circuit elements. Automating this translation could reduce sources of human error from the engineering process. But, it is only recently that artificial intelligence (AI) has demonstrated capabilities for machine-based end-to-end design translations. Commercially-available instruction-tuned Large Language Models (LLMs) such as OpenAI's ChatGPT and Google's Bard claim to be able to produce code in a variety of programming languages; but studies examining them for hardware are still lacking. In this work, we thus explore the challenges faced and opportunities presented when leveraging these recent advances in LLMs for hardware design. Given that these `conversational' LLMs perform best when used interactively, we perform a case study where a hardware engineer co-architects a novel 8-bit accumulator-based microprocessor architecture with the LLM according to real-world hardware constraints. We then sent the processor to tapeout in a Skywater 130nm shuttle, meaning that this `Chip-Chat' resulted in what we believe to be the world's first wholly-AI-written HDL for tapeout.
