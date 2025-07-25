---
layout: paper_detail
title: "BoolGebra: Attributed Graph-learning for Boolean Algebraic Manipulation"
date: 2024-01-19
arxiv_url: http://arxiv.org/abs/2401.10753v1
---

Boolean algebraic manipulation is at the core of logic synthesis in Electronic Design Automation (EDA) design flow. Existing methods struggle to fully exploit optimization opportunities, and often suffer from an explosive search space and limited scalability efficiency. This work presents BoolGebra, a novel attributed graph-learning approach for Boolean algebraic manipulation that aims to improve fundamental logic synthesis. BoolGebra incorporates Graph Neural Networks (GNNs) and takes initial feature embeddings from both structural and functional information as inputs. A fully connected neural network is employed as the predictor for direct optimization result predictions, significantly reducing the search space and efficiently locating the optimization space. The experiments involve training the BoolGebra model w.r.t design-specific and cross-design inferences using the trained model, where BoolGebra demonstrates generalizability for cross-design inference and its potential to scale from small, simple training datasets to large, complex inference datasets. Finally, BoolGebra is integrated with existing synthesis tool ABC to perform end-to-end logic minimization evaluation w.r.t SOTA baselines.
