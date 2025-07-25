---
layout: paper_detail
title: "LAAG-RV: LLM Assisted Assertion Generation for RTL Design Verification"
date: 2024-08-13
arxiv_url: http://arxiv.org/abs/2409.15281v1
---

Writing SystemVerilog Assertions (SVA) is an important but complex step in verifying Register Transfer Level (RTL) designs. Conventionally, experts need to understand the design specifications and write the SVA assertions, which is time-consuming and error-prone. However, with the recent advancement of transformer models, the Large Language Models (LLMs) assisted assertion generation for design verification is gaining interest in recent times. Motivated by this, we proposed a novel LLM-based framework, LAAG-RV, to generate SVA from the natural language specifications of the design. Our framework provides a one-time Verilog loop for signal synchronization in the generated SVA to improve the generated assertion quality. For our experiments, we created a custom LLM based on OpenAI GPT-4. Furthermore, we developed test cases to validate the LLM-generated assertions. Initial observations show that some generated assertions contain issues and did not pass all the test cases. However, by iteratively prompting the LLMs using carefully crafted manual prompts derived from test case failures in a simulator, the framework can generate correct SVAs. Our results on OpenTitan designs demonstrate that LLMs significantly simplify the process of generating assertions, making it efficient and less error-prone.
