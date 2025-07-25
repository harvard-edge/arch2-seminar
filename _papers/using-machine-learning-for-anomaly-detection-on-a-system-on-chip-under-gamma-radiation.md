---
layout: paper_detail
title: "Using Machine Learning for Anomaly Detection on a System-on-Chip under Gamma Radiation"
date: 2022-01-05
arxiv_url: http://arxiv.org/abs/2201.01588v1
---

The emergence of new nanoscale technologies has imposed significant challenges to designing reliable electronic systems in radiation environments. A few types of radiation like Total Ionizing Dose (TID) effects often cause permanent damages on such nanoscale electronic devices, and current state-of-the-art technologies to tackle TID make use of expensive radiation-hardened devices. This paper focuses on a novel and different approach: using machine learning algorithms on consumer electronic level Field Programmable Gate Arrays (FPGAs) to tackle TID effects and monitor them to replace before they stop working. This condition has a research challenge to anticipate when the board results in a total failure due to TID effects. We observed internal measurements of the FPGA boards under gamma radiation and used three different anomaly detection machine learning (ML) algorithms to detect anomalies in the sensor measurements in a gamma-radiated environment. The statistical results show a highly significant relationship between the gamma radiation exposure levels and the board measurements. Moreover, our anomaly detection results have shown that a One-Class Support Vector Machine with Radial Basis Function Kernel has an average Recall score of 0.95. Also, all anomalies can be detected before the boards stop working.
