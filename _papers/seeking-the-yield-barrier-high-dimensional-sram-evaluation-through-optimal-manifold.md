---
layout: paper_detail
title: "Seeking the Yield Barrier: High-Dimensional SRAM Evaluation Through Optimal Manifold"
date: 2023-07-28
arxiv_url: http://arxiv.org/abs/2307.15773v1
---

Being able to efficiently obtain an accurate estimate of the failure probability of SRAM components has become a central issue as model circuits shrink their scale to submicrometer with advanced technology nodes. In this work, we revisit the classic norm minimization method. We then generalize it with infinite components and derive the novel optimal manifold concept, which bridges the surrogate-based and importance sampling (IS) yield estimation methods. We then derive a sub-optimal manifold, optimal hypersphere, which leads to an efficient sampling method being aware of the failure boundary called onion sampling. Finally, we use a neural coupling flow (which learns from samples like a surrogate model) as the IS proposal distribution. These combinations give rise to a novel yield estimation method, named Optimal Manifold Important Sampling (OPTIMIS), which keeps the advantages of the surrogate and IS methods to deliver state-of-the-art performance with robustness and consistency, with up to 3.5x in efficiency and 3x in accuracy over the best of SOTA methods in High-dimensional SRAM evaluation.
