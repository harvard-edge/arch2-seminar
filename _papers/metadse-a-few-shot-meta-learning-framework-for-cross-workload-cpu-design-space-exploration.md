---
layout: paper_detail
title: "MetaDSE: A Few-shot Meta-learning Framework for Cross-workload CPU Design Space Exploration"
date: 2025-04-18
arxiv_url: http://arxiv.org/abs/2504.13568v1
---

Cross-workload design space exploration (DSE) is crucial in CPU architecture design. Existing DSE methods typically employ the transfer learning technique to leverage knowledge from source workloads, aiming to minimize the requirement of target workload simulation. However, these methods struggle with overfitting, data ambiguity, and workload dissimilarity.   To address these challenges, we reframe the cross-workload CPU DSE task as a few-shot meta-learning problem and further introduce MetaDSE. By leveraging model agnostic meta-learning, MetaDSE swiftly adapts to new target workloads, greatly enhancing the efficiency of cross-workload CPU DSE. Additionally, MetaDSE introduces a novel knowledge transfer method called the workload-adaptive architectural mask algorithm, which uncovers the inherent properties of the architecture. Experiments on SPEC CPU 2017 demonstrate that MetaDSE significantly reduces prediction error by 44.3\% compared to the state-of-the-art. MetaDSE is open-sourced and available at this \href{https://anonymous.4open.science/r/Meta_DSE-02F8}{anonymous GitHub.}
