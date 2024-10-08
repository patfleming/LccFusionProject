---
title: BLVD Card Assembly Guide
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
  - Hardware Testing & Maintenance
terms:
  # LCC Fusion Project Terms
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
  - low_voltage_detection
  - mcp23017
  - network_cable
  - stencil
  - tvs_diode

---





# BLVD Card Assembly Guide {#blvd_card_assembly}

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

### Introduction to the Block Low Voltage Detection (BLVD) Card

The Block Low Voltage Detection (BLVD) Card is a vital component for model railway enthusiasts using the LCC Fusion Project. This card continuously monitors the voltage levels of individual track blocks to ensure they remain within safe operating limits. It is designed to detect when the voltage drops below a predefined threshold, indicating potential issues such as poor connections, excessive load, or power supply problems.



### Key Features:

- **Voltage Monitoring**: Continuously measures the voltage across track blocks.
- **Low Voltage Indicators**: When configured with the LCC Configuration Tool, LCC Events are generated when a block’s voltage drops below 12V.  In addition,  an LED status indicator on the card turns on.
- **Comparator Circuit**: Utilizes an LM393 comparator to compare block voltage against a stable reference voltage.
- **Visual Indicators**: Supports LED indicators for each block, providing real-time status.
- **MCP23017 Integration**: Interfaces with MCP23017 GPIO expander to report low voltage conditions to a central controller.
- **Protection**: Includes TVS diode protection to safeguard against voltage spikes.

### When to Use It:

- **Track Power Monitoring**: Essential for ensuring consistent power delivery to locomotives.
- **Fault Detection**: Quickly identifies and alerts to low voltage conditions that could affect train operation.
- **Maintenance**: Aids in diagnosing and troubleshooting electrical issues within the layout.

By integrating the BLVD Card into your LCC Fusion Project, you can enhance the reliability and performance of your model railway system, ensuring smooth and uninterrupted operation of your locomotives and other track components.

The **BLVD Card** hardware configuration includes:

- communication address; I2C bus (0 or 1) and address offset (0-7)

### Common Causes of Low Voltage in Model Railway Layouts

1. **Short Circuits**: Direct connections between V+ and GND, often due to derailments or wiring issues, can cause significant voltage drops.
2. **High Current Draw**: Multiple locomotives or accessories drawing excessive current from the same track block can lower voltage levels.
3. **Poor Connections**: Loose, corroded, or poorly soldered connections increase resistance, causing voltage drops.
4. **Long Wire Runs**: Extended wiring increases resistance, leading to voltage loss over distance.
5. **Faulty Power Supply**: A malfunctioning or underpowered supply can fail to maintain stable voltage levels.
6. **Dirty Tracks**: Dust and dirt on the tracks can impede electrical contact, resulting in lower voltage at the rails.

{% include terminology.html %}

## Specifications

| **Characteristic**                                           | **Value**      |
| ------------------------------------------------------------ | -------------- |
| **Max Blocks Monitored**                                     | 8              |
| **Low Voltage Threshold**                                    | 12V            |
| **Maximum Number of Cards per LCC Fusion Node Cluster** | 16<sup>1</sup> |
| **LCC Fusion Node Bus HubConnectors** | 1              |

1. The LCC Fusion Node Cluster can support up to 16 cards, distributed across two I2C hardware buses, with a maximum of 8 cards per bus.
   - Note: total includes all cards using the I2C address range of ````0x20```` (MCP23017 IC).

### Additional Details:

- **TVS Diode**: Cathode to Track V+, Anode to Track Bus GND.
- **Current-Limiting Resistor for LED**: Typically 330Ω for a 3.3V or 5V supply.
- **Integration**: Easily integrates with existing LCC nodes for seamless operation.

This table provides a comprehensive overview of the key specifications and operational limits of the BLVD Card, ensuring end-users have all the necessary information for effective implementation and use.

## How It Works

The Block Low Voltage Detection (BLVD) Card operates by continuously monitoring the voltage levels of individual track blocks to ensure they remain within safe operating limits. Here’s a detailed overview of how the components work together:

