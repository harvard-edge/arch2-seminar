---
layout: paper_detail
title: "The Power of Graph Signal Processing for Chip Placement Acceleration"
date: 2025-02-24
arxiv_url: http://arxiv.org/abs/2502.17632v1
---

Placement is a critical task with high computation complexity in VLSI physical design. Modern analytical placers formulate the placement objective as a nonlinear optimization task, which suffers a long iteration time. To accelerate and enhance the placement process, recent studies have turned to deep learning-based approaches, particularly leveraging graph convolution networks (GCNs). However, learning-based placers require time- and data-consuming model training due to the complexity of circuit placement that involves large-scale cells and design-specific graph statistics.   This paper proposes GiFt, a parameter-free technique for accelerating placement, rooted in graph signal processing. GiFt excels at capturing multi-resolution smooth signals of circuit graphs to generate optimized placement solutions without the need for time-consuming model training, and meanwhile significantly reduces the number of iterations required by analytical placers. Experimental results show that GiFt significantly improving placement efficiency, while achieving competitive or superior performance compared to state-of-the-art placers. In particular, compared to DREAMPlace, the recently proposed GPU-accelerated analytical placer, GF-Placer improves total runtime over 45%.
