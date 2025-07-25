---
layout: paper_detail
title: "Technical Report for HW2VEC -- A Graph Learning Tool for Automating Hardware Security"
date: 2021-07-27
arxiv_url: http://arxiv.org/abs/2108.00078v1
---

In this technical report, we present HW2VEC [11], an open-source graph learning tool for hardware security, and its implementation details (Figure 1). HW2VEC provides toolboxes for graph representation extraction in the form of Data Flow Graphs (DFGs) or Abstract Syntax Trees (ASTs) from hardware designs at RTL and GLN levels. Besides, HW2VEC also offers graph learning tools for representing hardware designs in vectors that preserve both structural features and behavioral features. To the best of our knowledge, HW2VEC is the first open-source research tool that supports applying graph learning methods to hardware designs in different abstraction levels for hardware security. We organize the remainder of this technical report as follows: Section 2 introduces the architecture of HW2VEC; Section 3 gives information about the use-case implementations; Section 4 provides the experimental results and demonstrates the performance of HW2VEC for two hardware security applications: HT detection and IP piracy detection; finally, Section 5 will conclude this report.
