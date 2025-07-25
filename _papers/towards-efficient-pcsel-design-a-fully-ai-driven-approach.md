---
layout: paper_detail
title: "Towards Efficient PCSEL Design: A Fully AI-driven Approach"
date: 2025-03-14
arxiv_url: http://arxiv.org/abs/2503.11022v4
---

We present an fully AI-driven design framework for photonic crystals (PhCs), engineered to achieve high efficiency in photonic crystal surface-emitting lasers (PCSELs). By discretizing the PhC structure into a grid, where the edges of the holes are represented by the cross-sections of two-dimensional Gaussian surfaces, we achieve high-degree-of-freedom and fabrication-friendly hole design. Coupled-wave theory (CWT) generates a dataset by evaluating surface-emitting efficiency ($SEE$) and quality factor ($Q$) of PhC designs, while a multi-layered neural network (NN) learns and extracts essential features from these designs. Finally, black-box optimization (BBO) is employed to fine-tune the photonic crystal structure, enabling a fully AI-driven design process. The model achieves high prediction accuracy, with Pearson correlation coefficients of 0.780 for $SEE$ and 0.887 for the log-transformed $Q$. Additionally, we perform Shapley value analysis to identify the most important Fourier coefficients, providing insights into the factors that impact the performance of PCSEL designs. Our work accelerates the design process by over 1,000,000 times compared to traditional FDTD simulations, reducing parameter optimization from two weeks to just one second. Our work speeds up the design process and enables efficient optimization of high-performance PCSELs, driving the development of fully photonic design automation (PDA).
