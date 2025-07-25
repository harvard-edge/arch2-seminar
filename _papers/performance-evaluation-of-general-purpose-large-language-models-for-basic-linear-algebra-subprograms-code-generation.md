---
layout: paper_detail
title: "Performance Evaluation of General Purpose Large Language Models for Basic Linear Algebra Subprograms Code Generation"
date: 2025-07-07
arxiv_url: http://arxiv.org/abs/2507.04697v1
---

Generative AI technology based on Large Language Models (LLM) has been developed and applied to assist or automatically generate program codes. In this paper, we evaluate the capability of existing general LLMs for Basic Linear Algebra Subprograms (BLAS) code generation for CPUs. We use two LLMs provided by OpenAI: GPT-4.1, a Generative Pre-trained Transformer (GPT) model, and o4-mini, one of the o-series of Reasoning models. Both have been released in April 2025. For the routines from level-1 to 3 BLAS, we tried to generate (1) C code without optimization from routine name only, (2) C code with basic performance optimizations (thread parallelization, SIMD vectorization, and cache blocking) from routine name only, and (3) C code with basic performance optimizations based on Fortran reference code. As a result, we found that correct code can be generated in many cases even when only routine name are given. We also confirmed that thread parallelization with OpenMP, SIMD vectorization, and cache blocking can be implemented to some extent, and that the code is faster than the reference code.
