---
title: Button Card Assembly Guide
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
  - input_cards
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
# Button Card Assembly Guide {#button_card_assembly}
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

In conjunction with the **LCC Fusion Node Card** and a **Node Bus Hub**, the **Button Card** provides input control for up to 16 separate buttons. Typically when used for input in an LCC Node arrangement, this card can be attached to input buttons to have the an LCC Node produce LCC Events of on/off.  These events are subsequently consumed by a LCC Node to accurately control the functioning states of the other output devices.

{% include terminology.html %}

## Specifications

Specifications for the card include:

| Characteristic                                      | Value          |
| --------------------------------------------------- | -------------- |
| Max Buttons                                         | 16             |
| Maximum Number of Cards per LCC Fusion Node Cluster | 16<sup>1</sup> |

1. The LCC Fusion Node Cluster can support up to 16 cards, distributed across two I2C hardware buses, with a maximum of 8 cards per bus.
   - Note: total includes all cards using the I2C address range of ````0x20```` (MCP23017 IC).
2. GND, 5V, 12V (optional), SLA0/SDA0, and SDA1/SCL1 (optional)

---

### How It Works

The following outlines the operational flow for the **Button Card**, which implements an MCP23017 port expander connected to RJ45 sockets with current-limiting resistors that can be optionally set via slide switches:

The firmware of the **LCC Fusion Node Card** interfaces with the **Button Card's** MCP23017 port expander using I2C communication, following the bus and address details specified in the card's CDI I2C section.

The **Button Card** is designed to detect button presses and visually indicate their state while also detecting when an **I/O breakout board** is connected. Each button is connected to the card through a **Schmitt trigger** that cleans up the signal, ensuring reliable detection. When a button is pressed, the Schmitt trigger outputs a signal that is read by the **MCP23017** I/O expander, and the corresponding **LED** lights up to show the button press.

To detect whether the breakout board is connected, the card uses a small **current-sensing resistor** in combination with an **LM393 comparator**. When the breakout board is attached, a small current flows through the sensing resistor, causing a voltage drop. The LM393 detects this voltage drop, indicating the presence of the breakout board.

