---
title: Hardware Communications
typora-root-url: ..
layout: default
permalink: /:name/
nav_order: 3
use_cases:
  - Node Cluster Setup
  - Signaling Systems
  - System Configuration
  - Hardware Testing & Maintenance
---

# Hardware Communications  Configuration Guide {#hw_communications_configuration}
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

The LCC Node employs I2C hardware communication protocols to connect with I/O cards. This guide details essential configuration steps to establish this communication effectively:

- **Communication Bus Selection**: Determines which bus (A or B) the card utilizes, corresponding to processor hardware buses 0 and 1. 

- **Address Configuration**: Assigns a unique communication address to each card, which must align with the card's physical switch settings. 

  > It's imperative for each card within an LCC LCC Fusion Node Cluster to have a unique combination of bus and address within its Address Group, ensuring no overlap occurs. 

The LCC Node utilizes hardware communication protocols, specifically I2C, to interface with I/O cards. This section outlines the critical configuration steps necessary for establishing communication between the LCC Node and the I/O cards:

- **Communication Bus Selection**: Identifies the bus—either A or B—used by the card, corresponding to the hardware buses 0 and 1 on the processor.
- **Address Configuration**: Sets the unique communication address for each card, aligning with the physical switch settings on the card itself. It's crucial that each card within a given LCC LCC Fusion Node Cluster possesses a distinct bus and address pair within its Address Group to avoid conflicts.  

## Specifications

The maximum capacity of addressable cards within a single LCC LCC Fusion Node Cluster is outlined as follows:

| Address Group | Max Addressable Cards                     |
  | ------------- | ----------------------------------------- |
  | 1             | 16 cards (8 cards per Comminications Bus) |
  | 2             | 16 cards (8 cards per Comminications Bus) |
  | 3             | 16 cards (8 cards per Comminications Bus) |
  | 4             | 16 cards (8 cards per Comminications Bus) |
  | 5             | 16 cards (8 cards per Comminications Bus) |
  | 6             | 48 cards                                  |

  

## Detailed Specifications

The I2C address range depends on the specific I2C-enabled IC or ESP32 sketch supporting each card. Since several cards may utilize the same I2C IC, addresses must be distinct within a configured bus. 

For instance, the Output Card and BOD Card both employ the MCP23017 IC, necessitating unique bus and address pairs within an LCC LCC Fusion Node Cluster.

Below is a breakdown of the I2C addresses available to each card type. 

| Address Group | Card Name           | I2C IC   | I2C Adderss Range (per bus) |
| :-----------: | ------------------- | -------- | --------------------------- |
|       1       | Output Card         | MCP23017 | 0x20 - 0x27                 |
|       1       | BOD Card            | MCP23017 | 0x20 - 0x27                 |
|       1       | Button Card         | MCP23017 | 0x20 - 0x27                 |
|       1       | IO Card             | MCP23017 | 0x20 - 0x27                 |
|       1       | POD Card            | MCP23017 | 0x20 - 0x27                 |
|       1       | Stepper Motor Card  | MCP23017 | 0x20 - 0x27                 |
|       1       | Turnout Card        | MCP23017 | 0x20 - 0x27                 |
|       2       | DCC Card            | ESP32    | 0x10 - 0x17                 |
|       3       | Sound Card          | ESP32    | 0x30 - 0x37                 |
|       4       | PWM Card            | PCA9685  | 0x40 - 0x47                 |
|       5       | UOD Card            | ESP32    | 0x50 - 0x57                 |
|       6       | NFC Tag Reader Card | MFRC523  | 0x08 - 0x3F                 |

  
