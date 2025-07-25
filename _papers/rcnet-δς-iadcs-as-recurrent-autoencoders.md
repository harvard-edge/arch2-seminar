---
layout: paper_detail
title: "RCNet: $ΔΣ$ IADCs as Recurrent AutoEncoders"
date: 2025-06-20
arxiv_url: http://arxiv.org/abs/2506.16903v1
---

This paper proposes a deep learning model (RCNet) for Delta-Sigma ($\Delta\Sigma$) ADCs. Recurrent Neural Networks (RNNs) allow to describe both modulators and filters. This analogy is applied to Incremental ADCs (IADC). High-end optimizers combined with full-custom losses are used to define additional hardware design constraints: quantized weights, signal saturation, temporal noise injection, devices area. Focusing on DC conversion, our early results demonstrate that $SNR$ defined as an Effective Number Of Bits (ENOB) can be optimized under a certain hardware mapping complexity. The proposed RCNet succeeded to provide design tradeoffs in terms of $SNR$ ($>$13bit) versus area constraints ($<$14pF total capacitor) at a given $OSR$ (80 samples). Interestingly, it appears that the best RCNet architectures do not necessarily rely on high-order modulators, leveraging additional topology exploration degrees of freedom.
