---
layout: paper_detail
title: "AssertCoder: LLM-Based Assertion Generation via Multimodal Specification Extraction"
date: 2025-07-14
arxiv_url: http://arxiv.org/abs/2507.10338v1
---

Assertion-Based Verification (ABV) is critical for ensuring functional correctness in modern hardware systems. However, manually writing high-quality SVAs remains labor-intensive and error-prone. To bridge this gap, we propose AssertCoder, a novel unified framework that automatically generates high-quality SVAs directly from multimodal hardware design specifications. AssertCoder employs a modality-sensitive preprocessing to parse heterogeneous specification formats (text, tables, diagrams, and formulas), followed by a set of dedicated semantic analyzers that extract structured representations aligned with signal-level semantics. These representations are utilized to drive assertion synthesis via multi-step chain-of-thought (CoT) prompting. The framework incorporates a mutation-based evaluation approach to assess assertion quality via model checking and further refine the generated assertions. Experimental evaluation across three real-world Register-Transfer Level (RTL) designs demonstrates AssertCoder's superior performance, achieving an average increase of 8.4% in functional correctness and 5.8% in mutation detection compared to existing state-of-the-art approaches.
