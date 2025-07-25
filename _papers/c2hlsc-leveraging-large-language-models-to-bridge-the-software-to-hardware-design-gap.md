---
layout: paper_detail
title: "C2HLSC: Leveraging Large Language Models to Bridge the Software-to-Hardware Design Gap"
date: 2024-11-29
arxiv_url: http://arxiv.org/abs/2412.00214v2
---

High-Level Synthesis (HLS) tools offer rapid hardware design from C code, but their compatibility is limited by code constructs. This paper investigates Large Language Models (LLMs) for automatically refactoring C code into HLS-compatible formats. We present a case study using an LLM to rewrite C code for NIST 800-22 randomness tests, a QuickSort algorithm, and AES-128 into HLS-synthesizable C. The LLM iteratively transforms the C code guided by the system prompt and tool's feedback, implementing functions like streaming data and hardware-specific signals. With the hindsight obtained from the case study, we implement a fully automated framework to refactor C code into HLS-compatible formats using LLMs. To tackle complex designs, we implement a preprocessing step that breaks down the hierarchy in order to approach the problem in a divide-and-conquer bottom-up way. We validated our framework on three ciphers, one hash function, five NIST 800-22 randomness tests, and a QuickSort algorithm. Our results show a high success rate on benchmarks that are orders of magnitude more complex than what has been achieved generating Verilog with LLMs.
