---
title: DC Motor Driver Breakout Board Assembly Guide
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





# DC Motor Driver Breakout Board Assembly Guide {#dc-motor-driver-breakout_board_assembly}
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

The **DC Motor Driver Breakout Board**, in combination with the LCC LCC Fusion Node Card and I/O Card, provides a versatile and robust solution for controlling up to two DC motors in your project. Designed with flexibility and ease of use in mind, this breakout board is perfect for a wide range of applications, whether you're working on robotics, automation, or any other project requiring precise motor control.

#### Key Features:
- **Dual Motor Control**: The board supports two independent DC motors, allowing you to control each motor separately for complex maneuvers and operations.
- **Voltage Selector**: Easily switch between 5V and 12V operation with an onboard selector, making this board adaptable to different motor voltage requirements.
- **Layout Accessory Bus Input**: This board integrates seamlessly with your existing layout accessory bus, simplifying the connection process and ensuring compatibility with your setup.
- **Network Cable Connection**: The board connects to your PWM Card via a standard network cable, ensuring reliable communication and easy integration into your system.

With these features, the DC Motor Driver Breakout Board offers a powerful yet straightforward way to control your DC motors, making it an essential component for any motor-driven project. 

{% include terminology.html %}

## Specifications

Specifications for the DC Motor Driver Breakout Board include:

| Characteristic       | Value                                  |
| -------------------- | -------------------------------------- |
| Max DC Motors        | 2                                      |
| Max Output per Motor | 2A                                     |
| Output Voltage       | 5V, 12V<sup>1</sup>, INPUT<sup>2</sup> |
| Min Input            | 7V, 14V<sup>2</sup>                    |
| Max Input            | 35V                                    |

1. Output voltage selections include INPUT (voltage), 5V, and 12V.  
2. When selecting INPUT, the output voltage is 2V less than the input voltage
3. Input voltage must be at least 2V above output voltage.

### How It Works

The combination of the TC4428 MOSFET driver and the L298N H-Bridge provides a powerful and flexible way to control the speed and direction of DC motors. Here’s a step-by-step explanation of how this setup works:

1. **Motor Voltage Selection**

    A Jump Cap is used with the `MOTOR VOLTAGE` selector to select `5V`, `12V` or the `ACC PWR` voltage for the output to the motor.  When 5V or 12V is selected, a LM2596S-ADJ adjustable buck voltage converter is used to step down the accessory voltage to either 5V or 12.  Resistors are used to select the desired voltage output.

2. **Direction Control Using TC4428:**
    The TC4428 MOSFET driver is used to set the direction of the DC motor by controlling the logic levels sent to the L298N H-Bridge.
    The DIRA pin on the TC4428 determines the motor’s direction:
    High (H): Sets the motor to move forward by making IN1=H and IN2=L on the L298N.
    Low (L): Reverses the motor direction by setting IN1=L and IN2=H on the L298N.
    This enables precise control over which direction the motor spins.

3. **Speed Control Using PWM:**
    The motor’s speed is controlled by a Pulse Width Modulation (PWM) signal sent to the ENA pin of the L298N.
    By varying the duty cycle of the PWM signal, you can adjust the speed of the motor.
    The higher the duty cycle, the faster the motor will spin, and vice versa.

4. **Integration Between TC4428 and L298N:**

  The TC4428 takes in a digital signal from a microcontroller or control logic and amplifies it to drive the inputs of the L298N H-Bridge.

  1. For Forward Movement: DIRA=High → IN1=H, IN2=L

  1. For Reverse Movement: DIRA=Low → IN1=L, IN2=H

  The L298N then drives the motor in the appropriate direction based on these signals.

4. **Operational Modes:**
    Forward: When the DIRA pin is high, and the PWM signal is active, the motor runs forward.

  **Reverse**: When the DIRA pin is low, the motor runs in reverse.

  **Brake** (Fast Stop): When both IN1 and IN2 are high or low while the PWM signal is active, the motor quickly stops.

  **Motor Stop**: When the PWM signal (ENA) is low, the motor stops regardless of the state of IN1 and IN2.

5. **Practical Application:**
    This setup is useful for applications where precise control of motor speed and direction is needed, such as in robotics or automated systems.
    The integration between the TC4428 and L298N allows for both simple direction control and variable speed control using a single PWM signal.

### Connectors

