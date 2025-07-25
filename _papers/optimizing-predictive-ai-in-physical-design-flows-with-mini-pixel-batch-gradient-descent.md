---
layout: paper_detail
title: "Optimizing Predictive AI in Physical Design Flows with Mini Pixel Batch Gradient Descent"
date: 2024-02-08
arxiv_url: http://arxiv.org/abs/2402.06034v1
---

Exploding predictive AI has enabled fast yet effective evaluation and decision-making in modern chip physical design flows. State-of-the-art frameworks typically include the objective of minimizing the mean square error (MSE) between the prediction and the ground truth. We argue the averaging effect of MSE induces limitations in both model training and deployment, and good MSE behavior does not guarantee the capability of these models to assist physical design flows which are likely sabotaged due to a small portion of prediction error. To address this, we propose mini-pixel batch gradient descent (MPGD), a plug-and-play optimization algorithm that takes the most informative entries into consideration, offering probably faster and better convergence. Experiments on representative benchmark suits show the significant benefits of MPGD on various physical design prediction tasks using CNN or Graph-based models.
