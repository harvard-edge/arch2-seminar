---
layout: paper_detail
title: "A Machine Learning Framework for Register Placement Optimization in Digital Circuit Design"
date: 2018-01-06
arxiv_url: http://arxiv.org/abs/1801.02620v1
---

In modern digital circuit back-end design, designers heavily rely on electronic-design-automoation (EDA) tool to close timing. However, the heuristic algorithms used in the place and route tool usually does not result in optimal solution. Thus, significant design effort is used to tune parameters or provide user constraints or guidelines to improve the tool performance. In this paper, we targeted at those optimization space left behind by the EDA tools and propose a machine learning framework that helps to define what are the guidelines and constraints for registers placement, which can yield better performance and quality for back-end design. In other words, the framework is trying to learn what are the flaws of the existing EDA tools and tries to optimize it by providing additional information. We discuss what is the proper input feature vector to be extracted, and what is metric to be used for reference output. We also develop a scheme to generate perturbed training samples using existing design based on Gaussian randomization. By applying our methodology, we are able to improve the design runtime by up to 36% and timing quality by up to 23%.
