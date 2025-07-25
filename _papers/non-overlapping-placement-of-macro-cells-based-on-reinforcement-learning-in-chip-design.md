---
layout: paper_detail
title: "Non-Overlapping Placement of Macro Cells based on Reinforcement Learning in Chip Design"
date: 2024-07-26
arxiv_url: http://arxiv.org/abs/2407.18499v3
---

Due to the increasing complexity of chip design, existing placement methods still have many shortcomings in dealing with macro cells coverage and optimization efficiency. Aiming at the problems of layout overlap, inferior performance, and low optimization efficiency in existing chip design methods, this paper proposes an end-to-end placement method, SRLPlacer, based on reinforcement learning. First, the placement problem is transformed into a Markov decision process by establishing the coupling relationship graph model between macro cells to learn the strategy for optimizing layouts. Secondly, the whole placement process is optimized after integrating the standard cell layout. By assessing on the public benchmark ISPD2005, the proposed SRLPlacer can effectively solve the overlap problem between macro cells while considering routing congestion and shortening the total wire length to ensure routability. Codes are available at https://github.com/zhouyusd/SRLPlacer.
