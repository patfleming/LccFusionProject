---
title: Node Power
typora-root-url: ..
layout: default
permalink: /:name
nav_order: 1.1
use_cases:
  - Learning & Planning
  - Node Cluster Setup
  - System Configuration
---
# Node Power Planning Guide {#node_power_planning_guide}
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
When setting up your LCC LCC Fusion Node Cluster(s) for model railroad automation, a crucial consideration is the choice of power supply configuration. Efficient power management ensures stable operations, longevity of the components, and safety. It is essential to understand the power requirements of each component within the cluster to ensure that your chosen power supply can adequately support the entire system without risk of overload or insufficient power delivery.

Below are options for powering the LCC LCC Fusion Node Cluster using one or more power supplies and various connection option.  Select a method that works best based on planned usage.  

### Device Ground Wiring
Regardless of whether a single or multiple power supply configurations are used, the approach to device grounding remains consistent. This involves either directly connecting the device ground to the layout accessory ground or routing the ground circuit back to the LCC LCC Fusion Node Cluster ground. In all scenarios, connections ultimately converge at a common ground point, ensuring a stable and unified ground reference across the system. Establishing a unified ground reference is crucial for the prevention of potential electrical issues such as voltage differentials between components, which can lead to erratic behavior or damage to sensitive electronics.

## Power Supply Options for LCC Node Clusters
There are two main approaches to powering your LCC Node I/O cards and the attached LEDs, each with its benefits and considerations.

### Option 1: Single Power Supply Configuration
The simplest method is to employ a single power supply to power both the LCC LCC Fusion Node Cluster(s) and the layout accessories. In this configuration, all LCC Fusion Project components, including layout accessories like LEDs attached to the I/O cards, share a common ground. This approach minimizes complexity and reduces the number of components required. It's ideal for setups where all of the power requirements of the layout accessories and the LCC LCC Fusion Node Cluster are within the capacity of a single power supply, ensuring a streamlined and efficient power management system.

Advantages of the single power supply configuration include:

- **Simplicity:** Easier setup with fewer components to manage.
- **Cost-Effectiveness:** Reduces the need for multiple power supplies, saving on costs.
- **Unified Grounding:** With a shared common ground, there's a reduced risk of ground loop issues, which can be crucial in sensitive electronic environments.

### Option 2: Dual Power Supply Configuration

For more extensive setups or where the power demands exceed the capacity of a single supply, a dual power supply configuration can be used. In this scenario, one power supply is dedicated to the LCC LCC Fusion Node Cluster and its I/O cards, while a second, separate power supply is responsible for providing power to layout accessory devices (i.e. LEDs, etc.). Importantly, these devices  will ground through a layout accessory bus's common ground back to the second power supply. Despite using two power sources, both power supplies share the same ground—this can be achieved through a common power strip or connected to the layout room ground to ensure stability and prevent potential electrical interference.

The dual power supply configuration offers several benefits:

- **Flexibility:** Allows for greater power distribution thru segmentation, especially useful in larger or more power-intensive setups.
- **Stability:** By dividing the power load, each supply can operate within its optimal capacity, potentially increasing the lifespan of the components.
- **Safety:** Separating the power sources can enhance safety, as it allows for more controlled management of power flows and reduces the chances of overloading a single supply.

In summary, the choice between a single or dual power supply configuration depends on your specific needs, including the scale of your LCC LCC Fusion Node Cluster, power requirements, and considerations for cost, complexity, and safety. It's essential to carefully plan your power supply strategy to ensure a stable and efficient operation of your model railroad automation system.

## Use Cases

The LCC Fusion Project provides several methods of power a LCC LCC Fusion Node Cluster, a single LCC  Card, or just I/O cards.  This can be useful while testing new hardware, configuring an LCC Node, or for distributing multiple LCC Node Clusters or I/O cards around an under your layout.  These options can be use for both convience and simplifying layout wiring while providing optins for integration with a layout power grid.

