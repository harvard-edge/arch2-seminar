---
layout: paper_detail
title: "Towards the Imagenets of ML4EDA"
date: 2023-10-16
arxiv_url: http://arxiv.org/abs/2310.10560v1
---

Despite the growing interest in ML-guided EDA tools from RTL to GDSII, there are no standard datasets or prototypical learning tasks defined for the EDA problem domain. Experience from the computer vision community suggests that such datasets are crucial to spur further progress in ML for EDA. Here we describe our experience curating two large-scale, high-quality datasets for Verilog code generation and logic synthesis. The first, VeriGen, is a dataset of Verilog code collected from GitHub and Verilog textbooks. The second, OpenABC-D, is a large-scale, labeled dataset designed to aid ML for logic synthesis tasks. The dataset consists of 870,000 And-Inverter-Graphs (AIGs) produced from 1500 synthesis runs on a large number of open-source hardware projects. In this paper we will discuss challenges in curating, maintaining and growing the size and scale of these datasets. We will also touch upon questions of dataset quality and security, and the use of novel data augmentation tools that are tailored for the hardware domain.
