---
title: Node Card Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Card Assembly Guides
nav_order: 1
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
  - Device Control
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_cards
  - lcc_fusion_project
  - lcc_fusion_node_bus

  # LCC Fusion Connect Terms
  - lcc_fusion_node_card
  - lcc_fusion_io_cards
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
  - can_network
  - can_termination
  - cleaning_pcb
  - component
  - decoupling_capacitor
  - edge_card_connector
  - esp32_s3
  - jumper_caps
  - i2c
  - i2c_bus
  - network_cable
  - stencil
---
# LCC Fusion Node Card Assembly Guide {#node_card_assembly}
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

In conjunction with the Node Bus Hub, the **LCC Fusion Node Card** provides an LCC compatible  Node with ON/OFF control for up to 8 separate I/O devices. Typically, in an LCC Fusion Project LCC Fusion Node Cluster arrangement, there will be a Node Bus Hub, with one LCC Fusion Node Card, an optional I/O cards.

The **LCC Fusion Node Card** can be implemented with a number of **optional** features:

1. Power Supply options (see [Power Module](/Power_Module) for more details):
   1. 12V+ input via a network cable (CAT5/6), 5557 ATX connection, or a DC-005 barrel connection.
   2. 12V+ output via 5557 ATX connection for powering other LCC Fusion Node Cards.
   3. 5v+ output via USB-C for powering low voltage devices (e.g. RPI).
   4. 12V+ or input power selection for the LCC Fusion Node Bus Hubto control the high voltage for the I/O cards.

2. CAN serial connection via a network cable (CAT5/6) or connectors (JST XH or Spring terminal).
3. CANable adapter for Windows USB to CAN connection for JMRI integration.
4. CDI reset button (hold for 10 seconds to reset the CDI to factory setting)
5. Reset button to restart the Node.
6. LCC Fusion Node Bus Hub(RJ45) network cable connection to connect with a remote LCC Fusion Project **Node Bus Hub**

The **LCC Fusion Node Card** provides one RJ45 socket for use with up to (8) I/O devices.

- Touch pads
- LEDs
- Relays
- DC motor
- Buzzer
- Solenoids / Electromagnets
- Fan

The **LCC Fusion Node Card** hardware configuration includes:

- communication address; I2C bus (0 or 1)
- address offset (0-7)

{% include terminology.html %}

## Specifications

Specifications for the card include:

| Characteristic                            | Value |
| ----------------------------------------- | ----- |
| Max 5V output current (limited regulator) | 500mA |
| Max Input / Output Lines                  | 8     |

### How It Works

The following outlines the flow of activity for the LCC Fusion Node Card:

Got it! Here's the detailed protection table for the LCC Fusion Node Card, including CAN bus protection, decoupling for ESP32 Vcc, and I2C protection:

### Protection

The LCC Fusion Node Card is equipped with several protection components to ensure reliable operation and safeguard against electrical faults. Below is an overview of each protection element integrated into the LCC Fusion Node Card and its role:

| Protected Component       | Protection Component              | Function                                                     | Specifications                                               | Location                                                     |
| ------------------------- | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Entire Power-CAN Card** | **Fast Blow Fuse**                | Protects from current overflow                               | **Hold Current:** 3A                                         | In series with the incoming Vcc line                         |
| **Entire Power-CAN Card** | **Resettable Fuses**              | Protects from sustained overcurrent conditions by increasing resistance when the 3V3 or 5V current exceeds 1.5A. Resets once the fault condition is cleared. | **Hold Current:** 1.5A                                       | In series with the 5V, 3V3 output lines                      |
| **Entire Power-CAN Card** | **TVS Diode SMBJ18A**             | Protects from high-voltage transients by clamping voltage spikes, pthem from reaching sensitive components. | **Stand-off Voltage:** 18V<br>**Clamping Voltage:** 29.2V    | Across the incoming Vcc and GND lines                        |
| **CAN Bus**               | **Automatic Termination**         | Provides proper termination to prevent signal reflections on the CAN bus. | **Value:** 2x 60 ohms in series (120 ohms)                   | Across CANH and CANL lines, automatically applied based on CAN network voltage while using a low-pass filter to measure peak voltage. |
| **CAN Bus**               | **ESD Protection Diode PESD1CAN** | Protects the CAN bus lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Across CANH to GND and CANL to GND                           |
| **I2C Bus (each set)**    | **ESD Protection Diode PESD1CAN** | Protects the CAN bus lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Across CANH to GND and CANL to GND                           |
| **CAN Bus**               | **BLM31PG121SN1L Ferrite Beads**  | CAN Network Bus Data Line Noise Suppression Ferrite Bead     |                                                              | In series with the CAN network lines                         |
| **I2C Bus (each set)**    | **BLM31PG121SN1L Ferrite Beads**  | CAN Network Bus Data Line Noise Suppression Ferrite Bead     |                                                              | In series with the I2C network lines                         |
| **ESP32 Vcc**             | **Decoupling Capacitor**          | Filters out high-frequency noise and transient voltage spikes from the power supply, ensuring stable voltage for the ESP32. | **Value:** 0.1 µF, 10uF ceramic                              | Integrated into DevKit-C Board                               |
| **LM2596-5N Regulator**   | **Output Capacitor**              | Filters out high-frequency noise and transient voltage spikes from the output, ensuring stable 5V regulation. | **Value:** 680 µF electrolytic                               | Across the output (5V) and GND                               |
| **L7812CV Regulator**     | **Output Capacitor**              | Filters out high-frequency noise and transient voltage spikes from the output, ensuring stable 12V regulation. | **Value:** 10 µF ceramic                                     | Across the output (12V) and GND                              |
| **Ground Bus**            | **48mil Ground Bus**              | Provides a low-resistance path for all protection components, ensuring effective grounding and noise suppression. | **Width:** 48 mil                                            | Used by all protection components                            |

