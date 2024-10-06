---
title: Audio Card Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Card Assembly Guides
nav_order: 2
use_cases:
  - PCB Design & Assembly
  - Device Control
  - Automation Deployment
subjects:
  - Hardware
  - Automation
  - Assembly Guides
terms:
  - lcc_fusion_cards
  - can_network
  - i2c
  - i2s
  - component
  - jumper_caps
  - lcc_fusion_node_bus
  - stencil
  - lcc_configuration_tool
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_cards
  - lcc_fusion_project
  - lcc_fusion_node_bus

  # LCC Fusion Connect Terms
  - lcc_fusion_node_card
  - lcc_fusion_io_cards
  - hw_communications_address
  - hw_communications_bus

  # NMRA LCC Network Terms
  - lcc_event_monitoring_tool
  - lcc_configuration_tool
  - lcc_event_id

  # Model Railroad Automation Terms

  # Hardware and firmware Terms
  - amplifier
  - audio_signal
  - bus
  - cleaning_pcb
  - component
  - current_limiting_resistor
  - decoupling_capacitor
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
# Audio Card Assembly Guide {#audio_card_assembly}
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
Here's a revised version of your content, with some grammar fixes and rephrasing for clarity:

---

## Introduction

The **Audio Card** works alongside the **LCC Fusion** LCC Fusion Node Card and a Node Bus Hub to provide text-to-audio and .wav file playback capabilities through up to four speakers. Administrators can use an LCC Configuration Tool to assign specific LCC Event IDs to trigger the playback of either text messages or .wav files. The Audio Card receives text messages from one or more LCC Nodes, converts the text into audio, and then plays the audio through one of the four speakers using a low-power audio amplifier.

Potential applications for the Audio Card include:

- Providing audio feedback to LCC users with audio generated from:
  - Key error and status messages
  - User-defined messages triggered by specific LCC Event IDs (configured via CDI)

- Playing sound effects from .wav files, such as:
  - A metallic clanking sound for when turnout points are set
  - A bell sound

The **Audio Card** hardware configuration includes:

- **SuperMini ESP32-S3 module:** This module powers the firmware responsible for:
  - **Text-to-audio conversion:**
    - Receiving text messages via I2C or Bluetooth
    - Converting the text to audio signals using the Espeak-NG Text-to-Speech Library
    - Sending the audio signals via I2S to the audio amplifier

  - **.wav file playback:**
    - Reading the specified .wav file from a micro-SD card reader
    - Sending the .wav data via I2S to the audio amplifier

- **Audio Amplifier:** Supports up to four MAX98357A IC audio amplifiers, each capable of sending audio to a speaker via either RJ45 or 2-pin terminal connectors.

{% include terminology.html %}

## Specifications

The card's specifications are as follows:

| Characteristic                                               | Value            |
| ------------------------------------------------------------ | ---------------- |
| Max Speakers                                                 | 4                |
| Max Audio Amps                                               | 4                |
| Max Text Message Length                                      | 16K Characters   |
| Max .wav File Size                                           | 400K<sup>1</sup> |
| Maximum Number of Cards per LCC Fusion Node Cluster | 16<sup>2</sup>   |
| LCC Fusion Node Bus HubConnectors     | 1<sup>3</sup>    |

1. If the ESP32 has PSRAM, the .wav file size can be up to the size of PSRAM (e.g., 2MB).
2. The LCC Fusion Node Cluster can support up to 16 cards, distributed across two I2C hardware buses, with a maximum of 8 cards per bus.
   - Note: This total includes all cards using the I2C address range of `0x60`, as defined by the ESP32 firmware for audio.
3. Connections include GND, 5V, SCL0/SDA0, and SDA1/SCL1.

### How It Works

The following outlines the operational flow of the Audio Card:

The firmware of the LCC Fusion Node Card interfaces with the ESP32 on the Audio Card, leveraging the bus and address details specified in the card's CDI I2C section.

**Text-to-audio conversion:**

1. Upon receiving an LCC Event-related signal, the LCC Fusion Node Card firmware sends an I2C text message to the Audio Card, instructing it to convert the text into audio for the configured audio device.

   > Alternatively, the Audio Card can receive text messages via Bluetooth from a Bluetooth Serial App (e.g., on a phone).

