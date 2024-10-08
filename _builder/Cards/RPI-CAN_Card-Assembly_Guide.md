---
title: RPI-CAN Card Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Card Assembly Guides
nav_order: 3
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_cards
  - lcc_fusion_project
  - lcc_fusion_node_bus
  # LCC Fusion Connect Terms
  # NMRA LCC Network Terms
  # Model Railroad Automation Terms
  # Hardware and firmware Terms
  - bus
  - can_network
  - can_termination
  - cleaning_pcb
  - component
  - edge_card_connector
  - jumper_caps
---

# RPI-CAN Card Assembly Guide {#rpi_can_card_assembly}

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

This document provides a detailed guide the assembly of the RPI-CAN Card used to configure a Raspberry PI (RPI) running the Java Model Railroad Interface (JMRI) with the Controller Area Network (CAN) interface.  JRMI provides a GUI for both controlling a layout and for configuring LCC Nodes.    The card provides all of the wiring connections for between an RPI, a CAN Module, and the LCC Fusion Project. 

<img src="/assets/images/pcbs/RPI-CAN_Card/RPI.png" style="zoom:25%; float:right" />To facilitate CAN communication with LCC Nodes, a Raspberry Pi can be configured to run JMRI and function as a CAN end-node. This integration is streamlined through the use of a specialized Raspberry Pi (RPI) CAN card that incorporates the MCP2515 module (CAN Receiver). This card, which slots directly into the LCC Fusion Node Bus Hub, simplifies connectivity by negating the need for additional wiring.

<img src="/assets/images/parts/MCP2515_Module.png" style="zoom:25%;float:right" />In essence, connecting a Raspberry Pi to the LCC Node network is made straightforward with the Raspberry Pi CAN Card. The design of the card does away with the necessity of 10 separate connections:

1. It eliminates the need for eight connections typically used for SPI, 3.3V, and GND between the Raspberry Pi and the MCP2515.
2. It also removes the requirement for two CAN wires that would normally link the MCP2515 Module to the LCC Node.

The Raspberry Pi CAN card operates as a Raspberry Pi HAT, connecting beneath the card, while the MCP2515 module is mounted upside down on the top of the PCB. Once combined, this assembly is plugged into the LCC Fusion Node Bus Hub. It provides the essential connections: the Raspberry Pi to the LCC Fusion Node Bus Hubat 5V, and the MCP2515 Module to the Node's 3.3V and CAN network. Additionally, the Raspberry Pi's SPI is linked to the MCP2515 module through this card.

{% include terminology.html %}

