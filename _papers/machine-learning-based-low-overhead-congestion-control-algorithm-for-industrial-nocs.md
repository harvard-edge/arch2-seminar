---
layout: paper_detail
title: "Machine Learning-based Low Overhead Congestion Control Algorithm for Industrial NoCs"
date: 2023-02-24
arxiv_url: http://arxiv.org/abs/2302.12779v1
---

Network-on-Chip (NoC) congestion builds up during heavy traffic load and cripples the system performance by stalling the cores. Moreover, congestion leads to wasted link bandwidth due to blocked buffers and bouncing packets. Existing approaches throttle the cores after congestion is detected, reducing efficiency and wasting line bandwidth unnecessarily. In contrast, we propose a lightweight machine learning-based technique that helps predict congestion in the network. Specifically, our proposed technique collects the features related to traffic at each destination. Then, it labels the features using a novel time reversal approach. The labeled data is used to design a low overhead and an explainable decision tree model used at runtime congestion control. Experimental evaluations with synthetic and real traffic on industrial 6$\times$6 NoC show that the proposed approach increases fairness and memory read bandwidth by up to 114\% with respect to existing congestion control technique while incurring less than 0.01\% of overhead.
