---
layout: paper_detail
title: "OpenABC-D: A Large-Scale Dataset For Machine Learning Guided Integrated Circuit Synthesis"
date: 2021-10-21
arxiv_url: http://arxiv.org/abs/2110.11292v1
---

Logic synthesis is a challenging and widely-researched combinatorial optimization problem during integrated circuit (IC) design. It transforms a high-level description of hardware in a programming language like Verilog into an optimized digital circuit netlist, a network of interconnected Boolean logic gates, that implements the function. Spurred by the success of ML in solving combinatorial and graph problems in other domains, there is growing interest in the design of ML-guided logic synthesis tools. Yet, there are no standard datasets or prototypical learning tasks defined for this problem domain. Here, we describe OpenABC-D,a large-scale, labeled dataset produced by synthesizing open source designs with a leading open-source logic synthesis tool and illustrate its use in developing, evaluating and benchmarking ML-guided logic synthesis. OpenABC-D has intermediate and final outputs in the form of 870,000 And-Inverter-Graphs (AIGs) produced from 1500 synthesis runs plus labels such as the optimized node counts, and de-lay. We define a generic learning problem on this dataset and benchmark existing solutions for it. The codes related to dataset creation and benchmark models are available athttps://github.com/NYU-MLDA/OpenABC.git. The dataset generated is available athttps://archive.nyu.edu/handle/2451/63311
