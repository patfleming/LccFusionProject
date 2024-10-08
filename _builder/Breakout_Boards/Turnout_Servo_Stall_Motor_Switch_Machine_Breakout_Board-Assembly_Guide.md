---
title: Turnout Servo Stall Motor Switch Machine Breakout Board Assembly Guide
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





# Turnout Servo Stall Motor Switch Machine Breakout Board Assembly Guide {#turnout-servo-stall-motor-switch-machine-breakout_board_assembly}
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

The **Turnout Servo Stall Motor Switch Machine Breakout Board**, used in conjunction with the LCC **LCC Fusion Node Card**,  **Turnout Card**,  and a servo stall motor based switch machine, provides PWM based servo motor control and turnout point position sensing, while also handling frog polarity switching. The board leverages dual mechanical relays to reliably switch the frog between **Rail A** and **Rail B**, based on the turnout's position. Each relay is responsible for controlling one frog, ensuring proper electrical connection as the turnout moves between the **Thrown** and **Closed** positions.

> Requires a PWM based 5V 3-wires servo (i.e. SG90).

To accommodate various turnout and configuration, servo movement is configuable in increments of 15&deg; (15&deg;, 30&deg;, 45&deg;, 90&deg;) based on installation of a resistor.

By interfacing directly with the Turnout Card, this breakout board provides a seamless way to control the turnout motor direction and manage frog polarity automatically, making it ideal for complex layout control and automation.

**Usage**:

This breakout board is for use with 3-wire servo used as a stall motor switch machines.  Wiring examples:

| Manufacturer | Product | Breakout Board to Switch Machine Connects                    | Comments                                                     |
| ------------ | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <various>    | SG90 9g | Connect `S` to `Yellow` wire<br>Connect `V+` to `Red` wire<br>Connect `G` to `Black` wire | Servo comes with a standard JST XH 3P plug to plug into the breakout board JST XH socket |

{% include terminology.html %}

## Specifications

Specifications for the [Turnout Slow Motion Switch Machine Breakout Board](/slow-motion-switch-machine-breakout-board-assembly-guide/) include:

| Characteristic                                      | Value                         |
| --------------------------------------------------- | ----------------------------- |
| Max Servos                                          | 2                             |
| Output (servo)                                      | 5V                            |
| Max Output (servo)                                  | 1.5A                          |
| Max Output (frog)                                   | 2A, Track Bus (V)<sup>1</sup> |
| Min Input (accessory bus or dedicated power supply) | 7V (DC, not DCC)              |
| Min Input (turnout card)                            | 7V                            |
| Max Input (track bus)                               | 2A                            |

1. Output voltage is determined by the motor output voltage selection found on the Turnout Card.

Your description is clear and informative, but I made a few adjustments for flow and clarity. Here's the revised version of the "How It Works" section:

---

### How It Works

The **Turnout Servo Stall Motor Switch Machine Breakout Board** is designed to interface with the **Turnout Card** to control **servo stall motors** for managing turnout points, while also controlling the frog polarity based on the turnout position. The board enables **bidirectional motor control** and uses relays to switch the frog between **Rail A** and **Rail B** of the track bus, ensuring proper electrical continuity as the turnout moves between the **Thrown** and **Closed** positions.

