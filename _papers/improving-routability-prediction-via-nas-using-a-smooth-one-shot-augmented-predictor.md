---
layout: paper_detail
title: "Improving Routability Prediction via NAS Using a Smooth One-shot Augmented Predictor"
date: 2024-11-21
arxiv_url: http://arxiv.org/abs/2411.14296v1
---

Routability optimization in modern EDA tools has benefited greatly from using machine learning (ML) models. Constructing and optimizing the performance of ML models continues to be a challenge. Neural Architecture Search (NAS) serves as a tool to aid in the construction and improvement of these models. Traditional NAS techniques struggle to perform well on routability prediction as a result of two primary factors. First, the separation between the training objective and the search objective adds noise to the NAS process. Secondly, the increased variance of the search objective further complicates performing NAS. We craft a novel NAS technique, coined SOAP-NAS, to address these challenges through novel data augmentation techniques and a novel combination of one-shot and predictor-based NAS. Results show that our technique outperforms existing solutions by 40% closer to the ideal performance measured by ROC-AUC (area under the receiver operating characteristic curve) in DRC hotspot detection. SOAPNet is able to achieve an ROC-AUC of 0.9802 and a query time of only 0.461 ms.
