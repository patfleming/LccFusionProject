---
title: Card Assembly Guides
typora-root-url: ..
layout: default
permalink: /:name/
nav_order: 2
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
  - Device Control
  - Automation Deployment
has_children: True
---
# Card Assembly Guides {#card_assembly_guides}

{: .no_toc }
{:toc}
<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Introduction

<img src="{{ site.baseurl }}/assets/images/pcbs/Card.png/" style="zoom:20%; float:right" />The **LCC Fusion Project** refers to some of the PCB (boards) as **Cards**, which provide specific functions for adding layout automation. **LCC Fusion Cards** are connected using a **Node Bus Hub** to form the project's **LCC Fusion Node Cluster.** Each cluster requires one **LCC Fusion Node Card** to run the firmware for the **LCC Fusion Node Card.**

For detailed information on design best practices and considerations, please see the [PCB Design Guidelines](/pcb-design-guidelines/) section in our documentation.

## LCC Fusion Cards Assembly Guide: From Start to Finish

<img src="{{ site.baseurl }}/assets/images/pcbs/Sound_Card/Sound_Card_Flow.png" style="zoom:50%;float:right" />Below, you'll find links to specific guides for each **LCC Fusion Cards** (PCBs) included in the **LCC Fusion Project**. These guides are tailored to the unique aspects of assembling each type of LCC Fusion Cards, yet they all follow the same fundamental principles outlined in our sequence diagram. This consistency ensures that, no matter which LCC Fusion Cards you're working on, the process remains familiar and straightforward.

### Sequence of Activities

1. **Preparation**: Gathering the necessary tools and components.

2. **Soldering**: Step-by-step instructions for soldering components onto the PCB.

3. **Testing**: Guidelines for testing the LCC Fusion Cards to ensure functionality.

4. **Integration**: Advice on integrating the assembled LCC Fusion Cards into your model railroad layout.

5. **Troubleshooting**: Common issues and how to resolve them.

### Required LCC Fusion Cards

| LCC Fusion Cards                 | Description                                                  |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| **Power-CAN Card**      | Provides power and communications to a **LCC Fusion Node Cluster**. |
| **SuperMini Node Card** | Provides support for 1 to 4  **LCC Nodes**. |

### Optional LCC Fusion Cards

| LCC Fusion Cards          | Description                                                  |
| ----------------------------------------------- | ------------------------------------------------------------ |
| **Audio Card**   | Provides text to audio and .wav file play back to speakers using a low power **[Amplifier](/terminology/#amplifier).** |
| **Battery Card** | Provides battery backup to LCC Fusion Cards a LCC Fusion Node Cluster |
| **BLVD Card**    | Provides **Block Low Voltage Detection** of track blocks caused by shorts, bad connections, etc. |
| **BOD Card**     | Provides **Block Occupancy Detection** of locomotives and cars using current detection. |
| **Output Card**  | Provides control of output devices (LEDs, etc.).             |
| **PWM Card**     | Provides control of PWM devices (LEDs, motors, Signal Masts (LEDs)) |
| **RPI-CAN Card** | Provides RPI, JMRI, and CAN integration into the **LCC** **LCC Fusion Node Cluster** (no additional wiring). |
| **Sound Card**   | Provides adding sounds to the layout using MP3 players.      |

## Additional Materials:

### Supplies

- [PCB Components](/pcb-parts/) - a listing of items used for LCC Fusion Cards assembly
- [PCB Components](/pcb-components/) - a listing of components used for LCC Fusion Cards assembly

### How-To Guides

- [Builder’s Resources & Tips](/tips/)