1. **Inputs and Outputs Connections:**

   - **Input (Control Signals)**: 
     - The **Turnout Card** provides the control signals to the motor, determining the direction of movement. The board receives control signals via two input lines handling the **bidirectional motor control**:

       - **One polarity** moves the servo to the **Thrown** position.
       - **Reverse polarity** moves the servo to the **Closed** position.

     - As the control signals are sent from the **LCC Fusion Node Card** firmware, the **Turnout Card** uses its **MCP23017 GPIO** to switch between high and low states. The signals pass through a **TC4428 driver** to activate the servo motor, moving the turnout points accordingly.

     - The motor control signal is processed by an **NE556 dual timer**, which converts it into a **PWM signal** that drives the servo's signal line. The timer operates at **50Hz (20ms periods)**, generating two different pulse widths that control the servo's forward and backward movement. The timing circuit configures the pulse widths, determining the degree of servo movement.

     - The **Turnout Card** motor output selection can be configured for either **12V** or **9V**, as a **5V regulator** powers both the timer and the servo.


   - **Servo Motor Output:**

     - The servo, such as an **SG90**, uses a dual timer (NE556) to generate a **PWM control signal** to control the direction and position of the turnout points. The PWM signal determines the rotation angle of the servo.

       - Three connections are made to the servo:

         - **PWM control signal**

         - **5V power**

         - **GND**

       - The **PWM signal** generated by the **NE556 timer** controls the servo's movement by varying the pulse width, typically between **1ms to 2ms**, corresponding to the servo's rotational range (e.g., 0 to 180 degrees).
       - There are **no current-limiting resistors** in this configuration since the servo is powered directly by the **5V supply** and the **PWM signal** drives the movement.


2. **Relays for Frog Polarity Control:**

   - The **Turnout Servo Stall Motor Switch Machine Breakout Board** uses a mechanical relay to manage frog polarity. The relay switches the frog's connection between **Rail A** and **Rail B**, depending on the turnout position.

   - This setup guarantees the frog has the correct polarity, providing smooth operation and preventing short circuits as trains pass through the turnout.

### Connectors

The purpose of the **Turnout Servo Switch Machine Breakout Board** and its connectors is to facilitate quick and easy connections between the **Turnout Card** and a turnout controlled by a servo.

| Component Designator | **Connector Label ** | Connector Type          | **Connection Number** | **Description**                                              |
| -------------------- | -------------------- | ----------------------- | --------------------- | ------------------------------------------------------------ |
| **J1**               | ACC PWR              | JST XH, Spring Terminal | V+, GND               | Connection to the layouts accessory bus or dedicated power supply (not to DCC).  **GND must connected to the same ground plane as the LCC Fusion Node Card**. |
| **J2**               | FROGS                | JST XH, Spring Terminal | 1, 2                  | Connection to power turnout frogs                            |
| **J3, J4**           | MOTOR 1 / MOTOR 2    | JST XH, Spring Terminal | S, V+, G              | Connection to servo.  `S` is for the servo’s PWM signal wire, V+ is the 5V wire, and `G` is for the ground wire.  Note that most SG90 5V servos have a wiring harness with a JST XH plug that matches this arrangement. |
| **J5**               | TRACK BUS            | JST XH, Spring Terminal | A, B                  | Connections to the layout track bus for Rail A and Rail B.  Used to power the frog when.  If necessary, switch the connections to match the frog to the correct rail. |
| **J6**               | TURNOUT CARD         | RJ45 Socket             | 1 - 8                 | Refer to Turnout Card’s connection table for the function of each pin |

### Protection

| **Protected Component**       | **Protection Component**      | **Function**                                                 | **Specifications**                                           | **Location**                                                 |
| ----------------------------- | ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Entire Circuit**            | **PPTC Polyfuse**             | Protects from sustained overcurrent conditions by increasing resistance when the current exceeds 0.25A (250mA). Resets once the fault condition is cleared. | **Hold Current:** 0.25A   <br>**Trip Current:** 0.5A         | In series with the motor's Vcc line. Adjust the fuse type to match the max current expected by the servo motor. |
| **Track Power**               | **PPTC Polyfuse**             | Protects from sustained overcurrent conditions by increasing resistance. Resets once the fault condition is cleared. | **Fuse Rating:** Based on max track current (typically 0.5-3.5A depending on track power). | In series with the track power supply, between the power source and the track. |
| **Relay Coils, Stall Motors** | **Flyback Diode**             | Protects the circuit from high-voltage spikes caused by inductive loads (relay coils, stall motors) when switching off. | **Diode Type:** Schottky  <br> **Max Current:** Min 0.5A  <br>**Reverse Voltage:** Min 12V | Across the relay coil and servo motor terminals              |
| **LM7805CV Regulator**        | **Capacitors (Input/Output)** | Stabilizes voltage and reduces noise on the input and output of the voltage regulator. | **Input Cap:** 0.33µF   <br>**Output Cap:** 0.1µF            | Input cap across the input pin and GND. Output cap across the output pin and GND. |
| **DCC and ACC Circuits**      | **Separate Ground Planes**    | Isolates DCC and accessory grounds to prevent interference   | N/A                                                          | Between DCC and ACC                                          |

 ## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}turnout-slow-motion-switch-machine-breakout_board.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram before reference): 

