---
layout: paper_detail
title: "DeepSeq2: Enhanced Sequential Circuit Learning with Disentangled Representations"
date: 2024-11-01
arxiv_url: http://arxiv.org/abs/2411.00530v1
---

Circuit representation learning is increasingly pivotal in Electronic Design Automation (EDA), serving various downstream tasks with enhanced model efficiency and accuracy. One notable work, DeepSeq, has pioneered sequential circuit learning by encoding temporal correlations. However, it suffers from significant limitations including prolonged execution times and architectural inefficiencies. To address these issues, we introduce DeepSeq2, a novel framework that enhances the learning of sequential circuits, by innovatively mapping it into three distinct embedding spaces-structure, function, and sequential behavior-allowing for a more nuanced representation that captures the inherent complexities of circuit dynamics. By employing an efficient Directed Acyclic Graph Neural Network (DAG-GNN) that circumvents the recursive propagation used in DeepSeq, DeepSeq2 significantly reduces execution times and improves model scalability. Moreover, DeepSeq2 incorporates a unique supervision mechanism that captures transitioning behaviors within circuits more effectively. DeepSeq2 sets a new benchmark in sequential circuit representation learning, outperforming prior works in power estimation and reliability analysis.
