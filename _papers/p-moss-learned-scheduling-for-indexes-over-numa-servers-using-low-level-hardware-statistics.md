---
layout: paper_detail
title: "P-MOSS: Learned Scheduling For Indexes Over NUMA Servers Using Low-Level Hardware Statistics"
date: 2024-11-05
arxiv_url: http://arxiv.org/abs/2411.02933v1
---

Ever since the Dennard scaling broke down in the early 2000s and the frequency of the CPU stalled, vendors have started to increase the core count in each CPU chip at the expense of introducing heterogeneity, thus ushering the era of NUMA processors. Since then, the heterogeneity in the design space of hardware has only increased to the point that DBMS performance may vary significantly up to an order of magnitude in modern servers. An important factor that affects performance includes the location of the logical cores where the DBMS queries are scheduled, and the locations of the data that the queries access. This paper introduces P-MOSS, a learned spatial scheduling framework that schedules query execution to certain logical cores, and places data accordingly to certain integrated memory controllers (IMC), to integrate hardware consciousness into the system. In the spirit of hardware-software synergy, P-MOSS solely guides its scheduling decision based on low-level hardware statistics collected by performance monitoring counters with the aid of a Decision Transformer. Experimental evaluation is performed in the context of the B-tree and R-tree indexes. Performance results demonstrate that P-MOSS has up to 6x improvement over traditional schedules in terms of query throughput.