1. **Voltage Sensing**: The card receives V+ and GND from each track block. The AC inputs (V+ and GND) are fed into a bridge rectifier, which converts the AC-like DCC signal into a DC signal.

2. **Smoothing**: A 220µF capacitor is used to smooth the rectified DC voltage, providing a stable voltage for measurement.

3. **Reference Voltage**: A 12V Zener diode, in conjunction with a 1kΩ current-limiting resistor, provides a stable 12V reference voltage to the inverting input (IN1-) of the LM393 comparator. 

4. **Comparison**: The LM393 comparator compares the scaled voltage from the track block with the reference voltage. If the block voltage falls below the threshold of 12V, the comparator output changes state to LOW.  

5. **Output Signal**: The output of the LM393 is connected to an input pin on the MCP23017 GPIO expander. A pull-up resistor ensures a defined logic level when the comparator output is not active.  That is, when when the voltage is above 12V the comparator output remains HIGH because of  the MCP23017 internal pullup resistors.

   > The MCP23017 GPIO must be configured for input /w pullup to prevent the LM393 output pins from ‘floating’.

6. **Indicator**: Optionally, an LED can be connected to the output of the LM393 to provide a visual indication of a low voltage condition. The LED lights up when the comparator output goes low, indicating a problem.  The LED’s anode is provided 3V3 and the cathode sinks, thru 1k current liming resistor, when the LM393 output goes to  GND.  

7. **Protection**: A TVS diode is connected between the Track V+ and Track GND to protect the circuit from voltage spikes and transients.

This coordinated operation ensures that the BLVD Card accurately monitors and indicates low voltage conditions across the track blocks, enhancing the reliability and safety of the LCC Fusion Project.

### Protection

To ensure the reliable operation and longevity of your Block Occupancy Detection (BOD) card, several protection components have been integrated. These components safeguard the BOD Card from overcurrent, voltage spikes, and electrical noise. Below is a brief overview of each protection element and its role:

| Protected Component                                          | Protection Component              | Function                                                     | Specifications                                               | Location                                                     |
| ------------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Entire Circuit**                                           | **TVS Diode SMAJ5CA**             | Protects from high-voltage transients by clamping voltage spikes, preventing them from reaching sensitive components. | **Stand-off Voltage:** 5V<br>**Clamping Voltage:** 6.8-7.2V  | Across the Vcc and GND lines of the track voltage            |
| **MCP23017 GPIO**                                            | **10k ohm Resistor**              | Further limits current between the optocoupler output and the MCP23017 GPIO pin. | **Value:** 10k ohms                                          | Between the optocoupler output and MCP23017 input            |
| **MCP23017**                                                 | **Decoupling Capacitor 0.1 µF**   | Filters out high-frequency noise and transient voltage spikes from the power supply, ensuring a stable voltage for the MCP23017. | **Value:** 0.1 µF                                            | Across Vcc and GND near the MCP23017                         |
| **I2C Lines from LCC Fusion Node Bus Hub** | **Ferrite Bead BLM31PG121SN1L**   | Provides high-frequency noise suppression on the I2C lines.  | **Impedance:** 120 &Omega; at 100 MHz                        | In series with the SDA and SCL lines of the I2C bus          |
| **I2C Lines from LCC Fusion Node Bus Hub** | **ESD Protection Diode PESD1CAN** | Protects the I2C lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Across the SDA and SCL lines from the card’s edge connector to GND, near the MCP23017. |
| **LEDs**                                                     | **Current Limiting**              | Protects LEDs from current overload.                         | **Value:** 120 &Omega;                                       | In series with LED                                           |

## Components List

