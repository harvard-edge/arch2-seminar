---
layout: paper_detail
title: "Compiler Optimization for Quantum Computing Using Reinforcement Learning"
date: 2022-12-08
arxiv_url: http://arxiv.org/abs/2212.04508v2
---

Any quantum computing application, once encoded as a quantum circuit, must be compiled before being executable on a quantum computer. Similar to classical compilation, quantum compilation is a sequential process with many compilation steps and numerous possible optimization passes. Despite the similarities, the development of compilers for quantum computing is still in its infancy -- lacking mutual consolidation on the best sequence of passes, compatibility, adaptability, and flexibility. In this work, we take advantage of decades of classical compiler optimization and propose a reinforcement learning framework for developing optimized quantum circuit compilation flows. Through distinct constraints and a unifying interface, the framework supports the combination of techniques from different compilers and optimization tools in a single compilation flow. Experimental evaluations show that the proposed framework -- set up with a selection of compilation passes from IBM's Qiskit and Quantinuum's TKET -- significantly outperforms both individual compilers in 73% of cases regarding the expected fidelity. The framework is available on GitHub (https://github.com/cda-tum/MQTPredictor) as part of the Munich Quantum Toolkit (MQT).
