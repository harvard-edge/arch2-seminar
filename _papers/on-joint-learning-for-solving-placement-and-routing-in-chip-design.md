---
layout: paper_detail
title: "On Joint Learning for Solving Placement and Routing in Chip Design"
date: 2021-10-30
arxiv_url: http://arxiv.org/abs/2111.00234v2
---

For its advantage in GPU acceleration and less dependency on human experts, machine learning has been an emerging tool for solving the placement and routing problems, as two critical steps in modern chip design flow. Being still in its early stage, there are fundamental issues: scalability, reward design, and end-to-end learning paradigm etc. To achieve end-to-end placement learning, we first propose a joint learning method termed by DeepPlace for the placement of macros and standard cells, by the integration of reinforcement learning with a gradient based optimization scheme. To further bridge the placement with the subsequent routing task, we also develop a joint learning approach via reinforcement learning to fulfill both macro placement and routing, which is called DeepPR. One key design in our (reinforcement) learning paradigm involves a multi-view embedding model to encode both global graph level and local node level information of the input macros. Moreover, the random network distillation is devised to encourage exploration. Experiments on public chip design benchmarks show that our method can effectively learn from experience and also provides intermediate placement for the post standard cell placement, within few hours for training.
