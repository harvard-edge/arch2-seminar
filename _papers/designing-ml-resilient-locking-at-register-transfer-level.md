---
layout: paper_detail
title: "Designing ML-Resilient Locking at Register-Transfer Level"
date: 2022-03-10
arxiv_url: http://arxiv.org/abs/2203.05399v2
---

Various logic-locking schemes have been proposed to protect hardware from intellectual property piracy and malicious design modifications. Since traditional locking techniques are applied on the gate-level netlist after logic synthesis, they have no semantic knowledge of the design function. Data-driven, machine-learning (ML) attacks can uncover the design flaws within gate-level locking. Recent proposals on register-transfer level (RTL) locking have access to semantic hardware information. We investigate the resilience of ASSURE, a state-of-the-art RTL locking method, against ML attacks. We used the lessons learned to derive two ML-resilient RTL locking schemes built to reinforce ASSURE locking. We developed ML-driven security metrics to evaluate the schemes against an RTL adaptation of the state-of-the-art, ML-based SnapShot attack.
