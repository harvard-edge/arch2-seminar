---
layout: paper_detail
title: "ChIRAAG: ChatGPT Informed Rapid and Automated Assertion Generation"
date: 2024-01-31
arxiv_url: http://arxiv.org/abs/2402.00093v3
---

System Verilog Assertion (SVA) formulation -- a critical yet complex task is a prerequisite in the Assertion Based Verification (ABV) process. Traditionally, SVA formulation involves expert-driven interpretation of specifications, which is time-consuming and prone to human error. Recently, LLM-informed automatic assertion generation is gaining interest. We designed a novel framework called ChIRAAG, based on OpenAI GPT4, to generate SVA from natural language specifications of a design. ChIRAAG constitutes the systematic breakdown of design specifications into a standardized format, further generating assertions from formatted specifications using LLM. Furthermore, we used few test cases to validate the LLM-generated assertions. Automatic feedback of log messages from the simulation tool to the LLM ensures that the framework can generate correct SVAs. In our experiments, only 27% of LLM-generated raw assertions had errors, which was rectified in few iterations based on the simulation log. Our results on OpenTitan designs show that LLMs can streamline and assist engineers in the assertion generation process, reshaping verification workflows.
