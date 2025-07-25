---
layout: paper_detail
title: "Application of Machine Learning Techniques for Secure Traffic in NoC-based Manycores"
date: 2025-01-21
arxiv_url: http://arxiv.org/abs/2501.12034v1
---

Like most computer systems, a manycore can also be the target of security attacks. It is essential to ensure the security of the NoC since all information travels through its channels, and any interference in the traffic of messages can reflect on the entire chip, causing communication problems. Among the possible attacks on NoC, Denial of Service (DoS) attacks are the most cited in the literature. The state of the art shows a lack of work that can detect such attacks through learning techniques. On the other hand, these techniques are widely explored in computer network security via an Intrusion Detection System (IDS). In this context, the main goal of this document is to present the progress of a work that explores an IDS technique using machine learning and temporal series for detecting DoS attacks in NoC-based manycore systems. To fulfill this goal, it is necessary to extract traffic data from a manycore NoC and execute the learning techniques in the extracted data. However, while low-level platforms offer precision and slow execution, high-level platforms offer higher speed and data incompatible with reality. Therefore, a platform is being developed using the OVP tool, which has a higher level of abstraction. To solve the low precision problem, the developed platform will have its data validated with a low-level platform.
