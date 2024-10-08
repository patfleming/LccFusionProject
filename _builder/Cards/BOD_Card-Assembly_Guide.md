---
title: BOD Card Assembly Guide
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
# BOD Card Assembly Guide {#bod_card_assembly}
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

The Block Occupancy Detector Card (BOD Card), in synergy with the LCC Fusion Node Card, forms the detection backbone of the **LCC Fusion Project** system, facilitating precise detection of trains (locomotives and cars) within specified track blocks. This integration is pivotal for automating track occupancy detection, a core feature in advanced model railroad setups.

Upon detecting a train within a block, the BOD Card generates an LCC event, signaling the occupancy status. This event is captured by the LCC Node, which, depending on the setup, could trigger various responses such as activating the **PWM Card**. This activation allows for nuanced control over railroad signals and other trackside functionalities, enhancing the realism and operational efficiency of the model railroad environment.

### Detecting Positioning Turnout Points

The BOD Card can also be used to determine turnout points have been thrown or closed.  This is performed by connecting one of the BOD Card’s block lines one of points along with a 10K&Omega; reisistor.  This will result in the BOD Card detecting a current when that point’s rail is moved and touches a side rail.  The resulting ‘Occupied’ LCC event generated can be used to indicate the state of the point.  This is useful for turnout motors that are not wired to a switch tied to the points.

>  Note: this is not required for TORTOISE™ and DCCconcepts Cobalt Omega Classic Point Motor (CB1A) switch machines, which have a builtin switch for detecting turnout point positioning.

The **BOD Card** hardware configuration includes:

- communication address; I2C bus (0 or 1) and address offset (0-7)

{% include terminology.html %}

## Specifications

Specifications for the card include:

| **Characteristic**                                           | **Value**         |
| :----------------------------------------------------------- | :---------------- |
| Maximum BOD Detections                                       | 8                 |
| Maximum Cards per LCC Fusion Node Cluster | 16<sup>1</sup>    |
| Maximum Track Current                                        | 3.5A<sup>2</sup>  |
| Minimum Track Voltage                                        | 14.2V<sup>3</sup> |
| Maximum Block Breakout Board  | 2                 |

1. The LCC Fusion Node Cluster supports up to 16 cards, distributed across two I2C hardware buses, with a maximum of 8 cards per bus.
   - Note: This total includes all cards using the I2C address range of `0x20` (MCP23017 IC).
2. The BOD Card uses 32mil PCB traces,  to support up to 3.5A.  The card also uses a 3.5A fuse, and a 6A bridge rectifier.
3. The minimum track voltage is 14.2V due to the voltage drop from the bridge rectifier on the BOD Card (which reduces voltage by 2.2V). DCC decoders require at least 12V, in accordance with NMRA DCC standards.

### How It Works

The following outlines the flow of activity for the BOD Card:

The firmware of the LCC Fusion Node Card interfaces with the BOD Card's port expander (MCP23017), leveraging the bus and address details specified in the card's CDI I2C section. 

The BOD Card’s block occupancy detection details are as follows:

1. One of the Layout track rails is isolated in to ‘blocks’, typically for detection of a train within a designated section.  For example, for signaling purposes, at a turnout switch, before the switch, and on both the main and diverging routes.

2. When a locomotive (cab) or a car using a resistor mounted between wheelset hubs, enters the track’s block, current flows between the two track rails within that block.

   > Car detection can be performed using a 10k&Omega; resistor wired between one of the wheelset hubs.  Refer to [Wiring Wheelsets for Enhanced Block Occupancy Detection](/wiring-wheelsets-assembly-guide/).

3. When the block is connected to both a Block Breakout Board and a BOD Card, the flow of current is detected by the BOD Card.

> Wheelset detection can be erratic because of poor contact with track rails.  To help this, a 22µF ceramic capacitor is used to help smooth out erratic current flow and improve the reliability of current detection.

4. As the current flows from the rail to the BOD Card Track Bus GND connection, a small amount of current (controlled by the 1.5k&Omega; resistor) is also passed to the optocoupler input LEDs.   While the current is flowing thru the rails, to the BOD Card, and thru the optocoupler, the optocoupler results in the corresponding port expander I/O pin to go LOW.  When there is no DCC current flowing, the optocoupler’s output remains HIGH (via 10k&Omega;) pullup resistor.

   - Note that the BOD Card uses an unconventional approach with the bridge rectifier. Instead of converting the bipolar DCC AC signal into a pulsating DC signal, the rectifier is wired in such a way that it primarily passes the AC component (pins 2 and 3) through to the optocoupler. 


   - Additionally, pins 1 and 4 of the rectifier are connected together to help protect the circuit from voltage imbalances, ensuring that the DCC signal can be monitored directly for current isolation protection while also safeguarding against potential overvoltage conditions. 


   - Furthermore, both input LEDs of the optocoupler are used in opposite directions to handle the bipolar AC current, allowing the track's DCC signal to be connected in either direction without affecting the circuit's functionality.  That is, when the AC signal is present, one of the internal LEDs will always be forward-biased depending on the polarity of the AC cycle, allowing detection during both phases.

