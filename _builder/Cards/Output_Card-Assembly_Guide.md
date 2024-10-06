---
title: Output Card Assembly Guide
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
# Output Card Assembly Guide {#output_card_assembly}
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

In conjunction with the **LCC Fusion** LCC Fusion Node Card and a Node Bus Hub, the **Output Card** provides ON/OFF control for up to 16 separate output devices. Typically, in an LCC Node arrangement, a designated sensor based card produces on/off event IDs. These IDs are subsequently consumed by the LCC Node, which then employs the **Output Card** to accurately control the functioning states of the attached devices.

Examples of I/O devices include, but not limited to:

- LEDs
- Relays
- DC motor
- Buzzer
- Solenoids / Electromagnets
- Fan

The **Output Card** hardware configuration includes:

- communication address; I2C bus (0 or 1) and address offset (0-7)
- for either 5V or 12v output
- with or without limiting resistors
- use of Line 16 for either output or as a GND connection

{% include terminology.html %}

## Specifications

Specifications for the card include:

| Characteristic                           | Value          |
| ---------------------------------------- | -------------- |
| Max Output Lines                         | 16             |
| Max Output Line (based on M54562FP IC)   | 500mA          |
| Max Total Output (using Line 16)         | 16             |
| Maximum Number of Cards per LCC Fusion Node Cluster | 16<sup>1</sup> |
| LCC Fusion Node Bus HubConnectors                      | 1<sup>2</sup>  |

1. The LCC Fusion Node Cluster can support up to 16 cards, distributed across two I2C hardware buses, with a maximum of 8 cards per bus.
   - Note: total includes all cards using the I2C address range of ````0x20```` (MCP23017 IC).
2. GND, 5V, 12V (optional), SLA0/SDA0, and SDA1/SCL1 (optional)

### How It Works

The following outlines the flow of activity for the Output Card:

<img src="/assets/images/pcbs/Output_Card/Output_Card_How_It_Works_sequence.png" style="zoom:60%;float:right" />The firmware of the LCC Fusion Node Card interfaces with the Output Card's port expander (MCP23017), leveraging the bus and address details specified in the card's CDI I2C section.  

Output is performed on a line as follows:

1. Upon receiving an LCC Event-related signal, the LCC Fusion Node Card's firmware dispatches an I2C command to the Output Card, instructing it to set the port state to either HIGH or LOW.
2. The port expander sets the base of the corresponding Darlington Transistor Array's input pin HIGH/LOW, which then switches the current for the corresponding output line HIGH or LOW.  
3. The output voltage to the line, either 5V or 12V, is determined by the card's **VOLTAGE** selector switch.
4. The output current to the line is determined by the card’s **RESISTOR BYPASS** selection and corresponding line’s resistor value.

>  The output line must be attached to an output device (LED, etc.) that is grounded to the same common as the LCC Fusion Node Card using either Line 16 or the Accessory Bus.

### Protection

The Output Card is equipped with several protective components to ensure reliable operation and safeguard the board and connected devices from potential electrical issues. Below is an overview of the protection mechanisms implemented:

| **Protected Component**     | **Protection Component**            | **Function**                                                 | **Specifications**             | **Location**                                    |
| --------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------ | ----------------------------------------------- |
| **I2C Communication Lines** | **PESD1CAN Diode**                  | Protects the I2C lines from **ESD (Electrostatic Discharge)** and other electrical surges. | **Clamping voltage**: 24V max  | Located on I2C data (SDA, SCL) lines.           |
| **I2C Communication Lines** | **FB121S Diodes**                   | Provides additional protection to the I2C lines by filtering out high-frequency noise and protecting against voltage spikes. | **Bidirectional TVS diode**    | Positioned along I2C communication lines.       |
| **I/O Control Lines**       | **1kΩ Current Limiting Resistors**  | Limits the current on the output lines.                      | 1kΩ resistors to limit current | On the output lines.                            |
| **I2C Address Selector**    | **10kΩ Current Limiting Resistors** | Limits the current on the I2C address configuration pins, preventing excessive current from damaging the MCP23017. | 10kΩ resistors                 | On the I2C address offset selector switches.    |
| **MCP23017 Port Expander**  | **0.1µF Decoupling Capacitor**      | Reduces noise and stabilizes the power supply to the MCP23017, ensuring smooth operation. | **Capacitance**: 0.1µF         | Positioned near the MCP23017 power supply pins. |



 ## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}Output Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

