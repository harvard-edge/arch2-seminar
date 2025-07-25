---
layout: paper_detail
title: "An Agentic Flow for Finite State Machine Extraction using Prompt Chaining"
date: 2025-07-15
arxiv_url: http://arxiv.org/abs/2507.11222v1
---

Finite-State Machines (FSMs) are critical for modeling the operational logic of network protocols, enabling verification, analysis, and vulnerability discovery. However, existing FSM extraction techniques face limitations such as scalability, incomplete coverage, and ambiguity in natural language specifications. In this paper, we propose FlowFSM, a novel agentic framework that leverages Large Language Models (LLMs) combined with prompt chaining and chain-of-thought reasoning to extract accurate FSMs from raw RFC documents. FlowFSM systematically processes protocol specifications, identifies state transitions, and constructs structured rule-books by chaining agent outputs. Experimental evaluation across FTP and RTSP protocols demonstrates that FlowFSM achieves high extraction precision while minimizing hallucinated transitions, showing promising results. Our findings highlight the potential of agent-based LLM systems in the advancement of protocol analysis and FSM inference for cybersecurity and reverse engineering applications.
