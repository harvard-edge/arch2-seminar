---
layout: paper_detail
title: "Utilizing Generative Adversarial Networks for Image Data Augmentation and Classification of Semiconductor Wafer Dicing Induced Defects"
date: 2024-07-24
arxiv_url: http://arxiv.org/abs/2407.20268v1
---

In semiconductor manufacturing, the wafer dicing process is central yet vulnerable to defects that significantly impair yield - the proportion of defect-free chips. Deep neural networks are the current state of the art in (semi-)automated visual inspection. However, they are notoriously known to require a particularly large amount of data for model training. To address these challenges, we explore the application of generative adversarial networks (GAN) for image data augmentation and classification of semiconductor wafer dicing induced defects to enhance the variety and balance of training data for visual inspection systems. With this approach, synthetic yet realistic images are generated that mimic real-world dicing defects. We employ three different GAN variants for high-resolution image synthesis: Deep Convolutional GAN (DCGAN), CycleGAN, and StyleGAN3. Our work-in-progress results demonstrate that improved classification accuracies can be obtained, showing an average improvement of up to 23.1 % from 65.1 % (baseline experiment) to 88.2 % (DCGAN experiment) in balanced accuracy, which may enable yield optimization in production.
