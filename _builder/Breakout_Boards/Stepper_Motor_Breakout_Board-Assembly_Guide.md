---
title: Stepper Motor Breakout Board Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Breakout Board Assembly Guides
nav_order: 2
use_cases:
  - Automation Deployment
  - Node Cluster Setup
  - PCB Design & Assembly
subjects:
  - Assembly Guides
  - Automation
  - Hardware
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_breakout_boards
  - lcc_fusion_cards
  - lcc_fusion_project
  # LCC Fusion Connect Terms
  - lcc_fusion_node_card
  - network_cable
  # Model Railroad Automation Terms
  - accessory_bus
  # Hardware and firmware Terms
  - cleaning_pcb
  - component
---





# Stepper Motor Breakout Board Assembly Guide {#stepper-motor-breakout_board_assembly}
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

The **Stepper Motor Breakout Board**, in combination with the LCC LCC Fusion Node Card and I/O Card, is a versatile and powerful solution designed to control up to two 28BYJ-48 12V stepper motors in model railroad automation and other low-power, precision motor control applications. 

This breakout board interfaces with the I/O Card via a standard network cable, using the MCP23017 GPIO expander to send control signals. Each motor is driven by the M54562FP Darlington array, allowing for reliable and efficient operation of the stepper motors through a simple JST XH 5-wire connector. Powered by the layout accessory bus through an LM7812 voltage regulator, the Stepper Motor Breakout Board provides a stable 12V supply to the motors and control circuitry, ensuring smooth operation. Designed for integration into LCC Fusion systems, this board allows for precise motor control, supporting a wide range of automation tasks.

{% include terminology.html %}

## Specifications

Specifications for the Stepper Motor Breakout Board include:

| Characteristic                                               | Value |
| ------------------------------------------------------------ | ----- |
| Max Motors                                                   | 2     |
| Output                                                       | 12V   |
| Max Output<sup>1</sup> (per motor)                           | 1.5A  |
| Maximum Number of Stepper Motor Breakout Boards per I/O Card | 2     |

1. Max current per motor is based on the LM7812 voltage regulator and fuse.

### How It Works

**1. ESP32 Control via MCP23017 and AccelStepper Library:**

- The **ESP32** is responsible for controlling the stepper motors through the **MCP23017** GPIO expander using the **MCP23017AccelStepper.h** library.
- The **MCP23017** I/O expander communicates over the **I2C bus** and handles the GPIO pins needed to control the stepper motors, which allows the ESP32 to control multiple I/O devices with fewer pins.
- The **AccelStepper library** is great for handling stepper motor movements with smooth acceleration and deceleration. It supports both full-step and half-step modes, which is important for controlling the **28BYJ-48 stepper motors**.

**2. IO Card Connected via Network Cable to Stepper Motor Breakout Board:**

- The **IO Card** connects to the **Stepper Motor Breakout Board** via a network cable (likely using something like a CAT5 or CAT6 cable for signal routing), which is a good choice for distributing signals over a long distance.
- The **Stepper Motor Breakout Board** contains the **M54562FP**, which is responsible for switching the motor phases based on the signals from the MCP23017 GPIO.

**3. M54562FP Driving the 28BYJ-48 Stepper Motor:**

- The **M54562FP** is an 8-channel Darlington transistor array, which makes it ideal for controlling the **4 lines** needed for each stepper motor (since the 28BYJ-48 stepper motor uses 4 phases).
- The **M54562FP** is designed to handle the **12V supply** that powers the 28BYJ-48 stepper motors. It will sink the current through each of the motor's windings as needed to drive the motor in the correct sequence.

**4. Power Supply (LM7812) for 12V:**

- The **LM7812** linear voltage regulator provides a regulated **12V output**, which is necessary for the **M54562FP** to drive the **28BYJ-48 stepper motors**.
- Since the **28BYJ-48** is a **12V stepper motor**, the LM7812 ensures that both the motors and the **M54562FP** receive the correct voltage, allowing them to operate within their specifications.

**5. Supporting Multiple Stepper Motors:**

- The design allows the **IO Card** to support **2 Stepper Motor Breakout Boards**, with each Breakout Board controlling **2 stepper motors**.
- Since the **M54562FP** has **8 channels**, each motor will use **4 channels** to control its 4 phases. Therefore, each breakout board can support **2 stepper motors** using the 8 channels available on the M54562FP.
- The **JST XH 5-wire connector** on the breakout board makes it convenient to connect the **28BYJ-48 stepper motors** without complex wiring.

