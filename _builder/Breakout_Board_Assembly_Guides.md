---
title: Breakout Board Assembly Guides
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
# Breakout Board Assembly Guides {#breakout_board_assembly_guides}
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
 LCC Fusion Project refers to some of the PCB (boards) as **Breakout Boards**, which provide specific functions for adding layout automation.  Breakout Boards are connected to both the LCC Fusion Project **Cards** and the I/O devices on the layout.   These breakout boards typically have best suited for the type of device being connected.  For example, the **Block Breakout Board** is connected to a **BOD Card** using a network cable inserted into an RJ45 socket and also connected the track blocks using JST or spring terminal connectors.  

For detailed information on design best practices and considerations, please see the [PCB Design Guidelines](/pcb-design-guidelines/) section in our documentation.

## LCC Fusion Breakout Boards: From Start to Finish

<img src="{{ site.baseurl }}/assets/images/pcbs/Sound_Card/Sound_Card_Flow.png" style="zoom:50%;float:right" />Below, you'll find links to specific guides for PCB **LCC Fusion Breakout Boards** included in the LCC Fusion Project. These guides are tailored to the unique aspects of assembling each type of PCB, yet they all follow the same fundamental principles outlined in our sequence diagram. This consistency ensures that, no matter which PCB you're working on, the process remains familiar and straightforward.

**Sequence of Activities:**

1. **Preparation**: Gathering the necessary tools and components.

2. **Soldering**: Step-by-step instructions for soldering components onto the PCB.

3. **Testing**: Guidelines for testing the PCB to ensure functionality.

4. **Integration**: Advice on integrating the assembled PCB into your model railroad layout.

5. **Troubleshooting**: Common issues and how to resolve them.

## Required LCC Fusion Breakout Boards

| LCC Fusion Breakout Boards | Description                                                  |
| :----------------------------------------------- | :----------------------------------------------------------- |
| **Node Bus Hub**  | Provides connectivity between **BOD Card** and **LCC Fusion Cards** . |

## Optional LCC Fusion Breakout Boards

| LCC Fusion Breakout Boards             | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **Block Breakout Board**      | Provides connectivity between **BOD Card** and **Track Block** . |
| **DC Motor Driver Breakout Board** | Provides connectivity between **PWM Card** and  DC Motors.<br>Provides connectivity between **DCC Card** and  cab’s DCC decoders. |
| **Stepper Motor Breakout Board** | Provides connectivity between **I/O Card** and  stepper motors. |

## Additional Materials:

### Supplies
- [PCB Components](/pcb-parts/) - listing of items used for PCB assembly
- [PCB Components](/pcb-components/) - listing of components used for PCB assembly

### How To Guides
- [Builder’s Resources & Tips](/tips/)
