---
layout: paper_detail
title: "Chip Placement with Diffusion Models"
date: 2024-07-17
arxiv_url: http://arxiv.org/abs/2407.12282v3
---

Macro placement is a vital step in digital circuit design that defines the physical location of large collections of components, known as macros, on a 2D chip. Because key performance metrics of the chip are determined by the placement, optimizing it is crucial. Existing learning-based methods typically fall short because of their reliance on reinforcement learning (RL), which is slow and struggles to generalize, requiring online training on each new circuit. Instead, we train a diffusion model capable of placing new circuits zero-shot, using guided sampling in lieu of RL to optimize placement quality. To enable such models to train at scale, we designed a capable yet efficient architecture for the denoising model, and propose a novel algorithm to generate large synthetic datasets for pre-training. To allow zero-shot transfer to real circuits, we empirically study the design decisions of our dataset generation algorithm, and identify several key factors enabling generalization. When trained on our synthetic data, our models generate high-quality placements on unseen, realistic circuits, achieving competitive performance on placement benchmarks compared to state-of-the-art methods.
