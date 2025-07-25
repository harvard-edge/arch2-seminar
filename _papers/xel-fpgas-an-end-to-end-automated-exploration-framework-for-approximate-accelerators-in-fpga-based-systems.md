---
layout: paper_detail
title: "Xel-FPGAs: An End-to-End Automated Exploration Framework for Approximate Accelerators in FPGA-Based Systems"
date: 2023-03-08
arxiv_url: http://arxiv.org/abs/2303.04734v3
---

Generation and exploration of approximate circuits and accelerators has been a prominent research domain to achieve energy-efficiency and/or performance improvements. This research has predominantly focused on ASICs, while not achieving similar gains when deployed for FPGA-based accelerator systems, due to the inherent architectural differences between the two. In this work, we propose a novel framework, Xel-FPGAs, which leverages statistical or machine learning models to effectively explore the architecture-space of state-of-the-art ASIC-based approximate circuits to cater them for FPGA-based systems given a simple RTL description of the target application. We have also evaluated the scalability of our framework on a multi-stage application using a hierarchical search strategy. The Xel-FPGAs framework is capable of reducing the exploration time by up to 95%, when compared to the default synthesis, place, and route approaches, while identifying an improved set of Pareto-optimal designs for a given application, when compared to the state-of-the-art. The complete framework is open-source and available online at https://github.com/ehw-fit/xel-fpgas.
