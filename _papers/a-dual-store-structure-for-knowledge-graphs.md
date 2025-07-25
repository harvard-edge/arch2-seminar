---
layout: paper_detail
title: "A Dual-Store Structure for Knowledge Graphs"
date: 2020-12-13
arxiv_url: http://arxiv.org/abs/2012.06966v1
---

To effectively manage increasing knowledge graphs in various domains, a hot research topic, knowledge graph storage management, has emerged. Existing methods are classified to relational stores and native graph stores. Relational stores are able to store large-scale knowledge graphs and convenient in updating knowledge, but the query performance weakens obviously when the selectivity of a knowledge graph query is large. Native graph stores are efficient in processing complex knowledge graph queries due to its index-free adjacent property, but they are inapplicable to manage a large-scale knowledge graph due to limited storage budgets or inflexible updating process. Motivated by this, we propose a dual-store structure which leverages a graph store to accelerate the complex query process in the relational store. However, it is challenging to determine what data to transfer from relational store to graph store at what time. To address this problem, we formulate it as a Markov Decision Process and derive a physical design tuner DOTIL based on reinforcement learning. With DOTIL, the dual-store structure is adaptive to dynamic changing workloads. Experimental results on real knowledge graphs demonstrate that our proposed dual-store structure improves query performance up to average 43.72% compared with the most commonly used relational stores.
