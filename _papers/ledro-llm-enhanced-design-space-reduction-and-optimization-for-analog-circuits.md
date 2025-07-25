---
layout: paper_detail
title: "LEDRO: LLM-Enhanced Design Space Reduction and Optimization for Analog Circuits"
date: 2024-11-19
arxiv_url: http://arxiv.org/abs/2411.12930v2
---

Traditional approaches for designing analog circuits are time-consuming and require significant human expertise. Existing automation efforts using methods like Bayesian Optimization (BO) and Reinforcement Learning (RL) are sub-optimal and costly to generalize across different topologies and technology nodes. In our work, we introduce a novel approach, LEDRO, utilizing Large Language Models (LLMs) in conjunction with optimization techniques to iteratively refine the design space for analog circuit sizing. LEDRO is highly generalizable compared to other RL and BO baselines, eliminating the need for design annotation or model training for different topologies or technology nodes. We conduct a comprehensive evaluation of our proposed framework and baseline on 22 different Op-Amp topologies across four FinFET technology nodes. Results demonstrate the superior performance of LEDRO as it outperforms our best baseline by an average of 13% FoM improvement with 2.15x speed-up on low complexity Op-Amps and 48% FoM improvement with 1.7x speed-up on high complexity Op-Amps. This highlights LEDRO's effective performance, efficiency, and generalizability.
