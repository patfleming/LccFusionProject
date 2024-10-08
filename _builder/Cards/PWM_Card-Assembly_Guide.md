---
title: PWM Card Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Card Assembly Guides
nav_order: 2
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
  - Signaling Systems
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
  - esp32_s3
  - ferrite_bead
  - gpio_expander
  - jumper_caps
  - i2c
  - i2c_bus
  - mcp23017
  - network_cable
  - pwm
  - stencil
  - tvs_diode
---
# PWM Card Assembly Guide {#pwm_card_assembly}
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

The PWM (Pulse Width Modulation) Card, in synergy with the LCC Fusion Node Card, forms the signaling and motor controll backbone of the **LCC Fusion Project** system, controlling signal lamps and motors. 

Forexample, when controlling signals, upon detecting a train within a block, a BOD Card generates an LCC event, signaling the occupancy status. This event is captured by the LCC Node, which, depending on the setup, could trigger various responses such as activating the **PWM Card**. This activation allows for nuanced control over railroad signals and other trackside functionalities, enhancing the realism and operational efficiency of the model railroad environment.

The **PWM Card** hardware configuration includes:

- network cable sockets for up to 16 output lines
- selection of the communication bus (BUS or BUS B)
- selection of the communication address (0-7)
- selection of either 5V or 12V to the output lines
- selection of common V+ (anode) or V- (cathode) for LEDs
- selection of whether Line 16 is to be used for output or as a common (shared) line 

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

{% include terminology.html %}

## Specifications

Specifications for the card include:

| Characteristic                                   | Value          |
| ------------------------------------------------ | -------------- |
| Max output lines                                 | 16             |
| Max Current per line (TBD62063 transistor limit) | 500mA          |
| Maximum Number of Cards per LCC Fusion Node Cluster         | 16<sup>1</sup> |
| LCC Fusion Node Bus HubConnectors                              | 1              |

1. The LCC Fusion Node Cluster can support up to 16 cards, distributed across two I2C hardware buses, with a maximum of 8 cards per bus.
   - Note: total includes all cards using the I2C address range of ````0x40```` (PCA9685 IC).

### How It Works

This section delves into how the PWM Card operates within the system:

At its core, the PWM Card's operation is orchestrated through the LCC Fusion Node Card's firmware, which communicates with the PCA9685 IC— a crucial port expander on the PWM Card. This interaction is facilitated through specific bus and address settings detailed in the CDI I2C section of the card.

Upon receiving instructions to activate (set HIGH) or deactivate (set LOW) a pin, the PCA9685 IC controls a corresponding darlington transistor (TBD62034). This transistor, in turn, manages the switching of an output line on or off.

To tailor the PWM Card's behavior to specific needs, `Jumper Caps` are employed to configure the selection pins as outlined below:

| Selector Label            | Components Indicator |      Options       | Description                                                  |
| ------------------------- | :------------: | :----------------: | ------------------------------------------------------------ |
| `OUTPUT`                  |      JP6      |    `5V`, `12V`     | Sets the voltage level for all output lines.                 |
| `LINE 16`                 |      JP5      | `OUTPUT`, `COMMON` | Configures line 16 for either: <br> - `OUTPUT` mode, where it behaves like the other 15 output lines.<br>- `COMMON` mode, serving as a collective ground or power supply for the other lines. <br>For instance, if controlling 15 LEDs with lines 1-15, line 16 can act as a common ground or power source, depending on the `OUTPUT COMMON` setting. |
| `OUTPUT COMMON`           |    JP3, JP4    |    `GND`, `V+`     | Decides if line 16 operates as a ground (GND) or a power supply (V+).<br>Note:<br>1) Both JP5 and JP6 must align in their setting.<br>2) The `LINE 16` selector must be on `COMMON` for this setting to apply. |
| `LINE 16 RESISTOR BYPASS` |      JP7       |     `ON`,`OFF`     | Determines if the resistor on line 16 is bypassed:<br>- `ON` bypasses the resistor, useful when line 16 is in `COMMON` mode and you want to avoid limiting current to all lines.<br>- `OFF` keeps the resistor active, suitable for when you want current limiting on `OUTPUT` mode or additional current limiting on `COMMON` mode. |

