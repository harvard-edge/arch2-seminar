---
layout: paper_detail
title: "Feature Engineering for Scalable Application-Level Post-Silicon Debugging"
date: 2021-02-08
arxiv_url: http://arxiv.org/abs/2102.04554v1
---

We present systematic and efficient solutions for both observability enhancement and root-cause diagnosis of post-silicon System-on-Chips (SoCs) validation with diverse usage scenarios. We model specification of interacting flows in typical applications for message selection. Our method for message selection optimizes flow specification coverage and trace buffer utilization. We define the diagnosis problem as identifying buggy traces as outliers and bug-free traces as inliers/normal behaviors, for which we use unsupervised learning algorithms for outlier detection. Instead of direct application of machine learning algorithms over trace data using the signals as raw features, we use feature engineering to transform raw features into more sophisticated features using domain specific operations. The engineered features are highly relevant to the diagnosis task and are generic to be applied across any hardware designs. We present debugging and root cause analysis of subtle post-silicon bugs in industry-scale OpenSPARC T2 SoC. We achieve a trace buffer utilization of 98.96\% with a flow specification coverage of 94.3\% (average). Our diagnosis method was able to diagnose up to 66.7\% more bugs and took up to 847$\times$ less diagnosis time as compared to the manual debugging with a diagnosis precision of 0.769.
