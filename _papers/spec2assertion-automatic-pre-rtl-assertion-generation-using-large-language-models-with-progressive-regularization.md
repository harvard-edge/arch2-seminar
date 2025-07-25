---
layout: paper_detail
title: "Spec2Assertion: Automatic Pre-RTL Assertion Generation using Large Language Models with Progressive Regularization"
date: 2025-05-12
arxiv_url: http://arxiv.org/abs/2505.07995v2
---

SystemVerilog Assertions (SVAs) play a critical role in detecting and debugging functional bugs in digital chip design. However, generating SVAs has traditionally been a manual, labor-intensive, and error-prone process. Recent advances in automatic assertion generation, particularly those using machine learning and large language models (LLMs), have shown promising potential, though most approaches remain in the early stages of development. In this work, we introduce Spec2Assertion, a new technique for automatically generating assertions from design specifications prior to RTL implementation. It leverages LLMs with progressive regularization and incorporates Chain-of-Thought (CoT) prompting to guide assertion synthesis. Additionally, we propose a new evaluation methodology that assesses assertion quality across a broad range of scenarios. Experiments on multiple benchmark designs show that Spec2Assertion generates 70% more syntax-correct assertions with 2X quality improvement on average compared to a recent state-of-the-art approach.
