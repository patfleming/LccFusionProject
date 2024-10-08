---
title: POD Card Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Card Assembly Guides
nav_order: 2
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
  - Signaling Systems
  - Train Detection
  - Automation Deployment
terms:
  # LCC Fusion Project Terms
  - can_network
  - lcc_fusion_cards
  - lcc_fusion_project
  - lcc_fusion_node_bus
  - lcc_fusion_breakout_boards

  # LCC Fusion Connect Terms
  - lcc_fusion_node_card
  - hw_communications_address
  - hw_communications_bus

  # NMRA LCC Network Terms
  - lcc_event_monitoring_tool
  - lcc_configuration_tool
  - lcc_event_id

  # Model Railroad Automation Terms
  - track_bus

  # Hardware and firmware Terms
  - bridge_rectifier
  - bus
  - dcc_signal
  - edge_card_connector
  - cleaning_pcb
  - component
  - current_limiting_resistor
  - decoupling_capacitor
  - esd_protection_diode
  - ferrite_bead
  - gpio_expander
  - jumper_caps
  - i2c
  - i2c_bus
  - mcp23017
  - network_cable
  - optocoupler
  - stencil
  - tvs_diode
---
# [POD Card](/pod-card-assembly-guide/) Assembly Guide {#bod_card_assembly}
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
## Overview

The Position Occupancy Detector Card ([POD Card](/pod-card-assembly-guide/)), in synergy with the LCC Fusion Node Card, provides detection of the **LCC Fusion Project** system, facilitating precise detection of trains (locomotives and cars) within specified track positions. This integration is pivotal for automating track occupancy detection, a core feature in advanced model railroad setups.

Upon detecting a train at a position, the [POD Card](/pod-card-assembly-guide/) generates an LCC event, signaling the occupancy status. This event is captured by the LCC Node, which, depending on the setup, could trigger various responses such as activating the **PWM Card**. This activation allows for nuanced control over railroad signals and other trackside functionalities, enhancing the realism and operational efficiency of the model railroad environment.

Unlike the BOD Card detection of a train vy current, the [POD Card](/pod-card-assembly-guide/) uses photo sensors to detect changes in lightness as a train passes over a track position.  This method doesn’t required current limiting resistors in wheelsets and also enables persise positioning of trains during spotting operations.  Train direction can also be detected by detecting two seperate locations near each other to determine the order (direction) of detection.

{% include terminology.html %}

## Specifications

Specifications for the card include:

| **Characteristic**                                           | **Value**      |
| :----------------------------------------------------------- | :------------- |
| Maximum POD Detections                                       | 8              |
| Maximum [POD Breakout Board](/pod-breakout-board-assembly-guide/)    | 4              |
| Maximum Cards per LCC Fusion Node Cluster | 16<sup>1</sup> |

1. The LCC Fusion Node Cluster supports up to 16 cards, distributed across two I2C hardware buses, with a maximum of 8 cards per bus.
   - Note: This total includes all cards using the I2C address range of `0x20` (MCP23017 IC).

### How It Works

The following outlines the flow of activity for the [POD Card](/pod-card-assembly-guide/):

1. **Phototransistor Pair**:
   - Two **PT204 phototransistors** work together to detect absence of light when a train is present.  One phototransistors is placed between the rails and a second one is positioned next to the track.
2. **Comparator Operation**:
   - A **LM2903 comparator** compares the voltage from the phototransistors (based on light detection) with a reference voltage set by the resistor network.
   - The output of each comparator will change state depending on the light levels detected by the phototransistors.
3. **Output to MCP23017**:
   - When the PT204 detects a train (blocking or reflecting light), the comparator output changes. The MCP23017 sees this as a **LOW** state due to the comparator pulling the output low. If no train is detected, the comparator output remains high, and the MCP23017 reads this as **HIGH** due to its internal pull-up resistors.
4. **Resistor Network**:
   - The resistors set the reference voltage and current through the phototransistors.
   - These resistors ensure that the comparator has a baseline to compare against the signal from the PT204s.

**System Flow:**

