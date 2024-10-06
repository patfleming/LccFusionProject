---
title: Turnout Twin-Coils Switch Machine Breakout Board Assembly Guide
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





# [Turnout Twin Coils Switch Machine Breakout Board](/turnout-twin-coils-switch-machine-breakout-board-assembly-guide/) Assembly Guide {#turnout-twin-coils-switch-machine-breakout_board_assembly}
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

The **Turnout Twin Coils Switch Machine Breakout Board**, used in conjunction with the LCC **LCC Fusion Node Card**,  **Turnout Card**,  and a twin-coil switch machine, provides both motor control and turnout point position sensing, while also handling frog polarity switching. The board leverages dual mechanical relays to reliably switch the frog between **Rail A** and **Rail B**, based on the turnout's position. Each relay is responsible for controlling one frog, ensuring proper electrical connection as the turnout moves between the **Thrown** and **Closed** positions.

By interfacing directly with the Turnout Card, this breakout board provides a seamless way to control the turnout motor direction and manage frog polarity automatically, making it ideal for complex layout control and automation.

> This board contains a **Capacitor Discharge Unit (CDU)** to drive the switch machines using solenoid coils to move the points.

**Usage**:

This breakout board is for use with 3-wire twin coil (solenoid) switch machines.  

 Wiring examples:****