PCB for the card and solder stencil can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}BOD_Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier | Count | Type                       | Value            | Package         | Required | Purpose                                                      |
| -------------------- | ----- | -------------------------- | ---------------- | --------------- | -------- | ------------------------------------------------------------ |
| BR1-BR8              | 8     | Bridge Rectifier           | 4A               | PTH             | Required | Converts DCC pulsating AC-like waveform into a DC-like pulsating waveform for current detection. |
| C1 - C8              | 8     | Polymer Solid Capacitor    | 220uF, 25V       | 8x10.5mm, SMD   | Required | Smooths DC signal.                                           |
| C9                   | 1     | Ceramic Capacitor          | 0.1uF (100nF)    | SMD             | Required | Conditions/filters the current for the IC (U1).              |
| D1-D8                | 8     | TVS Diode                      | SMBJ5CA          | SMB SMD         | Required | Protects from high-voltage transients (>6.8-7.2V).           |
| D9                   | 1     | ESD Diode                      | PESD1CAN         | SOT-23 SMD      | Optional | Provides I2C data bus electrostatic discharge (ESD) protection. |
| D10                  | 1     | Zener Diode                | 12V              | 1206/DO-213 SMD | Required | Creates a reference voltage determining lower track block voltage. |
| FB1, FB2             | 2     | Ferrite Bead               | BLM31PG121SN1L   | 1206 SMD        | Required | Suppresses noise on I2C data lines.                          |
| J1, J2               | 2     | RJ45 Socket                | 8P8C             | PTH             | Required | Provides network cable (CAT5/6) connection to (1 or 2) Block Breakout Boards. |
| JP1, JP2             | 2     | Male Header                | 3P, 0.1" spacing | PTH             | Required | Used for COMM BUS selection (I2C hardware bus) for either BUS A or BUS B. |
| LED1 - LED8          | 8     | LED                        | Green            | 1206 SMD        | Optional | Used as block low voltage indicators, green when voltage is >12V. |
| LED9                 | 1     | LED                        | Red              | 1206 SMD        | Optional | Power status indicator.                                      |
| R1-R8                | 8     | Resistor                   | 1kΩ              | 1206 SMD        | Optional | Limits current to the MCP23017 GPIO pins and block low voltage LEDs. |
| R9, R10, R11         | 3     | Resistor                   | 10kΩ             | 1206 SMD        | Required | Limits current to SW1 and MCP23017 for the I2C address.      |
| R12                  | 1     | Resistor                   | 10kΩ             | 1206 SMD        | Required | Current limiting for MCP23017 reset.                         |
| R13                  | 1     | Resistor                   | 1kΩ              | 1206 SMD        | Required | Current limiting for diode (reference voltage).              |
| R14                  | 1     | Resistor                   | 1kΩ              | 1206 SMD        | Required | Current limiting for power LED.                              |
| SW1                  | 1     | DIP / Slide Switch         | 3P, 2.54mm       | PTH             | Required | Used for COMM ADDR selection (I2C address offset, 0-7).      |
| U1-U4                | 4     | IC (Voltage Comparator)    | LM393 or LM2903N | SO-8, SMD       | Required | Used for detecting low voltage (<12.1V).                     |
| U5                   | 1     | I/O Expander (MCP23017 IC) | SSOP28           | SMD             | Required | Controls 16 GPIO pins using I2C serial interface.            |
| SH1, SH2             | 2     | Jumper Cap                 | 2.54mm           | —               | Required | Used with I2C Bus and Vcc selections. Recommend tall caps for ease of use. |

## Tools Required

For a list of recommended tools, refer to [List of recommended tools](/pcb-tools/).

## Assembly Instructions

<img src="/assets/images/pcbs/BLVD_Card/BLVD_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the BOD Card:

1.  Below are the high level steps for assembly of the Audio Card:
2.  Position the card with the edge connector tabs facing down (see image on right).
3.  Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.
4.  When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

>  See also: [Soldering Tips](/pcb-soldering/)

