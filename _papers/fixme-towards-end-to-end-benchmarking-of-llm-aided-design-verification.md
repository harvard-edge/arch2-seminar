---
layout: paper_detail
title: "FIXME: Towards End-to-End Benchmarking of LLM-Aided Design Verification"
date: 2025-07-06
arxiv_url: http://arxiv.org/abs/2507.04276v1
---

Despite the transformative potential of Large Language Models (LLMs) in hardware design, a comprehensive evaluation of their capabilities in design verification remains underexplored. Current efforts predominantly focus on RTL generation and basic debugging, overlooking the critical domain of functional verification, which is the primary bottleneck in modern design methodologies due to the rapid escalation of hardware complexity. We present FIXME, the first end-to-end, multi-model, and open-source evaluation framework for assessing LLM performance in hardware functional verification (FV) to address this crucial gap. FIXME introduces a structured three-level difficulty hierarchy spanning six verification sub-domains and 180 diverse tasks, enabling in-depth analysis across the design lifecycle. Leveraging a collaborative AI-human approach, we construct a high-quality dataset using 100% silicon-proven designs, ensuring comprehensive coverage of real-world challenges. Furthermore, we enhance the functional coverage by 45.57% through expert-guided optimization. By rigorously evaluating state-of-the-art LLMs such as GPT-4, Claude3, and LlaMA3, we identify key areas for improvement and outline promising research directions to unlock the full potential of LLM-driven automation in hardware design verification. The benchmark is available at https://github.com/ChatDesignVerification/FIXME.
