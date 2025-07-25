---
layout: paper_detail
title: "VerilogDB: The Largest, Highest-Quality Dataset with a Preprocessing Framework for LLM-based RTL Generation"
date: 2025-07-09
arxiv_url: http://arxiv.org/abs/2507.13369v1
---

Large Language Models (LLMs) are gaining popularity for hardware design automation, particularly through Register Transfer Level (RTL) code generation. In this work, we examine the current literature on RTL generation using LLMs and identify key requirements for training and fine-tuning datasets. We construct a robust Verilog dataset through an automated three-pronged process involving database (DB) creation and management with PostgreSQL, data collection from code hosting sites like OpenCores and GitHub, and data preprocessing to verify the codes' syntax, run logic synthesis, and extract relevant module metadata. We implement a scalable and efficient DB infrastructure to support analysis and detail our preprocessing pipeline to enforce high-quality data before DB insertion. The resulting dataset comprises 20,392 Verilog samples, 751 MB of Verilog code data, which is the largest high-quality Verilog dataset for LLM fine-tuning to our knowledge. We further evaluate the dataset, address associated challenges, and explore potential applications for future research and development in LLM-based hardware generation.
