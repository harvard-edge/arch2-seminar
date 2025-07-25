---
layout: paper_detail
title: "PODTherm-GP: A Physics-based Data-Driven Approach for Effective Architecture-Level Thermal Simulation of Multi-Core CPUs"
date: 2023-05-03
arxiv_url: http://arxiv.org/abs/2305.01911v1
---

A thermal simulation methodology derived from the proper orthogonal decomposition (POD) and the Galerkin projection (GP), hereafter referred to as PODTherm-GP, is evaluated in terms of its efficiency and accuracy in a multi-core CPU. The GP projects the heat transfer equation onto a mathematical space whose basis functions are generated from thermal data enabled by the POD learning algorithm. The thermal solution data are collected from FEniCS using the finite element method (FEM) accounting for appropriate parametric variations. The GP incorporates physical principles of heat transfer in the methodology to reach high accuracy and efficiency. The dynamic power map for the CPU in FEM thermal simulation is generated from gem5 and McPACT, together with the SPLASH-2 benchmarks as the simulation workload. It is shown that PODTherm-GP offers an accurate thermal prediction of the CPU with a resolution as fine as the FEM. It is also demonstrated that PODTherm-GP is capable of predicting the dynamic thermal profile of the chip with a good accuracy beyond the training conditions. Additionally, the approach offers a reduction in degrees of freedom by more than 5 orders of magnitude and a speedup of 4 orders, compared to the FEM.
