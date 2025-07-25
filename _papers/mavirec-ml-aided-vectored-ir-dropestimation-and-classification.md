---
layout: paper_detail
title: "MAVIREC: ML-Aided Vectored IR-DropEstimation and Classification"
date: 2020-12-19
arxiv_url: http://arxiv.org/abs/2012.10597v1
---

Vectored IR drop analysis is a critical step in chip signoff that checks the power integrity of an on-chip power delivery network. Due to the prohibitive runtimes of dynamic IR drop analysis, the large number of test patterns must be whittled down to a small subset of worst-case IR vectors. Unlike the traditional slow heuristic method that select a few vectors with incomplete coverage, MAVIREC uses machine learning techniques -- 3D convolutions and regression-like layers -- for accurately recommending a larger subset of test patterns that exercise worst-case scenarios. In under 30 minutes, MAVIREC profiles 100K-cycle vectors and provides better coverage than a state-of-the-art industrial flow. Further, MAVIREC's IR drop predictor shows 10x speedup with under 4mV RMSE relative to an industrial flow.
