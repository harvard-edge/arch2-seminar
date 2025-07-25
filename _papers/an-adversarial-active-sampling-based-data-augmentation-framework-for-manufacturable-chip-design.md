---
layout: paper_detail
title: "An Adversarial Active Sampling-based Data Augmentation Framework for Manufacturable Chip Design"
date: 2022-10-27
arxiv_url: http://arxiv.org/abs/2210.15765v1
---

Lithography modeling is a crucial problem in chip design to ensure a chip design mask is manufacturable. It requires rigorous simulations of optical and chemical models that are computationally expensive. Recent developments in machine learning have provided alternative solutions in replacing the time-consuming lithography simulations with deep neural networks. However, the considerable accuracy drop still impedes its industrial adoption. Most importantly, the quality and quantity of the training dataset directly affect the model performance. To tackle this problem, we propose a litho-aware data augmentation (LADA) framework to resolve the dilemma of limited data and improve the machine learning model performance. First, we pretrain the neural networks for lithography modeling and a gradient-friendly StyleGAN2 generator. We then perform adversarial active sampling to generate informative and synthetic in-distribution mask designs. These synthetic mask images will augment the original limited training dataset used to finetune the lithography model for improved performance. Experimental results demonstrate that LADA can successfully exploits the neural network capacity by narrowing down the performance gap between the training and testing data instances.
