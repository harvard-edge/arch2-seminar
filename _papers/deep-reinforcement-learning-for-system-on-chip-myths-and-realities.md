---
layout: paper_detail
title: "Deep Reinforcement Learning for System-on-Chip: Myths and Realities"
date: 2022-07-29
arxiv_url: http://arxiv.org/abs/2207.14595v1
---

Neural schedulers based on deep reinforcement learning (DRL) have shown considerable potential for solving real-world resource allocation problems, as they have demonstrated significant performance gain in the domain of cluster computing. In this paper, we investigate the feasibility of neural schedulers for the domain of System-on-Chip (SoC) resource allocation through extensive experiments and comparison with non-neural, heuristic schedulers. The key finding is three-fold. First, neural schedulers designed for cluster computing domain do not work well for SoC due to i) heterogeneity of SoC computing resources and ii) variable action set caused by randomness in incoming jobs. Second, our novel neural scheduler technique, Eclectic Interaction Matching (EIM), overcomes the above challenges, thus significantly improving the existing neural schedulers. Specifically, we rationalize the underlying reasons behind the performance gain by the EIM-based neural scheduler. Third, we discover that the ratio of the average processing elements (PE) switching delay and the average PE computation time significantly impacts the performance of neural SoC schedulers even with EIM. Consequently, future neural SoC scheduler design must consider this metric as well as its implementation overhead for practical utility.
