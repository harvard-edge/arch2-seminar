---
layout: paper_detail
title: "Enabling Automated FPGA Accelerator Optimization Using Graph Neural Networks"
date: 2021-11-17
arxiv_url: http://arxiv.org/abs/2111.08848v2
---

High-level synthesis (HLS) has freed the computer architects from developing their designs in a very low-level language and needing to exactly specify how the data should be transferred in register-level. With the help of HLS, the hardware designers must describe only a high-level behavioral flow of the design. Despite this, it still can take weeks to develop a high-performance architecture mainly because there are many design choices at a higher level that requires more time to explore. It also takes several minutes to hours to get feedback from the HLS tool on the quality of each design candidate. In this paper, we propose to solve this problem by modeling the HLS tool with a graph neural network (GNN) that is trained to be used for a wide range of applications. The experimental results demonstrate that by employing the GNN-based model, we are able to estimate the quality of design in milliseconds with high accuracy which can help us search through the solution space very quickly.
