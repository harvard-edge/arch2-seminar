---
layout: paper_detail
title: "gigiProfiler: Diagnosing Performance Issues by Uncovering Application Resource Bottlenecks"
date: 2025-07-08
arxiv_url: http://arxiv.org/abs/2507.06452v1
---

Diagnosing performance bottlenecks in modern software is essential yet challenging, particularly as applications become more complex and rely on custom resource management policies. While traditional profilers effectively identify execution bottlenecks by tracing system-level metrics, they fall short when it comes to application-level resource contention caused by waiting for application-level events. In this work, we introduce OmniResource Profiling, a performance analysis approach that integrates system-level and application-level resource tracing to diagnose resource bottlenecks comprehensively. gigiProfiler, our realization of OmniResource Profiling, uses a hybrid LLM-static analysis approach to identify application-defined resources offline and analyze their impact on performance during buggy executions to uncover the performance bottleneck. gigiProfiler then samples and records critical variables related to these bottleneck resources during buggy execution and compares their value with those from normal executions to identify the root causes. We evaluated gigiProfiler on 12 real-world performance issues across five applications. gigiProfiler accurately identified performance bottlenecks in all cases. gigiProfiler also successfully diagnosed the root causes of two newly emerged, previously undiagnosed problems, with the findings confirmed by developers.
