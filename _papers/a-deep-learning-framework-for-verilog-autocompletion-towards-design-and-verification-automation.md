---
layout: paper_detail
title: "A Deep Learning Framework for Verilog Autocompletion Towards Design and Verification Automation"
date: 2023-04-26
arxiv_url: http://arxiv.org/abs/2304.13840v2
---

Innovative Electronic Design Automation (EDA) solutions are important to meet the design requirements for increasingly complex electronic devices. Verilog, a hardware description language, is widely used for the design and verification of digital circuits and is synthesized using specific EDA tools. However, writing code is a repetitive and time-intensive task. This paper proposes, primarily, a novel deep learning framework for training a Verilog autocompletion model and, secondarily, a Verilog dataset of files and snippets obtained from open-source repositories. The framework involves integrating models pretrained on general programming language data and finetuning them on a dataset curated to be similar to a target downstream task. This is validated by comparing different pretrained models trained on different subsets of the proposed Verilog dataset using multiple evaluation metrics. These experiments demonstrate that the proposed framework achieves better BLEU, ROUGE-L, and chrF scores by 9.5%, 6.7%, and 6.9%, respectively, compared to a model trained from scratch. Code and data are made available at: https://github.com/99EnriqueD/verilog_autocompletion .
