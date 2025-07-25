---
layout: paper_detail
title: "IICPilot: An Intelligent Integrated Circuit Backend Design Framework Using Open EDA"
date: 2024-07-17
arxiv_url: http://arxiv.org/abs/2407.12576v2
---

Open-source EDA tools are rapidly advancing, fostering collaboration, innovation, and knowledge sharing within the EDA community. However, the growing complexity of these tools, characterized by numerous design parameters and heuristics, poses a significant barrier to their widespread adoption. This complexity is particularly pronounced in integrated circuit (IC) backend designs, which place substantial demands on engineers' expertise in EDA tools. To tackle this challenge, we introduce IICPilot, an intelligent IC backend design system based on LLM technology. IICPilot automates various backend design procedures, including script generation, EDA tool invocation, design space exploration of EDA parameters, container-based computing resource allocation, and exception management. By automating these tasks, IICPilot significantly lowers the barrier to entry for open-source EDA tools. Specifically, IICPilot utilizes LangChain's multi-agent framework to efficiently handle distinct design tasks, enabling flexible enhancements independently. Moreover, IICPilot separates the backend design workflow from specific open-source EDA tools through a unified EDA calling interface. This approach allows seamless integration with different open-source EDA tools like OpenROAD and iEDA, streamlining the backend design and optimization across the EDA tools.