**Overall Design Workflow**:

1. **ESP32** sends commands via **I2C** to the **MCP23017**.
2. The **MCP23017** expands the GPIO pins and outputs the step sequence (using the **AccelStepper** library) to control the 4 lines of the stepper motors.
3. The **Stepper Motor Breakout Board**, containing the **M54562FP**, receives these signals and switches the appropriate motor phases by sinking the current through the motor windings.
4. The **LM7812** regulator supplies a stable **12V** to both the **M54562FP** and the **28BYJ-48 stepper motors**, allowing the motors to run reliably.

### Connectors

Component Designator  **Connector  Label**  Connector Type  **Connection Number**  **Description**

| Components Designator | **Connection Label**    | Connection Type | **Connection Number** | **Description**     | **Wired To**                                     |
| --------------- | -------------------------- | --------- | ------------------- | ------------------------------------------------ | ------------------------------------------------ |
| **J1, J2**      | **MOTOR A, MOTOR B** | JST XH 5P | **Pin 1** | Coil A (1st phase)  | RJ45 Pin 1 (Motor A)<br>RJ45 Pin 5 (Motor B)     |
| **J1, J2** | **MOTOR A, MOTOR B** | JST XH 5P | **Pin 2** | Coil B (2nd phase)  | RJ45 Pin 2 (Motor A)<br>RJ45 Pin 6 (Motor B)     |
| **J1, J2** | **MOTOR A, MOTOR B** | JST XH 5P | **Pin 3** | Coil C (3rd phase)  | RJ45 Pin 3 (Motor A)<br>RJ45 Pin 7 (Motor B)     |
| **J1, J2** | **MOTOR A, MOTOR B** | JST XH 5P | **Pin 4** | Coil D (4th phase)  | RJ45 Pin 4 (Motor A)<br>RJ45 Pin 8 (Motor B)     |
| **J1, J2** | **MOTOR A, MOTOR B** | JST XH 5P | **Pin 5** | VCC (Common 12V)    | Connected to Vss on M54562FP, powered by ACC BUS |
| **J3**          | **ACC BUS**                | JST XH 2P, Terminal Connector | **Pin 1** | GND                 | Ground reference for power and signal            |
| **J3** | **ACC BUS** | JST XH 2P, Terminal Connector | **Pin 2** | +12V (Power Supply) | Powers both the M54562FP and motors              |
| **J4**          | **I/O CARD** | RJ45 Socket | **Pin 1** | Motor A (1st phase) | Motor Wire 1 (JST XH Pin 1)                      |
| **J4** | **I/O CARD** | RJ45 Socket | **Pin 2** | Motor A (2nd phase) | Motor Wire 2 (JST XH Pin 2)                      |
| **J4** | **I/O CARD** | RJ45 Socket | **Pin 3** | Motor A (3rd phase) | Motor Wire 3 (JST XH Pin 3)                      |
| **J4** | **I/O CARD** | RJ45 Socket | **Pin 4** | Motor A (4th phase) | Motor Wire 4 (JST XH Pin 4)                      |
| **J4** | **I/O CARD** | RJ45 Socket | **Pin 5** | Motor B (1st phase) | Motor Wire 1 (JST XH Pin 1)                      |
| **J4** | **I/O CARD** | RJ45 Socket | **Pin 6** | Motor B (2nd phase) | Motor Wire 2 (JST XH Pin 2)                      |
| **J4** | **I/O CARD** | RJ45 Socket | **Pin 7** | Motor B (3rd phase) | Motor Wire 3 (JST XH Pin 3)                      |
| **J4** | **I/O CARD** | RJ45 Socket | **Pin 8** | Motor B (4th phase) | Motor Wire 4 (JST XH Pin 4)                      |

### Protection

The Stepper Motor Breakout Board includes several key protection mechanisms to safeguard both the board itself and the connected components. Below is a detailed table outlining the protection provided against flyback voltage and reverse voltage, ensuring the longevity and reliability of your setup.