| Manufacturer                          | Product                                                      | Breakout Board to Switch Machine Connects                    | Frog Polarity                                   | Points Status<sup>1</sup> | Comments                                                     |
| ------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------------- | ------------------------- | ------------------------------------------------------------ |
| Atlas                                 | Snap Switch Machines                                         | Connect `1` to left connector<br>Connect `COM` to middle connector<br>Connect `2` to right connector | Breakout Board                                  | Breakout Board            |                                                              |
| Hornby                                | R8014 Point Motor<br>R8243 Surface Mount Point Motor         | Connect `1` to `Red` wire<br/>Connect `COM` to `Black` wire<br/>Connect `2` to `Green` wire | Breakout Board                                  | Breakout Board            | Configure **Turnout Card** for12V DC motor output. <br>[R8014 Wiring (PDF)](https://support.hornby.com/hc/en-gb/article_attachments/360015938059)<br>[R8243 Wring (PDF)](https://support.hornby.com/hc/en-gb/article_attachments/360015938159) |
| Model Railroad Control Systems (MRCS) | MP1, MP1 (v2), MP5                                           | Connect `1` to `poz1` connector<br>Connect `COM` to `COM` connector<br>Connect `2` to `poz2` connector | Breakout Board, or <br/>MRCS MP1, MP5           | Breakout Board            | [MP1 Wiring (PDF)](https://www.modelrailroadcontrolsystems.com/content/MP1%20Instructions.pdf)<br>[MP5 Wiring (PDF)](https://www.modelrailroadcontrolsystems.com/content/MP5%20instruction_EN_V1.pdf)<br>For MP4 & MP10, use **Turnout Slow Motion Switch Machine Breakout Board** |
| Peco                                  | TwistLock Motor (PL-1000, PL-1000E<br>Turnout Motor PL-10/PL-10E<br>Pico Side Mount | Connect `1` to `Black` or `Red` wire<br>Connect `COM` to **both** `Green` wires<br>Connect `2` to other `Black` or `Red` wire | Breakout Board, or<br>Peco Turnout Motor (PL10) | Breakout Board            | [PL10 Wiring (PDF)](https://www.brian-lambert.co.uk/Electrical-Page-3.html)<br>Switch `1` and `2` connections to reverse motor |
| Rails Connect (by DCCconcepts)        | Rails Connect Point Motors RPM-SM.1, RPM-UB.1                | Connect `1` to `Red` wire<br>Connect `COM` to `Green` wire<br>Connect `2` to `Black` wire | Breakout Board                                  | Breakout Board            |                                                              |

1. To produce LCC Events, the breakout board is must be used since the switch machine itself is not integrated with LCC.

{% include terminology.html %}

## Specifications

Specifications for the [Turnout Slow Motion Switch Machine Breakout Board](/slow-motion-switch-machine-breakout-board-assembly-guide/) include:

| Characteristic                                  | Value                         |
| ----------------------------------------------- | ----------------------------- |
| Max Turnouts                                    | 2                             |
| Input (accessory bus or dedicated power supply) | 7V - 35V<sup>1</sup>          |
| Input (turnout card)                            | 7V - 35V                      |
| Max Input (track bus)                           | 2A                            |
| Max Output (frog)                               | 2A, Track Bus (V)<sup>2</sup> |
| Max Output (turnout coils)                      | 25 (V)<br>2200 (uF)           |

1. Input must be DC, not DCC.
1. Output voltage is determined by the motor output voltage selection found on the Turnout Card.

### How It Works

**NE556 Timer**: Dual timer that generates the 150ms pulse to control the two BSS138 MOSFETs, which in turn discharge the capacitor into the two motor coils.  

**BSS138 MOSFETs**: These N-channel MOSFETs act as switches to control the discharge of the 2200µF capacitor to either motor coil.

**2200µF Capacitor**: Stores the energy required to activate the twin-coil motor, providing a brief but powerful burst of current when triggered.

**TQ2-5V Latching Relay**: Switches the frog polarity between Rail A and Rail B and provides the turnout point status by connecting the sense line to GND.

**Powering the Board**:

- The board utilizes the **Accessory Bus** as its power source to charge the 2200uF capacitor which drives the turnout coils
- The board utilizes the **Track Bus** to optinally power the frogs
- A LM7805CV voltage regulator provides 5V to the NE556 timers.

**Power and Pulse Generation**:

- The board uses an **NE556 timer**, configured in **monostable mode**, to generate a **150ms pulse**.  Pulse duration is determined by a trigger circuit comprised of a resistor and capacitor.
- When the motor control signal is received (from the turnout card), the **NE556** sends a **150ms pulse** to the gate of a **BSS138 MOSFET**.
- The **BSS138 MOSFET** then allows the discharge of a **2200µF capacitor** to the selected twin-coil motor, energizing it just long enough to move the turnout points.  Diodes insure the current flows in only one direction thru the coils.

**Capacitor and Coil Discharge**:

- The **2200µF capacitor** is charged by the DC accessory bus or a dedicated accessory power supply.
- The capacitor's charge is directed to either motor coil (coil 1 or coil 2) by the **BSS138 MOSFETs**, which act as switches controlled by the NE556 timer. Only the selected coil receives the discharge, ensuring smooth and controlled operation of the turnout motor.

**Frog Polarity Control**:

- A **TQ2-5V latching relay** is used to switch the **frog** between **Rail A** and **Rail B**, based on the position of the turnout.
- When one of the motor coils is activated, the relay ensures that the frog is connected to the correct rail, maintaining consistent polarity as the points move.
- 5V voltage regulators (VR2, VR3) reduce the control line voltage as required by the relay.  Diodes ensure the bidirectional current flows only one direction to the relay coils.

**Turnout Point Sensing**:

- The **TQ2-5V relay** also provides a **point status signal**, setting the **sense output line** (from the turnout card) to **GND**. This allows the turnout card to detect whether the points are in the **thrown** or **closed** position.

> The relay latches after the coil is energized, ensuring the frog connection and turnout status remain stable until motor control direction changes.

| **Protected Component**           | **Protection Component**      | **Function**                                                 | **Specifications**                                           | **Location**                                                 |
| --------------------------------- | ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Track Power**                   | **PPTC Polyfuse**             | Protects from sustained overcurrent conditions by increasing resistance. Resets once the fault condition is cleared. | **Fuse Rating:** Based on max track current (typically 0.5-3.5A depending on track power). | In series with the track power supply, between the power source and the track. |
| **Relay Coils, Twin-Coil Motors** | **Flyback Diode**             | Protects the circuit from high-voltage spikes caused by inductive loads (relay and switch machine coils) when switching off. | **Diode Type:** Schottky <br>**Max Current:** Min 2A<br>**Reverse Voltage:** Min 25V | Across the relay coils and turnout switch machine twin-coils. |
| **LM7805CV Regulator**            | **Capacitors (Input/Output)** | Stabilizes voltage and reduces noise on the input and output of the voltage regulator. | **Input Cap:** 0.33µF    **Output Cap:** 0.1µF               | Input cap across the input pin and GND. Output cap across the output pin and GND. |
| **DCC and ACC Circuits**          | **Separate Ground Planes**    | Isolates DCC and accessory grounds to prevent interference   | N/A                                                          | Between DCC and ACC                                          |

### Connectors

The purpose of the **Turnout Twin Coils Switch Machine Breakout Board** and its connectors is to facilitate quick and easy connections between the **Turnout Card** and a turnout controlled by twin-coils (i.e. snap switches)

| Component Designator | **Connector Label ** | Connector Type          | **Connection Number** | **Description**                                              |
| -------------------- | -------------------- | ----------------------- | --------------------- | ------------------------------------------------------------ |
| **J1**               | ACC PWR              | JST XH, Spring Terminal | V+, GND               | Connection to the layouts accessory bus or dedicated power supply (not to DCC).  **GND must connected to the same ground plane as the LCC Fusion Node Card**. |
| **J2**               | FROGS                | JST XH, Spring Terminal | 1, 2                  | Connection to power turnout frogs                            |
| **J3, J4**           | MOTOR 1 / MOTOR 2    | JST XH, Spring Terminal | 1, COM, 2             | Connection to 1 or 2 twin-coils switch machines. Connections 1 and 2 are for one side of each coil.  COM is for the shared connection of the 2 coils. |
| **J5**               | TRACK BUS            | JST XH, Spring Terminal | A, B                  | Connections to the layout track bus for Rail A and Rail B.  Used to power the frog when.  If necessary, switch the connections to match the frog to the correct rail. |
| **J6**               | TURNOUT CARD         | RJ45 Socket             | 1 - 8                 | Refer to Turnout Card’s connection table for the function of each pin |

 ## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}turnout-slow-motion-switch-machine-breakout_board.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram before reference): 

| Component Identifier | Count | Type               | Value                    | Package                | Turnout 1           | Turnout 2           | Purpose                                                      |
| -------------------- | ----- | ------------------ | ------------------------ | ---------------------- | :------------------ | :------------------ | ------------------------------------------------------------ |
| C1, C14, C17         | 3     | Capacitor          | 0.1uF                    | 1206 SMD               | Required (C1, C14)  | Required (C17)      | Smooth output of voltage regulators                          |
| C2, C15, C16         | 3     | Tantalum Capacitor | 0.33uF                   | 3216 SMD               | Required (C2, C15)  | Required (C16)      | Smooth input for voltage regulators                          |
| C3, C4               | 2     | Capacitor          | 2200uF, 25V              | 13mm Aluminum          | Required (C3)       | Required (C4)       | Provides current to drive twin-coil switch coils             |
| C5, C6, C7, C8       | 4     | Capacitor          | 100uF                    | 1206 SMD               | Required (C5, C6)   | Required (C7, C8)   | Part of the 150ms pulse timing circuit for NE556 timer to control discharge rate |
| C9, C10, C11, C12    | 4     | Capacitor          | 0.1uF                    | 1206 SMD               | Required (C9, C10)  | Required (C11, C12) | Stabilizes the internal reference voltage in the timer       |
| C13, C18             | 2     | Capacitor          | 10nF                     | 1206 SMD               | Required (C13)      | Required (C18)      | Enables NE556 timer’s trigger to detect change in current from motor control lines |
| D1                   | 2     | Diode              | SS310, B240, B160        | SMD                    | Required (D1)       | Required (D2)       | Current flow control into 2200uF capacitors                  |
| D2, D3, D4, D5       | 4     | Diode              | SS310, B240, B160        | SMD                    | Required (D2, D3)   | Required (D4, D5)   | Flyback protection from switch machine coils                 |
| D6, D7, D8, D9       | 4     | Diode              | SS310, B240, B160        | SMD                    | Required (D6, D7)   | Required (D8, D9)   | Current flow control from BSS138 transistors to turnout coils |
| D10, D11             | 2     | Diode              | SS310, B240, B160        | SMD                    | Required (D10)      | Required (D11)      | Flyback protection from the TQ2-5V relay’s coils             |
| D12, D14             | 2     | Diode              | SS310, B240, B160        | SMD                    | Required (D12)      | Required (D14)      | Flow control from 5V voltage regulator output to relays      |
| D13, D15             | 2     | Diode              | SS310, B240, B160        | SMD                    | Required (D13)      | Required (D15)      | Flow control of bidirectional control line current to relay coils |
| F1, F2               | 2     | Resettable Fuse    | SK30, 1.5A, 5V (or more) | PTH                    | Required            | Required            | Current overload protection from track (frog)                |
| J1                   | 2     | JST XH Socket      | 2P, 2.54mm               | PTH or Spring Terminal | Required            | Required            | Connector to ACC BUS (V+, GND) for charging 2200uF capacitor and regulator for NE556 timer |
| J2                   | 2     | JST XH Socket      | 2P, 2.54mm               | PTH or Spring Terminal | Optional            | Optional            | Connector to turnout frog                                    |
| J3, J4               | 2     | JST XH Socket      | 2P, 2.54mm               | PTH or Spring Terminal | Required (J3)       | Required (J4)       | Connector to motor(s)                                        |
| J5                   | 2     | JST XH Socket      | 2P, 2.54mm               | PTH or Spring Terminal | Required            | Required            | Connector to track power rails (**Rail A** and **Rail B**)   |
| J6                   | 2     | RJ45 Socket        | 8P8C                     | PTH                    | Required            | Required            | Network cable (CAT5/6) connection from **I/O Card**          |
| K1, K2               | 2     | Relay              | DPDT, TQ2-5V             | PTH                    | Required (K1)       | Required (K2)       | Controls current to turnout frog and points sensing          |
| Q1 - Q4              | 4     | Transistor         | BSS138 NPN               | SOT-23                 | Required (Q1, Q2)   | Required (Q3, Q4)   | Controls the current to the motor coils                      |
| R1                   | 2     | Resistor           | 470Ω                     | 1206 SMD               | Required            | Required            | Limits current to capacitor for 1 sec charge time            |
| R2, R3, R4, R5       | 4     | Resistor           | 1.5kΩ                    | 1206 SMD               | Required (R2, R3)   | Required (R4, R5)   | Part of the 150ms pulse timing circuit for NE556 timer to control discharge rate |
| U1, U2               | 2     | Dual Timer         | NE556                    | DIP14, PTH             | Required (U1)       | Required (U2)       | Provides 150ms pulse to transistor to release current from 2200uF capacitor to motor coils |
| VR1, VR2, VR3        | 3     | Voltage Regulator  | LM7805CV                 | TO-220, SMD            | Required (VR1, VR2) | Required (VR1, VR3) | Provides 5V to relays and NE556 timer                        |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/Breakout_Boards/turnout_twin_coils_switch_machine_breakout_board_pcb.png/" style="zoom:50%; float:right" />Below are the high level steps for assembly of the [Turnout Twin Coils Switch Machine Breakout Board](/turnout-twin-coils-switch-machine-breakout-board-assembly-guide/):

Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

>  See also: [Soldering Tips](/pcb-soldering/)









| Component Identifier | Component (Package)                                          | Orientation                                                  |
| -------------------- | ------------------------------------------------------------ | :----------------------------------------------------------- |
| C1, C14, C17         | Capacitor, 0.1uF, 1206 SMD                                   | None                                                         |
| C2, C15, C16         | 0.33uF Tantalum Capacitor (3216 SMD)                         | Cathode end has a brown line and positioned towards PCB top edge |
| C3, C4               | Capacitor, 2200uF, Aluminum electrolytic, 25V, 13mm          | Position anode towards PCB right edge                        |
| C5, C6, C7, C8       | Capacitor, 100uF, 1206 SMD                                   | None                                                         |
| C9, C10, C11, C12    | Capacitor, 0.1uF, 1206 SMD                                   | None                                                         |
| C13, C18             | Capacitor, 10nF, 1206 SMD                                    | None                                                         |
| D1                   | Diode, SS310, B240, or B160 (SMD)                            | Cathode end has a white line and positioned towards PCB bottom edge |
| D2, D3, D4, D5       | Diode, SS310, B240, or B160 (SMD)                            | Cathode end has a white line and positioned towards PCB left edge |
| D6 - D15             | Diode, SS310, B240, or B160 (SMD)                            | Cathode end has a white line and positioned towards PCB top edge |
| F1, F2               | Resettable Fuse, 1.5A (PTH)                                  | None                                                         |
| J1 - J5              | JST XH Socket (2P, 2.54mm), or 2-Position Spring Terminal Connector (2.54mm, PTH, vertical or horizontal) | Position connection towards PCB top edge                     |
| J6                   | RJ45 socket (8P8C, PTH)                                      | Fits only one way                                            |
| K1, K2               | TQ2-5V (PTH)                                                 | Position IC’s small dimple in corner (pin 1) towards PCB top edge |
| Q1 - Q4              | BSS138 (SOT-23)                                              | Fits only one way                                            |
| R1                   | Resistor, 470Ω  (1206 SMD)                                   | None                                                         |
| R2, R3, R4, R5       | Resistor, 1.5kΩ  (1206 SMD)                                  | None                                                         |
| U1, U2               | Dual Timer, NE556, DIP14                                     | Position IC’s indent towards PCB top edge                    |
| VR1, VR2, VR3        | Voltage Regulator, LM7805CV (TO-220, SMD)                    | Position heat sink towards PCB top edge                      |

## Testing and Verification

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.
2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.


### Functional Testing

1. Connect accessory bus to `ACC BUS` connector (J1)

2. Connect track bus rails to `TRACK BUS` connector (J5)

3. Test Motor 1

   1. Connect a twin-coils switch machine to `MOTOR 1` (J3)

   2. Momentarily connect 12V+ (e.g. accessory bus) to RJ45 socket (J5) **pin 1** and GND to **pin 2**.  

      > Access RJ45 pins from PCB bottom).  Pin 1 has a **square solder pad**.  Pin 2 is position above it, with other pins alternating between the rows.

   3. **Results**:
      
      - one of the motor’s coils moves the turnout points.


    3. Check for movement by the 2nd turnout coil by momentarily touching 12V+ to **pin 2** and GND to **pin 1**.


## Troubleshooting

## References

- [Preparing a PCB for Soldering](/pcb-prep/)
- [Solder Tips](/pcb-soldering/)
- Turnout Motor list: [https://dccwiki.com/Turnout_Motors](https://dccwiki.com/Turnout_Motors)