### Summary
These protection components work together to safeguard the LCC Fusion Node Card from various electrical faults. The CAN termination resistor ensures proper signal integrity on the CAN bus, while the ESD protection diodes protect the CAN bus and I2C lines from voltage spikes and electrostatic discharge. The decoupling capacitor filters out noise and transient voltage spikes, ensuring stable power for the ESP32. The ferrite bead suppresses high-frequency noise on the I2C lines. The input Vcc is protected by the Power Module, which includes a polyfuse and TVS diode for overcurrent and overvoltage protection. Together, these components ensure the LCC Fusion Node Card operates reliably in a potentially harsh electrical environment.



 ## Components List

PCB for the LCC Fusion Node Card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}LCC Fusion Node Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram on right for reference): 

Here's the updated table with the count, type, and package columns added:

| **Component Identifier** | **Count** | **Type**                | **Value**                                      | **Package**     | **Required?** | **Purpose**                                                  |
| ------------------------ | --------- | ----------------------- | ---------------------------------------------- | --------------- | ------------- | ------------------------------------------------------------ |
| C1, C3                   | 2         | Ceramic Capacitor       | 0.1uF                                          | 1206 SMD        | Required      | IC protection                                                |
| C2                       | 1         | Tantalum Capacitor      | 0.33uF                                         | 3216 SMD        | Required      | IC protection                                                |
| C4                       | 1         | Ceramic Capacitor       | 0.1uF                                          | SMD 1206        | Required      | Filters high-frequency noise from CAN signals, smoothing the voltage for the comparator |
| C5                       | 1         | Polymer Solid Capacitor | 680uF, 10V                                     | 6x12mm, PTH     | Required      | Used by 5V voltage regulator for input filtering             |
| C6                       | 1         | Polymer Solid Capacitor | 220µF, 10V                                     | 6.3x5.8mm , SMD | Required      | Used by 5V voltage regulator for input filtering             |
| C7                       | 1         | Ceramic Capacitor       | 47uF                                           | 1206 SMD        | Required      | CAN termination circuit                                      |
| D1                       | 1         |TVS Diode                   | SMBJ18A                                        | SMB SMD         | Optional      | Protects from high-voltage transients (>29V)                 |
| D2, D4, D5               | 3         | Diode                   | SS310, B240, or B160                           | SMD             | Optional      | Circuit protection, required when providing power input (J1, J2, J3, or J4) |
| D3, D6, D7               | 3         | ESD Diode                   | PESD1CAN                                       | SOT-23 SMD      | Required      | I2C data bus electrostatic discharge (ESD) protection        |
| FH1                      | 1         | Fuse Holder             | 1808 with 3A                                   | n/a             | Required      | Protects from sustained overcurrent conditions               |
| F1                       | 1         | Resettable Fuse         | 1.5A                                           | 1206 SMD        | Required      | Protects from sustained overcurrent conditions               |
| FB1, FB2                 | 2         | Ferrite Bead            | BLM31PG121SN1L                                 | 1206 SMD        | Required      | CAN Network Bus Data Line Noise Suppression Ferrite Bead     |
| FB3 - FB6 | 4 | Ferrite Bead | BLM31PG121SN1L | 1206 SMD | Required | I2C Network Bus Data Line Noise Suppression Ferrite Bead |
| J1                       | 1         | USB-C Socket            | 4-Pin                                          | SMD             | Optional      | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus network cable |
| J2                       | 1         | Connector               | 5557 ATX RA                                    | N/A             | Optional      | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus network cable |
| J3                       | 1         | Power Jack              | DC-005                                         | N/A             | Optional      | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus network cable |
| J4                       | 1         | Connector               | 5557 ATX RA                                    | N/A             | Optional      | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus network cable |
| J5, J6                   | 2         | RJ45 Socket             | 8P8C                                           | PTH             | Required      | Network cable (CAT5/6) connection to CAN Bus for communicating with other LCC Nodes |
| J7                       | 1         | RJ45 Socket             | 8P8C                                           | PTH             | Optional      | Network cable (CAT5/6) connection to I/O devices             |
| J8                       | 1         | RJ45 Socket             | 8P8C                                           | PTH             | Optional      | Network cable (CAT5/6) connection to LCC Fusion Node Bus Hubfor communicating with LCC Fusion Project |
| J9                       | 1         | USB-C Socket            | 4-Pin                                          | SMD             | Optional      | Power output connector used to power other 12V+ devices      |
| J10                      | 1         | Header                  | 6-Pin male/female                              | N/A             | Optional      | Used to mount Micro-SD Reader Module for copying files to/from storage |
| J12                      | 1         | 2-Position Connector    | N/A                                            | N/A             | Optional      | Used for CAN Bus network connection, an alternative to using a CAN Bus network cable |
| JP1                      | 1         | Header                  | 2-Pin Male                                     | N/A             | Optional      | Used to bypass the 3A fuse (FH1)                             |
| JP2                      | 1         | Header                  | 3-Pin Male                                     | N/A             | Required      | Bypass selector for 12V output                               |
| L1                       | 1         | Inductor                | 33uH                                           | PTH             | Required      | Used for 5V voltage regulation                               |
| R1                       | 1         | Resistor                | 1kΩ                                            | SMD 1206        | Required      | Current limiting for reference voltage                       |
| R2                       | 1         | Resistor                | 100Ω                                           | SMD 1206        | Requried      | Low Pass Filter for low signal detection                     |
| R3, R4                   | 2         | Resistor                | 60Ω                                            | 1206 SMD        | Required      | CAN termination circuit                                      |
| R5                       | 1         | Resistor                | 1.5kΩ                                          | 1206 SMD        | Optional      | Part of CDI Factory Reset circuit                            |
| S1, S2                   | 2         | Tact Button Switch      | N/A                                            | N/A             | Optional      | Used to request a reset of the CDI to factory settings or to restart the LCC Node ESP32 processor |
| U1                       | 1         | CAN Transceiver         | SN65HVD233DR                                   | N/A             | Required      | CAN Transceiver for use with ESP32 to provide CAN communications |
| U2                       | 1         | MCU (processor)         | ESP32 DevKitC-V4 Module /w ESP32-WROOM-32D 4MB | 38-pin wide     | Required      | MCU (processor) for the LCC Fusion Node Card                 |
| U3                       | 1         | IC (Voltage Comparator) | LM393 or LM2903N                               | SO-8, SMD       | Required      | Used for detecting low voltage in the I2C lines (less than 2.4v) |
| VR1                      | 1         | Voltage Regulator       | L7812CV                                        | TO-220 PTH      | Optional      | 12V voltage regulator for LCC Fusion Node Bus Hub            |
| VR2                      | 1         | Voltage Regulator       | LM2596-5 C                                     | SMD             | Required      | 5V voltage regulator (buck) for ESP32 Development Board and Node Bus Hub |
| VR3                      | 1         | Voltage Regulator       | LM1117-3V3 IC                                  | SMD             | Required      | 3.3V voltage regulator for Node Bus Hub                      |
| J11, J12                 | 2         | Female Headers          | 19-Pin                                         | N/A             | Required      | Used to mount the ESP32 DevKit-C module                      |
| ZD1                      | 1         | Zener-Diode             | 2.4V                                           | BZT52           | Required      | Used for a 2.4V reference voltage                            |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/Node_Card/NODE_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the LCC Fusion Node Card:

1. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.
2. When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

> See also: [Soldering Tips](/pcb-soldering/)

| Component Identifier | Value                | Required? | Orientation                                                  |
| -------------------- | -------------------- | :-------- | ------------------------------------------------------------ |
| C1, C3, C4           | 0.1uF                | Required  | None                                                         |
| C2                   | 0.33uF Tantalum      | Required  | Cathode end has a brown line and positioned towards PCB **bottom** edge |
| C5                   | 680uF, 25V           | Required  | Anode positioned toward PCB **top** edge                     |
| C6                   | 220uF, 25V           | Required  | Anode positioned toward PCB **top** edge                     |
| C7                   | 47uF                 | Required  | None                                                         |
| D1                   | SMBJ18A              | Optional  | Anode positioned toward PCB **top** edge                     |
| D2, D4, D5           | SS310, B240, or B160 | Optional  | Cathode end has a white line and positioned towards PCB **bottom** edge |
| D3, D6, D7           | PESD1CAN             | Required  | Fits only one way                                            |
| FH1                  | Fuse Holder /w 3A    | Required  | None                                                         |
| F1                   | 1.5A                 | Required  | None                                                         |
| FB1 - FB6            | BLM31PG121SN1L       | Required  | None                                                         |
| J1                   | 4-Pin                | Optional  | None                                                         |
| J2, J4               | 5557 ATX RA          | Optional  | GND pin is marked on board with square pad                   |
| J3                   | DC-005               | Optional  | Fits only one way                                            |
| J5, J6               | 8P8C                 | Required  | Fits only one way                                            |
| J7, J8               | 8P8C                 | Optional  | Fits only one way                                            |
| J9                   | 4-Pin                | Optional  | None                                                         |
| J10                  | 6-Pin male/female    | Optional  | None                                                         |
| JP1                  | 2-Pin male header    | Optional  | None                                                         |
| JP2                  | 3-Pin male header    | Required  | None                                                         |
| L1                   | 33uH                 | Required  | None                                                         |
| R1                   | 1kΩ                  | Required  | None                                                         |
| R2                   | 100Ω                 | Requried  | None                                                         |
| R3, R4               | 60Ω                  | Required  | None                                                         |
| R4                   | 1.5kΩ                | Optional  | None                                                         |
| S1, S2               | N/A                  | Optional  | None                                                         |
| U1                   | SN65HVD233DR         | Required  | Package has small dimple in corner (pin 1) which is position to PCB **top** right edges |
| U2                   | ESP32 DevKitC-V4     | Required  | Position ESP32 development board’s USB connector to PCB **right** edge |
| VR1                  | L7812CV              | Optional  | Heat sink towards top of board                               |
| VR2                  | LM2596-5             | Required  | Fits only one way                                            |
| VR3                  | LM1117-3V3           | Required  | Fits only one way                                            |
| J11, J12             | 19-Pin               | Required  | None                                                         |
| ZD1                  | 2.4V                 | Required  | Cathode end has a white line and positioned towards PCB **right** edge |

