---
layout: paper_detail
title: "HDL-GPT: High-Quality HDL is All You Need"
date: 2024-07-25
arxiv_url: http://arxiv.org/abs/2407.18423v1
---

This paper presents Hardware Description Language Generative Pre-trained Transformers (HDL-GPT), a novel approach that leverages the vast repository of open-source High Definition Language (HDL) codes to train superior quality large code models. The core premise of this paper is the hypothesis that high-quality HDL is all you need to create models with exceptional performance and broad zero-shot generalization abilities. The paper elucidates the methods employed for the curation and augmentation of large corpora from open-source HDL code, transforming highly variable quality data into high-quality data through careful prompting and context maintenance. We demonstrate that the careful selection, filtering, and augmentation of data across HDLs can yield powerful models that surpass current state-of-the-art models. We also explore the impact of different fine-tuning methods on the quality of results. We describe experimental results across a range of fine-tuned SOTA LLMs, substantiating our claims. We demonstrate improvements of 50% to 200% over SOTA HDL models on current benchmarks in tasks ranging from HDL circuit explanations, code generation, formal and simulation testbench creation, triaging bugs, and fixing them. HDL-GPT opens new avenues for the development of advanced model training techniques for circuit design tasks.
