---
title: Multi-Node Cluster
typora-root-url: ..
layout: default
permalink: /:name/
nav_order: 1.2
use_cases:
  - Learning & Planning
  - Device Control
  - System Configuration
---
# Wireless Node-to-Node Planning Guide {#wireless_node_to_node_planning_guide}
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
## Setting Up Wireless Node-to-Node Communication Using ESP-NOW in LCC Fusion

## Overview

In the LCC Fusion Project, seamless communication between nodes is essential for effective model railroad automation. ESP-NOW (Wake on Wireless) enables low-power, wireless communication between nodes. End users can configure node-to-node communication by setting up each node as either a server or a client through the Configuration Description Information (CDI).

### Configuring Node-to-Node Communication

#### Step 1: Configure the Server Node

1. **Access the CDI Configuration:**
   - Open the CDI configuration interface for the node you wish to set as a server.
2. **Set the Node Role:**
   - In the CDI settings, configure the node role to "Server."
3. **Save Configuration:**
   - Save the CDI settings to apply the server role to the node.

#### Step 2: Configure the Client Node

1. **Access the CDI Configuration:**
   - Open the CDI configuration interface for the node you wish to set as a client.
2. **Set the Node Role:**
   - In the CDI settings, configure the node role to "Client."
3. **Select the Server:**
   - In the client node’s CDI settings, select the server node you want it to connect to. This is usually performed by entering the server node's ID or address.
4. **Save Configuration:**
   - Save the CDI settings to apply the client role and server selection.

### Creating Virtual Clusters

Virtual clusters are groups of nodes that communicate wirelessly. By configuring nodes as clients and servers, you can create virtual clusters that interact seamlessly.

1. **Identify Nodes:**
   - Identify which nodes will act as servers and which will act as clients.
2. **Cluster Configuration:**
   - Configure each client node to connect to the appropriate server node as described in the previous steps.
3. **Verify Connections:**
   - Ensure that all nodes in the cluster can communicate effectively. This can be verified through the LCC Fusion firmware interface, where you can monitor node connections and communication status.

### Example Scenario

1. **Server Node Configuration:**
   - Node A is configured as a server using the CDI settings.
2. **Client Node Configuration:**
   - Node B and Node C are configured as clients. In their CDI settings, both are set to connect to Node A.
3. **Virtual Cluster:**
   - Nodes A, B, and C form a virtual cluster, with Node A acting as the central server and Nodes B and C as clients communicating with Node A.

### Benefits of ESP-NOW in LCC Fusion

- **Low Power Consumption:** ESP-NOW allows nodes to communicate wirelessly while minimizing power usage, ideal for battery-operated setups.
- **Flexibility:** Users can easily reconfigure nodes to change roles or connections, providing flexibility in managing the layout.
- **Scalability:** Virtual clusters can be expanded by adding more nodes and configuring them as needed, allowing for scalable model railroad automation.

### Conclusion

Setting up node-to-node communication using ESP-NOW in the LCC Fusion Project is straightforward with the CDI configuration. By designating nodes as servers or clients and connecting them appropriately, users can create efficient and flexible virtual clusters for their model train environments. This setup ensures reliable and low-power communication, enhancing the overall automation and control of the model railroad layout.