---
layout: paper_detail
title: "Deep Learning Assisted End-to-End Synthesis of mm-Wave Passive Networks with 3D EM Structures: A Study on A Transformer-Based Matching Network"
date: 2022-01-06
arxiv_url: http://arxiv.org/abs/2201.02141v1
---

This paper presents a deep learning assisted synthesis approach for direct end-to-end generation of RF/mm-wave passive matching network with 3D EM structures. Different from prior approaches that synthesize EM structures from target circuit component values and target topologies, our proposed approach achieves the direct synthesis of the passive network given the network topology from desired performance values as input. We showcase the proposed synthesis Neural Network (NN) model on an on-chip 1:1 transformer-based impedance matching network. By leveraging parameter sharing, the synthesis NN model successfully extracts relevant features from the input impedance and load capacitors, and predict the transformer 3D EM geometry in a 45nm SOI process that will match the standard 50$\Omega$ load to the target input impedance while absorbing the two loading capacitors. As a proof-of-concept, several example transformer geometries were synthesized, and verified in Ansys HFSS to provide the desired input impedance.
