---
layout: paper_detail
title: "LOSTIN: Logic Optimization via Spatio-Temporal Information with Hybrid Graph Models"
date: 2022-01-20
arxiv_url: http://arxiv.org/abs/2201.08455v2
---

Despite the stride made by machine learning (ML) based performance modeling, two major concerns that may impede production-ready ML applications in EDA are stringent accuracy requirements and generalization capability. To this end, we propose hybrid graph neural network (GNN) based approaches towards highly accurate quality-of-result (QoR) estimations with great generalization capability, specifically targeting logic synthesis optimization. The key idea is to simultaneously leverage spatio-temporal information from hardware designs and logic synthesis flows to forecast performance (i.e., delay/area) of various synthesis flows on different designs. The structural characteristics inside hardware designs are distilled and represented by GNNs; the temporal knowledge (i.e., relative ordering of logic transformations) in synthesis flows can be imposed on hardware designs by combining a virtually added supernode or a sequence processing model with conventional GNN models. Evaluation on 3.3 million data points shows that the testing mean absolute percentage error (MAPE) on designs seen and unseen during training are no more than 1.2% and 3.1%, respectively, which are 7-15X lower than existing studies.
