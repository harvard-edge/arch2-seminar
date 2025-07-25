---
layout: paper_detail
title: "OpeNPDN: A Neural-network-based Framework for Power Delivery Network Synthesis"
date: 2021-10-27
arxiv_url: http://arxiv.org/abs/2110.14184v1
---

Power delivery network (PDN) design is a nontrivial, time-intensive, and iterative task. Correct PDN design must account for considerations related to power bumps, currents, blockages, and signal congestion distribution patterns. This work proposes a machine learning-based methodology that employs a set of predefined PDN templates. At the floorplan stage, coarse estimates of current, congestion, macro/blockages, and C4 bump distributions are used to synthesize a grid for early design. At the placement stage, the grid is incrementally refined based on more accurate and fine-grained distributions of current and congestion. At each stage, a convolutional neural network (CNN) selects an appropriate PDN template for each region on the chip, building a safe-by-construction PDN that meets IR drop and electromigration (EM) specifications. The CNN is initially trained using a large synthetically-created dataset, following which transfer learning is leveraged to bridge the gap between real-circuit data (with a limited dataset size) and synthetically-generated data. On average, the optimization of the PDN frees thousands of routing tracks in congestion-critical regions, when compared to a globally uniform PDN, while staying within the IR drop and EM limits.