5. When current is detected by the BOD Card, a corresponding MCP23017 port expander pin (A0-A7) on BOD Card goes LOW.   The pins state change is detected by the LCC Node’s firmware, which then generates an LCC Event. 

6. Status LEDs turn ON when the optocoupler’s output is LOW from AC current flowing.  Each LED’s anode is connected to 3V3 and the cathode to the optocoupler’s output via 1k&Omega; current limiting resistor.


### Protection

To ensure the reliable operation and longevity of your BOD Card, several protection components have been integrated. These components safeguard the BOD Card from overcurrent, voltage spikes, and electrical noise. Below is a brief overview of each protection element and its role:

| Protected Component                                          | Protection Component              | Function                                                     | Specifications                                               | Location                                                     |
| ------------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Entire Circuit**                                           | **Optocoupler**                   | Provides electrical isolation, protecting the circuit from high voltages and noise by isolating different sections. | **Current Rating:** 60 mA<br>**Surge Current:** 1.5 A        | Between the track voltage input and the MCP23017 GPIO pin    |
| **Entire Circuit**                                           | **PPTC Polyfuse**             | Protects from sustained overcurrent conditions by increasing resistance when the current exceeds 3A. Resets once the fault condition is cleared. | **Hold Current:** 3A<br>**Trip Current:** 6A                 | In series with the track Vcc line.  Adjust the fuse type to match the MAX amperage expected within the block. |
| **Entire Circuit**                                           | **TVS Diode SMBJ18A**             | Protects from high-voltage transients by clamping voltage spikes, preventing them from reaching sensitive components. | **Stand-off Voltage:** 18V<br>**Clamping Voltage:** 29.2V    | Across the Vcc and GND lines of the track voltage            |
| **LEDs**                                                     | **1K ohm Resistor**               | Limits current to LED to create about 15% brightness         | **Value:** 1k ohms                                           | Between the optocoupler output and LED anode                 |
| **Optocoupler**                                              | **1.5K ohm Resistor**             | Limits inrush current to the optocoupler, protecting it from sudden surges. | **Value:** 1.5k ohms                                         | In series with the anode of the optocoupler                  |
| **MCP23017 GPIO**                                            | **10k ohm Resistor**              | Further limits current between the optocoupler output and the MCP23017 GPIO pin. | **Value:** 10k ohms                                          | Between the optocoupler output and MCP23017 input            |
| **MCP23017**                                                 | **Decoupling Capacitor 0.1 µF**   | Filters out high-frequency noise and transient voltage spikes from the power supply, ensuring a stable voltage for the MCP23017. | **Value:** 0.1 µF                                            | Across Vcc and GND near the MCP23017                         |
| **I2C Lines from LCC Fusion Node Bus Hub** | **Ferrite Bead BLM31PG121SN1L**   | Provides high-frequency noise suppression on the I2C lines.  | **Impedance:** 120 ohms at 100 MHz                           | In series with the SDA and SCL lines of the I2C bus          |
| **I2C Lines from LCC Fusion Node Bus Hub** | **ESD Protection Diode PESD1CAN** | Protects the I2C lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Across the SDA and SCL lines from the card’s edge connector to GND, near the MCP23017. |

### Summary
These protection components work together to safeguard the BOD Card from various electrical faults. The polyfuse provides overcurrent protection, the TVS diode clamps high-voltage spikes, the current limiting resistors control the current flow, and the decoupling capacitor filters out noise. The ferrite bead suppresses high-frequency noise on the I2C lines, and the ESD protection diode protects the I2C lines from electrostatic discharge and voltage spikes. The optocoupler provides electrical isolation, protecting the entire circuit from high voltages and noise. Together, they ensure the BOD Card operates reliably in a potentially harsh electrical environment.

## Components List