| Component Identifier | Count | Type               | Value                    | Package       | Motor 1             | Motor 2             | Purpose                                                      |
| -------------------- | ----- | ------------------ | ------------------------ | ------------- | :------------------ | ------------------- | :----------------------------------------------------------- |
| C1, C2, C3, C4       | 4     | Ceramic Capacitor  | 100µF                    | 1206 SMD      | Required (C1, C2)   | Required (C3, C4)   | Timing Circuit for PWM 50Hz (period / duty cycle)            |
| C5, C8, C10          | 3     | Tantalum Capacitor | 0.33µF                   | 3216 SMD      | Required (C5, C8)   | Required (C5, C10)  | Used by 5V voltage regulator for input filtering.            |
| C6, C7, C9           | 3     | Ceramic Capacitor  | 0.1µF                    | 1206 SMD      | Required (C6, C7)   | Required (C6, C9)   | Used by 5V voltage regulator for output filtering.           |
| D1, D2, D3, D8       | 4     | Diode              | SS310                    | SMD           | Optional (D1, D3)   | Optional (D2, D8)   | Circuit protection against flyback from motors and coils.    |
| D4, D5, D6, D7       | 4     | Diode              | SS310                    | SMD           | Required (D4, D5)   | Required (D6, D7)   | Ensures the 2 timer generated PWM signals don’t reverse flow back to the timer since they share the same servo motor connection. |
| D9, D10, D11, D12    | 4     | Diode              | SS310                    | SMD           | Required (D9, D10)  | Required (D11, D12) | Forces bidirectional motor current to flow only one way to LM7805 voltage regulator |
| F1, F2               | 2     | Resettable Fuse    | JK30, 3A, 12V (or more)  | PTH           | Required (F1)       | Required (F2)       | Current overload protection to frog. Adjust value to match max current expected. |
| F3                   | 1     | Resettable Fuse    | JK30, 1.5A, 5V (or more) | 1206 PPTC SMD | Required            | Required            | Current overload protection to servo motors. Adjust value to match max current expected during servo stall operations. |
| J1                   | 1     | Connector          | JST XH (2P)              | 2.54mm        | Required            | Required            | Connector to ACC BUS ground connection. Ground must be connected to the same ground as the **LCC Fusion Node Card** |
| J2                   | 1     | Connector          | JST XH (2P)              | 2.54mm        | Optional            | Optional            | Connector to turnout frog                                    |
| J3, J4               | 2     | Connector          | JST XH (2P)              | 2.54mm        | Required (J3)       | Required (J4)       | Connector to servo motor(s)                                  |
| J5                   | 1     | Connector          | RJ45 (8P8C)              | PTH           | Required            | Required            | Network cable (CAT5/6) connection from Turnout Card.         |
| R1, R2, R3, R4       | 4     | Resistor           | 10kΩ                     | 1206 SMD      | Required (R1, R2)   | Required (R3, R4)   | Controls the charge time for Timing Circuit and frequency for the PWM signal |
| R5, R6, R9, R10      | 4     | Resistor           | 10kΩ                     | 1206 SMD      | Required (R5, R6)   | Required (R9, R10)  | Controls the discharge time for Timing Circuit for the PWM signal |
| R7, R11<sup>1</sup>  | 2     | Resistor           | 270Ω                     | 1206 SMD      | Required (R7)       | Required (R8)       | Determine the pulse width for the servo forward movement.    |
| R8, R12<sup>1</sup>  | 2     | Resistor           | 470Ω                     | 1206 SMD      | Required (R7)       | Required (R8)       | Determine the pulse width for the servo reverse movement.    |
| K1, K2               | 2     | Relay              | DPDT TQ2-5V              | PTH           | Required (K1)       | Required (K2)       | Controls track Rail A and Rail B to frog and Point Sense line to ground |
| U1, U2               | 2     | Timer IC           | NE556                    | DIP14, PTH    | Required (U1)       | Required (U2)       | Provides PWM signal to servo motors.                         |
| VR1, VR2, VR3        | 3     | Voltage Regulator  | LM7805CV                 | TO-220 SMD    | Required (VR1, VR2) | Required (VR1, VR3) | Provides 5V to NE556 timer and servo motor(s)                |

