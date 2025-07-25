---
layout: paper_detail
title: "A Novel Frequency-Spatial Domain Aware Network for Fast Thermal Prediction in 2.5D ICs"
date: 2025-04-19
arxiv_url: http://arxiv.org/abs/2504.14237v1
---

In the post-Moore era, 2.5D chiplet-based ICs present significant challenges in thermal management due to increased power density and thermal hotspots. Neural network-based thermal prediction models can perform real-time predictions for many unseen new designs. However, existing CNN-based and GCN-based methods cannot effectively capture the global thermal features, especially for high-frequency components, hindering prediction accuracy enhancement. In this paper, we propose a novel frequency-spatial dual domain aware prediction network (FSA-Heat) for fast and high-accuracy thermal prediction in 2.5D ICs. It integrates high-to-low frequency and spatial domain encoder (FSTE) module with frequency domain cross-scale interaction module (FCIFormer) to achieve high-to-low frequency and global-to-local thermal dissipation feature extraction. Additionally, a frequency-spatial hybrid loss (FSL) is designed to effectively attenuate high-frequency thermal gradient noise and spatial misalignments. The experimental results show that the performance enhancements offered by our proposed method are substantial, outperforming the newly-proposed 2.5D method, GCN+PNA, by considerable margins (over 99% RMSE reduction, 4.23X inference time speedup). Moreover, extensive experiments demonstrate that FSA-Heat also exhibits robust generalization capabilities.
