---
layout: paper_detail
title: "LLM4SecHW: Leveraging Domain Specific Large Language Model for Hardware Debugging"
date: 2024-01-28
arxiv_url: http://arxiv.org/abs/2401.16448v1
---

This paper presents LLM4SecHW, a novel framework for hardware debugging that leverages domain specific Large Language Model (LLM). Despite the success of LLMs in automating various software development tasks, their application in the hardware security domain has been limited due to the constraints of commercial LLMs and the scarcity of domain specific data. To address these challenges, we propose a unique approach to compile a dataset of open source hardware design defects and their remediation steps, utilizing version control data. This dataset provides a substantial foundation for training machine learning models for hardware. LLM4SecHW employs fine tuning of medium sized LLMs based on this dataset, enabling the identification and rectification of bugs in hardware designs. This pioneering approach offers a reference workflow for the application of fine tuning domain specific LLMs in other research areas. We evaluate the performance of our proposed system on various open source hardware designs, demonstrating its efficacy in accurately identifying and correcting defects. Our work brings a new perspective on automating the quality control process in hardware design.
