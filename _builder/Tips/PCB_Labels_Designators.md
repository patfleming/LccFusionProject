---
title: PCB Labels and Designators
typora-root-url: ..
layout: default
permalink: /:name/
parent: Builder's Resources & Tips
use_cases:
  - PCB Design & Assembly
  - Learning & Planning
---
# PCB Labels and Designators {#pcb_designators}

Each PCB to be assembly has a silkscreen layer on both the top and bottom of the PCB.  Silkscreens consist of boxes, lettering, and component outlines are used for PCB information, instructions, and references for assembly.
> Silkscreens are printed in white on PCBs, except for the white PCB where they are printed in black.

## PCB **top**
All PCBs for the project have the following on the PCB **top** (silkscreen):

- **Connector Identification** provides end-user assistance in understand the purpose of a connector (sockets, connectors, jumpers, etc.).
- **Component Outlines** to assist in the location and orientation when placing components on the PCB.
- IC and Module component names to help with identification
- **Component Identifiers** consisting of a letter followed by a unique number.  For example, R1 means resistor one.  Identifiers are referenced in the assembly instructions, component listings, and by PCB fabricators providing assembly services.  Common component designators are listed below.

## PCB **bottom**

Cards and most Breakout Boards for the project have on the PCB **bottom** (silkscreen) the board's name, along with a version number.  Some PCBs may provide additional information, such maximum current specifications, etc.

> Note that components are not mounted on bottom since most PCB are setup for reflow soldering which can only be performed on side (top)

## Component Designators

Below are a list of industry standard component designators used for the project's PCB:

| Designator | Component                     | Examples  |
| ---------- | ----------------------------- | --------- |
| BR         | Bridge Rectifier              | BR1       |
| C          | Capacitor                     | C1, C1-C5 |
| D          | Diodes (includes LEDs)        | D1        |
| J          | Jack, Socket (male or female) | J1        |
| IR         | Infrared-Diode                | IR1       |
| JP         | Jumper (male pins)            | JP1       |
| L          | Inductor                      | L1        |
| OP         | Opto-isolator                 | OP1       |
| Q          | Transistor                    | Q1        |
| R          | Resistor                      | R1, R1-R5 |
| S, SW      | Switch                        | S1, SW1   |
| U          | IC                            | U1        |
| VR         | Voltage Regulator             | VR1       |
| Y          | Oscillator                    | Y1        |

## Reference

1. [Reference Designators (WikiPedia)](https://en.wikipedia.org/wiki/Reference_designator)
