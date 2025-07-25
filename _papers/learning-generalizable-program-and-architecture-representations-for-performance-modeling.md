---
layout: paper_detail
title: "Learning Generalizable Program and Architecture Representations for Performance Modeling"
date: 2023-10-25
arxiv_url: http://arxiv.org/abs/2310.16792v3
---

Performance modeling is an essential tool in many areas, including performance characterization/optimization, design space exploration, and resource allocation problems, to name a few. However, existing performance modeling approaches have limitations, such as high computational cost for discrete-event simulators, narrow flexibility of hardware emulators, or restricted accuracy/generality of analytical/data-driven models. To address these limitations, this paper proposes PerfVec, a novel deep learning-based performance modeling framework that learns high-dimensional and independent/orthogonal program and microarchitecture representations. Once learned, a program representation can be used to predict its performance on any microarchitecture, and likewise, a microarchitecture representation can be applied in the performance prediction of any program. Additionally, PerfVec yields a foundation model that captures the performance essence of instructions, which can be directly used by developers in numerous performance modeling related tasks without incurring its training cost. The evaluation demonstrates that PerfVec is more general and efficient than previous approaches.
