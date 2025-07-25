---
layout: paper_detail
title: "Extremal Testing for Network Software using LLMs"
date: 2025-07-16
arxiv_url: http://arxiv.org/abs/2507.11898v1
---

Physicists often manually consider extreme cases when testing a theory. In this paper, we show how to automate extremal testing of network software using LLMs in two steps: first, ask the LLM to generate input constraints (e.g., DNS name length limits); then ask the LLM to generate tests that violate the constraints. We demonstrate how easy this process is by generating extremal tests for HTTP, BGP and DNS implementations, each of which uncovered new bugs. We show how this methodology extends to centralized network software such as shortest path algorithms, and how LLMs can generate filtering code to reject extremal input. We propose using agentic AI to further automate extremal testing. LLM-generated extremal testing goes beyond an old technique in software testing called Boundary Value Analysis.
