---
layout: paper_detail
title: "PowerNet: Transferable Dynamic IR Drop Estimation via Maximum Convolutional Neural Network"
date: 2020-11-26
arxiv_url: http://arxiv.org/abs/2011.13494v1
---

IR drop is a fundamental constraint required by almost all chip designs. However, its evaluation usually takes a long time that hinders mitigation techniques for fixing its violations. In this work, we develop a fast dynamic IR drop estimation technique, named PowerNet, based on a convolutional neural network (CNN). It can handle both vector-based and vectorless IR analyses. Moreover, the proposed CNN model is general and transferable to different designs. This is in contrast to most existing machine learning (ML) approaches, where a model is applicable only to a specific design. Experimental results show that PowerNet outperforms the latest ML method by 9% in accuracy for the challenging case of vectorless IR drop and achieves a 30 times speedup compared to an accurate IR drop commercial tool. Further, a mitigation tool guided by PowerNet reduces IR drop hotspots by 26% and 31% on two industrial designs, respectively, with very limited modification on their power grids.
