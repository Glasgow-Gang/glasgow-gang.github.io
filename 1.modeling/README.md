---
title: Modeling
layout: default
has_children: true
nav_order: 2
---

# Modeling

<div align=center>
<img src="../imgs/hardware_jointname.jpg">
<p>

## Work Order

<div align=center>
<img src="../imgs/modeling.png" >
<p>

## Joints to model

|Joint Name|Parameters|Forward Kinematics|Inverse Kinematics|Physical Equation|State-space Model|Controller|
|-|-|-|-|-|-|-|
|Head|✅|✅|❌|✅|✅|✅|
|ArmShoulder|❌|❌|❌|❌|❌|❌|
|ArmElbow|❌|❌|❌|❌|❌|❌|
|LegHip(Supported)|❌|❌|❌|❌|❌|❌|
|LegKnee(Supported)|❌|❌|❌|❌|❌|❌|
|LegAnkle(Supported)|❌|❌|❌|❌|❌|❌|
|LegHip(Floating)|❌|❌|❌|❌|❌|❌|
|LegKnee(Floating)|❌|❌|❌|❌|❌|❌|
|LegAnkle(Floating)|❌|❌|❌|❌|❌|❌|

For example. In the picture below the right leg is supported, and the left leg is floating.

![img](../imgs/robot.png)
