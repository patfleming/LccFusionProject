---
title: Sound Card Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Card Assembly Guides
nav_order: 2
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
  - Device Control
  - Automation Deployment
subjects:
  - Hardware
  - Automation
  - Assembly Guides
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_cards
  - lcc_fusion_project
  - lcc_fusion_node_bus
  # LCC Fusion Connect Terms
  - lcc_fusion_node_card
  - output_cards
  - hw_communications_address
  - hw_communications_bus

  # NMRA LCC Network Terms
  - lcc_event_monitoring_tool
  - lcc_configuration_tool
  - lcc_event_id

  # Model Railroad Automation Terms

  # Hardware and firmware Terms
  - bus
  - cleaning_pcb
  - component
  - decoupling_capacitor
  - edge_card_connector
  - esd_protection_diode
  - esp32_s3
  - ferrite_bead
  - jumper_caps
  - i2c
  - i2c_bus
  - network_cable
  - stencil
  - tvs_diode
---
# Sound Card Assembly Guide {#sound_card_assembly}
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

The Sound Card is used with the LCC LCC Fusion Node Card to play sounds simultaneously from up to four different low cost MP3 players.   Initiated thru LCC Events, MP3 files can be played/stopped for sounds for layout automation.

{% include terminology.html %}

## Specifications

The card has the following:

- Maximum of 4 MP3 devices can be used.   
- Requires a mini MP3 player.  Supported players are the [DFRobots DFPlayer Mini](https://www.dfrobot.com/product-1121.html) and compatible (MP3-TF-16P player)
- Only 4-8 ohm speaker(s) can be attached
- Max of 4 watts of output is provided by player device
- LCC Fusion Node Bus Hubconnections; GND, 5V, SLA0/SDA0, and SDA1/SCL1 (optional)

In the sections below, are the steps to assemble the card.


- Description of the final assembled board's functionality.

### How It Works

The following outlines the flow of activity for the Sound Card:

1. Activity starts with an LCC Event sound related event being received by an LCC Fusion Node Card (firmware)

2. The LCC Node uses the Sound Card's CDI configuration information to determine the I2C address of the card

3. A unique text message is sent to the Sound Card via I2C communications.  The text message indicates one of the following:

   - **play** a specific mp3 file at the specified volume from a specific player (1-4).  MP3 files are identified by their relative file number (0001xxx.mp3, 0002yyyy.mp3, etc.)

   - **loop** a specific MP3 file continously

   - **pause** playing the current MP3 file on a specific player device

   - **reset** causes the MP3 players saved setting to be reset (setting are saved by default to NVS)

4. The Sound Card's ESP32 devices processes the message and uses UART serial communications to connect to the specified MP3 device and sends MP3 commands to the player (play/pause, file #, and volume level)

5. MP3 player device plays/pauses the MP3.  MP3 files are loaded from micro-SD card inserted in the player's SD card reader.

### Protection

The Sound Card is equipped with several protective components to ensure reliable operation and safeguard the board and connected devices from potential electrical issues. Below is an overview of the protection mechanisms implemented:

| **Protected Component**     | **Protection Component**            | **Function**                                                 | **Specifications**            | **Location**                                 |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ----------------------------- | -------------------------------------------- |
| **I2C Communication Lines** | **PESD1CAN Diode**                  | Protects the I2C lines from **ESD (Electrostatic Discharge)** and other electrical surges. | **Clamping voltage**: 24V max | Located on I2C data (SDA, SCL) lines.        |
| **I2C Communication Lines** | **BLM31 Diodes**                    | Provides additional protection to the I2C lines by filtering out high-frequency noise and protecting against voltage spikes. | **Bidirectional TVS diode**   | Positioned along I2C communication lines.    |
| **I2C Address Selector**    | **10kΩ Current Limiting Resistors** | Limits the current on the I2C address configuration pins, preventing excessive current from damaging the MCP23017. | 10kΩ resistors                | On the I2C address offset selector switches. |

 ## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}Sound Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier | Count        | Type               | Value/Description                                            | Package    | Required? | Purpose                                                      |
| -------------------- | ------------ | ------------------ | ------------------------------------------------------------ | ---------- | --------- | ------------------------------------------------------------ |
| D1, D2               | 2            | ESD Diode              | PESD1CAN                                                     | SOT-23 SMD | Required  | I2C data bus electrostatic discharge (ESD) protection |
| FB1, FB2 | 2 | Ferrite Bead | BLM31PG121SN1L | 1206 SMD | Required | I2C Network Bus Data Line Noise Suppression |
| J1                   | 1            | RJ45 Socket        | 8P8C                                                         | PTH        | Required  | Speaker connections                                          |
| J2-J5                | 4            | Spring Terminal    | 8P, 2.54mm                                                   | PTH        | Optional  | Speaker connections                                          |
| J6-J9                | 4            | Male Headers       | 2P, 0.1" spacing                                             | PTH        | Optional  | Earphone/Speaker connections for testing                     |
| JP1, JP2             | 2            | Male Header        | 3P, 0.1" spacing                                             | PTH        | Required  | Used to set the I2C bus to be used (A or B). These are the ESP32 hardware buses used for serial communications (0 or 1). |
| JP11-JP14            | 4            | DFPlayer Mini      | DFRobots DFPlayer Mini                                       | PTH        | Required  | [DFRobots DFPlayer Mini](https://www.dfrobot.com/product-1121.html) (or compatible MP3-TF-16P player) to play files from mini-SD card |
| R2, R4-7             | 5            | Resistor           | 33kΩ                                                         | 1206 SMD   | Required  | Limits the current to the Tact button and MP3 player (play/pause function) |
| R1                   | 1            | Resistor           | 15kΩ                                                         | 1206 SMD   | Required  | Limits the current to the Tact button and MP3 player (volume+ long press) |
| R3                   | 1            | Resistor           | 24kΩ                                                         | 1206 SMD   | Required  | Limits the current to the Tact button and MP3 player (volume- long press) |
| R7-R9                | 3            | Resistor           | 10kΩ                                                         | 1206 SMD   | Required  | Limits the current to SW1 and ESP32 for the I2C address      |
| SW1                  | 1            | DIP / Slide Switch | 3P, 2.54mm                                                   | PTH        | Required  | Sets I2C address offset (0-7), added to base address of ESP32 (0x10). |
| SW2-SW6              | 5            | Tact Button        | N/A                                                          | SMD     | Optional  | Controls for play/pause, and volume + / - (player 1)         |
| U2                   | 1            | ESP32 Module       | ESP32 DevKitC                                                | DevKitC    | Required  | Processes I2C text messages from the Node Card and sends player commands via UART |
| SH1, SH2             | 2           | Jumper Cap         | [Jumper Cap (2.54mm)](https://www.aliexpress.us/w/wholesale-jumper-caps.html?spm=a2g0o.detail.search.0) | 2.54mm     | Required  | Used with I2C Bus selection                                  |
|                      | 1 per player | MicroSD Card       | N/A                                                          | N/A        | Required  | Stores MP3 files to play (one per player). Filenames must be formatted as 000nn<optional-name>.mp3, where nn is a number from 1-100. |

## Tools Required

> [List of recommended tools](@ref pcb_tools).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/Sound_Card/Sound_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the Sound Card:

1. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

2. When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

3. Apply soldering paste for all SMD components

4. Place SMD components into paste.  

| Component Identifier | Component (Package)                                          | Required? | Orientation                                   |
| -------------------- | ------------------------------------------------------------ | --------- | --------------------------------------------- |
| D1, D2               | PESD1CAN (SMD)                                               | Required  | Fits only one way                             |
| FB1, FB2             | Diode, BLM31PG121SN1L, 1206 SMD                              | Required  | None                                          |
| J1                   | 8P8C                                                         | Required  | Fits only one way                             |
| J2-J5                | 8P, 2.54mm                                                   | Optional  | None                                          |
| J6-J9                | 2P, 0.1" spacing                                             | Optional  | None                                          |
| JP1, JP2             | 3P, 0.1" spacing                                             | Required  | None                                          |
| JP11-JP14            | DFRobots DFPlayer Mini                                       | Required  | Position SD card slot to PCB **right** edge   |
| R2, R4-7             | 33kΩ                                                         | Required  | None                                          |
| R1                   | 15kΩ                                                         | Required  | None                                          |
| R3                   | 24kΩ                                                         | Required  | None                                          |
| R7-R9                | 10kΩ                                                         | Required  | None                                          |
| SW1                  | 3P, 2.54mm                                                   | Required  |                                               |
| SW2-SW6              | N/A                                                          | Optional  | Fits only one way                             |
| U2                   | ESP32 DevKitC                                                | Required  | Position USB connection to PCB **right** edge |
| SH1, SH2             | [Jumper Cap (2.54mm)](https://www.aliexpress.us/w/wholesale-jumper-caps.html?spm=a2g0o.detail.search.0) | Required  |                                               |

1. Insert MP3 player devices.  Position the players using the diagram on the PCB.  The SD card slot should be facing out.

2. Insert ESP32, using diagram on the PCB.  USB-C socket should face outward.  Note, firmware is loaded before inserting ESP32 into headers.

3. Add pair of Jumper Shunts to JP10 to set the I2C communications bus (A or B).  Insure that both I2C lines are set to the same A or B value.

4. Set I2C communications address using slide DIP switch (SW1).  Address can be set to 0 thru 7.  This value must match the card's configuration in the CDI.

5. Attached speaker wires to the spring terminal connector(s) and/or using network cable (CAT5/6) using RJ45 socket.

6. Install card into Node Bus Hub, along with a LCC Fusion Node Card for testing. 

   > Note that cards must be orientated in Node Bus Hub to align their **card key** with Node Bus Hub cutout.

>  See also: [Soldering Tips](/pcb-soldering/)

## Testing and Verification

The following test and verifications of the card should be performed after a through inspection of the card's soldering.  Check all of the PTH component pins and SMD pads.  Make sure there are no solder bridges between pins and pads.

## Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.

2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

3. **Component Orientation**: the IC's are correctly oriented according to the PCB silkscreen or schematic.

## Connectivity Testing

1. **Continuity Check**: Use a multimeter in continuity mode to check for shorts between power rails and ground, and to ensure there are no open circuits in critical connections.

## Power-Up Tests

1. **Apply Power**:  Check for correct voltage levels at these locations:
   1. Using the tabs at the base of the card, verify at the base of the card that the LCC Fusion Node Bus Hubis providing 3V3, 5V, and 12+V.   If verification fails, there is a component that is not installed correctly, or a solder bridge.
2. **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

## Functional Testing

### I2C Verification

1. Verify that the I2C connection between the  LCC Fusion Node Card and the IO Card work.  See [Testing I2C Cards](/test-i2c-cards/) for details on how to test the I2C for a I2C enabled card.

### MP3 Player Verification

After validating the LCC Fusion Node Card can connect with the IO card, test each of the MP3 players as follows:

## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

1.  [DFPlayer Specifications](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299)
1.  [DFPlayer Purchase (AliExpress)](https://www.aliexpress.us/w/wholesale-dfplayer.html?spm=a2g0o.detail.auto_suggest.1.6502nwzInwzI9o)
1.  [MP3Gain](https://sourceforge.net/projects/mp3gain/files/MP3Gain-Windows%20%28Stable%29/1.2.5/mp3gain-win-full-1_2_5.exe/download) tool for configuring the gain (sound level) of MP3 files
1.  [Micro SD Cards (AliExpress)](https://www.aliexpress.us/w/wholesale-sd-card-2gb.html?spm=a2g0o.home.search.0) - recommend low cost 2GB-4GB cards
1.  [ESP32 DevKitC Module](https://www.aliexpress.us/w/wholesale-esp32-devkitc.html?spm=a2g0o.detail.search.0) - 38Pin ESP32 DevKitC with ESP32-WROOM-32D

