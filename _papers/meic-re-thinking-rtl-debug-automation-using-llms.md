---
layout: paper_detail
title: "MEIC: Re-thinking RTL Debug Automation using LLMs"
date: 2024-05-10
arxiv_url: http://arxiv.org/abs/2405.06840v1
---

The deployment of Large Language Models (LLMs) for code debugging (e.g., C and Python) is widespread, benefiting from their ability to understand and interpret intricate concepts. However, in the semiconductor industry, utilising LLMs to debug Register Transfer Level (RTL) code is still insufficient, largely due to the underrepresentation of RTL-specific data in training sets. This work introduces a novel framework, Make Each Iteration Count (MEIC), which contrasts with traditional one-shot LLM-based debugging methods that heavily rely on prompt engineering, model tuning, and model training. MEIC utilises LLMs in an iterative process to overcome the limitation of LLMs in RTL code debugging, which is suitable for identifying and correcting both syntax and function errors, while effectively managing the uncertainties inherent in LLM operations. To evaluate our framework, we provide an open-source dataset comprising 178 common RTL programming errors. The experimental results demonstrate that the proposed debugging framework achieves fix rate of 93% for syntax errors and 78% for function errors, with up to 48x speedup in debugging processes when compared with experienced engineers. The Repo. of dataset and code: https://anonymous.4open.science/r/Verilog-Auto-Debug-6E7F/.
