---
layout: paper_detail
title: "GNN-ACLP: Graph Neural Networks Based Analog Circuit Link Prediction"
date: 2025-04-14
arxiv_url: http://arxiv.org/abs/2504.10240v3
---

Circuit link prediction identifying missing component connections from incomplete netlists is crucial in automating analog circuit design. However, existing methods face three main challenges: 1) Insufficient use of topological patterns in circuit graphs reduces prediction accuracy; 2) Data scarcity due to the complexity of annotations hinders model generalization; 3) Limited adaptability to various netlist formats. We propose GNN-ACLP, a Graph Neural Networks (GNNs) based framework featuring three innovations to tackle these challenges. First, we introduce the SEAL (Subgraphs, Embeddings, and Attributes for Link Prediction) framework and achieve port-level accuracy in circuit link prediction. Second, we propose Netlist Babel Fish, a netlist format conversion tool leveraging retrieval-augmented generation (RAG) with a large language model (LLM) to enhance the compatibility of netlist formats. Finally, we construct SpiceNetlist, a comprehensive dataset that contains 775 annotated circuits across 10 different component classes. Experiments demonstrate accuracy improvements of 16.08% on SpiceNetlist, 11.38% on Image2Net, and 16.01% on Masala-CHAI compared to the baseline in intra-dataset evaluation, while maintaining accuracy from 92.05% to 99.07% in cross-dataset evaluation, exhibiting robust feature transfer capabilities.
