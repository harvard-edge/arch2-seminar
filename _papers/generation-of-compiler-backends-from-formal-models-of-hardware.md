---
layout: paper_detail
title: "Generation of Compiler Backends from Formal Models of Hardware"
date: 2024-08-27
arxiv_url: http://arxiv.org/abs/2408.15429v1
---

Compilers convert between representations -- usually, from higher-level, human writable code to lower-level, machine-readable code. A compiler backend is the portion of the compiler containing optimizations and code generation routines for a specific hardware target. In this dissertation, I advocate for a specific way of building compiler backends: namely, by automatically generating them from explicit, formal models of hardware using automated reasoning algorithms. I describe how automatically generating compilers from formal models of hardware leads to increased optimization ability, stronger correctness guarantees, and reduced development time for compiler backends. As evidence, I present two case studies: first, Glenside, which uses equality saturation to increase the 3LA compiler's ability to offload operations to machine learning accelerators, and second, Lakeroad, a technology mapper for FPGAs which uses program synthesis and semantics extracted from Verilog to map hardware designs to complex, programmable hardware primitives.
