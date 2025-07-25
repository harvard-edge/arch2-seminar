---
layout: paper_detail
title: "Supervised Learning for Coverage-Directed Test Selection in Simulation-Based Verification"
date: 2022-05-17
arxiv_url: http://arxiv.org/abs/2205.08524v3
---

Constrained random test generation is one of the most widely adopted methods for generating stimuli for simulation-based verification. Randomness leads to test diversity, but tests tend to repeatedly exercise the same design logic. Constraints are written (typically manually) to bias random tests towards interesting, hard-to-reach, and yet-untested logic. However, as verification progresses, most constrained random tests yield little to no effect on functional coverage. If stimuli generation consumes significantly less resources than simulation, then a better approach involves randomly generating a large number of tests, selecting the most effective subset, and only simulating that subset. In this paper, we introduce a novel method for automatic constraint extraction and test selection. This method, which we call coverage-directed test selection, is based on supervised learning from coverage feedback. Our method biases selection towards tests that have a high probability of increasing functional coverage, and prioritises them for simulation. We show how coverage-directed test selection can reduce manual constraint writing, prioritise effective tests, reduce verification resource consumption, and accelerate coverage closure on a large, real-life industrial hardware design.
