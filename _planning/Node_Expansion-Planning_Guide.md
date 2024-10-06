---
title: Multi-Node
typora-root-url: ..
layout: default
permalink: /:name/
nav_order: 1.2
use_cases:
  - Learning & Planning
  - Node Cluster Setup
  - System Configuration
---
# Multi-Node Planning Guide {#multi_node_planning_guide}
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
The LCC Fusion Project incorporates a versatile and scalable approach to model railroad automation by leveraging the power of ESP32 microcontrollers. This documentation outlines the structure and functionality of a multi-LCC Fusion Node Cluster within the project, illustrating how various nodes, each with its unique role and characteristics, come together to form a cohesive system. This setup allows for an efficient distribution of computational tasks and resources, addressing the limitations of individual ESP32 units while enhancing overall system capability.

The LCC Fusion Project is designed to ensure seamless scalability and interoperability between multiple PCBs. At the heart of this modular system is the concept of **Primary** and **Secondary LCC Fusion Node Cards**. While each card operates independently, offering robust control and automation capabilities for different sections of your model railroad, they are differentiated by their connection and role within the network.

> Please refer to the [Terminology](/terminology/) section for further details about LCC Fusion Project Nodes, Node Bus Hub and Node Clusters.

## Understanding the Roles

- **Primary LCC Fusion Node Card**: This is the first LCC Fusion Node Card you'll connect to your system. It plays a pivotal role by being the initial point of contact to the CAN network and power supply. The Primary LCC Fusion Node Card ensures that these critical resources are available to the other LCC Fusion Node Cards in the network.
- **Secondary LCC Fusion Node Cards**: These LCC Fusion Node Cards are connected to the system after the Primary LCC Fusion Node Card. They leverage the CAN network and power distributed through the Primary LCC Fusion Node Card, making them equally capable but designated as expansions to the primary setup.

## Simplifying Layouts with Node Clusters

The strategic deployment of a Primary Node with multiple Secondary Nodes within an LCC LCC Fusion Node Cluster, all connected through the Node Bus Hub, significantly streamlines the wiring complexity traditionally associated with electronic layouts in model railroad setups or similar automation projects. This organization minimizes the need for extensive wiring for sharing of both power and communications, offering a cleaner, more manageable approach to system configuration and expansion.

- **Reduced Wiring Complexity**: By centralizing communication through the Node Bus Hub, the LCC LCC Fusion Node Cluster reduces the amount of individual connections needed between nodes and I/O cards. This setup mitigates the potential for wiring errors and simplifies troubleshooting, making the system more accessible for both novice and experienced users alike.
- **Efficient Space Management**: The consolidation of nodes into a unified cluster facilitates a more efficient use of space. This is particularly beneficial in environments where physical space is at a premium, allowing for a more organized and aesthetically pleasing setup.
- **Scalability with Simplified Management**: Expanding a model railroad layout or automation project becomes significantly less daunting when the primary concern of managing a tangle of wires is removed. The LCC Node Cluster’s design supports straightforward scalability, allowing for the easy integration of additional nodes and I/O cards without the burden of complex wiring requirements.

Incorporating primary and secondary nodes into a single Node Bus Hub within the LCC Fusion Node Cluster not only enhances the communication efficiency between devices but also represents a leap forward in reducing the physical and logistical complexities typically associated with electronic layouts. This approach ensures that enthusiasts and professionals alike can focus more on the creative and functional aspects of their projects, rather than being bogged down by the intricacies of wiring.

## Network Communications in LCC Node Clusters

The architecture of the LCC Node Clusters facilitates intricate communication pathways between LCC Fusion Node Cards and I/O cards, employing two distinct network communication protocols. These protocols are designed to accommodate multiple devices on each of their networks, enabling the seamless integration of various LCC Fusion Node Cards and I/O cards. Below is an overview of the network communication methods utilized within the system:

- **CAN Network**: This network is integral for facilitating communication among LCC-enabled devices, such as LCC Fusion Node Cards and systems interfacing with JMRI, predominantly through LCC Events. The CAN network accommodates connectivity via a physical 2-wire interface or a WiFi network, offering flexibility in network topology. Within this setup, the Node Bus Hub acts as a central point for the 2-wire CAN connection, linking a primary LCC Fusion Node Card with one or more secondary LCC Fusion Node Cards to form a cohesive network.
- **Serial Network**: The Serial Network, specifically employing the I2C communications protocol, is crucial for the interaction between LCC Fusion Project **LCC Fusion Node Cards** and their respective I/O cards. This connection is facilitated through a 2-wire interface from the LCC Fusion Node Cards to the I/O cards via the Node Bus Hub. Utilizing I2C allows for **multiple ESP32 modules on the LCC Fusion Node Cards to communicate over the same serial connection** with I2C-enabled ICs present on the I/O cards, ensuring efficient and coordinated data exchange within the system.

