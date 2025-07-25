---
layout: paper_detail
title: "Fit2Form: 3D Generative Model for Robot Gripper Form Design"
date: 2020-11-12
arxiv_url: http://arxiv.org/abs/2011.06498v1
---

The 3D shape of a robot's end-effector plays a critical role in determining it's functionality and overall performance. Many industrial applications rely on task-specific gripper designs to ensure the system's robustness and accuracy. However, the process of manual hardware design is both costly and time-consuming, and the quality of the resulting design is dependent on the engineer's experience and domain expertise, which can easily be out-dated or inaccurate. The goal of this work is to use machine learning algorithms to automate the design of task-specific gripper fingers. We propose Fit2Form, a 3D generative design framework that generates pairs of finger shapes to maximize design objectives (i.e., grasp success, stability, and robustness) for target grasp objects. We model the design objectives by training a Fitness network to predict their values for pairs of gripper fingers and their corresponding grasp objects. This Fitness network then provides supervision to a 3D Generative network that produces a pair of 3D finger geometries for the target grasp object. Our experiments demonstrate that the proposed 3D generative design framework generates parallel jaw gripper finger shapes that achieve more stable and robust grasps compared to other general-purpose and task-specific gripper design algorithms. Video can be found at https://youtu.be/utKHP3qb1bg.
