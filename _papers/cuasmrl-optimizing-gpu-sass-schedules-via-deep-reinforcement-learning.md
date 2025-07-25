---
layout: paper_detail
title: "CuAsmRL: Optimizing GPU SASS Schedules via Deep Reinforcement Learning"
date: 2025-01-14
arxiv_url: http://arxiv.org/abs/2501.08071v1
---

Large language models (LLMs) are remarked by their substantial computational requirements. To mitigate the cost, researchers develop specialized CUDA kernels, which often fuse several tensor operations to maximize the utilization of GPUs as much as possible. However, those specialized kernels may still leave performance on the table as CUDA assembly experts show that manual optimization of GPU SASS schedules can lead to better performance, and trial-and-error is largely employed to manually find the best GPU SASS schedules.   In this work, we employ an automatic approach to optimize GPU SASS schedules, which thus can be integrated into existing compiler frameworks. The key to automatic optimization is training an RL agent to mimic how human experts perform manual scheduling. To this end, we formulate an assembly game, where RL agents can play to find the best GPU SASS schedules. The assembly game starts from a \textit{-O3} optimized SASS schedule, and the RL agents can iteratively apply actions to mutate the current schedules. Positive rewards are generated if the mutated schedules get higher throughput by executing on GPUs. Experiments show that CuAsmRL can further improve the performance of existing specialized CUDA kernels transparently by up to $26\%$, and on average $9\%$. Moreover, it is used as a tool to reveal potential optimization moves learned automatically.
