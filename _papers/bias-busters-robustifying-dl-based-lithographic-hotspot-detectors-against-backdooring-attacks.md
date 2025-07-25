---
layout: paper_detail
title: "Bias Busters: Robustifying DL-based Lithographic Hotspot Detectors Against Backdooring Attacks"
date: 2020-04-26
arxiv_url: http://arxiv.org/abs/2004.12492v1
---

Deep learning (DL) offers potential improvements throughout the CAD tool-flow, one promising application being lithographic hotspot detection. However, DL techniques have been shown to be especially vulnerable to inference and training time adversarial attacks. Recent work has demonstrated that a small fraction of malicious physical designers can stealthily "backdoor" a DL-based hotspot detector during its training phase such that it accurately classifies regular layout clips but predicts hotspots containing a specially crafted trigger shape as non-hotspots. We propose a novel training data augmentation strategy as a powerful defense against such backdooring attacks. The defense works by eliminating the intentional biases introduced in the training data but does not require knowledge of which training samples are poisoned or the nature of the backdoor trigger. Our results show that the defense can drastically reduce the attack success rate from 84% to ~0%.