| Components Designator | **Connector Label**            | Connector  Type | **Connection Number** | **Function**      | **Description**                                              |
| --------------- | -------------- | ---------------------------------- | ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **J1**          | **ACC BUS** | JST XH, Spring Terminal | 1              | Vcc               | Power supply from the layout accessory bus                   |
| **J1** | **ACC BUS** | JST XH, Spring Terminal | 2              | GND               | Ground connection                                            |
| **J2**          | **MOTORS 1-2**       | JST XH, Spring Terminal | 1 (+)          | Motor 1 (+)       | Positive terminal of Motor 1                                 |
| **J2** | **MOTORS 1-2** | JST XH, Spring Terminal | 2 (-)          | Motor 1 (-)       | Negative terminal of Motor 1                                 |
| **J3**          | **MOTORS 1-2**  | JST XH, Spring Terminal | 1 (+)          | Motor 2 (+)       | Positive terminal of Motor 2                                 |
| **J3** | **MOTORS 1-2** | JST XH, Spring Terminal | 2 (-)          | Motor 2 (-)       | Negative terminal of Motor 2                                 |
| **J4**          | **PWM CARD** | RJ45 Socket | 1              | Motor Direction 1 | Controls the direction of Motor 1 (e.g., forward/reverse)    |
| **J4** | **PWM CARD** | RJ45 Socket | 2              | Motor Direction 2 | Controls the direction of Motor 2 (e.g., forward/reverse)    |
| **J4** | **PWM CARD** | RJ45 Socket | 3              | PWM (Enable) 1    | Controls the speed of Motor 1 via PWM signal (ENA pin on L298N) |
| **J4** | **PWM CARD** | RJ45 Socket | 4              | PWM (Enable) 2    | Controls the speed of Motor 2 via PWM signal (ENB pin on L298N) |
| **J4** | **PWM CARD** | RJ45 Socket | 5              | Current Sense 1   | Monitors the current through Motor 1 (SENSE A pin on L298N)  |
| **J4** | **PWM CARD** | RJ45 Socket | 6              | Current Sense 2   | Monitors the current through Motor 2 (SENSE B pin on L298N)  |
| **J4** | **PWM CARD** | RJ45 Socket | 7              | GND               | Ground connection                                            |
| **J4** | **PWM CARD** | RJ45 Socket | 8              | Vcc               | Power supply for logic and motor driver                      |
| **JP1**         | **MOTOR VOLTAGE** | 3-Pin Male Header | INPUT, 5V 12V | 5V                | Uses a Jumper Cap to select the voltage of the motor, `5V`, `12V`, `INPUT`.  Selecting `INPUT`results in `ACC BUS` voltage to be used for the motor. |

### Protection

The DC Motor Driver Breakout Board includes several key protection mechanisms to safeguard both the board itself and the connected components. Below is a detailed table outlining the protection provided against flyback voltage and reverse voltage, ensuring the longevity and reliability of your setup.

| **Protected Component**  | **Protection Component** | **Function**                                                 | **Specifications**                  | **Location**                                    |
| ------------------------ | ------------------------ | ------------------------------------------------------------ | ----------------------------------- | ----------------------------------------------- |
| **L298N H-Bridge**       | Internal Flyback Diodes  | Protects against inductive kickback from DC motors.          | Integrated into the L298N H-Bridge. | Within the L298N H-Bridge IC.                   |
| **L298N H-Bridge**       | B240 Schottky Diode      | Protects against reverse voltage and reverse current.        | Reverse Voltage: 40V, Current: 2A.  | On the DC Motor Driver PCB, across power lines. |
| **LM2596-ADJ Regulator** | **Output Capacitor**     | Filters out high-frequency noise and transient voltage spikes from the output, ensuring stable 5V regulation. | **Value:** 680 µF Polymer Solid     | Across the output (5V) and GND                  |
| **IC’s**                 | **Decoupling Capacitor** | Filters out high-frequency noise and transient voltage spikes from the power supply, ensuring stable voltage for the IC’s. | **Value:** 0.1 µF, 44uF ceramic     | Across the Vcc input and GND                    |

 ## Components List {#components}

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}dc-motor-driver-breakout_board.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram below for reference): 

