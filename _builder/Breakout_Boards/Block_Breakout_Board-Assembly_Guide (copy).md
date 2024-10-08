---
title: Block Breakout Board Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Breakout Board Assembly Guides
nav_order: 2
use_cases:
  - Automation Deployment
  - Node Cluster Setup
  - PCB Design & Assembly
  - Signaling Systems
  - Train Detection
subjects:
  - Assembly Guides
  - Automation
  - Hardware
  - Signaling
  - Train Detection
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_breakout_boards
  - lcc_fusion_cards
  - lcc_fusion_project
  # LCC Fusion Connect Terms
  - lcc_fusion_node_card
  - network_cable
  # Model Railroad Automation Terms
  - track_bus
  # Hardware and firmware Terms
  - cleaning_pcb
  - component
---





# Block Breakout Board Assembly Guide {#block-breakout_board_assembly}
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

Thank you for the clarification! Based on your feedback, here’s the refined version that reflects the role of the Node Card firmware in generating the events and the Block Breakout Board's role in simplifying wiring:

------

The **Block Breakout Board**, in combination with the LCC LCC Fusion Node Card, is used to simplify wiring for monitoring track blocks. The board can be configured in two different scenarios:

1. **Occupancy Detection**: When used with the **BOD Card**, the **Block Breakout Board** connects to track rails to facilitate the detection of trains (both locomotives and rolling stock) within specific track blocks. The **BOD Card** provides status updates via its GPIO pins to the  LCC Fusion Node Card.  The LCC Fusion Node Card firmware processes these updates to generate LCC events, which can then be used by other systems, such as the PWM Card, for tasks like managing signal operations based on track occupancy.
2. **Low Voltage Detection (BLVD)**: When paired with the **BLVD Card**, the Block Breakout Board helps detect low voltage conditions within a track block. The **BLVD Card** reports the voltage status through its GPIO pins to the LCC Fusion Node Card. The LCC Fusion Node Card firmware generates LCC events to alert the system of any low voltage conditions, allowing for appropriate corrective actions or notifications.

In both scenarios, the **Block Breakout Board** simplifies the wiring between track blocks and the BOD Card or BLVD Card, ensuring efficient monitoring and reporting of block conditions within the LCC Node framework.

{% include terminology.html %}

## Specifications

Specifications for the Block Breakout Board include:

| Characteristic    | Value                 |
| ----------------- | --------------------- |
| Max Track Blocks  | 4                     |
| Max Track Current | 2750mA<sup>1, 2</sup> |

1. Block Breakout Board uses 48mil traces that support up to 2750 mA.  
1. A CAT6 network cable with 23 awg wiring is limited to 1000mA.  

### How It Works

For track block occupancy detection details, refer to the BOD Card How it Works](/bod-card-assembly-guide/) section. 

### Connectors

The purpose of the **Block Breakout Board** and its connectors is to facilitate quick and easy connections between the **BOD Card** or **BLVD Card** and the track rails. For setups with multiple distant blocks, breakout boards can be daisy-chained together, or a network cable with a splitter can be used to provide multiple connections efficiently.

| Component Designator | **Connector Label**  | Connector  Type         | **Connection Number** | **Description**                                              |
| -------------------- | -------------------- | ----------------------- | --------------------- | ------------------------------------------------------------ |
| **J1, J2**           | TRACK BLOCKS         | JST XH, Spring Terminal | 1, 2, 3, 4            | Connection to insulated block rails                          |
| **J3**               | TRACK COM            | JST XH, Spring Terminal | 1                     | Connection to non-insulated rail                             |
| **J4, J5**           | BOD/BLVD CARD        | RJ45 Socket             | 1/2, 3/4, 5/6, 7/8    | Each pin pair connects to blocks 1 thru 4.  Cable to BOD Card for detection of trains, and/or cable to BLVD Card for low voltage detection caused by shorts or faulty connections. |
| **J6**               | TEST BOARD CONNECTOR | Card Edge               | 1, 2, 3, 4, COM       | Connection to Test Board for connections to the test board track |

 ## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}block-breakout_board.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram before reference): 

1. Use of 2-pin JST XH pre-wired plugs soldered to track rail drop wires makes for easy wiring and fast connect/disconnect.

2. Use of 2-position Spring Terminals (2.54mm) allow for rail drop wires to be connected directly pulling back a spring lever.  These connectors can be ordered as 2-Position or assembled into a set of 2-Positions.

3. Make sure this track rail has isolators creating blocks, where each block is wired to one or more of Block Breakout Boards and a BOD Card.

   | Component Identifier | Count | Type                                                  | Value      | Package                     | Required | Purpose                                                      |
   | -------------------- | ----- | ----------------------------------------------------- | ---------- | --------------------------- | -------- | ------------------------------------------------------------ |
   | J1-J2                | 2     | JST XH Socket or 2-Position Spring Terminal Connector | 2P, 2.54mm | PTH, vertical or horizontal | Required | Connectors to track **Block Rails** (isolated into block).   |
   | J3                   | 1     | JST XH Socket or 2-Position Spring Terminal Connector | 2P, 2.54mm | PTH, vertical or horizontal | Required | Connector to track **Common Rail** (non-isolated).           |
   | J4, J5               | 2     | RJ45 Socket                                           | 8P8C       | PTH                         | Required | Network cable (CAT5/6) connection from BOD Card. |
   | J6                   | 1     | Card Edge Connector                                   | -          | -                           | Optional | For use with **Test Breakout Board**.                        |


## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="{{ site.baseurl }}/assets/images/pcbs/Breakout_Boards/block_breakout_board_pcb.png/" style="zoom:50%; float:right" />Below are the high level steps for assembly of the Block Breakout Board:

Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

>  See also: [Soldering Tips](/pcb-soldering/)

| Designator (value) | Component                         | Required?                                                    | Orientation                 |
| ------------------ | --------------------------------- | ------------------------------------------------------------ | --------------------------- |
| J1, J2             | JST XH Socket, Terminal Connector | Requires at least 1 connector, placed within a white rectangle | Position connection outward |
| J3                 | JST XH Socket, Terminal Connector | Required                                                     | Position connection outward |
| J4, J5             | RJ45 Socket                       | Optional, for daisy chaining breakout boards                 | None                        |

## Testing and Verification

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.
2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.
3. Use an **Digital Multimeter (DMM)** to test for continuity between:
   - RJ45 socket pins (2, 4, 6, 8) and the 4 block connectors (J1, J2).
   - RJ45 socket pins (1, 3, 5, 7) and the Track Bus connector (J3)


### Functional Testing

Refer to BOD Card for details on testing the Block Breakout Board with the BOD Card.


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

- [Preparing a PCB for Soldering](/pcb-prep/)
- [Solder Tips](/pcb-soldering/)

