---
layout: paper_detail
title: "ChipXplore: Natural Language Exploration of Hardware Designs and Libraries"
date: 2024-07-17
arxiv_url: http://arxiv.org/abs/2407.12749v3
---

Hardware design workflows rely on Process Design Kits (PDKs) from different fabrication nodes, each containing standard cell libraries optimized for speed, power, or density. Engineers typically navigate between the design and target PDK to make informed decisions, such as selecting gates for area optimization or enhancing the speed of the critical path. However, this process is often manual, time-consuming, and prone to errors. To address this, we present ChipXplore, a multi-agent collaborative framework powered by large language models that enables engineers to query hardware designs and PDKs using natural language. By exploiting the structured nature of PDK and hardware design data, ChipXplore retrieves relevant information through text-to-SQL and text-to-Cypher customized workflows. The framework achieves an execution accuracy of 97.39\% in complex natural language queries and improves productivity by making retrieval 5.63x faster while reducing errors by 5.25x in user studies. Compared to generic workflows, ChipXplore's customized workflow is capable of orchestrating reasoning and planning over multiple databases, improving accuracy by 29.78\%. ChipXplore lays the foundation for building autonomous agents capable of tackling diverse physical design tasks that require PDK and hardware design awareness.
