---
layout: paper_detail
title: "Theta-Resonance: A Single-Step Reinforcement Learning Method for Design Space Exploration"
date: 2022-11-03
arxiv_url: http://arxiv.org/abs/2211.02052v2
---

Given an environment (e.g., a simulator) for evaluating samples in a specified design space and a set of weighted evaluation metrics -- one can use Theta-Resonance, a single-step Markov Decision Process (MDP), to train an intelligent agent producing progressively more optimal samples. In Theta-Resonance, a neural network consumes a constant input tensor and produces a policy as a set of conditional probability density functions (PDFs) for sampling each design dimension. We specialize existing policy gradient algorithms in deep reinforcement learning (D-RL) in order to use evaluation feedback (in terms of cost, penalty or reward) to update our policy network with robust algorithmic stability and minimal design evaluations. We study multiple neural architectures (for our policy network) within the context of a simple SoC design space and propose a method of constructing synthetic space exploration problems to compare and improve design space exploration (DSE) algorithms. Although we only present categorical design spaces, we also outline how to use Theta-Resonance in order to explore continuous and mixed continuous-discrete design spaces.
