---
layout: paper_detail
title: "Hardware Trojan Detection Using Unsupervised Deep Learning on Quantum Diamond Microscope Magnetic Field Images"
date: 2022-04-29
arxiv_url: http://arxiv.org/abs/2204.14228v1
---

This paper presents a method for hardware trojan detection in integrated circuits. Unsupervised deep learning is used to classify wide field-of-view (4x4 mm$^2$), high spatial resolution magnetic field images taken using a Quantum Diamond Microscope (QDM). QDM magnetic imaging is enhanced using quantum control techniques and improved diamond material to increase magnetic field sensitivity by a factor of 4 and measurement speed by a factor of 16 over previous demonstrations. These upgrades facilitate the first demonstration of QDM magnetic field measurement for hardware trojan detection. Unsupervised convolutional neural networks and clustering are used to infer trojan presence from unlabeled data sets of 600x600 pixel magnetic field images without human bias. This analysis is shown to be more accurate than principal component analysis for distinguishing between field programmable gate arrays configured with trojan free and trojan inserted logic. This framework is tested on a set of scalable trojans that we developed and measured with the QDM. Scalable and TrustHub trojans are detectable down to a minimum trojan trigger size of 0.5% of the total logic. The trojan detection framework can be used for golden-chip free detection, since knowledge of the chips' identities is only used to evaluate detection accuracy
