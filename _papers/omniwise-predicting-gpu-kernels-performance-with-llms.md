---
layout: paper_detail
title: "Omniwise: Predicting GPU Kernels Performance with LLMs"
date: 2025-06-25
arxiv_url: http://arxiv.org/abs/2506.20886v1
---

In recent years, the rapid advancement of deep neural networks (DNNs) has revolutionized artificial intelligence, enabling models with unprecedented capabilities in understanding, generating, and processing complex data. These powerful architectures have transformed a wide range of downstream applications, tackling tasks beyond human reach. In this paper, we introduce Omniwise, the first end-to-end, self-supervised fine-tuning pipeline that applies large language models (LLMs) to GPU kernel performance prediction--a novel use case in performance profiling. Omniwise is model-agnostic and lightweight, achieving strong results even with a small 3B-parameter model. It can predict key performance metrics, including memory bandwidth, cache hit rates, GFLOPs, and arithmetic intensity, directly from kernel code without the need for code execution or profiling tools. Our approach achieves over 90% of predictions within 10% relative error on GPU kernels executed on AMD MI250 and MI300X architectures. In addition to the pipeline, we develop an online inference server and a Visual Studio Code plugin that seamlessly integrate LLM-based performance prediction into developers' workflows.
