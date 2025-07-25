---
layout: paper_detail
title: "Neural Model Checking"
date: 2024-10-31
arxiv_url: http://arxiv.org/abs/2410.23790v1
---

We introduce a machine learning approach to model checking temporal logic, with application to formal hardware verification. Model checking answers the question of whether every execution of a given system satisfies a desired temporal logic specification. Unlike testing, model checking provides formal guarantees. Its application is expected standard in silicon design and the EDA industry has invested decades into the development of performant symbolic model checking algorithms. Our new approach combines machine learning and symbolic reasoning by using neural networks as formal proof certificates for linear temporal logic. We train our neural certificates from randomly generated executions of the system and we then symbolically check their validity using satisfiability solving which, upon the affirmative answer, establishes that the system provably satisfies the specification. We leverage the expressive power of neural networks to represent proof certificates as well as the fact that checking a certificate is much simpler than finding one. As a result, our machine learning procedure for model checking is entirely unsupervised, formally sound, and practically effective. We experimentally demonstrate that our method outperforms the state-of-the-art academic and commercial model checkers on a set of standard hardware designs written in SystemVerilog.
