---
layout: paper_detail
title: "Location is Key: Leveraging Large Language Model for Functional Bug Localization in Verilog"
date: 2024-09-23
arxiv_url: http://arxiv.org/abs/2409.15186v2
---

Bug localization in Verilog code is a crucial and time-consuming task during the verification of hardware design. Since introduction, Large Language Models (LLMs) have showed their strong programming capabilities. However, no work has yet considered using LLMs for bug localization in Verilog code. This paper presents Location-is-Key, an opensource LLM solution to locate functional errors in Verilog snippets. LiK achieves high localization accuracy, with a pass@1 localization accuracy of 93.3% on our test dataset based on RTLLM, surpassing GPT-4's 77.9% and comparable to Claude-3.5's 90.8%. Additionally, the bug location obtained by LiK significantly improves GPT-3.5's bug repair efficiency (Functional pass@1 increased from 40.39% to 58.92%), highlighting the importance of bug localization in LLM-based Verilog debugging. Compared to existing methods, LiK only requires the design specification and the erroneous code snippet, without the need for testbenches, assertions, or any other EDA tools. This research demonstrates the feasibility of using LLMs for Verilog error localization, thus providing a new direction for automatic Verilog code debugging.