> The selector for`LINE 8` and `LINE 16` can be set to either `INPUT` or `GND` to indicate the function of the line.  When set to `GND` the line will connect the button device to the  **[LCC Fusion Node Bus](/terminology/#node-bus)** `GND` connection.  This is necessary when the I/O device does not have access to this same GND connection (ground plane).

**LCC Node Operation**:

1. The firmware configures the MCP23017 port expander with **internal pull-up resistors** (set to 3.3V). When an input device (such as a switch) pulls an input line to **LOW (GND)**, the corresponding GPIO line of the port expander is pulled to LOW.
2. When the **LCC Node** firmware detects a GPIO state change to LOW, it generates an **LCC Event** to indicate the **ON** state. When the input device resets (e.g., the button is released), the GPIO line returns to HIGH, and the firmware generates an **LCC Event** for the **OFF** state.

### Protection

The Button Card provides detection of button presses. The following is an overview of each protection component integrated into the Button Card and its role:

| Protected Component     | Protection Component              | Function                                                     | Specifications                                               | Location                                                |
| ----------------------- | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------- |
| **Entire Battery Card** | **PPTC Polyfuse**                 | Protects from sustained overcurrent conditions by increasing resistance when the current exceeds 1.5A and 3A. Resets once the fault condition is cleared. | **Hold Current:** 500mA                                      | In series with the incoming Power line                  |
| **MCP23017 IC**         | **Decoupling Capacitors**         | Filters out high-frequency noise and transient voltage spikes from the power supply, ensuring stable voltage to MCP23017 IC. | **Values:** 0.1 µF ceramic                                   | Across Vcc and GND near IC.                             |
| **I2C Lines**           | **Ferrite Bead BLM31PG121SN1L**   | Provides high-frequency noise suppression on the I2C lines.  | **Impedance:** 120 ohms at 100 MHz                           | In series with the SDA and SCL lines of the I2C bus     |
| **I2C Lines**           | **ESD Protection Diode PESD1CAN** | Protects the I2C lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Across the SDA and SCL lines to GND                     |
| **Button Lines**        | **Current Limiting**              | Current limiting to protect IC’s from incorrect wiring of lines with current  (i.e. LEDs) | **Impedance:** 1k&Omega;                                     | In series with input lines, selectable via slide switch |
| **Button Lines**        | **Noise Limiting**                | Low-Pass Filter to filter out noise and prevent unwanted transient signals | **Value**: 10nF                                              | Between input line and GND                              |

 ## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}I/O Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

The design of the Output Card includes provisions for integrating current-limiting resistors and an optional bypass feature.  These resistors do not have to be 10k&Omega; as shown on the PCB.  Instead, match the resistor to the needs of the devices.  For LEDs, see  [Choosing the Right Resistor for LEDs](/led-card-usage-guide/) for additional information.

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier | Count | Type                    | Value            | Package    | Required?                   | Purpose                                                      |
| -------------------- | :---: | ----------------------- | ---------------- | ---------- | :-------------------------- | ------------------------------------------------------------ |
| C1 - C16             |  16   | Ceramic Capacitor       | 10nF             | 1206 SMD   | Required                    | Low-Pass Filter to filter out noise and prevent unwanted transient signals |
| C17                  |   1   | Ceramic Capacitor       | 0.1uF            | 1206 SMD   | Required                    | Decoupling capacitor for IC protection.                      |
| D1                   |   1   | ESD Diode                   | PESD1CAN         | SOT-23 SMD | Required                    | I2C data bus electrostatic discharge (ESD) protection.       |
| F1                   |   1   | Resettable Fuse         | PPTC, 0.2A       | 1206 SMD   | Required                    | Protects from sustained overcurrent conditions               |
| FB1, FB2             |   2   | Ferrite Bead            | BLM31PG121SN1L   | 1206 SMD   | Required                    | I2C network bus data line noise suppression.                 |
| J1, J2               |   2   | RJ45 Socket             | 8P8C             | N/A        | Required                    | Network cable (CAT5/6) connection to I/O breakout board connected to buttons. |
| JP1, JP2             |   2   | Male Header             | 3P, 0.1" spacing | N/A        | Required                    | Used for `LINE 8` and `LINE 16` selection of either `GND` or `INPUT`. Set to `GND` when button require this card to provide the circuit's GND connection. |
| JP3, JP4             |   2   | Male Header             | 3P, 0.1" spacing | N/A        | Required                    | Used for `COMM BUS` selection (I2C hardware bus) for either `A` or `B`. Must match the configuration within the LCC Node (CDI). |
| LED1-LED16           |  16   | LED                     | Red              | 1206 SMD   | Optional                    | Indicates button has been pressed                            |
| LED17, LED18         |   2   | LED                     | Green            | 1206 SMD   | Optional                    | Indicates I/O breakout board is connected to RJ45 socket     |
| Q1, Q2               |   2   | Transistor              | BSS138           | SOT-23     | Optional                    | Used to turn on LED17 and LED18 when a I/O Breakout Board is connected to J1 or J2 |
| R1 - R16             |  16   | Resistor                | 1kΩ              | 1206 SMD   | Required when using R17-R34 | Current limiting for LED1 - LED16                            |
| R17 - R32            |  16   | Resistor                | 10kΩ             | 1206 SMD   | Required                    | Used to limit possible current from output line because of incorrect wiring |
| R33 - R34            |   2   | Resistor                | 15kΩ             | 1206 SMD   | Required                    | Used as a current sensing resistor to help detect a voltage drop when a I/O Breakout Board is attached. |
| R35 - R36            |   2   | Resistor                | 1kΩ              | 1206 SMD   | Required                    | Current limiting for LED17 - LED18                           |
| R37                  |   1   | Resistor                | 10kΩ             | 1206 SMD   | Required                    | Pull for the NPN transistor gate                             |
| R38 - R41            |   4   | Resistor                | 10kΩ             | 1206 SMD   | Required                    | Used by switch SW1 to pullup the MCP23017 for I2C address.   |
| SW1                  |   1   | DIP / Slide Switch      | 3P, 2.54mm       | N/A        | Required                    | Used for COMM ADDR selection (I2C address offset, 0-7). Up to 8 cards can be installed per I2C bus. Must match the LCC Node configuration (CDI). |
| U1, U3, U5           |   3   | IC (Schmitt Trigger)    | SN74HCT14        | DIP-14 PTH | Required                    | Contains 6 triggers to  transform noisy or slow-changing input signals into clean, fast digital outputs. |
| U2                   |   1   | IC (Voltage Comparator) | LM393 or LM2903N | SO-8, SMD  | Required                    | Used for detecting a voltage drop on line 1 by connecting a I/O Breakout Board (with 10kΩ resistor) |
| U4                   |   1   | IC (GPIO expander)      | MCP23017         | SSOP28     | Required                    | I/O expander using I2C serial interface to control 16 GPIO pins. |
| SH1, SH2             |   2   | Jumper Caps             | 2.54mm           | N/A        | Required                    | Used with I2C Bus and LINE 8/16 selections. Recommend tall caps for ease of use. |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/Button_Card/Button_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the I/O Card:

1. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.
2. When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

>  See also: [Soldering Tips](/pcb-soldering/)

| Component Identifier | Value                 | Required?                   | Orientation                                                  |
| -------------------- | --------------------- | :-------------------------- | ------------------------------------------------------------ |
| C1 - C16             | 10nF                  | Required                    | None                                                         |
| C17                  | 0.1uF                 | Required                    | None                                                         |
| D1                   | PESD1CAN              | Required                    | Fits only one way                                            |
| F1                   | Resettable Fuse, 0.25 | Required                    | None                                                         |
| FB1, FB2             | BLM31PG121SN1L        | Required                    | None                                                         |
| J1, J2               | 8P8C                  | Required                    | Fits only one way                                            |
| JP1, JP2             | 3P, 0.1" spacing      | Required                    | None                                                         |
| JP3, JP4             | 3P, 0.1" spacing      | Required                    | None                                                         |
| LED1-LED16           | Red                   | Optional                    | Reference back of LED, position cathode towards PCB **left** edge<img src="/_builder/Cards/images/LED_Orientation.png" style="zoom: 15%; float: right;" /> |
| LED17, LED18         | Green                 | Optional                    | Reference back of LED, position cathode towards PCB **left** edge<img src="/_builder/Cards/images/LED_Orientation.png" style="zoom: 15%; float: right;" /> |
| Q1, Q2               | BSS138                | Optional                    | Fits only one way                                            |
| R1 - R16             | 1kΩ                   | Required when using R17-R34 | None                                                         |
| R17 - R32            | 10kΩ                  | Required                    | None                                                         |
| R33 - R34            | 15kΩ                  | Required                    | None                                                         |
| R35 - R36            | 1kΩ                   | Required                    | None                                                         |
| R37                  | 10kΩ                  | Required                    | None                                                         |
| R38 - R41            | 10kΩ                  | Required                    | None                                                         |
| SW1                  | 3P, 2.54mm            | Required                    | Position ON towards PCB **top**.                                 |
| U1, U3, U5           | SN74HCT14             | Required                    | Position IC’s dimple (pin 1) towards PCB **left** edge           |
| U2                   | LM393 or LM2903N      | Required                    | Position IC’s dimple (pin 1) towards PCB **top** edge            |
| U4                   | MCP23017              | Required                    | Position IC’s indent (pin 1) towards PCB **left** edge           |
| SH1, SH2             | 2.54mm                | Required                    |                                                              |

## Testing and Verification

Configure the card:

1. Select the I2C bus (**COMM BUS**) by positioning (2) Jumper Caps on either BUS A or BUS B male header pins (JP1, JP2)
2. Select the I2C address **(COMM ADDR)** switch (SW1) by slide each of the 3 switches to either the ON or OFF position.  Setting a switch to ON increments the address by 1, 2, or 4 for an address range of 0 to 7.  Up to 8 devices can then be configured for BUS A and 8 for BUS B.

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


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

1.  [Choosing the Right Resistor for LEDs](/led-card-usage-guide/).

