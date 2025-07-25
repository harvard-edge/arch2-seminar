---
layout: paper_detail
title: "Automatic Routability Predictor Development Using Neural Architecture Search"
date: 2020-12-03
arxiv_url: http://arxiv.org/abs/2012.01737v2
---

The rise of machine learning technology inspires a boom of its applications in electronic design automation (EDA) and helps improve the degree of automation in chip designs. However, manually crafted machine learning models require extensive human expertise and tremendous engineering efforts. In this work, we leverage neural architecture search (NAS) to automate the development of high-quality neural architectures for routability prediction, which can help to guide cell placement toward routable solutions. Our search method supports various operations and highly flexible connections, leading to architectures significantly different from all previous human-crafted models. Experimental results on a large dataset demonstrate that our automatically generated neural architectures clearly outperform multiple representative manually crafted solutions. Compared to the best case of manually crafted models, NAS-generated models achieve 5.85% higher Kendall's $\tau$ in predicting the number of nets with DRC violations and 2.12% better area under ROC curve (ROC-AUC) in DRC hotspot detection. Moreover, compared with human-crafted models, which easily take weeks to develop, our efficient NAS approach finishes the whole automatic search process with only 0.3 days.
