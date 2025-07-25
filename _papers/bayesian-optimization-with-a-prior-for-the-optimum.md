---
layout: paper_detail
title: "Bayesian Optimization with a Prior for the Optimum"
date: 2020-06-25
arxiv_url: http://arxiv.org/abs/2006.14608v4
---

While Bayesian Optimization (BO) is a very popular method for optimizing expensive black-box functions, it fails to leverage the experience of domain experts. This causes BO to waste function evaluations on bad design choices (e.g., machine learning hyperparameters) that the expert already knows to work poorly. To address this issue, we introduce Bayesian Optimization with a Prior for the Optimum (BOPrO). BOPrO allows users to inject their knowledge into the optimization process in the form of priors about which parts of the input space will yield the best performance, rather than BO's standard priors over functions, which are much less intuitive for users. BOPrO then combines these priors with BO's standard probabilistic model to form a pseudo-posterior used to select which points to evaluate next. We show that BOPrO is around 6.67x faster than state-of-the-art methods on a common suite of benchmarks, and achieves a new state-of-the-art performance on a real-world hardware design application. We also show that BOPrO converges faster even if the priors for the optimum are not entirely accurate and that it robustly recovers from misleading priors.
