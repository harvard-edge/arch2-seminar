---
layout: paper_detail
title: "Hierarchical Source-to-Post-Route QoR Prediction in High-Level Synthesis with GNNs"
date: 2024-01-14
arxiv_url: http://arxiv.org/abs/2401.08696v1
---

High-level synthesis (HLS) notably speeds up the hardware design process by avoiding RTL programming. However, the turnaround time of HLS increases significantly when post-route quality of results (QoR) are considered during optimization. To tackle this issue, we propose a hierarchical post-route QoR prediction approach for FPGA HLS, which features: (1) a modeling flow that directly estimates latency and post-route resource usage from C/C++ programs; (2) a graph construction method that effectively represents the control and data flow graph of source code and effects of HLS pragmas; and (3) a hierarchical GNN training and prediction method capable of capturing the impact of loop hierarchies. Experimental results show that our method presents a prediction error of less than 10% for different types of QoR metrics, which gains tremendous improvement compared with the state-of-the-art GNN methods. By adopting our proposed methodology, the runtime for design space exploration in HLS is shortened to tens of minutes and the achieved ADRS is reduced to 6.91% on average.