The card utilizes current-limiting resistors for each line to manage device output current. The default resistor value is marked for creating about 50% LED brightness, but this can be adjusted by replacing the resistor for each line to suit specific requirements. Notably, if line 16 is set to `COMMON`, placing a resistor on this line impacts the current across all outputs. However, this can be circumvented by applying a `Jumper Cap` on the `LINE 16 RESISTOR BYPASS` selector to exclude line 16’s resistor from the circuit.

## Components List

PCB for the card and solder stencil can be ordered from any PCB fabricator using these  [Gerber Files]({{site.gerber_dir}}PWM_Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier | Count | Type              | Value              | Package        | Required? | Purpose                                                      |
| -------------------- | ----- | ----------------- | ------------------ | -------------- | --------- | :----------------------------------------------------------- |
| C1                   | 1     | Ceramic Capacitor | 0.01 uF (100nF)    | 1206 SMD       | Required  | Used to condition/filter the current for the IC (U1)         |
| D1                   | 1     | ESD Diode             | PESD1CAN           | SOT-23 SMD     | Required  | I2C data bus electrostatic discharge (ESD) protection        |
| FB1, FB2       | 2     | Ferrite Bead      | BLM31PG121SN1L     | 1206 SMD       | Required  | I2C Data Line Noise Suppression Ferrite Bead                 |
| J1, J2               | 2     | Connector         | RJ45 socket (8P8C) | PTH            | Required  | Network cable (CAT5/6) connection to (1 or 2) breakout boards (e.g. Signal Masts Breakout Board) |
| JP1, JP2             | 2     | Male Header       | 3-Pin              | 2.54mm PTH     | Required  | Use for setting line 16 to operate as ground (GND) or a power supply (V+) |
| JP3                  | 1     | Male Header       | 3-Pin              | 2.54mm PTH     | Required  | Use for setting `LINE 16` to be either an `OUTPUT`line or a `COMMON`line |
| JP4                 | 1     | Male Header       | 3-Pin              | 2.54mm PTH     | Required  | Use for setting the voltage level for all output lines       |
| JP5                 | 1     | Male Header       | 2-Pin              | 2.54mm PTH     | Optional  | Use to bypass line 16 resistor                               |
| JP6, JP7             | 2     | Male Header       | 3-Pin              | 2.54mm PTH     | Required  | Used for COMM BUS selection (I2C hardware bus) for either BUS A or BUS B. These are the ESP32 hardware buses used for serial comms |
| R1-R16               | 16    | Resistor          | 1.5KΩ              | 1206 SMD       | Required  | Used to limit the current to SW1 and MCP23017 for the I2C address |
| R19-21               | 3     | Resistor          | 10KΩ               | 1206 SMD       | Required  | Used to limit the current for the BUS ADDR lines             |
| SW1                  | 1     | DIP Switch        | 3-Pin              | 2.54mm PTH     | Required  | Used for COMM ADDR selection (I2C address offset, 0-7). This offset is added to the I2C base address of the MCP23017 IC (0x20) |
| U1                   | 1     | IC                | PCA9685            | TSSOP28 SMD    | Required  | PWM Expander using I2C serial interface to control 16 PWM pins, each connected to an output line |
| Q1, Q2               | 2     | IC                | TBD62083           | SOIC-18/SOP-18 | Required  | Darlington Transistor Array for switching supply voltage to the output lines. Controlled by the PCA9685 IC signals |
| SH1 - SH7          | 7     | Jumper Cap        | 2.54mm             | N/A            | Required  | Used with I2C Bus and Vcc selections. Recommend tall caps for ease of use |

## Tools Required

For a list of recommended tools, refer to [List of recommended tools](/pcb-tools/).

## Assembly Instructions

<img src="{{ site.baseurl }}/assets/images/pcbs/PWM_Card/PWM_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the PWM Card:

1. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.
2. When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.
3. Apply soldering paste for all SMD components
4. Place SMD components into paste.  
5. 

| Component Identifier         | Component (Package) | Component (Package) | Required? | Orientation                                                  |
| ---------------------------- | ------------------- | ------------------- | --------- | ------------------------------------------------------------ |
| C1                           | Ceramic Capacitor   | 0.01 uF (100nF)     | Required  | None                                                         |
| D1                           | ESD Diode           | PESD1CAN            | Required  | None                                                         |
| FB1, FB2                     | Ferrite Bead        | BLM31PG121SN1L      | Required  | None                                                         |
| J1, J2                       | Connector           | RJ45 socket (8P8C)  | Required  | Fits only one way                                            |
| JP1, JP2, JP3, JP4, JP6, JP7 | Male Header         | 3-Pin               | Required  | None                                                         |
| JP5                          | Male Header         | 2-Pin               | Optional  | None                                                         |
| R1-R16                       | Resistor            | 1.5KΩ               | Required  | None                                                         |
| R19-21                       | Resistor            | 10KΩ                | Required  | None                                                         |
| SW1                          | DIP Switch          | 3-Pin               | Required  | Position so switch so **ON** is towards PCB **top** edge     |
| U1                           | IC                  | PCA9685             | Required  | IC dimple in corner (pin 1) is positioned towards PCB **right** edge |
| Q1                           | IC                  | TBD62083            | Required  | IC indent (pin 1) is positioned towards PCB **left** edge    |
| Q2                           | IC                  | TBD62083            | Required  | IC indent (pin 1) is positioned towards PCB **bottom** edge  |
| SH1 - SH7                    | Jumper Cap          | 2.54mm              | Required  |                                                              |

## Testing and Verification

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.

2. **Solder Join Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

3. **Component Orientation**: the IC's are correctly oriented according to the PCB silkscreen or schematic.

### Connectivity Testing

**Continuity Check**: Use a multimeter in continuity mode to check for shorts between power rails and ground, and to ensure there are no open circuits in critical connections.

### Card Configuration Settings

1. The following test and verifications of the card should be performed after a through inspection of the card's soldering.  Check all of the PTH component pins and SMD pads.  Make sure there are no solder bridges between pins and pads.

2. Configure the PWM Card:

   1. Select the `COMM BUS` by positioning (2) Jumper Caps on either `A` or `B` male header pins (JP1, JP2)

   2. Select the `COMM ADDRESS` switch (SW1) by sliding each of the 3 switches to either the `ON `or `OFF` position.  Setting a switch to ON increments the address by 1, 2, or 4 for an address range of 0 to 7.  Up to 8 devices can then be configured for `A` and 8 for `B`.

   3. Select the `OUTPUT` supply voltage for either 5V or 12V by positioning a Jump Cap on the corresponding 2 pins.

   4. Select the `LINE 16` function to be `OUTPUT` to verify the connection to an LED works.  

      > Later change `LINE 16` selector to `COMMON` along `OUTPUT COMMON` set to either `GND` ro `V+`to test using line 16 for completing the circuit for the LEDs (either as a GND connection or as the V+ connection to the LEDs). 

### Power-Up Tests

1. Assembly a tested Power Module to the LCC Fusion Node Card.
2. Apply Power to the Power Module and verify the following:
   - **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

Functional testing of the card can be performed after completing the power-up testing.  Testing consists of testing network communiations, followed by controling signal lamps (LEDs).

#### HW Communications Testing

Communications testing verifies the LCC Node can communicate with the BOD Card’s I2C IC via the Node Bus Hub connections.  This is performed using the LCC Fusion Node Card’s testing firmware and a serial monitor.

1. Insert the PWM Card into a Node Bus Hub along with a LCC Fusion Node Card.

2. Install LCC Fusion Project firmware that includes serial monitor for testing.

3. Verify that the I2C connection between the  LCC Fusion Node Card and the PWM Card work.  

   > See [Testing I2C Cards](/test-i2c-cards/) for details on how to test the communications for a I2C enabled card.

#### PWM IC Testing

After hardware communication has been established, verify the PWM IC is able to drive LED devices using a Signal Masts Breakout Board.  Use the Node’s serial monitor to simulate an output request to drive of the PWM Card’s output pins to an LED connected to the Signal Masts Breakout Board as follows:

1. In the serial monitor’s input, enter `M` for the LCC Node’s serial monitor **Main Menu**.
2. Select `[1] Node Management` and `[1] Device Testing Management`
3. Select `[5] Simlulate PWM Device Output`
4. From the list of MCP devices, select the device # for the PWM Card being tested
5. Enter the number for the pin to tested.
6. Verify the output device (LED) is turned on
7. Repeat for each of the output lines


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