| **Protected Component**       | **Protection Component**  | **Function**                                                 | **Specifications**                                  | **Location**                                           |
| ----------------------------- | ------------------------- | ------------------------------------------------------------ | --------------------------------------------------- | ------------------------------------------------------ |
| **Stepper Motors**            | Polyfuse or Fuse          | Prevents excessive current draw that could damage motors or driver | 1.5A resettable fuse (polyfuse)                     | In series with the 12V supply to the motors            |
| **Stepper Motors**            | Power Supply (LM7812)     | Provides regulated 12V supply to prevent overvoltage to motors and driver | 12V regulated output, 1A or higher current capacity | Power input section, supplying 12V to the board        |
| **Stepper Motors**            | Capacitors (C1, C2)       | Smooths out voltage fluctuations and reduces noise from the power supply | 100µF electrolytic capacitor for input and output   | Located near the power input (before and after LM7812) |
| **M54562FP Darlington Array** | Flyback Diodes (internal) | Protects against voltage spikes (back EMF) from inductive loads such as stepper motors | Integrated into each channel of the M54562FP        | Internal to the M54562FP Darlington Array              |

 ## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}stepper-motor-breakout_board.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram below for reference): 

| Component Identifier | Count | Type                                                  | Value                     | Package  | Required | Purpose                                                      |
| -------------------- | ----- | ----------------------------------------------------- | ------------------------- | -------- | :------- | ------------------------------------------------------------ |
| C1, C2               | 2     | Tantalum Capacitor                                    | 0.33uF                    | 3216 SMD | Required | Capacitors for filtering and stabilizing input/output current |
| C3, D4               | 2     | Capacitor                                             | 220uF, 25V                | SMD      | Required | Used by 12V voltage regulator for input/output filtering.    |
| F1, F2               | 2     | Resettable Fuse                                       | JK30, 1.5A, 12V (or more) | PTH      | Required | Protection from current overload from 12V motor              |
| J1, J2               | 2     | JST XH Socket                                         | 5P, 2.54mm                | -        | Required | Connectors to motor                                          |
| J3                   | 1     | JST XH Socket or 2-Position Spring Terminal Connector | 2P, 2.54mm                | PTH      | Required | Connectors to layout accessory bus                           |
| J4                   | 1     | RJ45 Socket                                           | k8P8C                     | PTH      | Required | Network cable (CAT5/6) connection from I/O Card.             |
| U1                   | 1     | IC                                                    | M54562FP                  | SOP20    | Required | Darlington transistor array to amplify low-current signals for stepper motor control |
| VR1                  | 1     | Voltage Regulator                                     | L7812CV                   | PTH      | Optional | 12V voltage regulator for driving stepper motor(s)           |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/Breakout_Boards/stepper_motor_breakout_board_pcb.png/" style="zoom:50%; float:right" />Below are the high level steps for assembly of the Stepper Motor Breakout Board:

Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

>  See also: [Soldering Tips](/pcb-soldering/)

| Component Identifier | Component (Package)                                          | Required | Orientation                                                  |
| -------------------- | ------------------------------------------------------------ | :------- | ------------------------------------------------------------ |
| C1, C2               | 0.33uF Tantalum Capacitor (3216 SMD)                         | Required | Cathode end has a brown line and positioned towards PCB bottom edge |
| C3, C4               | Capacitor, 220uF, 25V, (SMD)                                 | Required | Anode is position towards PCB top edge                       |
| F1, F2               | Resettable Fuse, 1.5A (PTH)                                  | Required | None                                                         |
| J1, J2               | JST XH Socket (5P, 2.54mm)                                   | Required | Position so stepper motor plug will align with socket labels |
| J3                   | JST XH Socket (2P, 2.54mm) 2-Position Spring Terminal Connector (2.54mm, PTH, vertical or horizontal) | Required | Position connector to PCB top edge                           |
| J4                   | RJ45 socket (8P8C, PTH)                                      | Required | Fits only one way                                            |
| U1                   | M54562FP IC (SOP20)                                          | Required | Position IC indent toward PCB left edge                      |
| VR1                  | L7812CV (PTH)                                                | Optional | Heat sink towards PC top edge                                |

## Testing and Verification

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.
2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.


### Functional Testing


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

- [Preparing a PCB for Soldering](/pcb-prep/)
- [Solder Tips](/pcb-soldering/)
