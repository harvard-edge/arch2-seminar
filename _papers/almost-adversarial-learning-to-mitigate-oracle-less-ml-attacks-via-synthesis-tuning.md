---
layout: paper_detail
title: "ALMOST: Adversarial Learning to Mitigate Oracle-less ML Attacks via Synthesis Tuning"
date: 2023-03-06
arxiv_url: http://arxiv.org/abs/2303.03372v1
---

Oracle-less machine learning (ML) attacks have broken various logic locking schemes. Regular synthesis, which is tailored for area-power-delay optimization, yields netlists where key-gate localities are vulnerable to learning. Thus, we call for security-aware logic synthesis. We propose ALMOST, a framework for adversarial learning to mitigate oracle-less ML attacks via synthesis tuning. ALMOST uses a simulated-annealing-based synthesis recipe generator, employing adversarially trained models that can predict state-of-the-art attacks' accuracies over wide ranges of recipes and key-gate localities. Experiments on ISCAS benchmarks confirm the attacks' accuracies drops to around 50\% for ALMOST-synthesized circuits, all while not undermining design optimization.