- **Default State**: With no train present, the phototransistor allows current to flow, keeping the comparator's output in a default state (likely **HIGH**, depending on the MCP23017 pull-ups).
- **Train Present**: When a train blocks the light or reflects it differently, the phototransistor's current changes, causing the comparator to output a **LOW** signal, which is then read by the MCP23017 as **LOW** (train detected).

This configuration provides a simple and reliable way of detecting a train’s presence using light and feeding that signal into a digital I/O expander like the MCP23017.


### Protection

To ensure the reliable operation and longevity of your [POD Card](/pod-card-assembly-guide/), several protection components have been integrated. These components safeguard the [POD Card](/pod-card-assembly-guide/) from overcurrent, voltage spikes, and electrical noise. Below is a brief overview of each protection element and its role:

| Protected Component                                          | Protection Component              | Function                                                     | Specifications                                               | Location                                                     |
| ------------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Entire Circuit**                                           | **TVS Diode SMBJ18A**             | Protects from high-voltage transients by clamping voltage spikes, preventing them from reaching sensitive components. | **Stand-off Voltage:** 18V<br>**Clamping Voltage:** 29.2V    | Across the Vcc and GND lines of the track voltage            |
| **LEDs**                                                     | **1K ohm Resistor**               | Limits current to LED to create about 15% brightness         | **Value:** 1k ohms                                           | Between the optocoupler output and LED anode                 |
| **MCP23017**                                                 | **Decoupling Capacitor 0.1 µF**   | Filters out high-frequency noise and transient voltage spikes from the power supply, ensuring a stable voltage for the MCP23017. | **Value:** 0.1 µF                                            | Across Vcc and GND near the MCP23017                         |
| **I2C Lines from LCC Fusion Node Bus Hub** | **Ferrite Bead BLM31PG121SN1L**   | Provides high-frequency noise suppression on the I2C lines.  | **Impedance:** 120 ohms at 100 MHz                           | In series with the SDA and SCL lines of the I2C bus          |
| **I2C Lines from LCC Fusion Node Bus Hub** | **ESD Protection Diode PESD1CAN** | Protects the I2C lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Across the SDA and SCL lines from the card’s edge connector to GND, near the MCP23017. |

### Summary
These protection components work together to safeguard the [POD Card](/pod-card-assembly-guide/) from various electrical faults. The TVS diode clamps high-voltage spikes, the current limiting resistors control the current flow, and the decoupling capacitor filters out noise. The ferrite bead suppresses high-frequency noise on the I2C lines, and the ESD protection diode protects the I2C lines from electrostatic discharge and voltage spikes.  Together, they ensure the [POD Card](/pod-card-assembly-guide/) operates reliably in a potentially harsh electrical environment.

## Components List