2. The ESP32 on the Audio Card uses a text-to-speech library to convert the text to audio signals and passes them to the audio amplifier via an I2S (serial) connection.

3. The audio amplifier outputs the audio signal to a speaker connected via a JST XH socket or an RJ45 socket.

**Wav file playback:**

1. Upon receiving an LCC Event-related signal, the LCC Fusion Node Card firmware sends an I2C message to the Audio Card, instructing it to play a specific .wav file from the micro-SD card.

   > Alternatively, the Audio Card can receive text messages via Bluetooth from a Bluetooth Serial App (e.g., on a phone).

2. The ESP32 on the Audio Card reads the specified .wav file (by name) from the micro-SD card reader and passes the audio data to the audio amplifier via an I2S connection.

### Protection

The Audio Card converts text messages into audio signals, which are then amplified and outputted through speakers. The following is an overview of each protection component integrated into the Audio Card and its role:

| Protected Component    | Protection Component              | Function                                                     | Specifications                                               | Location                                            |
| ---------------------- | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------- |
| **Speaker Connectors** | **SS310 Diodes**                  | Protect against reverse voltage by blocking current flow in the wrong direction. | **Reverse Voltage:** 100V<br>**Forward Current:** 3A         | In series with each input/output power connector    |
| **Audio Amp**          | **Decoupling Capacitors**         | Filters out high-frequency noise and transient voltage spikes from the power supply, ensuring stable voltage to audio amp IC. | **Values:** 0.1 µF ceramic, 10 µF electrolytic or ceramic    | Across Vcc and GND near IC.                         |
| **I2C Lines**          | **Ferrite Bead BLM31PG121SN1L**   | Provides high-frequency noise suppression on the I2C lines.  | **Impedance:** 120 ohms at 100 MHz                           | In series with the SDA and SCL lines of the I2C bus |
| **I2C Lines**          | **ESD Protection Diode PESD1CAN** | Protects the I2C lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Across the SDA and SCL lines to GND                 |
| **Speaker Connectors** | **SS310 Diodes**                  | Protect against reverse voltage by blocking current flow in the wrong direction. | **Reverse Voltage:** 100V<br>**Forward Current:** 3A         | In series with each speaker connectors              |

## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}Audio Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram on right for reference):

| Component Identifier | Count | Type                 | Value                | Package                | Required | Purpose                                                      |
| -------------------- | ----- | -------------------- | -------------------- | ---------------------- | -------- | ------------------------------------------------------------ |
| C1, C3, C5, C7, C10  | 5     | Capacitor            | 0.1uF                | 1206 SMD               | Required | Decoupling Capacitor for IC Protection                       |
| C2, C4, C6, C8, C9   | 5     | Capacitor            | 10uF                 | 1206 SMD               | Required | Decoupling Capacitor for IC Protection                       |
| D1 - D8              | 8     | Diode                | SS310                | SMD                    | Required | Circuit protection from reverse current from speaker connections. |
| D5                   | 1     | Diode                | PESD1CAN             | SOT-23 SMD             | Optional | I2C data bus electrostatic discharge (ESD)                   |
| F1                   | 1     | PPTC Resettable Fuse | 0.2A, 3V (or higher) | 1206 SMD               | Required | Protects overload from SD Module                             |
| F2                   | 1     | PPTC Resettable Fuse | 1A, 5V (or higher)   | 1206 SMD               | Required | Protects overload from audio speakers                        |
| FB1, FB2             | 2     | Ferrite Bead         | BLM31PG121           | 1206 SMD               | Required | I2C Network Bus Data Line Noise Suppression                  |
| J1 - J4              | 4     | JST XH Socket        | 2P, 2.54mm           | PTH or Spring Terminal | Optional | Connectors to speakers                                       |
| J5                   | 1     | RJ45 Socket          | 8P8C                 | PTH                    | Optional | Network cable (CAT5/6) connections to speakers (4 pairs).    |
| J6, J7               | 2     | Female Header        | 9-Pin                | PTH                    | Required | Socket for Super-Mini ESP32-S3 development board(s)          |
| J8                   | 1     | Female Header        | 8-Pin                | PTH                    | Optional | Required when using Micro-SD Card Reader for playing .wav files. |
| JP1, JP2             | 2     | Male Header          | 3P, 0.1"             | PTH                    | Required | Used for COMM BUS selection (I2C hardware bus) for either BUS A or BUS B. |
| R1, R2, R3           | 3     | Resistor             | 1kΩ                  | 1206 SMD               | Required | Used to limit the current to SW1 and MCP23017 for the I2C address |
| SW1                  | 1     | Slide Switch         | 3P, 2.54mm           | PTH                    | Required | Used for COMM ADDR selection (I2C address offset, 0-7).      |
| U1, U2, U3, U4       | 4     | Audio Amp            | MAX98357A            | 16TQFN                 | Required | Class D audio amplifier supporting I2S connections           |
| Micro-SD Card Reader | 1     | Module               | SPI                  | N/A                    | Optional | Micro-SD Card Reader is required for playing .wav files.     |
| Micro-SD Card        | 1     | SD Card              | N/A                  | N/A                    | Optional | Required for storing .wav files.                             |
| SH1, SH2             | 2     | Jumper Cap (Shunt)   | 2.54mm               | -                      | Required | Used to set the COMM BUS selection (JP1, JP2)                |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

