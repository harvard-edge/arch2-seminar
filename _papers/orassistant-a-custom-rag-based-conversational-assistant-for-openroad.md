---
layout: paper_detail
title: "ORAssistant: A Custom RAG-based Conversational Assistant for OpenROAD"
date: 2024-10-04
arxiv_url: http://arxiv.org/abs/2410.03845v2
---

Open-source Electronic Design Automation (EDA) tools are rapidly transforming chip design by addressing key barriers of commercial EDA tools such as complexity, costs, and access. Recent advancements in Large Language Models (LLMs) have further enhanced efficiency in chip design by providing user assistance across a range of tasks like setup, decision-making, and flow automation. This paper introduces ORAssistant, a conversational assistant for OpenROAD, based on Retrieval-Augmented Generation (RAG). ORAssistant aims to improve the user experience for the OpenROAD flow, from RTL-GDSII by providing context-specific responses to common user queries, including installation, command usage, flow setup, and execution, in prose format. Currently, ORAssistant integrates OpenROAD, OpenROAD-flow-scripts, Yosys, OpenSTA, and KLayout. The data model is built from publicly available documentation and GitHub resources. The proposed architecture is scalable, supporting extensions to other open-source tools, operating modes, and LLM models. We use Google Gemini as the base LLM model to build and test ORAssistant. Early evaluation results of the RAG-based model show notable improvements in performance and accuracy compared to non-fine-tuned LLMs.