## Testing and Verification

### Card Configuration

1. If the LCC Fusion Node Card is at the end of the CAN Bus Network, set the CAN TERM selection to `TERMINATION` (single jumper caps positioned across the top 2 pins).
1. If the LCC Fusion Node Card is not at the end of the CAN Bus Network, set the CAN TERM selection to `No-Term` (2 jumper caps each positioned vertically on the left and right set of pins).

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.

2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

3. **Component Orientation**: the IC's are correctly oriented according to the PCB silkscreen or schematic.

### Connectivity Testing

1. **Continuity Check**: Use a multimeter in continuity mode to check for shorts between power rails and ground, and to ensure there are no open circuits in critical connections.

### Power-Up Tests

1. Assembly a tested Power Module to the LCC Fusion Node Card.
2. **Apply Power** to the Power Module and verify the following:
   1. Use an voltage meeter to check the tabs at the base edge of the LCC Fusion Node Card verifying 3V3, 5V, and 12V+.   If verification fails, there is a component that is not installed correctly, or a solder bridge.
3. Remove the power supply and assembly an DevKit-C Module to the LCC Fusion Node Card.
4. Power up the LCC Fusion Node Card again and verify the red LED power indicator on the DevKit-C Module is on indicating 5V is being supplied to the ESP32.
5. **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

1. <img src="/assets/images/pcbs/Node_Card/Serial_Menu_Display_CAN_Status.png" style="zoom:70%; float:right" />Using a USB cable, connect the DevKit-C module to a computer.
1. Install LCC Fusion Project firmware.
1. Using a serial monitor, verify the firmware starts correctly.
1. Check the LCC Fusion Node Card’s CAN Network connectivity using the Node’s serial monitor menu.
1. Connect the computer to the LCC Fusion Node Card using a CANable Adapter.
1. Run JMRI and connect to the CAN Network.
1. While using the JMRI LCC Configuration Tool, verify that the Node appears in the network of LCC Nodes.


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

1.  [ESP32 DevKitC Module](https://www.aliexpress.us/w/wholesale-esp32-devkitc.html?spm=a2g0o.detail.search.0) - 38Pin ESP32 DevKitC with ESP32-WROOM-32D

