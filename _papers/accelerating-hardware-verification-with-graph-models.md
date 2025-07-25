---
layout: paper_detail
title: "Accelerating Hardware Verification with Graph Models"
date: 2024-12-17
arxiv_url: http://arxiv.org/abs/2412.13374v2
---

The increasing complexity of modern processor and IP designs presents significant challenges in identifying and mitigating hardware flaws early in the IC design cycle. Traditional hardware fuzzing techniques, inspired by software testing, have shown promise but face scalability issues, especially at the gate-level netlist where bugs introduced during synthesis are often missed by RTL-level verification due to longer simulation times.   To address this, we introduce GraphFuzz, a graph-based hardware fuzzer designed for gate-level netlist verification. In this approach, hardware designs are modeled as graph nodes, with gate behaviors encoded as features. By leveraging graph learning algorithms, GraphFuzz efficiently detects hardware vulnerabilities by analyzing node patterns. Our evaluation across benchmark circuits and open-source processors demonstrates an average prediction accuracy of 80% and bug detection accuracy of 70%, highlighting the potential of graph-based methods for enhancing hardware verification.
