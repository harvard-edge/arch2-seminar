---
layout: paper_detail
title: "PICBench: Benchmarking LLMs for Photonic Integrated Circuits Design"
date: 2025-02-05
arxiv_url: http://arxiv.org/abs/2502.03159v1
---

While large language models (LLMs) have shown remarkable potential in automating various tasks in digital chip design, the field of Photonic Integrated Circuits (PICs)-a promising solution to advanced chip designs-remains relatively unexplored in this context. The design of PICs is time-consuming and prone to errors due to the extensive and repetitive nature of code involved in photonic chip design. In this paper, we introduce PICBench, the first benchmarking and evaluation framework specifically designed to automate PIC design generation using LLMs, where the generated output takes the form of a netlist. Our benchmark consists of dozens of meticulously crafted PIC design problems, spanning from fundamental device designs to more complex circuit-level designs. It automatically evaluates both the syntax and functionality of generated PIC designs by comparing simulation outputs with expert-written solutions, leveraging an open-source simulator. We evaluate a range of existing LLMs, while also conducting comparative tests on various prompt engineering techniques to enhance LLM performance in automated PIC design. The results reveal the challenges and potential of LLMs in the PIC design domain, offering insights into the key areas that require further research and development to optimize automation in this field. Our benchmark and evaluation code is available at https://github.com/PICDA/PICBench.
