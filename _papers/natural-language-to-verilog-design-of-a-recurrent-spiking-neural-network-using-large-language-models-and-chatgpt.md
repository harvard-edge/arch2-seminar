---
layout: paper_detail
title: "Natural Language to Verilog: Design of a Recurrent Spiking Neural Network using Large Language Models and ChatGPT"
date: 2024-05-02
arxiv_url: http://arxiv.org/abs/2405.01419v3
---

This paper investigates the use of Large Language Models (LLMs) and natural language prompts to generate hardware description code, namely Verilog. Building on our prior work, we employ OpenAI's ChatGPT4 and natural language prompts to synthesize an RTL Verilog module of a programmable recurrent spiking neural network, while also generating test benches to assess the system's correctness. The resultant design was validated in three simple machine learning tasks, the exclusive OR, the IRIS flower classification and the MNIST hand-written digit classification. Furthermore, the design was validated on a Field-Programmable Gate Array (FPGA) and subsequently synthesized in the SkyWater 130 nm technology by using an open-source electronic design automation flow. The design was submitted to Efabless Tiny Tapeout 6.