PCB for the card and solder stencil can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}POD_Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier                                         | Count | Type               | Value          | Package    | Required? | Purpose                                                      |
| ------------------------------------------------------------ | ----- | ------------------ | -------------- | ---------- | --------- | ------------------------------------------------------------ |
| C1 - C16                                                     | 16    | Ceramic Capacitor  | 1uF            | 1206 SMD   | Optional  | Smooths signal from phototransistors for improved detection  |
| C17                                                          | 1     | Ceramic Capacitor  | 0.1uF          | 1206 SMD   | Required  | Conditions/filters the current for the IC (U1)               |
| D9                                                           | 1     | ESD Diode              | PESD1CAN       | SOT-23 SMD | Optional  | I2C data bus electrostatic discharge (ESD) protection        |
| FB1, FB2                                                     | 2     | Ferrite Bead       | BLM31PG121SN1L | 1206 SMD   | Required  | I2C Data Line Noise Suppression Ferrite Beads                |
| J1 - J4                                                      | 4     | RJ45 Socket        | 8P8C           | PTH        | Required  | Network cable (CAT5/6) connection to [POD Breakout Board](/pod-breakout-board-assembly-guide/)s |
| JP1, JP2                                                     | 2     | Male Header        | 3P, 0.1"       | PTH        | Required  | COMM BUS selection (I2C hardware bus) for either BUS A or BUS B. Must match configuration in LCC Node CDI setup |
| LED1 - LED8                                                  | 8     | LED                | Red            | 1206 SMD   | Optional  | Position occupancy indicators (ON means detection)           |
| R1, R3, R4, R6, R7, R9, R10, R12, R13, R15, R16, R18, R19, R21, R22, R24 | 15    | Resistor           | 10kΩ           | 1206 SMD   | Required  | Sets reference voltage and current through phototransistors  |
| R2, R5, R8, R11, R14, R17, R20, R23                          | 8     | Resistor           | 5.6kΩ          | 1206 SMD   | Required  | Sets reference voltage and current through phototransistors  |
| R25                                                          | 1     | Resistor           | 10kΩ           | 1206 SMD   | Required  | Limits current to MCP23017 Reset pin (normal operation)      |
| R26 - R32                                                    | 7     | Resistor           | 1kΩ            | 1206 SMD   | Optional  | Limits current to status LEDs                                |
| R33 - R36                                                    | 4     | Resistor           | 10kΩ           | 1206 SMD   | Required  | Limits current to SW1 and MCP23017 for I2C address configuration |
| SW1                                                          | 1     | DIP / Slide Switch | 3P, 2.54mm     | PTH        | Required  | COMM ADDR selection (I2C address offset 0-7). Configures address for MCP23017 for CDI setup |
| U1                                                           | 1     | I/O Expander       | MCP23017       | SSOP28 SMD | Required  | I/O Expander using I2C to detect 8 pairs of sensors          |
| U2 - U9                                                      | 8     | Voltage Comparator | LM2903         | DIP-8 PTH  | Required  | Voltage comparator to detect differences in phototransistors |
| SH1, SH2                                                     | 2     | Jumper Cap         | 2.54mm         | N/A        | Required  | Used with I2C Bus and Vcc selections. Recommend tall caps for ease of use |

## Tools Required

