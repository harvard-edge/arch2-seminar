---
layout: paper_detail
title: "AutoCkt: Deep Reinforcement Learning of Analog Circuit Designs"
date: 2020-01-06
arxiv_url: http://arxiv.org/abs/2001.01808v2
---

Domain specialization under energy constraints in deeply-scaled CMOS has been driving the need for agile development of Systems on a Chip (SoCs). While digital subsystems have design flows that are conducive to rapid iterations from specification to layout, analog and mixed-signal modules face the challenge of a long human-in-the-middle iteration loop that requires expert intuition to verify that post-layout circuit parameters meet the original design specification. Existing automated solutions that optimize circuit parameters for a given target design specification have limitations of being schematic-only, inaccurate, sample-inefficient or not generalizable. This work presents AutoCkt, a machine learning optimization framework trained using deep reinforcement learning that not only finds post-layout circuit parameters for a given target specification, but also gains knowledge about the entire design space through a sparse subsampling technique. Our results show that for multiple circuit topologies, AutoCkt is able to converge and meet all target specifications on at least 96.3% of tested design goals in schematic simulation, on average 40X faster than a traditional genetic algorithm. Using the Berkeley Analog Generator, AutoCkt is able to design 40 LVS passed operational amplifiers in 68 hours, 9.6X faster than the state-of-the-art when considering layout parasitics.