| **Component Identifier** | **Count** | **Type**                         | **Value**            | **Package**   | **Required** | **Purpose**                                      |
| ------------------------ | --------- | -------------------------------- | -------------------- | ------------- | ------------ | ------------------------------------------------ |
| C1                       | 1         | Ceramic Capacitor                | 47µF                 | 1206 SMD      | Required     | Decoupler for LM298N.                            |
| C2                       | 1         | Ceramic Capacitor                | 0.1µF (100nF)        | 1206 SMD      | Required     | Decouplers for ICs.                              |
| C3                       | 1         | Polymer Solid Capacitor          | 680uF, 10V           | 6x12mm, PTH   | Required     | Input filtering for the voltage regulator.       |
| C4                       | 1         | Polymer Solid Capacitor          | 220µF, 10V           | 6.3x5.8mm SMD | Required     | Input filtering for the voltage regulator.       |
| D1 - D8                  | 8         | Diode                            | SS310, B240, or B160 | SMD           | Required     | Circuit protection.                              |
| D9                       | 1         | Diode                            | SS310, B240, or B160 | SMD           | Required     | Required by LM2574N.                             |
| J1                       | 1         | JST XH Socket or Spring Terminal | 2P, 2.54mm           | PTH           | Required     | Connectors to layout accessory bus (V+, GND).    |
| J2, J3                   | 2         | JST XH Socket or Spring Terminal | 2P, 2.54mm           | PTH           | Required     | Connectors to the DC motor(s).                   |
| J4                       | 1         | RJ45 Socket                      | 8P8C                 | PTH           | Required     | Network cable (CAT5/6) connection from PWM Card. |
| L1                       | 1         | Inductor                         | 33µH                 | PTH           | Required     | Used for 5V voltage regulation.                  |
| R1                       | 1         | Resistor                         | 1KΩ                  | PTH           | Required     | Used with voltage regulator feed back pin        |
| R2                       | 1         | Resistor                         | 4.7KΩ                | PTH           | Required     | Used to adjust voltage regulator to 5V           |
| R3                       | 1         | Resistor                         | 10KΩ                 | PTH           | Required     | Used to adjust voltage regulator to 12V          |
| R4, R5                   | 2         | Resistor                         | 0.5Ω                 | 1206 SMD      | Required     | Current limiting for L298N CS selectors to GND.  |
| U1                       | 1         | Dual Full Bridge Driver          | L298N                | PTH           | Required     | Provides dual full-bridge motor control.         |
| U2, U3                   | 2         | Mosfet Driver                    | TC4428               | SMD           | Required     | Provides high-speed switching.                   |
| VR1                      | 1         | Buck Converter                   | LM2596S-ADJ          | SMD           | Required     | 5V buck converter for voltage regulation.        |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="{{ site.baseurl }}/assets/images/pcbs/Breakout_Boards/dc_motor_driver_breakout_board_pcb.png/" style="zoom:50%; float:right" />Below are the high level steps for assembly of the DC Motor Driver Breakout Board:

Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

>  See also: [Soldering Tips](/pcb-soldering/)



| Component Identifier | Component (Package)                                          | Required | Orientation                                     |
| -------------------- | ------------------------------------------------------------ | :------- | ----------------------------------------------- |
| C1                   | Capacitor, 47uF (1206 SMD)                                   | Required | None                                            |
| C2                   | Capacitor, 0.1uF (100nF, 1206 SMD)                           | Required | None                                            |
| C3                   | Capacitor, 680uF, 25V, (SMD)                                 | Required | Anode positioned toward PCB **top** edge            |
| C4                   | Capacitor, 220uF, 25V, (SMD)                                 | Required | Anode positioned toward PCB **top** edge            |
| D1 - D4              | Diode, SS310, B240, or B160 (SMD)                            | Required | Anode positioned toward PCB **right** edge          |
| D5 - D8              | Diode, SS310, B240, or B160 (SMD)                            | Required | Anode positioned toward PCB **bottom** edge         |
| D9                   | Diode, SS310, B240, or B160 (SMD)                            | Required | Anode positioned toward PCB **left** edge           |
| J1, J2, J3           | JST XH Socket (2P, 2.54mm), or<br>2-Position Spring Terminal Connector (2.54mm, PTH, vertical or horizontal) | Required | Position connection toward PCB **top** edge         |
| J4                   | RJ45 socket (8P8C, PTH)                                      | Required | Position connection toward PCB **bottom** edge      |
| L1                   | Inductor, 33uH (PTH)                                         | Required | None                                            |
| R1                   | 1k&Omega; Resistor (1206 SMD)                                | Required | None                                            |
| R2                   | 4.7k&Omega; Resistor (1206 SMD)                              | Required | None                                            |
| R3                   | 10k&Omega; Resistor (1206 SMD)                               | Required | None                                            |
| R4, R5               | 0.5&Omega; Resistor (1206 SMD)                               | Required | None                                            |
| U1                   | L298N (PTH)                                                  | Required | Fits only one way                               |
| U2, U3               | TC4428 Mosfet Driver (SMD)                                   | Required | Position indent (pin 1) towards PCB **left** edge   |
| VR1                  | LM2596S-ADJ (SMD)                                            | Required | Position indent (pin 1) towards PCB **bottom** edge |

## 

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
