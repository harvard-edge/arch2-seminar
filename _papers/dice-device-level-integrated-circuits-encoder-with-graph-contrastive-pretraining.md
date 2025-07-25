---
layout: paper_detail
title: "DICE: Device-level Integrated Circuits Encoder with Graph Contrastive Pretraining"
date: 2025-02-13
arxiv_url: http://arxiv.org/abs/2502.08949v2
---

Pretraining models with unsupervised graph representation learning has led to significant advancements in domains such as social network analysis, molecular design, and electronic design automation (EDA). However, prior work in EDA has mainly focused on pretraining models for digital circuits, overlooking analog and mixed-signal circuits. To bridge this gap, we introduce DICE, a Device-level Integrated Circuits Encoder, which is the first graph neural network (GNN) pretrained via self-supervised learning specifically tailored for graph-level prediction tasks in both analog and digital circuits. DICE adopts a simulation-free pretraining approach based on graph contrastive learning, leveraging two novel graph augmentation techniques. Experimental results demonstrate substantial performance improvements across three downstream tasks, highlighting the effectiveness of DICE for both analog and digital circuits. The code is available at github.com/brianlsy98/DICE.
