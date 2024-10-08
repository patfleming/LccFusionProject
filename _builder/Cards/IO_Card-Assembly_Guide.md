---
title: IO Card Assembly Guide
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
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_cards
  - lcc_fusion_project
  - lcc_fusion_node_bus
  - lcc_fusion_breakout_boards

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
  - accessory_bus

  # Hardware and firmware Terms
  - bus
  - cleaning_pcb
  - component
  - current_limiting_resistor
  - decoupling_capacitor
  - edge_card_connector
  - esd_protection_diode
  - ferrite_bead
  - gpio_expander
  - jumper_caps
  - i2c
  - i2c_bus
  - mcp23017
  - network_cable
  - stencil
  - tvs_diode
---
# I/O Card Assembly Guide {#io_card_assembly}
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

In conjunction with the **LCC Fusion** LCC Fusion Node Card and a Node Bus Hub, the **I/O Card** provides input and output control for up to 16 separate devices. Typically when used for input in an LCC Node arrangement, this card can be attached to input devices (buttons, sensors, etc.) to produce on/off event IDs.  These IDs are subsequently consumed by the LCC Node, which then employs either this card for output, or the **Output Card** to accurately control the functioning states of the attached devices.

{% include terminology.html %}

## Specifications

Specifications for the card include:

| Characteristic                                      | Value            |
| --------------------------------------------------- | ---------------- |
| Max Output Lines                                    | 16<sup>1</sup>   |
| Max Output Per Line (based on MCP23017 IC)          | 25mA<sup>1</sup> |
| Output                                              | 5V               |
| Maximum Number of Cards per LCC Fusion Node Cluster | 16<sup>2</sup>   |
| LCC Fusion Node Bus Hub Connectors                  | 1<sup>3</sup>    |

1. For 12V or higher output current, use the  **Output Card**.
2. The LCC Fusion Node Cluster can support up to 16 cards, distributed across two I2C hardware buses, with a maximum of 8 cards per bus.
   - Note: total includes all cards using the I2C address range of ````0x20```` (MCP23017 IC).
3. GND, 5V, 12V (optional), SLA0/SDA0, and SDA1/SCL1 (optional)

---

### How It Works

The following outlines the operational flow for the **I/O Card**, which implements an MCP23017 port expander connected to RJ45 sockets with current-limiting resistors that can be optionally set via slide switches:

The firmware of the **LCC Fusion Node Card** interfaces with the **I/O Card's** MCP23017 port expander using I2C communication, following the bus and address details specified in the card's CDI I2C section.

**Output Operation**:

1. When an LCC Event is triggered, the **LCC Fusion Node Card** firmware sends an I2C command to the **I/O Card**, instructing the MCP23017 to set the specified port state (HIGH or LOW).
2. The port expander adjusts the corresponding I/O line, setting it to either **5V (HIGH)** or **GND (LOW)**, as instructed by the I2C command.
3. The selector for **LINE 8** and **LINE 16** can be set to either `I/O` or `GND` to indicate the function of the line.  When set to `GND` the line will connect the I/O device to the  **[LCC Fusion Node Bus](/terminology/#node-bus)** `GND` connection.  This is useful when the I/O device does not have access to this same GND connection (ground plane).

> **Note**: For output functionality, devices like LEDs or relays should be connected to the I/O lines. These devices must share a common ground with the **LCC Fusion Node Card** through either **Line 16** or the **Accessory Bus**.

**Input Operation**:

1. The firmware configures the MCP23017 port expander with **internal pull-up resistors** (set to 3.3V). When an input device (such as a switch) pulls an input line to **LOW (GND)**, the corresponding GPIO line of the port expander is pulled to LOW.
2. When the **LCC Node** firmware detects a GPIO state change to LOW, it generates an **LCC Event** to indicate the **ON** state. When the input device resets (e.g., the button is released), the GPIO line returns to HIGH, and the firmware generates an **LCC Event** for the **OFF** state.

### Protection

The I/O Card provides input / output control of devices. The following is an overview of each protection component integrated into the I/O Card and its role:

| Protected Component | Protection Component              | Function                                                     | Specifications                                               | Location                                              |
| ------------------- | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------------------- |
| **MCP23017 IC**     | **Decoupling Capacitors**         | Filters out high-frequency noise and transient voltage spikes from the power supply, ensuring stable voltage to MCP23017 IC. | **Values:** 0.1 µF ceramic                                   | Across Vcc and GND near IC.                           |
| **I2C Lines**       | **Ferrite Bead BLM31PG121SN1L**   | Provides high-frequency noise suppression on the I2C lines.  | **Impedance:** 120 ohms at 100 MHz                           | In series with the SDA and SCL lines of the I2C bus   |
| **I2C Lines**       | **ESD Protection Diode PESD1CAN** | Protects the I2C lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Across the SDA and SCL lines to GND                   |
| **I/O Lines**       | **Current Limiting**              | Current limiting to protect I/O devices (i.e. LEDs)          | **Impedance:** 1k&Omega;                                     | In series with I/O lines, selectable via slide switch |

 ## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}I/O Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

The design of the Output Card includes provisions for integrating current-limiting resistors and an optional bypass feature.  These resistors do not have to be 10k&Omega; as shown on the PCB.  Instead, match the resistor to the needs of the devices.  For LEDs, see  [Choosing the Right Resistor for LEDs](/led-card-usage-guide/) for additional information.

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier | Count | Type               | Value            | Package    | Required? | Purpose                                                      |
| -------------------- | :---: | ------------------ | ---------------- | ---------- | :-------- | ------------------------------------------------------------ |
| C1                   |   1   | Ceramic Capacitor  | 0.1uF            | 1206 SMD   | Required  | Decoupling capacitor for IC protection.                      |
| D1                   |   1   | ESD Diode              | PESD1CAN         | SOT-23 SMD | Required  | I2C data bus electrostatic discharge (ESD) protection.       |
| FB1, FB2             |   2   | Ferrite Bead       | BLM31PG121SN1L   | 1206 SMD   | Required  | I2C network bus data line noise suppression.                 |
| J1, J2               |   2   | RJ45 Socket        | 8P8C             | N/A        | Required  | Network cable (CAT5/6) connection to I/O devices.            |
| JP1, JP2             |   2   | Male Header        | 3P, 0.1" spacing | N/A        | Required  | Used for LINES 8 & 16 selection for either GND or I/O. Set to GND when I/O devices require this card to provide the circuit's GND connection. |
| JP3, JP4             |   2   | Male Header        | 3P, 0.1" spacing | N/A        | Required  | Used for COMM BUS selection (I2C hardware bus) for either BUS A or BUS B. Must match the configuration within the LCC Node (CDI). |
| R5 - R23             |  19   | Resistor           | 10kΩ             | 1206 SMD   | Optional  | Used to limit current to the I/O devices. Required when limiting output current. Optionally bypassed by setting the corresponding DIP switch (SW2, SW3) to ON. Modify the resistor value to match the requirements of the I/O device. For LEDs, see [Choosing the Right Resistor for LEDs](/led-card-usage-guide/). |
| R1 - R4              |   4   | Resistor           | 10kΩ             | 1206 SMD   | Required  | Used to limit current to SW1 and MCP23017 for I2C address.   |
| SW1                  |   1   | DIP / Slide Switch | 3P, 2.54mm       | N/A        | Required  | Used for COMM ADDR selection (I2C address offset, 0-7). Up to 8 cards can be installed per I2C bus. Must match the LCC Node configuration (CDI). |
| SW2, SW3             |   2   | DIP / Slide Switch | 8P, 2.54mm       | N/A        | Optional  | Used to enable/disable limiting resistors for each I/O line. Required to bypass current-limiting resistors (R5-R23). |
| U1                   |   1   | IC                 | MCP23017         | SSOP28     | Required  | I/O expander using I2C serial interface to control 16 GPIO pins. |
| SH1, SH2, SH3, SH4   |   4   | Jumper Caps        | 2.54mm           | N/A        | Required  | Used with I2C Bus and LINE 8/16 selections. Recommend tall caps for ease of use. |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/Output_Card/Output_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the I/O Card:

1. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.
2. When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

>  See also: [Soldering Tips](/pcb-soldering/)

| Component Identifier | Component (Package)             | Required? | Orientation                                          |
| -------------------- | ------------------------------- | :-------- | ---------------------------------------------------- |
| C1                   | 0.1uF Capacitor (1206 SMD)      | Required  | None                                                 |
| D1                   | Diode, PESD1CAN, SOT-23 SMD     | Required  | Fits only one way                                    |
| FB1, FB2             | Diode, BLM31PG121SN1L, 1206 SMD | Required  | None                                                 |
| J1, J2               | RJ45 socket (8P8C)              | Required  | Fits only one way                                    |
| JP1, JP2             | Male header (3P, 0.1" spacing)  | Required  | None                                                 |
| JP3, JP4             | Male headers (3P, 0.1" spacing) | Required  | None                                                 |
| R1 - R23             | 10kΩ resistors (1206 SMD)       | Optional  | None                                                 |
| SW1, SW2, SW3        | DIP / Slide Switch (3P, 2.54mm) | Required  | Position so switch so **ON** is towards PCB **top** edge |
| U1                   | MCP23017 IC (SSOP28)            | Required  | Position IC’s dent towards PCB **right** edge            |

## Testing and Verification

Configure the card:

1. Select the I2C bus (**COMM BUS**) by positioning (2) Jumper Caps on either BUS A or BUS B male header pins (JP1, JP2)
2. Select the I2C address **(COMM ADDR)** switch (SW1) by slide each of the 3 switches to either the ON or OFF position.  Setting a switch to ON increments the address by 1, 2, or 4 for an address range of 0 to 7.  Up to 8 devices can then be configured for BUS A and 8 for BUS B.
3. Select the output voltage by positioning a Jump Cap on (1) pair of **VOLTAGE** male header pins (JP5)
4. Select the function of Line 16 as an output line or as a ground (GND) connection by positioning a Jumper Cap on (1) pair of **LINE 8** and **LINE 16** male header pins (JP3, JP4).

The following test and verifications of the card should be performed after a through inspection of the card's soldering.  Check all of the PTH component pins and SMD pads.  Make sure there are no solder bridges between pins and pads.

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.

2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

3. **Component Orientation**: the IC's are correctly oriented according to the PCB silkscreen or schematic.

### Connectivity Testing

### Power-Up Tests

1. Assembly a tested Power Module to the LCC Fusion Node Card.
2. Apply Power to the Power Module and verify the following:
   - **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

#### I2C Verification

#### Line Verification

After validating the LCC Fusion Node Card can connect with the I/O Card, test each of the I/O lines as follows:
1. Connect an network cable (CAT5/6) to RJ45 connector.  Use the other end of the cable with a breakout board, or exposed wires to connect to devices for testing.
2. Configure each line of the card for output using an LCC CDI Configuration Tool
  3. Attach an LED anode to each line.  Attach the LED cathode to common (GND) used by the LCC Fusion Node Card.
  4. Set the current limiting DIP switches to ON
  6. Test using LCC events:

        1. Send the configured on/off LCC Event ID's for each output line

        2. Validate that LED(s) turn on/off

            - If some of the lines work and some don't, it probably a soldering connection for the bad line

            - If none of the lines work correctly, check the connections for the voltage settings  


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

1.  [Choosing the Right Resistor for LEDs](/led-card-usage-guide/).

