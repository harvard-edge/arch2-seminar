---
layout: paper_detail
title: "DeepGate: Learning Neural Representations of Logic Gates"
date: 2021-11-26
arxiv_url: http://arxiv.org/abs/2111.14616v3
---

Applying deep learning (DL) techniques in the electronic design automation (EDA) field has become a trending topic. Most solutions apply well-developed DL models to solve specific EDA problems. While demonstrating promising results, they require careful model tuning for every problem. The fundamental question on "How to obtain a general and effective neural representation of circuits?" has not been answered yet. In this work, we take the first step towards solving this problem. We propose DeepGate, a novel representation learning solution that effectively embeds both logic function and structural information of a circuit as vectors on each gate. Specifically, we propose transforming circuits into unified and-inverter graph format for learning and using signal probabilities as the supervision task in DeepGate. We then introduce a novel graph neural network that uses strong inductive biases in practical circuits as learning priors for signal probability prediction. Our experimental results show the efficacy and generalization capability of DeepGate.