## Specifications

 ## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}RPI-CAN Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Note that the PCB shows two sets of RPI headers that are not used, only the 20P breakout is utilized

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier | Count | Type          | Value/Description                                            | Package          | Required? | Purpose                                                      |
| -------------------- | ----- | ------------- | ------------------------------------------------------------ | ---------------- | --------- | :----------------------------------------------------------- |
|                      | 1     | Raspberry PI  | RPI (4B+)                                                    | N/A              | Required  | Raspberry PI provides JRMI and other services for LCC Nodes. |
| M1                   | 1     | Module        | MCP2515                                                      | CAN Module (SPI) | Required  | CAN receiver module (SPI)                                    |
| J1                   | 1     | Female Header | 2P Stackable Long Leg Female Header (2.54mm, straight, single row) | 2.54mm PTH       | Required  | Provide CAN connections between MCP2515 Module and LCC Fusion Node Bus Hub. Headers on TOP. |
| J2                   | 1     | Female Header | 8P Stackable Female Header (2.54mm, straight, single row)    | 2.54mm PTH       | Required  | Provide SPI connections between the RPI and the MCP2515 Module. Headers on TOP. |
| J3                   | 1     | GPIO Header   | 2x20P Female Extra Tall GPIO Stacking Headers for RPI (2.54mm, straight, double row) | 2.54mm PTH       | Required  | Provide connections to the RPI (4B+) pins. Mounted under the PCB, as an RPI HAT. |
| SH1                  | 1     | Jumper Cap    | [Jumper Cap (2.54mm)](https://www.aliexpress.us/w/wholesale-jumper-caps.html?spm=a2g0o.detail.search.0) | 2.54mm           | Required  | Used for selection setting CAN bus termination. Recommend tall caps for easy use. |

## Tools Required

The card only requires soldering three sets of PTH female pin headers.  Required tools required are:

- soldering iron
- solder
- tacky putty (hold components while soldering)

> See [List of recommended tools](/pcb-tools/) for more details on these tools.

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/RPI-CAN_Card/rpi-can_card_pcb.png" style="zoom: 33%; float: right;" />Here are the step-by-step instructions for assembling the card:

> See also: [Soldering Tips](/pcb-soldering/)

1. Solder headers:

   1. Solder each header individually.

   2. Attach the 2x20P female header (J3) to the **BOTTOM** of the **PCB**. This will be used for attaching the RPI underneath the PCB using its male pins later.

   3. <img src="/assets/images/pcbs/RPI-CAN_Card/RPI-CAN_Card_headers.png" style="zoom: 9%; float: right;" />Solder the 2p stackable long legged header (J1) to the **TOP** of the **PCB** (long legs down thru the 2 holes).  The 2 long legs provide a connection in the MCP2515 Module’s 2P male header connector (CAN-H and CAN-L communications).

   4. Solder the 8p header (J2) to the **TOP** of the **PCB** (legs down thru the 8 holes).  This header provides a connection to the MCP2515 Modules power and SPI communications connector.

      > These will be used for connecting the MCP2515 board in an upside-down position using its male pins.

      > Utilize tacky putty to secure each header during the soldering process.

   5. <img src="/assets/images/pcbs/RPI-CAN_Card/RPI-CAN_Card_solder.png" style="zoom: 8%; float: right;" />Ensure each header is aligned straight and fits snugly against the PCB. 

      > Tip: After soldering the first pin of a header, remove the putty, press down on the header, and reheat the soldered pin to set the header flush and straight against the PCB.

   6. Complete the soldering for the rest of the pins on each header.

   7. Follow this process for all headers.

2. <img src="/assets/images/pcbs/RPI-CAN_Card/RPI-CAN_Card_MCP2515.png" style="zoom: 8%; float: right;" />Install the MCP2515 Module on PCB 

   1. Configure for CAN termination
      - If the MCP2515 Module is at the end of a CAN network, the module be configured with a CAN terminator.  This is performed by removing the MPC2515 Module from the PCB and installing a Jumper Cap on the 2 male pins (on the side of the module’s PCB marked J1)

   2. Insert the MCP2515 Module on the PCB **top**, making sure both sets of male pins are inserted into PCB’s female headers correctly.
   3. Attach four 10mm PCB standoffs on the PCB **top** to secure the MCP2515 to the board.

3. <img src="/assets/images/pcbs/RPI-CAN_Card/RPI-CAN_Card_finished.png" style="zoom: 15%; float: right;" />Install the RPI

   1. Insert the RPI into the 2x20P headers on the PCB **bottom**
   2. Install (4) sets of 2x11mm PCB standoffs on the PCB **bottom** to mount the RPI, using the provided holes in the card.


## Testing and Verification

The following test and verifications of the card should be performed after a through in+spection of the card's soldering.  Check all of the PTH component pins.  Make sure there are no solder bridges between pins.

## Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.
2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

## Power-Up Tests

1. **Apply Power**:  **<u>Without</u>** the RPI and MCP2515 Module added, check for correct voltage levels at these locations:
   1. Using the tabs at the base of the card, verify at the base of the card that the LCC Fusion Node Bus Hubis providing 3V3, 5V, and 12+V.   
2. Check for 5V at the PCB pin marked 5V.
3. Check for 3V3 at the PCB pin marked 3V3.

## Functional Testing

1. Configure RPI for CAN communications.  Refer to [RPI CAN Configuration](/rpi-can-configuration-guide/).
2. Plugin in the RPI and check that it powers up correctly.
3. Plugin in the MCP2515 Module and check if Linux connects to it.
4. [Configure a JMRI connection](/rpi-can-configuration-guide/) to verify that JMRI running on the RPI can connect to an LCC Node using wired CAN communications.


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

1. [Adding CAN to the Raspberry PI](https://www.beyondlogic.org/adding-can-controller-area-network-to-the-raspberry-pi/) - provides information on selection of the MCP2515 board and information used in the design of RPI-CAN Card and Linux configuration.

