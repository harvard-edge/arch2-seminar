---
layout: paper_detail
title: "ChiPFormer: Transferable Chip Placement via Offline Decision Transformer"
date: 2023-06-26
arxiv_url: http://arxiv.org/abs/2306.14744v2
---

Placement is a critical step in modern chip design, aiming to determine the positions of circuit modules on the chip canvas. Recent works have shown that reinforcement learning (RL) can improve human performance in chip placement. However, such an RL-based approach suffers from long training time and low transfer ability in unseen chip circuits. To resolve these challenges, we cast the chip placement as an offline RL formulation and present ChiPFormer that enables learning a transferable placement policy from fixed offline data. ChiPFormer has several advantages that prior arts do not have. First, ChiPFormer can exploit offline placement designs to learn transferable policies more efficiently in a multi-task setting. Second, ChiPFormer can promote effective finetuning for unseen chip circuits, reducing the placement runtime from hours to minutes. Third, extensive experiments on 32 chip circuits demonstrate that ChiPFormer achieves significantly better placement quality while reducing the runtime by 10x compared to recent state-of-the-art approaches in both public benchmarks and realistic industrial tasks. The deliverables are released at https://sites.google.com/view/chipformer/home.