1. The value for these resistors determines both the direction and degrees of the servo’s movement. Use the table below to determine the resistor values for the amount of movement from the servo’s 90° position. Note that the values shown below are **additive to the 10kΩ resistor** and are calculated for use with a **0.1uF capacitor**.

| **Movement (Degrees)** | **Position / Resistor ** | **Position / Resistor** |
| ---------------------- | ------------------------ | ----------------------- |
| **15°**                | 75&deg; / 300Ω           | 105&deg; / 420Ω         |
| **30°**                | 60&deg; / 270Ω           | 120&deg; / 470Ω         |
| **45°**                | 45&deg; /130Ω            | 135&deg; / 530Ω         |
| **60°**                | 30&deg; / 60Ω            | 150&deg; / 580Ω         |
| **75&deg; **           | 15&deg; / 0Ω             | 165&deg; / 600Ω         |
| **90°**                | 0&deg; /0Ω               | 180&deg; / 720Ω         |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/Breakout_Boards/turnout_servo_stall_motor_switch_machine_breakout_board_pcb.png/" style="zoom:70%; float:right" />Below are the high level steps for assembly of the Block Breakout Board:

Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

>  See also: [Soldering Tips](/pcb-soldering/)















| Component Identifier | Component (Package)                                          | Orientation                                                  |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| C1, C2, C3, C4       | Capacitor, 100uF (1206 SMD)                                  | None                                                         |
| C5, C8, C10          | 0.33uF Tantalum Capacitor (3216 SMD)                         | Position cathode end (tan line) to PCB **top** edge              |
| C6, C7, C9           | Capacitor, 0.1uF (1206 SMD)                                  | None                                                         |
| D1, D2               | Diode, SS310 (SMD)                                           | Position cathode end (white line) to PCB **left** edge           |
| D3 - D12             | Diode, SS310 (SMD)                                           | Position cathode end (white line) to PCB **top** edge            |
| F1, F2               | Resettable Fuse, 3A (PTH)                                    | None                                                         |
| F3                   | Resettable Fuse, 1.5A (PTH)                                  | None                                                         |
| J1 - J4              | JST XH Socket (2P, 2.54mm), or 2-Position Spring Terminal Connector (2.54mm, PTH, vertical or horizontal) | Position connection towards PCB **top** edge                     |
| J5                   | RJ45 socket (8P8C, PTH)                                      | Fits only one way                                            |
| R1 - R6, R9, R10     | 10kΩ resistors (1206 SMD)                                    | None                                                         |
| R7, R11              | 270Ω resistors (1206 SMD)                                    | None                                                         |
| R8, R12              | 470Ω resistors (1206 SMD)                                    | None                                                         |
| K1, K2               | Relay, DPDT, TQ2-5V (PTH)                                    | Position IC’s small dimple in corner (pin 1) towards PCB **top** edge |
| U1, U2               | Dual timer, NE556 (PTH)                                      | Position IC indent towards PCB **top** edge                      |
| VR1, VR2, VR3        | Voltage Regulator, LM7805CV (TO-220, SMD)                    |                                                              |

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