| Designator (value) | Component          | Required?                       | Orientation                                                  |
| ------------------ | ------------------ | ------------------------------- | ------------------------------------------------------------ |
| BR1 - BR8          | KBL406             | Required                        | Position the rectifier’s clipped corner (pin 1) toward PCB **right** edge |
| C1 - C8            | 220uF              | Required                        | Cathode is position to PCB’s right side                      |
| C9                 | 0.1uF              | Required                        | None                                                         |
| D1 - D8            | SMAJ5CA            | Optional                        | Cathode end has a white line and positioned towards PCB **left** side |
| D9                 | PESD1CAN           | Optional                        | None                                                         |
| D10                | 12V Zener          | Required                        | Cathode end has a white line and positioned towards PCB **left** side |
| FB1, FB2           | BLM31PG121SN1L     | Required                        | None                                                         |
| J1, J2             | RJ45 socket        | Optional                        | None                                                         |
| JP1, JP2           | 3-Pin Male Headers | Required                        | None                                                         |
| LED1 - LED8        | Green LED          | Optional                        | Reference back of LED, position cathode towards PCB **bottom**<img src="/_builder/Cards/images/LED_Orientation.png" style="zoom: 15%; float: right;" /> |
| R1 - R8            | 1K&Omega;          | Required when using status LEDs | None                                                         |
| R13                | 1K&Omega;          | Required                        | None                                                         |
| R9 - R12           | 10K&Omega;         | Required                        | None                                                         |
| SW1                | DIP / Slide Switch | Required                        | Position ON towards PCB **top**.                                 |
| U1, U2, U3, U4     | LM393              | Required                        | Small dot (pin 1) on package is positioned to the upper left corner on the PCB |
| U5                 | MCP23017           | Required                        | Dent on package positioned downward on the PCB               |

## Testing and Verification

Configure the  BOD Card:

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

1. Assembly a tested Power Module to the LCC Fusion Node Card.
2. Apply Power to the Power Module and verify the following:
   - **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

Functional testing of the card can be performed after completing the power-up testing.  Testing consists of testing network communiations, followed by the sensing of current in a layout track block.

#### HW Communications Testing

Communications testing verifies the LCC Node can communicate with the BOD Card’s I2C IC via the Node Bus Hub connections.  This is performed using the LCC Fusion Node Card’s testing firmware and a serial monitor.

1. Insert the BOD Card into a Node Bus Hub along with a LCC Fusion Node Card.

2. Install LCC Fusion Project firmware that includes serial monitor for testing.

3. Verify that the I2C connection between the  LCC Fusion Node Card and the BOD Card work.  

   > See [Testing I2C Cards](/test-i2c-cards/) for details on how to test the communications for a I2C enabled card.

#### MCP IC Testing

After hardware communication has been established, to verify the MCP IC, use the Node’s serial monitor to simulate an input from each of card’s input pins as follows:

1. In the serial monitor’s input, enter `M` for the LCC Node’s serial monitor **Main Menu**.
2. Select `[1] Node Management` and `[1] Device Testing Management`
3. Select `[5] Simlulate MCP Device Input`
4. From the list of MCP devices, select the device # for the BOD Card being tested
5. Enter the number for the pin to tested.
6. Using the JMRI Event Monitor, verify the correct Event ID was issued.

#### Track Block Testing

After validating the LCC Fusion Node Card can communicate (find) the BOD Card, test each of the BOD Card block connections.  

>  Track block detection verification is performed using a Block Breakout Board connected to a track block.

1. Connect a network cable (CAT5/6) to one of the BOD Card’s RJ45 connector.

2. Connect the other end of the network cable to (1) Block Breakout Board.
3. Connect one of the **Test Track** rails directly to the **Track Bus V+** connection.
4. Connect the other **Test Track** rails to one of the **Block Breakout Board block connections** (BLK1 - BLK4)
5. Connect the **Test Track Bus GND** to the Block Breakout Board **TRACK BUS GND** connection
6. Configure each of the card’s device lines using an LCC CDI Configuration Tool.
7. Open an LCC Event Monitoring tool (e.g. JMRI Event Monitoring tool).
8. Test each of the Breakout Board device connections using a locomotive (one at a time)

   1. draw current on the track by either 
      - placing a 10K&Omega; resistor across the track, or
      - placing a locomotive on to the track
   2. Turn on the Track Power (let locomotive idle)
   3. Validate the configure Event ID for Block Occupied is sent by viewing the Event Monitoring tool
9. Repeat testing for all (8) BOD Card connections as follows:
   1. Connect the Block Breakout Board to the first RJ45 socket (J1) for blocks 1-4.
   2. Reconnect to 2nd RJ46 socket (J2) for blocks 5-8.

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References



