---
title: Modeling
layout: default
has_children: true
nav_order: 2
---

# Modeling

<div align="center">
<img src="../imgs/hardware_jointname.jpg" alt="Joint names">
</div>

## Work Order

<div align="center">
<img src="../imgs/modeling.png" alt="Modeling process">
</div>

## Joints to model

| Joint Name            | Parameters | Forward Kinematics | Inverse Kinematics | Physical Equation | State-space Model | Controller |
|-----------------------|------------|--------------------|--------------------|-------------------|-------------------|------------|
| Head                  | ✅         | ✅                 | ❌                 | ✅                | ✅                | ✅         |
| ArmShoulder           | ❌         | ❌                 | ❌                 | ❌                | ❌                | ❌         |
| ArmElbow              | ❌         | ❌                 | ❌                 | ❌                | ❌                | ❌         |
| LegHip (Supported)    | ❌         | ❌                 | ❌                 | ❌                | ❌                | ❌         |
| LegKnee (Supported)   | ❌         | ❌                 | ❌                 | ❌                | ❌                | ❌         |
| LegAnkle (Supported)  | ❌         | ❌                 | ❌                 | ❌                | ❌                | ❌         |
| LegHip (Floating)     | ❌         | ❌                 | ❌                 | ❌                | ❌                | ❌         |
| LegKnee (Floating)    | ❌         | ❌                 | ❌                 | ❌                | ❌                | ❌         |
| LegAnkle (Floating)   | ❌         | ❌                 | ❌                 | ❌                | ❌                | ❌         |

---

For example, in the picture below, the right leg is supported, and the left leg is floating.

![Robot legs](../imgs/robot.png)