1.  <img src="/assets/images/pcbs/Audio_Card/Audio_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the Audio Card:
2. Position the card with the edge connector tabs facing down (see image on right).
3. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.
4. When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

>  See also: [Soldering Tips](/pcb-soldering/)

| Designator (value)  | Component                     | Required?                           | Orientation                                                  |
| ------------------- | ----------------------------- | ----------------------------------- | ------------------------------------------------------------ |
| C1, C3, C5, C7, C10 | 0.1uF                         | Required                            | None                                                         |
| C2, C4, C6, C8, C9  | 0.10uF                        | Required                            | None                                                         |
| D1 - D8             | SS310                         | Required                            | Cathode end has a white line and positioned towards PCB left edge |
| D9, D10             | PESD1CAN                      | Optional                            | None                                                         |
| F1                  | Fuse, 0.2A                    | Required                            | None                                                         |
| F2                  | Fuse, 1A                      | Required                            | None                                                         |
| FB1, FB2            | BLM31PG121SN1L                | Required                            | None                                                         |
| J1 - J4             | JSX XH, or Terminal Connector | Required                            | None                                                         |
| J5                  | RJ45 socket                   | Optional                            | Fits only one way                                            |
| J6, J7              | 9-Pin Female Headers          | Required                            | None                                                         |
| J8                  | 8-Pin Female Header           | Optional                            | None                                                         |
| JP1, JP2            | 3-Pin Male Headers            | Required                            | None                                                         |
| R1, R2, R3          | 10k&Omega;                    | Required                            | None                                                         |
| SW1                 | DIP / Slide Switch            | Required                            | Position ON towards PCB top edge                             |
| U1, U2, U3, U4      | MAX98357A                     | At least one audio amps<sup>1</sup> | Small dot (pin 1) on package is positioned to PCB bottom and right edges |

1. Each audio amp configuration consists of MAX39357A IC, 2 capacitors (0.1 uF, 10uF), 2 diodes (SS310), and speaker connections (JST XH and/or RJ45 socket).

## Testing and Verification

The following test and verifications of the card should be performed after a through inspection of the card's soldering.  Check all of the PTH component pins and SMD pads.  Make sure there are no solder bridges between pins and pads.

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.

2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

3. **Component Orientation**: the IC's are correctly oriented according to the PCB silkscreen or schematic.

### Connectivity Testing

1. **Continuity Check**: Use a multimeter in continuity mode to check for shorts between power rails and ground, and to ensure there are no open circuits in critical connections.

### Power-Up Tests

1. Assembly a tested Power Module to the LCC Fusion Node Card.
2. Apply Power to the Power Module and verify the following:
   - **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

#### I2C Verification

1. Verify that the I2C connection between the  LCC Fusion Node Card and the Audio Card work.  See [Testing I2C Cards](@ref testing_I2C_cards) for details on how to test the I2C for a I2C enabled card.


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

1.  [Choosing the Right Resistor for LEDs](/led-card-usage-guide/)
1.  Super-Mini ESP32-S3 pin assignments.<img src="/assets/images/pcbs/Node_Card/SuperMini_ESP32-S3_pinout.png" alt="image-20240813095602688" style="zoom:70%; float:right" />

