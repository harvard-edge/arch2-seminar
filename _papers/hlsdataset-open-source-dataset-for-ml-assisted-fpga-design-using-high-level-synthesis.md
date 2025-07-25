---
layout: paper_detail
title: "HLSDataset: Open-Source Dataset for ML-Assisted FPGA Design using High Level Synthesis"
date: 2023-02-17
arxiv_url: http://arxiv.org/abs/2302.10977v2
---

Machine Learning (ML) has been widely adopted in design exploration using high level synthesis (HLS) to give a better and faster performance, and resource and power estimation at very early stages for FPGA-based design. To perform prediction accurately, high-quality and large-volume datasets are required for training ML models.This paper presents a dataset for ML-assisted FPGA design using HLS, called HLSDataset. The dataset is generated from widely used HLS C benchmarks including Polybench, Machsuite, CHStone and Rossetta. The Verilog samples are generated with a variety of directives including loop unroll, loop pipeline and array partition to make sure optimized and realistic designs are covered. The total number of generated Verilog samples is nearly 9,000 per FPGA type. To demonstrate the effectiveness of our dataset, we undertake case studies to perform power estimation and resource usage estimation with ML models trained with our dataset. All the codes and dataset are public at the github repo.We believe that HLSDataset can save valuable time for researchers by avoiding the tedious process of running tools, scripting and parsing files to generate the dataset, and enable them to spend more time where it counts, that is, in training ML models.
