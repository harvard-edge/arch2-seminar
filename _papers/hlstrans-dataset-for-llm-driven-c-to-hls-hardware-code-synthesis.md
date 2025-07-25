---
layout: paper_detail
title: "HLStrans: Dataset for LLM-Driven C-to-HLS Hardware Code Synthesis"
date: 2025-07-06
arxiv_url: http://arxiv.org/abs/2507.04315v1
---

High-level synthesis (HLS) enables software developers to describe and implement hardware at a higher level of abstraction by using C/C++ instead of traditional hardware description languages to automatically generate FPGA-ready designs. However, generating HLS code significantly differs from standard C/C++: it disallows certain coding idioms, relies on specialized libraries, and critically requires fine-grained transformations and the insertion of optimization directives (pragmas) to achieve high performance. Large language models (LLMs) have shown promise in automating such transformations, yet existing open-source datasets lack sufficient complexity and optimization diversity. To address this gap, we introduce the HLStrans dataset, a comprehensive collection of 137 distinct real word programs, each annotated with a variety of C-to-HLS transformations that yield over 23K labeled design variants. These include a broad spectrum of pragmas and code-level optimizations. We benchmark state-of-the-art LLMs on this dataset to evaluate their ability to generate synthesizable, high-performance HLS code. As part of an ongoing effort, we plan to expand the HLStrans dataset in both scale and program variety, further empowering research at the intersection of AI and hardware synthesis.