The design of the Output Card includes provisions for integrating current-limiting resistors and an optional bypass feature.  These resistors do not have to be 10k&Omega; as shown on the PCB.  Instead, match the resistor to the needs of the devices.  For LEDs, see  [Choosing the Right Resistor for LEDs](/led-card-usage-guide/) for additional information.

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier | Count | Type                  | Value              | Package    | Required? | Purpose                                                      |
| -------------------- | ----- | --------------------- | ------------------ | ---------- | --------- | ------------------------------------------------------------ |
| C1                   | 1     | Capacitor             | 0.1uF              | 1206 SMD   | Required  | Decoupling Capacitor for IC Protection                       |
| D1, D2               | 2     | Diode                 | SS310              | SMD        | Required  | Circuit protection from reverse current from the lines       |
| D3                   | 1     | Diode                 | PESD1CAN           | SOT-23 SMD | Required  | I2C data bus electrostatic discharge (ESD) protection        |
| FB1, FB2             | 2     | Ferrite Bead          | BLM31PG121SN1L     | 1206 SMD   | Required  | I2C Network Bus Data Line Noise Suppression                  |
| J1, J2               | 2     | RJ45 Socket           | 8P8C               | PTH        | Required  | Network cable (CAT5/6) connection to a breakout board or the Node’s I/O connector. |
| JP1, JP2             | 2     | Male Header           | 3P, 0.1" spacing   | PTH        | Required  | COMM BUS selection (I2C hardware bus) for BUS A or BUS B. Must match configuration in the LCC Node CDI setup. |
| JP3                  | 1     | Male Header           | 3P, 0.1" spacing   | PTH        | Required  | LINE 16 selection to GND or Output. Set to GND when Output devices require this card to provide GND. |
| JP4                  | 1     | Male Header           | 3P, 0.1" spacing   | PTH        | Required  | VOLTAGE selection for setting Vcc for output lines. Affects all output lines (e.g., 5V for LEDs, 12V for relays). |
| R1-R16               | 16    | Resistor              | 1kΩ                | 1206 SMD   | Optional  | Limits current to the output device. May be bypassed by setting the corresponding DIP switch (SW2, SW3) to ON. |
| R17-R19              | 3     | Resistor              | 10kΩ               | 1206 SMD   | Required  | Limits current to SW1 and MCP23017 for I2C address configuration. |
| SW1                  | 1     | DIP / Slide Switch    | 3P, 2.54mm spacing | PTH        | Required  | COMM ADDR selection (I2C address offset 0-7). Added to base address of MCP23017 (0x20). Configure for CDI setup. |
| SW2, SW3             | 2     | DIP / Slide Switch    | 8P, 2.54mm spacing | PTH        | Optional  | Enable/disable current limiting resistors (R1-R16). Used to bypass the resistors for higher current outputs. |
| U1, U3               | 2     | Darlington Transistor | M54562FP           | SOP20      | Required  | Amplifies low-current signals from MCP23017, driving high-current loads on output lines. |
| U2                   | 1     | I/O Expander          | MCP23017           | SSOP28     | Required  | Expands I2C serial interface to control 16 GPIO pins, each connected to an output line. |
| SH1, SH2             | 2     | Jumper Caps           | 2.54mm             | N/A        | Required  | Used with I2C Bus and Vcc selections. Tall caps are recommended for easy handling. |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/Output_Card/Output_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the Output Card:

1. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

2. When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

3. Apply soldering paste for all SMD components

