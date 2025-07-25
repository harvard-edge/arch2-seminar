---
layout: paper_detail
title: "LLMPerf: GPU Performance Modeling meets Large Language Models"
date: 2025-03-14
arxiv_url: http://arxiv.org/abs/2503.11244v1
---

Performance modeling, a pivotal domain in program cost analysis, currently relies on manually crafted models constrained by various program and hardware limitations, especially in the intricate landscape of GPGPU. Meanwhile, Large Language Models (LLMs) have demonstrated their effectiveness in addressing diverse programming challenges. Our work establishes a connection between LLMs and performance modeling, employing the LLM as a performance estimator. Through experimental exploration with carefully designed large-scale OpenCL datasets, we highlight the potential capability as well as the main difficulties of using LLMs in handling performance modeling tasks for OpenCL device source programs. As the first study for this line of work, our LLM-based performance model achieves a mean absolute percentage error of $24.25\%$ for a large-scale generated validation set. On a set of publicly available OpenCL programs, our model achieves a mean absolute percentage error of $46.1\%$.
