---
layout: paper_detail
title: "DeepGate3: Towards Scalable Circuit Representation Learning"
date: 2024-07-15
arxiv_url: http://arxiv.org/abs/2407.11095v1
---

Circuit representation learning has shown promising results in advancing the field of Electronic Design Automation (EDA). Existing models, such as DeepGate Family, primarily utilize Graph Neural Networks (GNNs) to encode circuit netlists into gate-level embeddings. However, the scalability of GNN-based models is fundamentally constrained by architectural limitations, impacting their ability to generalize across diverse and complex circuit designs. To address these challenges, we introduce DeepGate3, an enhanced architecture that integrates Transformer modules following the initial GNN processing. This novel architecture not only retains the robust gate-level representation capabilities of its predecessor, DeepGate2, but also enhances them with the ability to model subcircuits through a novel pooling transformer mechanism. DeepGate3 is further refined with multiple innovative supervision tasks, significantly enhancing its learning process and enabling superior representation of both gate-level and subcircuit structures. Our experiments demonstrate marked improvements in scalability and generalizability over traditional GNN-based approaches, establishing a significant step forward in circuit representation learning technology.
