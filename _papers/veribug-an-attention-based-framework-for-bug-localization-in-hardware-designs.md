---
layout: paper_detail
title: "VeriBug: An Attention-based Framework for Bug-Localization in Hardware Designs"
date: 2024-01-17
arxiv_url: http://arxiv.org/abs/2401.09494v1
---

In recent years, there has been an exponential growth in the size and complexity of System-on-Chip designs targeting different specialized applications. The cost of an undetected bug in these systems is much higher than in traditional processor systems as it may imply the loss of property or life. The problem is further exacerbated by the ever-shrinking time-to-market and ever-increasing demand to churn out billions of devices. Despite decades of research in simulation and formal methods for debugging and verification, it is still one of the most time-consuming and resource intensive processes in contemporary hardware design cycle. In this work, we propose VeriBug, which leverages recent advances in deep learning to accelerate debugging at the Register-Transfer Level and generates explanations of likely root causes. First, VeriBug uses control-data flow graph of a hardware design and learns to execute design statements by analyzing the context of operands and their assignments. Then, it assigns an importance score to each operand in a design statement and uses that score for generating explanations for failures. Finally, VeriBug produces a heatmap highlighting potential buggy source code portions. Our experiments show that VeriBug can achieve an average bug localization coverage of 82.5% on open-source designs and different types of injected bugs.