## Expanding the LCC Node Cluster

The design and implementation of these network communications underpin the modular and expandable nature of the LCC LCC Fusion Node Cluster, allowing for the addition of new nodes and I/O cards as system requirements evolve. This flexibility ensures that the network can scale to meet the increasing complexity of model railroad layouts or other automation projects, all while maintaining robust and reliable communication across the cluster.

## LCC Node Cluster Configuration Example

 

The core of the multi-node configuration is the **LCC Node Bus Hub**, a central unit that facilitates communication and power distribution among the connected nodes. The diagram (Figure 1) represents a typical setup where multiple LCC Fusion Node Cards are connected to the same Node Bus Hub, each serving a distinct purpose:

<img src="/assets/images/Secondary_Nodes.png" style="zoom: 70%; float: right;" />

- **Node 1**: The primary node, equipped with its own power supply and firmware configured to control input/output devices across the layout. As the primary node, it is connected to:
  - a power supply and providing power to the LCC Node Bus Hub for use by secondary LCC Fusion Node Cards and I/O cards.
  - CAN network for communications with other Nodes and LCC Configuration Tool (e.g. JMRI Configuration Tool)

- **Node 2**: A secondary node dedicated to driving signaling devices, without an independent power supply, leveraging power from the primary node or bus hub.  Its firmware is configured to support driving the signal lamps for signaling. 
- **Node 3**: Another secondary node with firmware configured for implementing signal logic and conditional operations, enhancing the dynamic response of signaling devices.
- **Node 4**: A secondary node designated for testing purposes, featuring a serial monitor connection for testing and debugging.

## Scalability and Specialization

The design philosophy behind the LCC Fusion Project's multi-node configuration is twofold: scalability and specialization. By distributing tasks across multiple nodes, the system can scale out to meet the demands of extensive model railroad layouts without overburdening a single ESP32 unit. This approach not only mitigates the memory constraints of individual microcontrollers but also allows for a more refined and specialized control over different aspects of the layout.

## Administration and Resource Management

The separation into multiple nodes also simplifies administration and maintenance. Each node can be updated, replaced, or debugged independently, reducing system downtime and facilitating easier upgrades. Moreover, the specialization of nodes allows for more efficient resource allocation and management, ensuring that each microcontroller is optimized for its specific tasks.

## Conclusion

The LCC Fusion Project's multi-node configuration exemplifies a forward-thinking approach to model railroad automation. By leveraging the strengths of ESP32 microcontrollers in a distributed and specialized system, the project achieves a balance between scalability, flexibility, and efficiency. This architecture not only addresses the inherent limitations of single microcontrollers but also paves the way for more sophisticated and responsive control mechanisms within the hobbyist community.

## Key Features

- **Shared Resources**: Both Primary and Secondary LCC Fusion Node Cards share the CAN Bus communications and power, ensuring a cohesive and efficient operation across your system.
- **Independence**: Despite their shared resources, each LCC Fusion Node Card operates independently, managing its segment of the railroad automation with its dedicated ESP32 and firmware.
- **Ease of Expansion**: Adding Secondary LCC Fusion Node Cards is straightforward. Connect them to the existing network through the Node Bus Hub, and they automatically integrate into the system, sharing resources and communication protocols with the Primary LCC Fusion Node Card.
- **Uniform Functionality**: Except for the initial connection to the CAN network and power supply, Primary and Secondary LCC Fusion Node Cards are functionally identical, ensuring a uniform user experience and simplifying the system's scalability.

## Conclusion

The distinction between Primary and Secondary LCC Fusion Node Cards is designed to facilitate easy expansion and management of your LCC Fusion system. With this setup, you can effortlessly scale your model railroad automation, knowing that each addition seamlessly integrates into the network, maintaining high performance and reliability across the board. This approach not only simplifies the expansion process but also ensures that your system remains flexible and adaptable to future needs.