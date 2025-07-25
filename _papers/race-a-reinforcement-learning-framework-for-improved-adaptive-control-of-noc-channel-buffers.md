---
layout: paper_detail
title: "RACE: A Reinforcement Learning Framework for Improved Adaptive Control of NoC Channel Buffers"
date: 2022-05-26
arxiv_url: http://arxiv.org/abs/2205.13130v1
---

Network-on-chip (NoC) architectures rely on buffers to store flits to cope with contention for router resources during packet switching. Recently, reversible multi-function channel (RMC) buffers have been proposed to simultaneously reduce power and enable adaptive NoC buffering between adjacent routers. While adaptive buffering can improve NoC performance by maximizing buffer utilization, controlling the RMC buffer allocations requires a congestion-aware, scalable, and proactive policy. In this work, we present RACE, a novel reinforcement learning (RL) framework that utilizes better awareness of network congestion and a new reward metric ("falsefulls") to help guide the RL agent towards better RMC buffer control decisions. We show that RACE reduces NoC latency by up to 48.9%, and energy consumption by up to 47.1% against state-of-the-art NoC buffer control policies.
