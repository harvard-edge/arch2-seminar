---
layout: paper_detail
title: "Improving Simulation Regression Efficiency using a Machine Learning-based Method in Design Verification"
date: 2024-05-24
arxiv_url: http://arxiv.org/abs/2405.17481v1
---

The verification throughput is becoming a major challenge bottleneck, since the complexity and size of SoC designs are still ever increasing. Simply adding more CPU cores and running more tests in parallel will not scale anymore. This paper discusses various methods of improving verification throughput: ranking and the new machine learning (ML) based technology introduced by Cadence i.e. Xcelium ML. Both methods aim at getting comparable coverage in less CPU time by applying more efficient stimulus. Ranking selects specific seeds that simply turned out to come up with the largest coverage in previous simulations, while Xcelium ML generates optimized patterns as a result of finding correlations between randomization points and achieved coverage of previous regressions. Quantified results as well as pros & cons of each approach are discussed in this paper at the example of three actual industry projects. Both Xcelium ML and Ranking methods gave comparable compression & speedup factors around 3 consistently. But the optimized ML based regressions simulated new random scenarios occasionally producing a coverage regain of more than 100%. Finally, a methodology is proposed to use Xcelium ML efficiently throughout the product development.
