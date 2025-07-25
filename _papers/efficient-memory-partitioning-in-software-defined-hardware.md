---
layout: paper_detail
title: "Efficient Memory Partitioning in Software Defined Hardware"
date: 2022-02-02
arxiv_url: http://arxiv.org/abs/2202.01261v3
---

As programmers turn to software-defined hardware (SDH) to maintain a high level of productivity while programming hardware to run complex algorithms, heavy-lifting must be done by the compiler to automatically partition on-chip arrays. In this paper, we introduce an automatic memory partitioning system that can quickly compute more efficient partitioning schemes than prior systems. Our system employs a variety of resource-saving optimizations and an ML cost model to select the best partitioning scheme from an array of candidates. We compared our system against various state-of-the-art SDH compilers and FPGAs on a variety of benchmarks and found that our system generates solutions that, on average, consume 40.3% fewer logic resources, 78.3% fewer FFs, 54.9% fewer Block RAMs (BRAMs), and 100% fewer DSPs.
