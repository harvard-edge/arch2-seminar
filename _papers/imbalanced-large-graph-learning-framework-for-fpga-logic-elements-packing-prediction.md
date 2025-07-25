---
layout: paper_detail
title: "Imbalanced Large Graph Learning Framework for FPGA Logic Elements Packing Prediction"
date: 2023-08-07
arxiv_url: http://arxiv.org/abs/2308.03231v1
---

Packing is a required step in a typical FPGA CAD flow. It has high impacts to the performance of FPGA placement and routing. Early prediction of packing results can guide design optimization and expedite design closure. In this work, we propose an imbalanced large graph learning framework, ImLG, for prediction of whether logic elements will be packed after placement. Specifically, we propose dedicated feature extraction and feature aggregation methods to enhance the node representation learning of circuit graphs. With imbalanced distribution of packed and unpacked logic elements, we further propose techniques such as graph oversampling and mini-batch training for this imbalanced learning task in large circuit graphs. Experimental results demonstrate that our framework can improve the F1 score by 42.82% compared to the most recent Gaussian-based prediction method. Physical design results show that the proposed method can assist the placer in improving routed wirelength by 0.93% and SLICE occupation by 0.89%.
