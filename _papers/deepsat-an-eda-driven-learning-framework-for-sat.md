---
layout: paper_detail
title: "DeepSAT: An EDA-Driven Learning Framework for SAT"
date: 2022-05-27
arxiv_url: http://arxiv.org/abs/2205.13745v2
---

We present DeepSAT, a novel end-to-end learning framework for the Boolean satisfiability (SAT) problem. Unlike existing solutions trained on random SAT instances with relatively weak supervision, we propose applying the knowledge of the well-developed electronic design automation (EDA) field for SAT solving. Specifically, we first resort to logic synthesis algorithms to pre-process SAT instances into optimized and-inverter graphs (AIGs). By doing so, the distribution diversity among various SAT instances can be dramatically reduced, which facilitates improving the generalization capability of the learned model. Next, we regard the distribution of SAT solutions being a product of conditional Bernoulli distributions. Based on this observation, we approximate the SAT solving procedure with a conditional generative model, leveraging a novel directed acyclic graph neural network (DAGNN) with two polarity prototypes for conditional SAT modeling. To effectively train the generative model, with the help of logic simulation tools, we obtain the probabilities of nodes in the AIG being logic `1' as rich supervision. We conduct comprehensive experiments on various SAT problems. Our results show that, DeepSAT achieves significant accuracy improvements over state-of-the-art learning-based SAT solutions, especially when generalized to SAT instances that are relatively large or with diverse distributions.
