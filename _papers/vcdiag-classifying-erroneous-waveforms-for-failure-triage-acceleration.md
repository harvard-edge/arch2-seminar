---
layout: paper_detail
title: "VCDiag: Classifying Erroneous Waveforms for Failure Triage Acceleration"
date: 2025-06-04
arxiv_url: http://arxiv.org/abs/2506.03590v2
---

Failure triage in design functional verification is critical but time-intensive, relying on manual specification reviews, log inspections, and waveform analyses. While machine learning (ML) has improved areas like stimulus generation and coverage closure, its application to RTL-level simulation failure triage, particularly for large designs, remains limited. VCDiag offers an efficient, adaptable approach using VCD data to classify failing waveforms and pinpoint likely failure locations. In the largest experiment, VCDiag achieves over 94% accuracy in identifying the top three most likely modules. The framework introduces a novel signal selection and statistical compression approach, achieving over 120x reduction in raw data size while preserving features essential for classification. It can also be integrated into diverse Verilog/SystemVerilog designs and testbenches.