4. Place SMD components into paste.  

   | Component Identifier | Component (Package)             | Required? | Orientation                                                  |
   | -------------------- | ------------------------------- | :-------- | ------------------------------------------------------------ |
   | C1                   | 0.1uF Capacitor (1206 SMD)      | Required  | None                                                         |
   | D1, D2               | Diode, SS310 (SMD)              | Required  | Cathode end has a white line and positioned towards PCB left edge |
   | D3                   | Diode, PESD1CAN, SOT-23 SMD     | Required  | Fits only one way                                            |
   | FB1, FB2             | Diode, BLM31PG121SN1L, 1206 SMD | Required  | None                                                         |
   | J1, J2               | RJ45 socket (8P8C)              | Required  | Fits only one way                                            |
   | JP1, JP2, J3, J4     | Male headers (3P, 0.1" spacing) | Required  | None                                                         |
   | U1, U3               | M54562FP IC (SOP20)             | Required  | IC indent (pin 1) is positioned towards PCB left edge        |
   | R1-R16               | 1kΩ resistors (1206 SMD)        | Optional  | None                                                         |
   | R17-R19              | 10kΩ resistors (1206 SMD)       | Required  | None                                                         |
   | SW1, SW2, SW3        | DIP / Slide Switch (3P, 2.54mm) | Required  | Position so switch so **ON** is towards PCB top edge         |
   | U2                   | MCP23017 IC (SSOP28)            | Required  | IC indent (pin 1) is positioned towards PCB left edge        |
   
   1. Capacitors: no specific orientation required (C1)
   2. Diodes SS310: note orientation, cathode (vertical line) faces left (D1,D2)
   
3. Diodes PESD1CAN with no orientation required  (D3)
   
   4. Ferrite Beads: BLM31 with no orientation required (FB1,FB2)

   5. Resistors: no orientation (R1-R19)

   6. MCP23017 IC: orientation ident is on the left side (U1)

   7. M54562FP IC: orientation indent is right side (Q1, Q2)

5. Reflow the solder for the SMD component (refer to  [Soldering Tips](/pcb-soldering/)).

6. Place PTH components (, starting with the smaller components.
   1. Solder (5) 3-Pin Male Pin Headers (JP1, JP2, JP3, JP4, JP5)
   2. Solder (1) 3-Position DIP Slide Switch (SW1)
   3. Solder (2) RJ45 sockets (J1, J2)

>  See also: [Soldering Tips](/pcb-soldering/)

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

1. **Continuity Check**: Use a multimeter in continuity mode to check for shorts between power rails and ground, and to ensure there are no open circuits in critical connections.

### Power-Up Tests

1. Assembly a tested Power Module to the LCC Fusion Node Card.
2. Apply Power to the Power Module and verify the following:
   - **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

#### I2C Verification

1. Verify that the I2C connection between the  LCC Fusion Node Card and the Output Card work.  See [Testing I2C Cards](@ref testing_I2C_cards) for details on how to test the I2C for a I2C enabled card.

#### Output Line Verification

After validating the LCC Fusion Node Card can connect with the Output Card, test each of the output lines as follows:
1. Connect an network cable (CAT5/6) to RJ45 connector.  Use the other end of the cable with a breakout board, or exposed wires to connect to devices for testing.

2. Configure each line of the card for output using an LCC CDI Configuration Tool

  3. Attach an LED anode to each line.  Attach the LED cathode to common (GND) used by the LCC Fusion Node Card.

  4. Set the card's Vcc (5V or 12V)

  5. Set the current limiting DIP switches to ON

  6. Test using LCC events:

        1. Send the configured on/off LCC Event ID's for each output line

        2. Validate that LED(s) turn on/off

            - If some of the lines work and some don't, it probably a soldering connection for the bad line

            - If none of the lines work correctly, check the connections for the voltage settings  


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

1.  [Choosing the Right Resistor for LEDs](/led-card-usage-guide/).