For a list of recommended tools, refer to [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="{{ site.baseurl }}/assets/images/pcbs/POD_Card/POD_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the [POD Card](/pod-card-assembly-guide/):

1. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.
2. When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

> See also: [Soldering Tips](/pcb-soldering/)

| Component Identifier                                         | Component (Package)               | Required? | Orientation                                                  |
| ------------------------------------------------------------ | --------------------------------- | --------- | ------------------------------------------------------------ |
| C1 - C16                                                     | 1 uF (100nF) (1206, SMD)          | Optional  | None                                                         |
| C17                                                          | 0.1 uF (100nF) (1206, SMD)        | Required  | None                                                         |
| D9                                                           | Diode, PESD1CAN (SOT-23, SMD)     | Optional  | Fits only one way                                            |
| FB1, FB2                                                     | Diode, BLM31PG121SN1L, (1206 SMD) | Required  | None                                                         |
| J1 - J4                                                      | RJ45 socket (8P8C)                | Required  | Fits only one way                                            |
| JP1, JP2                                                     | Male headers (3P, 0.1" spacing)   | Required  | None                                                         |
| LED1 - LED8                                                  | LED (1206 SMD, Red)               | Optional  | Reference back of LED, position cathode towards PCB **right** edge<img src="/_builder/Cards/images/LED_Orientation.png" style="zoom: 15%; float: right;" /> |
| R1, R3, R4, R6,  R7, R9, R10, R12, R13, R15, R16, R18, R19, R21, R22, R24 | 10KΩ resistors (1206 SMD)         | Required  | None                                                         |
| R2, R5, R8, R11, R14, R17, R20, R23                          | 5.6KΩ resistors (1206 SMD)        | Required  | None                                                         |
| R25                                                          | 10KΩ resistors (1206 SMD)         | Required  | None                                                         |
| R26 - R32                                                    | 1KΩ resistors (1206 SMD)          | Optional  | None                                                         |
| R33 - R36                                                    | 10KΩ resistors (1206 SMD)         | Required  | None                                                         |
| SW1                                                          | DIP / Slide Switch (3P, 2.54mm)   | Required  | Position switch for ON setting to PCB **top** edge               |
| U1                                                           | MCP23017 IC (SSOP28, SMD)         | Required  | Position IC’s indent towards PCB **bottom** edge                 |
| U2-U9                                                        | LM2903 IC (DIP-8, PTH)            | Required  | Position IC’s corner dimple (pin 1) towards PCB **bottom** edge  |

## Testing and Verification

Configure the  [POD Card](/pod-card-assembly-guide/):

1. Select the `COMM BUS` by positioning (2) Jumper Caps on either `A` or `B` male header pins (JP1, JP2)

2. Select the `COMM ADDRESS` switch (SW1) by sliding each of the 3 switches to either the `ON `or `OFF` position.  Setting a switch to ON increments the address by 1, 2, or 4 for an address range of 0 to 7.  Up to 8 devices can then be configured for `A` and 8 for `B`.

The following test and verifications of the card should be performed after a through inspection of the card's soldering.  Check all of the PTH component pins and SMD pads.  Make sure there are no solder bridges between pins and pads.

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.

2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

3. **Component Orientation**: the IC's are correctly oriented according to the PCB silkscreen or schematic.

### Connectivity Testing

**Continuity Check**: Use a multimeter in continuity mode to check for shorts between power rails and ground, and to ensure there are no open circuits in critical connections.

### Power-Up Tests

1. Assembly a tested to the LCC Fusion Node Card.
2. Apply Power to the Power Module and verify the following:
   - **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

Functional testing of the card can be performed after completing the power-up testing.  Testing consists of testing network communiations, followed by the sensing of a train over a phototransistor.

#### HW Communications Testing

Communications testing verifies the LCC Node can communicate with the [POD Card](/pod-card-assembly-guide/)’s I2C IC via the Node Bus Hub connections.  This is performed using the LCC Fusion Node Card’s testing firmware and a serial monitor.

1. Insert the [POD Card](/pod-card-assembly-guide/) into a Node Bus Hub along with a LCC Fusion Node Card.

2. Install LCC Fusion Project firmware that includes serial monitor for testing.

3. Verify that the I2C connection between the  LCC Fusion Node Card and the [POD Card](/pod-card-assembly-guide/) work.  

   > See [Testing I2C Cards](/test-i2c-cards/) for details on how to test the communications for a I2C enabled card.

#### MCP IC Testing

After hardware communication has been established, to verify the MCP IC, use the Node’s serial monitor to simulate an input from each of card’s input pins as follows:

1. In the serial monitor’s input, enter `M` for the LCC Node’s serial monitor **Main Menu**.
2. Select `[1] Node Management` and `[1] Device Testing Management`
3. Select `[5] Simlulate MCP Device Input`
4. From the list of MCP devices, select the device # for the [POD Card](/pod-card-assembly-guide/) being tested
5. Enter the number for the pin to tested.
6. Using the JMRI Event Monitor, verify the correct Event ID was issued.

#### Position Occupancy Detection Testing

After validating the LCC Fusion Node Card can communicate (find) the [POD Card](/pod-card-assembly-guide/), test each of the [POD Card](/pod-card-assembly-guide/) positions.  

>  Position occupancy detection verification is performed using a [POD Breakout Board](/pod-breakout-board-assembly-guide/) with a pair of phototransistors (PT204) position between the rails and next to the rails.

1. Connect a network cable (CAT5/6) to one of the [POD Card](/pod-card-assembly-guide/)’s RJ45 connector.
2. Connect the other end of the network cable to (1) [POD Breakout Board](/pod-breakout-board-assembly-guide/).
3. Setup the  [POD Breakout Board](/pod-breakout-board-assembly-guide/)
   1. Connect a PT204 to the `POSITION 1` `BETWEEN RAILS` connector
   2. Connect a PT204 to the `POSITION 1` `TRACK SIDE` connector

4. Configure each of the card’s device lines using an LCC CDI Configuration Tool
5. Open an LCC Event Monitoring tool (e.g. JMRI Event Monitoring tool).
6. Test each the POD sensor, cover of the two PT204 sensors, simulating a train passing over it.
7. Further test the sensitivity by placing one of the PT204 between the track rails with the 2nd PT204 next to the track.
8. Repeat testing for all (8) [POD Card](/pod-card-assembly-guide/) PODs


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References



