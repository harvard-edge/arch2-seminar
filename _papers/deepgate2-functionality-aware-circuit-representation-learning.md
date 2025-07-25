---
layout: paper_detail
title: "DeepGate2: Functionality-Aware Circuit Representation Learning"
date: 2023-05-25
arxiv_url: http://arxiv.org/abs/2305.16373v1
---

Circuit representation learning aims to obtain neural representations of circuit elements and has emerged as a promising research direction that can be applied to various EDA and logic reasoning tasks. Existing solutions, such as DeepGate, have the potential to embed both circuit structural information and functional behavior. However, their capabilities are limited due to weak supervision or flawed model design, resulting in unsatisfactory performance in downstream tasks. In this paper, we introduce DeepGate2, a novel functionality-aware learning framework that significantly improves upon the original DeepGate solution in terms of both learning effectiveness and efficiency. Our approach involves using pairwise truth table differences between sampled logic gates as training supervision, along with a well-designed and scalable loss function that explicitly considers circuit functionality. Additionally, we consider inherent circuit characteristics and design an efficient one-round graph neural network (GNN), resulting in an order of magnitude faster learning speed than the original DeepGate solution. Experimental results demonstrate significant improvements in two practical downstream tasks: logic synthesis and Boolean satisfiability solving. The code is available at https://github.com/cure-lab/DeepGate2