PCB for the card and solder stencil can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}BOD_Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier | Count<sup>1</sup> | Type               | Value                   | Package    | Required? | Purpose                                                      |
| -------------------- | :---------------: | ------------------ | ----------------------- | ---------- | :-------- | ------------------------------------------------------------ |
| BR1-BR8              |         8         | Bridge Rectifier   | KBL406, 4A              | PTH        | Required  | Converts the DCC pulsating AC-like waveform into a DC-like pulsating waveform for current detection without interfering with DCC signals. |
| C1                   |         1         | Ceramic Capacitor  | 0.01uF (100nF)          | 1206 SMD   | Required  | Conditions/filters the current for IC (U1).                  |
| C2-C9                |         8         | Ceramic Capacitor  | 22uF                    | 1206 SMD   | Optional  | Smooths incoming current for better detection when using resistor-equipped wheelsets. |
| D1-D8                |         8         |TVS Diode              | SMBJ18A                 | SMB        | Optional  | Protects from high-voltage transients (>29V).                |
| D9                   |         1         | ESD Diode              | PESD1CAN                | SOT-23 SMD | Optional  | I2C data bus electrostatic discharge (ESD) protection.       |
| FB1, FB2             |         2         | Ferrite Bead       | BLM31PG121SN1L          | 1206 SMD   | Required  | Noise suppression for I2C data lines.                        |
| F1-F8                |         8         | PPTC Polyfuse      | JK30, 3A, 16V (or more) | PTH        | Required  | Protects from sustained overcurrent conditions.              |
| J1, J2               |         2         | RJ45 Socket        | 8P8C                    | PTH        | Required  | Network cable (CAT5/6) connection to 1 or 2 Block Breakout Board. |
| JP1, JP2             |         2         | Male Header        | 3P, 0.1" spacing        | PTH        | Required  | Used for COMM BUS selection (I2C hardware bus) for either BUS A or BUS B. Must match LCC Node configuration (CDI). |
| LED1-LED8            |         8         | LED                | Red                     | 1206 SMD   | Optional  | Indicates block occupancy (current flow).                    |
| LED9                 |         1         | LED                | Green                   | 1206 SMD   | Optional  | PWR status indicator.                                        |
| R1-R8                |         8         | Resistor           | 1.5KΩ                   | 1206 SMD   | Required  | Limits current from the track rail to the optocoupler.       |
| R9-R10               |         3         | Resistor           | 10KΩ                    | 1206 SMD   | Required  | Limits current to SW1 and MCP23017 for I2C addressing.       |
| R12-R19              |         8         | Resistor           | 1KΩ                     | 1206 SMD   | Optional  | Limits current to status LEDs.                               |
| R20                  |         1         | Resistor           | 10KΩ                    | 1206 SMD   | Required  | Limits current to the MCP23017 reset pin.                    |
| SW1                  |         1         | DIP / Slide Switch | 3P, 2.54mm              | N/A        | Required  | Used for COMM ADDR selection (I2C address offset, 0-7).      |
| U1                   |         1         | IC                 | MCP23017                | SSOP28 SMD | Required  | I/O Expander using I2C serial interface to control 16 GPIO pins. |
| U2-U9                |         8         | Optocoupler        | MCT6H                   | DIP-8 PTH  | Required  | Detects current flow.                                        |
| SH1, SH2             |         2         | Jumper Cap         | 2.54mm                  | N/A        | Required  | Used with I2C Bus and Vcc selections. Recommend tall caps for ease of use. |

1. For components with counts of 8, only one of the specified component is required for a specific DOD detection circuits.

## Tools Required

For a list of recommended tools, refer to [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/BOD_Card/BOD_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the BOD Card:

1. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.
2. When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

> See also: [Soldering Tips](/pcb-soldering/)


| Component Identifier | Component (Package)              | Required?                       | Orientation                                                  |
| -------------------- | -------------------------------- | ------------------------------- | :----------------------------------------------------------- |
| BR1-BR8              | KBL406                           | Required                        | Position the rectifier’s clipped corner (pin 1) toward PCB **right** edge |
| C1                   | 0.01uF                           | Required                        | None                                                         |
| C2 - C9              | 22 uF (1206, SMD)                | Optional                        | None                                                         |
| D1 - D8              | SMBJ18A                          | Optional                        | Cathode end has a white line and positioned towards PCB **left** side |
| D9                   | PESD1CAN                         | Optional                        | None                                                         |
| FB1, FB2             | BLM31PG121SN1L                   | Required                        | Cathode end has a white line and positioned towards PCB **left** side |
| F1-F8                | Polyfuse, 3A (PTH)               | Required                        | None                                                         |
| J1, J2               | RJ45 socket                      | Required                        | None                                                         |
| JP1, JP2             | 3-Pin Male Headers               | Required                        | None                                                         |
| LED1 - LED8          | LED (1206 SMD, Red)              | Optional                        | Reference back of LED, position cathode towards PCB **top**<img src="/_builder/Cards/images/LED_Orientation.png" style="zoom: 15%; float: right;" /> |
| LED9                 | LED (1206 SMD, Green)            | Optional                        | Reference back of LED, position cathode towards PCB **top**      |
| R1-R8                | 1.5K&Omega; resistors (1206 SMD) | Required when using status LEDs | None                                                         |
| R9, R10, R11         | 10K&Omega; resistors (1206 SMD)  | Required                        | None                                                         |
| R12 - R19            | 1K&Omega; resistors (1206 SMD)   | Optional                        | None                                                         |
| R20                  | 10K&Omega; resistors (1206 SMD)  | Required                        | None                                                         |
| SW1                  | DIP / Slide Switch (3P, 2.54mm)  | Required                        | Position ON towards PCB **top**.                                 |
| U1                   | MCP23017 IC (SSOP28, SMD)        | Required                        | Position IC’s indent (pin 1) towards PCB **bottom**              |
| U2-U9                | MCT6H IC (DIP-8, PTH)            | Required                        | Position IC’s indent (pin 1) towards PCB **top**                 |

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

1. Assembly a tested to the LCC Fusion Node Card.
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
6. Configure each of the card’s device lines using an LCC CDI Configuration Tool
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


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References



