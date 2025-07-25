---
layout: paper_detail
title: "Hardware Trojan Detection using Graph Neural Networks"
date: 2022-04-25
arxiv_url: http://arxiv.org/abs/2204.11431v1
---

The globalization of the Integrated Circuit (IC) supply chain has moved most of the design, fabrication, and testing process from a single trusted entity to various untrusted third-party entities around the world. The risk of using untrusted third-Party Intellectual Property (3PIP) is the possibility for adversaries to insert malicious modifications known as Hardware Trojans (HTs). These HTs can compromise the integrity, deteriorate the performance, and deny the functionality of the intended design. Various HT detection methods have been proposed in the literature; however, many fall short due to their reliance on a golden reference circuit, a limited detection scope, the need for manual code review, or the inability to scale with large modern designs. We propose a novel golden reference-free HT detection method for both Register Transfer Level (RTL) and gate-level netlists by leveraging Graph Neural Networks (GNNs) to learn the behavior of the circuit through a Data Flow Graph (DFG) representation of the hardware design. We evaluate our model on a custom dataset by expanding the Trusthub HT benchmarks \cite{trusthub1}. The results demonstrate that our approach detects unknown HTs with 97% recall (true positive rate) very fast in 21.1ms for RTL and 84% recall in 13.42s for Gate-Level Netlist.
