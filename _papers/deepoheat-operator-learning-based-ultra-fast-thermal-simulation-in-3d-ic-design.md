---
layout: paper_detail
title: "DeepOHeat: Operator Learning-based Ultra-fast Thermal Simulation in 3D-IC Design"
date: 2023-02-25
arxiv_url: http://arxiv.org/abs/2302.12949v1
---

Thermal issue is a major concern in 3D integrated circuit (IC) design. Thermal optimization of 3D IC often requires massive expensive PDE simulations. Neural network-based thermal prediction models can perform real-time prediction for many unseen new designs. However, existing works either solve 2D temperature fields only or do not generalize well to new designs with unseen design configurations (e.g., heat sources and boundary conditions). In this paper, for the first time, we propose DeepOHeat, a physics-aware operator learning framework to predict the temperature field of a family of heat equations with multiple parametric or non-parametric design configurations. This framework learns a functional map from the function space of multiple key PDE configurations (e.g., boundary conditions, power maps, heat transfer coefficients) to the function space of the corresponding solution (i.e., temperature fields), enabling fast thermal analysis and optimization by changing key design configurations (rather than just some parameters). We test DeepOHeat on some industrial design cases and compare it against Celsius 3D from Cadence Design Systems. Our results show that, for the unseen testing cases, a well-trained DeepOHeat can produce accurate results with $1000\times$ to $300000\times$ speedup.
