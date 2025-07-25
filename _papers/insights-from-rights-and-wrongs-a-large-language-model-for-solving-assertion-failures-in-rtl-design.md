---
layout: paper_detail
title: "Insights from Rights and Wrongs: A Large Language Model for Solving Assertion Failures in RTL Design"
date: 2025-03-06
arxiv_url: http://arxiv.org/abs/2503.04057v1
---

SystemVerilog Assertions (SVAs) are essential for verifying Register Transfer Level (RTL) designs, as they can be embedded into key functional paths to detect unintended behaviours. During simulation, assertion failures occur when the design's behaviour deviates from expectations. Solving these failures, i.e., identifying and fixing the issues causing the deviation, requires analysing complex logical and timing relationships between multiple signals. This process heavily relies on human expertise, and there is currently no automatic tool available to assist with it. Here, we present AssertSolver, an open-source Large Language Model (LLM) specifically designed for solving assertion failures. By leveraging synthetic training data and learning from error responses to challenging cases, AssertSolver achieves a bug-fixing pass@1 metric of 88.54% on our testbench, significantly outperforming OpenAI's o1-preview by up to 11.97%. We release our model and testbench for public access to encourage further research: https://github.com/SEU-ACAL/reproduce-AssertSolver-DAC-25.
