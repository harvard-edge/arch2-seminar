---
layout: paper_detail
title: "Worst-Case Dynamic Power Distribution Network Noise Prediction Using Convolutional Neural Network"
date: 2022-04-27
arxiv_url: http://arxiv.org/abs/2204.13109v1
---

Worst-case dynamic PDN noise analysis is an essential step in PDN sign-off to ensure the performance and reliability of chips. However, with the growing PDN size and increasing scenarios to be validated, it becomes very time- and resource-consuming to conduct full-stack PDN simulation to check the worst-case noise for different test vectors. Recently, various works have proposed machine learning based methods for supply noise prediction, many of which still suffer from large training overhead, inefficiency, or non-scalability. Thus, this paper proposed an efficient and scalable framework for the worst-case dynamic PDN noise prediction. The framework first reduces the spatial and temporal redundancy in the PDN and input current vector, and then employs efficient feature extraction as well as a novel convolutional neural network architecture to predict the worst-case dynamic PDN noise. Experimental results show that the proposed framework consistently outperforms the commercial tool and the state-of-the-art machine learning method with only 0.63-1.02% mean relative error and 25-69$\times$ speedup.