Below is a table summarizing the use cases for each type of power input connector available with the LCC Fusion Project hardware. This table is designed to help planners choose the most appropriate connector based on their requirements, including the number of secondary LCC Nodes, LCC Node Clusters, LCC Node Bus Hub(s), and I/O cards to connect and their preferred power sources.

> Refer to [Termnology](terminology) for an explanation of terms used below

| Connector Location               | Power Input Connector                                        | Power Module | Max Current / Voltage | Use Cases                                                    | Why Choose This?                                             | Considerations                                               |
| -------------------------------- | ------------------------------------------------------------ | :----------: | --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| DevKit-C Module on LCC LCC Fusion Node Card | USB Connector                                                |      No      | 2A / 5V               | Use while testing a LCC LCC Fusion Node Cluster and using the computer’s serial monitor. | LCC Node has an integrated management system for bench testing hardware.  Don’t use for non-testing to prevent damage to the DevKit-C Module circuitry. | Use computer based serial monitors such as Arduino IDE, PuTTY, RealTerm,Tera Term, CoolTerm, and YAT. |
| LCC Node Bus Hub                 | USB-C Connector                                              |      No      | 3A / 5V               | Use while testing or temporarily powering a small LCC LCC Fusion Node Cluster. | Simplifies adding power from any location using a USB cable.  When using a LCC LCC Fusion Node Card, consider using a Power Module for more robust power supply and protection. | Use temporarily when 12V+ is not required and working with a small LCC configuration.  Computer power adapters can provide up to 3A with a USB-C plug. |
| LCC Node Bus Hub                 | 1) Network Cable Sockets (RJ45)<br>2) 8-Pin Female Pin Headers |      No      | 600mA / 3V3, 5V, 12V+ | Use when expanding the LCC [LCC Fusion Node Bus](/terminology/#node-bus) with additional LCC Node Bus Hubs without a Primary LCC LCC Fusion Node Card. | Required for expansion (secondary) LCC Node Bus Hub to receive power and communications from another LCC Node Bus Hub.<br>Useful when powering additional Node Bus Hubs with centralized locations around the layout. | Use CAT6 network cable to carry more current.  Secondary Node Bus Hub can be daisy chained together. |
| LCC LCC Fusion Node Card                    | CAN Bus Network  Cable Sockets (RJ45)                        |     Yes      | 600mA / 12-35V        | Smaller networks with a focus on simplicity and integration of power and communication in one cable. Ideal for scenarios where the layout is compact or the number of secondary LCC Nodes is limited. | Simplifies cabling by integrating power and communications. Less clutter and easier to manage in smaller setups. | Limited to 3-5 secondary LCC Nodes.  Requires network cable between LCC Nodes. |
| Power Module                     | USB-C or DC-005 (barrel connector)                           |     Yes      | 2A / 12-35V           | Use as a power supply to primary LCC Node in an LCC LCC Fusion Node Cluster.<br>Medium-sized networks requiring more secondary LCC Nodes. <br>Suitable for users with readily available USB-C power supplies (e.g., laptop chargers). Good balance between power capacity and convenience. | Easy connect/disconnect of power. <br>Utilizes common, modern power supplies. <br>Offers a good mix of power capacity and ease of use. | Suitable for a moderate number of secondary LCC Nodes.       |
| Power Module                     | Spring/Screw Terminal, or ATX 5557 Connector                 |     Yes      | 3A / 12-35V           | Larger networks with a higher number of secondary LCC Nodes. Ideal for users who prefer to use their layout accessory power supply, providing the highest power capacity. | Maximizes the number of secondary LCC Nodes that can be connected. Best for extensive layouts requiring significant power distribution. | Leverages existing layout accessory power supply.<br>Supports max number of LCC Nodes.<br>LCC LCC Fusion Node Cluster can be serially connected using both input and output ATX connectors. |

This table offers a straightforward comparison to help planners make informed decisions based on their specific needs and preferences for their model railroad automation projects. Each connector option caters to different scales and complexities of layout setups, ensuring flexibility and adaptability in planning and implementation.

