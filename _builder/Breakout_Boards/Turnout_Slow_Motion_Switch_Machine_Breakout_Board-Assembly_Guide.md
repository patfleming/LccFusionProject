---
title: Turnout Slow Motion Switch Machine Breakout Board Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Breakout Board Assembly Guides
nav_order: 2
use_cases:
  - Automation Deployment
  - Node Cluster Setup
  - PCB Design & Assembly
  - Signaling Systems
  - Train Detection
subjects:
  - Assembly Guides
  - Automation
  - Hardware
  - Signaling
  - Train Detection
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_breakout_boards
  - lcc_fusion_cards
  - lcc_fusion_project
  # LCC Fusion Connect Terms
  - lcc_fusion_node_card
  - network_cable
  # Model Railroad Automation Terms
  - track_bus
  # Hardware and firmware Terms
  - cleaning_pcb
  - component
---





# [Turnout Slow Motion Switch Machine Breakout Board](/slow-motion-switch-machine-breakout-board-assembly-guide/) Assembly Guide {#turnout-slow-motion-switch-machine-breakout_board_assembly}
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

The **Turnout Slow Motion Switch Machine Breakout Board**, used in conjunction with the LCC **LCC Fusion Node Card**,  **Turnout Card**,  and a slow-motion stall motor based switch machine, provides both motor control and turnout point position sensing, while also handling frog polarity switching. The board leverages dual mechanical relays to reliably switch the frog between **Rail A** and **Rail B**, based on the turnout's position. Each relay is responsible for controlling one frog, ensuring proper electrical connection as the turnout moves between the **Thrown** and **Closed** positions.

By interfacing directly with the Turnout Card, this breakout board provides a seamless way to control the turnout motor direction and manage frog polarity automatically, making it ideal for complex layout control and automation.

**Usage**:

This breakout board is for use with 2-wire slow motion switch machines.  Wiring examples:

