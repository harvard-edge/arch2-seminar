---
layout: paper_detail
title: "TAFA: Design Automation of Analog Mixed-Signal FIR Filters Using Time Approximation Architecture"
date: 2021-12-15
arxiv_url: http://arxiv.org/abs/2112.07825v1
---

A digital finite impulse response (FIR) filter design is fully synthesizable, thanks to the mature CAD support of digital circuitry. On the contrary, analog mixed-signal (AMS) filter design is mostly a manual process, including architecture selection, schematic design, and layout. This work presents a systematic design methodology to automate AMS FIR filter design using a time approximation architecture without any tunable passive component, such as switched capacitor or resistor. It not only enhances the flexibility of the filter but also facilitates design automation with reduced analog complexity. The proposed design flow features a hybrid approximation scheme that automatically optimize the filter's impulse response in light of time quantization effects, which shows significant performance improvement with minimum designer's efforts in the loop. Additionally, a layout-aware regression model based on an artificial neural network (ANN), in combination with gradient-based search algorithm, is used to automate and expedite the filter design. With the proposed framework, we demonstrate rapid synthesis of AMS FIR filters in 65nm process from specification to layout.
