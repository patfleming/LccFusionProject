---
title: LCC Event ID
typora-root-url: ..
layout: default
permalink: /:name/
parent: Builder's Resources & Tips
use_cases:
  - LCC Event Management
  - System Configuration
  - Learning & Planning
  - Hardware Testing & Maintenance
---

# LCC Event IDs {#lcc_event_ids}
{:toc}
## Introduction

The LCC Node firmware uses LCC Events (messages) that contain a unique Event ID.  Each unique identifier is used within the LCC system to trigger actions or changes in the state of connected devices.  An Event ID is a 64-bit number in a dotted hexadecimal format.  For example: 05.01.01.01.5C.65.00.00.  The LCC Node firmware provides default values that can be modified and reused thru the use of a LCC configuration tool such as the one provided by NMRA JMRI application.

For example, pressing a button could be detected by the LCC Node firmware and would result in the production of an LCC Event containing a unique LCC Event ID.  Since the LCC Fusion Project supports many different I/O cards, each supporting multiple devices, a significant number of events are generated.  

To provide consistency and structure to the Event ID, the LCC Node firmware uses the following format when generating an Event ID.  Note that all Event IDs are 64-bits (8 bytes) and typically shown using dotted hexadecimal format where digits consists of 0-9, A-F (base 16).

| Byte Position | Description                                   | Details                                                      |
| ------------- | --------------------------------------------- | ------------------------------------------------------------ |
| 1-5           | OpenLCB Group Assigned for LCC Fusion Project | LCC Fusion Project firmware generated Event IDs start with this prefix.  Other prefixes are provided by the NMRA LCC organization.  [View OpenLCB Unique ID Ranges](https://registry.openlcb.org/uniqueidranges) provides a list of current NMRA LCC assigned Event ID ranges and the ability for individuals to request their own range. |
| 6             | Node ID Qualifier                             | In combination with bytes 1-5, the Node ID qualifier provides a 6-byte **LCC Node ID** which must be unique within a specific LCC Node network.  This qualifier must be configured for each LCC Node.  LCC Node Fusion Project Node firmware defaults to a value of 0x65 which can be changed using a CDI configuration tool or serial monitor. |
| 7 (digit 1)   | Source Identifier                             | Source Identifier groups Event ID ranges by their source or use. |
| 7 (digit 2)   | Card Number                                   | Card Number  further groups Event IDs by their assigned card (0 for non-card related Event IDs). |
| 8             | Sequential Qualifier                          | Sequentially generated value assigned to the Event ID.  When combined with bytes 1-7, results in a unique Event ID for the LCC Node. |

## LCC Fusion Project Default Events IDs

Shown below are the default Event IDs ranges per source.  Note that a unique Event ID range is provided for each card type and card number, allowing the LCC Node firmware to be updated with different configurations of card types and number of cards.  For example, the default Event ID range for the first two cards will remain unchanged, as the third BOD Card will be assigned its own range.

> To reduce documentation and reconfiguration, use producer generated default Event ID to simplify Event ID management when configuring Event IDs to be used by consumers.  For example, use the default BOD Card’s Event IDs when configuring Event IDs to be consumed by Signal Logics and Conditionals.

| Source (card name) | Card Identifier (1st digit of byte 7)(hex) | Card Number (2nd digit of byte 7) (hex) | Devices per Card | Events per Device | MAX Events (per Card/Node) | Event ID Range Offset | Event ID Range (Low/High Example)                   |
| ------------------ | :----------------------------------------: | :-------------------------------------: | :--------------: | :---------------: | :------------------------: | :-------------------: | :-------------------------------------------------- |
| BOD Card           |                     0                      |                0-F (16)                 |        8         |         2         |         16 (Card)          |         0x00          | 05.01.01.01.5C.xx.00.00 <br>05.01.01.01.5C.xx.07.0F |
| POD Card           |                     0                      |                0-F (16)                 |        4         |         2         |          8 (Card)          |         0x20          | 05.01.01.01.5C.00.00.20 <br>05.01.01.01.5C.xx.07.37 |
| Input Card         |                     2                      |                 0-7 (8)                 |        16        |         2         |         32 (Card)          |         0x00          | 05.01.01.01.5C.xx.20.00 <br>05.01.01.01.5C.xx.27.1F |
| Button Card        |                     2                      |                 0-7 (8)                 |        16        |         2         |         32 (Card)          |         0x20          | 05.01.01.01.5C.xx.20.20 <br>05.01.01.01.5C.xx.27.3F |
| Output Card        |                     3                      |                 0-7 (8)                 |        16        |         2         |         32 (Card)          |         0x00          | 05.01.01.01.5C.xx.30.00 <br>05.01.01.01.5C.xx.37.1F |
| I/O Card           |                     3                      |                 0-7 (8)                 |        16        |         2         |         32 (Card)          |         0x20          | 05.01.01.01.5C.xx.30.20 <br>05.01.01.01.5C.xx.37.3F |
| Turnout Card       |                     4                      |                 0-7 (8)                 |        8         |         4         |         32 (Card)          |         0x00          | 05.01.01.01.5C.xx.40.00 <br>05.01.01.01.5C.xx.47.1F |
| Signaling Rules    |                     5                      |                 0-7 (8)                 |  8x4 (Masts x )  |         3         |         96 (Card)          |         0x00          | 05.01.01.01.5C.xx.50.00 <br>05.01.01.01.5C.xx.50.5F |
| Signaling Circuits |                     5                      |                    0                    |       n/a        |         8         |          8 (Node)          |         0xE0          | 05.01.01.01.5C.xx.50.E0 <br>05.01.01.01.5C.xx.50.E7 |
| Signaling Masts    |                     5                      |                 0-7 (8)                 |        8         |         1         |          8 (Card)          |         0xF0          | 05.01.01.01.5C.xx.50.F0 <br>05.01.01.01.5C.xx.57.F7 |
| Signaling Logics   |                     6                      |                    0                    |       n/a        |                   |         160 (Node)         |         0x00          | 05.01.01.01.5C.xx.60.00 <br>05.01.01.01.5C.xx.60.FF |
