---
layout: paper_detail
title: "DRAGON (Differentiable Graph Execution) : A suite of Hardware Simulation and Optimization tools for Modern AI/Non-AI Workloads"
date: 2022-04-13
arxiv_url: http://arxiv.org/abs/2204.06676v8
---

We introduce DRAGON, a fast and explainable hardware simulation and optimization toolchain that enables hardware architects to simulate hardware designs, and to optimize hardware designs to efficiently execute workloads.   The DRAGON toolchain provides the following tools: Hardware Model Generator (DGen), Hardware Simulator (DSim) and Hardware Optimizer (DOpt).   DSim provides the simulation of running algorithms (represented as data-flow graphs) on hardware described. DGen describes the hardware in detail, with user input architectures/technology (represented in a custom description language). A novel methodology of gradient descent from the simulation allows us optimize the hardware model (giving the directions for improvements in technology parameters and design parameters), provided by Dopt.   DRAGON framework (DSim) is much faster than previously avaible works for simulation, which is possible through performance-first code writing practices, mathematical formulas for common computing operations to avoid cycle-accurate simulation steps, efficient algorithms for mapping, and data-structure representations for hardware state. DRAGON framework (Dopt) generates performance optimized architectures for both AI and Non-AI Workloads, and provides technology improvement directions for 100x-1000x better future computing systems.