| Manufacturer                   | Product                                                      | Breakout Board to Switch Machine Connects                    | Motor Resistor Bypass | Turnout Card Motor Voltage Selection | Frog Polarity                                                | Points Status<sup>1</sup> | Comments                                                     |
| ------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------- | ------------------------------------ | ------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------ |
| Micro-Mark®                    | Switch Tender Switch Machine 83201                           | Connect `1` to one connection<br>Connect `2` to other connection | No                    | 12V                                  | Breakout Board                                               | Breakout Board            | [83201 Wiring (PDF)](https://www.manualslib.com/manual/2107795/Micro-Mark-Switch-Tender-83201.html)<br>Increase R1 to slow switch machine |
| Rapido Trains Inc              | RailCrew Switch Machine                                      | Connect `1` to `Red` wire<br>Connect `2` to `Black` wire     | Bypass                | 12V                                  | Breakout Board, or<br>RailCrew Switch Machine                | Breakout Board            | [RailCrew Wiring (PDF)](https://rapidotrains.com/media/pdf/12switch-Instructions_may2020.pdf) |
| DCCconcepts                    | Cobalt Omega, Cobalt iP Analog, or Cobalt Classic Point Motor | Connect `1` to `S2-L` & `S3-C`  connections<br>Connect `2` to `S2-C` & `S3-R` connections | Bypass                | 9V, 12V                              | Breakout Board, or <br>Cobalt Classic Omega Point Motor, Cobalt iP Analog, or Cobalt Classic Point Motor | Breakout Board            | [Cobalt Omega Wiring (PDF)](https://www.dccconcepts.com/wp-content/uploads/2016/02/Cobalt-Classic-Omega-NEW-summary-Instruction.pdf)<br>[Cobalt iP Analog](https://www.dccconcepts.com/wp-content/uploads/2016/02/Cobalt-iP-Analog-NEW-summary-Instruction.pdf)<br>[Cobalt Classic Wiring (PDF)](https://www.dccconcepts.com/wp-content/uploads/2016/02/M-Owners-Manual-Cobalt-Classic-Point-Motors.pdf)<br>Since motor control lines are bidirectional, wire to switch machine for both directions |
| Walters&reg;                   | Walters Controls Switch Machine 942-101                      | Connect `1` to one `IN` connection<br>Connect `2` to other `IN` connection | Bypass                | 12V                                  | Breakout Board, or <br>942-101 Switch Machine                | Breakout Board            | [942-101 Wiring (PDF)](https://s3.amazonaws.com/aws.walthers.com/942-101+Switch+Machine+Advance+Control+Manual.pdf)<br>Configures for **Polarity Route Option** in support of bidirectional current |
| Model Railroad Control Systems | MP4, MP5, MP10                                               | Connect `1` to `M1` connection<br>Connect `2` to `M2` connection | Bypass                | 9V, 12V                              | Breakout Board, or<br>MRCS MP4, MP5, MP10                    | Breakout Board            | [MP4 Wiring (PDF)](https://www.mtb-model.com/files/produkty/MP4-instr-CZ_EN_DEwebV1.pdf)<br/>[MP5 Wiring (PDF)](https://www.modelrailroadcontrolsystems.com/content/MP5%20instruction_EN_V1.pdf)<br/>[MP10 Wiring (PDF)](https://www.modelrailroadcontrolsystems.com/content/MP10_Instructions.pdf)<br>For MP1 & MP5, use **Turnout Twin Coils Switch Machine Breakout Board** |

1. To produce LCC Events, the breakout board is must be used since the switch machine itself is not integrated with LCC.

{% include terminology.html %}

## Specifications

Specifications for the [Turnout Slow Motion Switch Machine Breakout Board](/slow-motion-switch-machine-breakout-board-assembly-guide/) include:

| Characteristic | Value               |
| -------------- | ------------------- |
| Output         | 9V, 12V<sup>1</sup> |
| Max Turnouts   | 2                   |

1. Output voltage is determined by the motor output voltage selection found on the Turnout Card.

### How It Works

The ** [Turnout Slow Motion Switch Machine Breakout Board](/slow-motion-switch-machine-breakout-board-assembly-guide/) ** is designed to interface with the ** Turnout Card ** to control slow-motion stall motors for managing turnout points, while also controlling the frog polarity based on turnout position. The board enables bidirectional motor control and uses relays to switch the frog between **Rail A** and **Rail B** of the track bus, ensuring proper electrical continuity as the turnout moves between the **Thrown** and **Closed** positions.

1. **Inputs and Outputs Connections:**

   - **Input (Control Signals)**: 
     - The board receives control signals from the Turnout Card via two input lines that handle the **bidirectional motor control**. Based on the Turnout Card motor output selection, motor control signals are 9V or 12V outputs that set the motor's direction to move the turnout points to either **Thrown** or **Closed**.
   - **Motor Output**: 
     - Two motor output terminals connect directly to the slow-motion stall motor. The motor is driven in one direction or the other depending on the polarity of the control signals.
     - The board includes current limiting resistors to control current to the motors.  Use the motor’s documentation to determine the correct amount of current to the motor.
     - The board also includes optional protection using resettable fuses (PPTCs) on the motor control lines to protect against overcurrent conditions that could damage the driver circuitry.
2. **Bidirectional Motor Control**:

   - The **Turnout Card** controls the motor direction. Depending on the control signal:
     - **One polarity** drives the motor in the direction to set the turnout to the **Thrown** position.
     - **The reverse polarity** drives the motor in the direction to set the turnout to the **Closed** position.
   - As the control signals are received from the LCC Fusion Node Card firmware, the Turnout Card MCP23017 GPIO switches between high and low states and uses a TC4428 to drive the motor, moving the turnout points to the required position.
3. **Relays for Frog Polarity Control**:

   - The [Turnout Slow Motion Switch Machine Breakout Board](/slow-motion-switch-machine-breakout-board-assembly-guide/) uses a mechanical relay to control the frog polarity. The relay switches the frog's connection between **Rail A** and **Rail B** based on the position of the turnout.
   - This ensures that the frog always has the correct polarity based on the turnout’s position, providing smooth operation and preventing short circuits as the train moves through the turnout.

### Connectors

The purpose of the **Turnout Servo Switch Machine Breakout Board** and its connectors is to facilitate quick and easy connections between the **Turnout Card** and a turnout controlled by a servo.

| Component Designator | **Connector Label ** | Connector Type          | **Connection Number** | **Description**                                              |
| -------------------- | -------------------- | ----------------------- | --------------------- | ------------------------------------------------------------ |
| **J1**               | ACC GND              | JST XH, Spring Terminal | GND                   | Connection to the layouts accessory bus or dedicated power supply (not to DCC).  **GND must connected to the same ground plane as the LCC Fusion Node Card**. |
| **J2**               | FROGS                | JST XH, Spring Terminal | 1, 2                  | Connection to power turnout frogs                            |
| **J3, J4**           | MOTOR 1 / MOTOR 2    | JST XH, Spring Terminal | 1, 2                  | Connection to switch machine.  Note the current is bidirectional. |
| **J5**               | TRACK BUS            | JST XH, Spring Terminal | A, B                  | Connections to the layout track bus for Rail A and Rail B.  Used to power the frog when.  If necessary, switch the connections to match the frog to the correct rail. |
| **J6**               | TURNOUT CARD         | RJ45 Socket             | 1 - 8                 | Refer to Turnout Card’s connection table for the function of each pin |



### Protection

| **Protected Component**       | **Protection Component**      | **Function**                                                 | **Specifications**                                           | **Location**                                                 |
| ----------------------------- | ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Entire Circuit**            | **PPTC Polyfuse**             | Protects from sustained overcurrent conditions by increasing resistance when the current exceeds 0.25A (250mA). Resets once the fault condition is cleared. | **Hold Current:** 0.25A   <br>**Trip Current:** 0.5A         | In series with the motor's Vcc line. Adjust the fuse type to match the max current expected by the stall motor. |
| **Track Power**               | **PPTC Polyfuse**             | Protects from sustained overcurrent conditions by increasing resistance. Resets once the fault condition is cleared. | **Fuse Rating:** Based on max track current (typically 0.5-3.5A depending on track power). | In series with the track power supply, between the power source and the track. |
| **Relay Coils, Stall Motors** | **Flyback Diode**             | Protects the circuit from high-voltage spikes caused by inductive loads (relay coils, stall motors) when switching off. | **Diode Type:** Schottky  <br> **Max Current:** Min 0.5A  <br>**Reverse Voltage:** Min 12V | Across the relay coil or stall motor terminals (one diode for each direction in bidirectional motor circuits). |
| **LM7805CV Regulator**        | **Capacitors (Input/Output)** | Stabilizes voltage and reduces noise on the input and output of the voltage regulator. | **Input Cap:** 0.33µF   <br>**Output Cap:** 0.1µF            | Input cap across the input pin and GND. Output cap across the output pin and GND. |
| **Stall Motor**               | **Current-Limiting Resistor** | Limits the current flowing through the stall motor to prevent damage or overheating. | **Resistor value** is determined by the stall motor's voltage and current rating. | In series with the stall motor, resistor size based on motor specifications. |
| **DCC and ACC Circuits**      | **Separate Ground Planes**    | Isolates DCC and accessory grounds to prevent interference   | N/A                                                          | Between DCC and ACC                                          |

 ## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}turnout-slow-motion-switch-machine-breakout_board.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram before reference): 

| Component Identifier | Count | Type               | Value                   | Package            | Required                           | Purpose                                                      |
| -------------------- | ----- | ------------------ | ----------------------- | ------------------ | ---------------------------------- | ------------------------------------------------------------ |
| C1, C3               | 2     | Ceramic Capacitor  | 0.1uF                   | 1206 SMD           | Required                           | Used by 5V voltage regulator for output filtering.           |
| C2, C4               | 2     | Tantalum Capacitor | 0.33uF                  | 3216 SMD           | Required                           | Used by 5V voltage regulator for input filtering.            |
| D1 - D6              | 6     | Diode              | SS310                   | SMD                | Optional                           | Circuit protection against flyback from motors and coils.    |
| D7 - D10             | 2     | Diode              | SS310                   | SMD                | Required                           | Forces bidirectional motor current to flow only one way to LM7805 voltage regulator |
| F1, F4               | 2     | Resettable Fuse    | 0.2A                    | 1206 PPTC SMD      | Required                           | Current overload protection to motors. Adjust value to match max current expected. |
| F2, F3               | 2     | Resettable Fuse    | SK30, 3A, 5V  (or more) | PTH                | Required                           | Current overload protection to track bus. Adjust value to match max current expected. |
| J1                   | 1     | JST XH Socket      | 2P, 2.54mm              | PTH or Spring Term | Required                           | Connector to ACC BUS ground connection. Ground must be connected to the same ground as the **LCC Fusion Node Card** |
| J2                   | 1     | JST XH Socket      | 2P, 2.54mm              | PTH or Spring Term | Optional                           | Connector to turnout frog                                    |
| J3, J4               | 2     | JST XH Socket      | 2P, 2.54mm              | PTH or Spring Term | Required                           | Connector to motor(s)                                        |
| J5                   | 1     | JST XH Socket      | 2P, 2.54mm              | PTH or Spring Term | Required                           | Connector to track power rails (**Rail A** and **Rail B**)   |
| J6                   | 1     | RJ45 socket        | 8P8C                    | PTH                | Required                           | Network cable (CAT5/6) connection from **Turnout Card**.     |
| JP1, JP2             | 2     | Male Header        | 2-Pin                   | PTH                | Optional                           | Used to bypass current limiting resistor (R1,R2) to the motor. |
| K1, K2               | 2     | Relay              | DPDT                    | TQ2-5V (PTH)       | Required                           | Controls track Rail A and Rail B to frog and Point Sense line to ground |
| R1, R2               | 2     | Resistor           | 220Ω                    | 1206 SMD           | Optional (when JP1, JP2 are used)k | Limit current to motor, adjust value based on stall motor requirements. |
| VR1, VR2             | 2     | Voltage Regulator  | LM7805CV                | TO-220, SMD        | Required                           | Provides 5V power to NE555 timer and servo motor(s).         |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="{{ site.baseurl }}/assets/images/pcbs/Breakout_Boards/turnout_slow_motion_switch_machine_breakout_board_pcb.png/" style="zoom:70%; float:right" />Below are the high level steps for assembly of the Block Breakout Board:

Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

>  See also: [Soldering Tips](/pcb-soldering/)

| Designator (value) | Component                                                    | Required?                         | Orientation                                                  |
| ------------------ | ------------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------ |
| C1, C3             | Capacitor, 0.1uF (1206 SMD)                                  | Required                          | None                                                         |
| C2, C4             | Capacitor, 0.33uF (SMD)                                      | Required                          | Position cathode end (white line) to PCB **left** and right edges (alternate) |
| D1 - D4            | SS310 (SMD)                                                  | Optional                          | Position cathode end (white line) to PCB **left** and right edges (alternate) |
| D5 - D10           | SS310 (SMD)                                                  | Required                          | Position cathode end (white line) to PCB **top** edge            |
| F1, F4             | Resettable Fuse, 0.2A (SMD)                                  | Required                          | None                                                         |
| F2, F3             | Resettable Fuse, 3A (PTH)                                    | Required                          | None                                                         |
| J1, J3, J4, J5     | JST XH Socket (2P, 2.54mm), or<br/>2-Position Spring Terminal Connector (2.54mm, PTH, vertical or horizontal) | Required                          | Position connection outward                                  |
| J2                 | JST XH Socket (2P, 2.54mm), or<br/>2-Position Spring Terminal Connector (2.54mm, PTH, vertical or horizontal) | Optional                          | Position connection outward                                  |
| J4                 | RJ45 Socket                                                  | Required                          | Fits only one way                                            |
| JP1, Jp2           | 2-Pin Male Header                                            | Optional                          | None                                                         |
| K1, K2             | Relay  TQ2-5V (PTH)                                          | Required, one per motor           | Position IC’s small dimple in corner (pin 1) towards PCB **top** edge |
| R1, R2             | 220&Omega; resistors (1206 SMD)                              | Optional (when JP1, JP2 are used) | None                                                         |
| VR1, VR2           | Voltage Regulator LM7805CV (TO-220, PTH)                     | Required, one per motor           | Position heat sink towards PCB **top** edge                      |

## Testing and Verification

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.
2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.


### Functional Testing

- Supported slow-motion (stall) switch machines (bidirectional):

  1. [Switch Tender Switch Machine (MicroMark, 12V, slow motion)](https://www.micromark.com/Switch-Tender-Switch-Machine_2?gclid=Cj0KCQiA1NebBhDDARIsAANiDD395-fEHQAW2unLZSZcbtWsWf56Mii8qrHaPxNAeSPj-wASOkz55nUaArlBEALw_wcB) w/o switch

     Note: Use different size resistors to get stall current to be as small as possible

  2. [Rapido RailCrew Switch Machine](https://www.whiterosehobbies.com/products/rapido-trains-320101-railcrew-switch-machine-operating-switch-stand-single)

     - [instructions](https://rapidotrains.com/media/pdf/12switch-Instructions_may2020.pdf), [wiring](https://rapidotrains.com/warranty/product-support/railcrew-switch-machines-product-support)

  3. [DCC Concepts Cobalt (point motor)](https://www.dccconcepts.com/product-category/the-cobalt-collection/cobalt-point-motors/)

  4. [Walthers 942-101 Switch       Machine $25](https://www.walthers.com/walthers-control-system-switch-machine), ([instructions](https://s3.amazonaws.com/aws.walthers.com/942-101+Switch+Machine+Instruction+Sheet+and+Advance+Control+Manual.pdf) 

     - Note: Refer to section 4.5 on connecting 'stall' motor type of wiring to the 2 POWER pins

  5. [MP4, MP5 and MP10 Switch Machine by Model Railroad Control Systems](https://www.modelrailroadcontrolsystems.com/mp10-switch-machine/)

     - [MP4](https://www.modelrailroadcontrolsystems.com/mp4-switch-motor/) - 3rd wire for bidirectional ([wiring PDF)](https://www.modelrailroadcontrolsystems.com/content/MP Motor Wiring Application Note.pdf)

- Note Supported (non-stall motor)

  1. [Tam Valley Singlet Servo](https://www.tamvalleydepot.com/defunctsingletii.html) and [SwitchWright Servo Driver Board](https://www.tamvalleydepot.com/products/switchwrightboard.html) (servo controlled)
  2. [MP1 Version 2 Switch Motor](https://www.modelrailroadcontrolsystems.com/mp1-version-2-switch-motor/)


## Troubleshooting

## References

- [Preparing a PCB for Soldering](/pcb-prep/)
- [Solder Tips](/pcb-soldering/)
- Turnout Motor list: [https://dccwiki.com/Turnout_Motors](https://dccwiki.com/Turnout_Motors)
