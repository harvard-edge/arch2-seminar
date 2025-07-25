---
layout: paper_detail
title: "DeepFlow: A Cross-Stack Pathfinding Framework for Distributed AI Systems"
date: 2022-11-07
arxiv_url: http://arxiv.org/abs/2211.03309v2
---

Over the past decade, machine learning model complexity has grown at an extraordinary rate, as has the scale of the systems training such large models. However there is an alarmingly low hardware utilization (5-20%) in large scale AI systems. The low system utilization is a cumulative effect of minor losses across different layers of the stack, exacerbated by the disconnect between engineers designing different layers spanning across different industries. We propose CrossFlow, a novel framework that enables cross-layer analysis all the way from the technology layer to the algorithmic layer. We also propose DeepFlow (built on top of CrossFlow using machine learning techniques) to automate the design space exploration and co-optimization across different layers of the stack. We have validated CrossFlow accuracy with distributed training on real commercial hardware and showcase several DeepFlow case studies demonstrating pitfalls of not optimizing across the technology-hardware-software stack for what is likely, the most important workload driving large development investments in all aspects of computing stack.
