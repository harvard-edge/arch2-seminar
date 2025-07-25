---
layout: paper_detail
title: "DeepSeq: Deep Sequential Circuit Learning"
date: 2023-02-27
arxiv_url: http://arxiv.org/abs/2302.13608v2
---

Circuit representation learning is a promising research direction in the electronic design automation (EDA) field. With sufficient data for pre-training, the learned general yet effective representation can help to solve multiple downstream EDA tasks by fine-tuning it on a small set of task-related data. However, existing solutions only target combinational circuits, significantly limiting their applications. In this work, we propose DeepSeq, a novel representation learning framework for sequential netlists. Specifically, we introduce a dedicated graph neural network (GNN) with a customized propagation scheme to exploit the temporal correlations between gates in sequential circuits. To ensure effective learning, we propose to use a multi-task training objective with two sets of strongly related supervision: logic probability and transition probability at each node. A novel dual attention aggregation mechanism is introduced to facilitate learning both tasks efficiently. Experimental results on various benchmark circuits show that DeepSeq outperforms other GNN models for sequential circuit learning. We evaluate the generalization capability of DeepSeq on a downstream power estimation task. After fine-tuning, DeepSeq can accurately estimate power across various circuits under different workloads.
