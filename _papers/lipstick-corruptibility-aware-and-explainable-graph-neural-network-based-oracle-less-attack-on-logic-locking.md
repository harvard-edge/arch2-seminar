---
layout: paper_detail
title: "LIPSTICK: Corruptibility-Aware and Explainable Graph Neural Network-based Oracle-Less Attack on Logic Locking"
date: 2024-02-06
arxiv_url: http://arxiv.org/abs/2402.04235v1
---

In a zero-trust fabless paradigm, designers are increasingly concerned about hardware-based attacks on the semiconductor supply chain. Logic locking is a design-for-trust method that adds extra key-controlled gates in the circuits to prevent hardware intellectual property theft and overproduction. While attackers have traditionally relied on an oracle to attack logic-locked circuits, machine learning attacks have shown the ability to retrieve the secret key even without access to an oracle. In this paper, we first examine the limitations of state-of-the-art machine learning attacks and argue that the use of key hamming distance as the sole model-guiding structural metric is not always useful. Then, we develop, train, and test a corruptibility-aware graph neural network-based oracle-less attack on logic locking that takes into consideration both the structure and the behavior of the circuits. Our model is explainable in the sense that we analyze what the machine learning model has interpreted in the training process and how it can perform a successful attack. Chip designers may find this information beneficial in securing their designs while avoiding incremental fixes.
