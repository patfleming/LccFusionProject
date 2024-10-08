---
title: Power Module
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Card Assembly Guides
nav_order: 1
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
published: False
---
# Power Module Assembly Guide {#power_module_assembly}
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

In conjunction with the **LCC Fusion Project** the **Power Module** provides power to both the **LCC Fusion Node Card** and the **Node Bus Hub**.  The Power Module is inserted on top of the LCC Fusion Node Card, converting input power to 3V3, 5V and 12V for use by other LCC Fusion Project cards and breakout boards.

> When using multiple LCC Fusion Node Cards with in the same LCC Fusion Node Cluster (on the same Node Bus Hub), the Power Module must be added **only** to the **Primary LCC Fusion Node Card**.  Note that **Secondary LCC Fusion Node Card(s)** receive power via the Node Bus Hub.  Multiple Power Modules on the same Node Bus Hub may cause damage over time and is not recommended.

The Power Module accommodates several methods of connecting different types of power.   Refer to the [Planning for Node Power](/planning-node-power/) for descriptions of possible use cases and recommendations for supplying power to the LCC Fusion Node Card.

{% include terminology.html %}

## Specifications

Specifications for the Power Module include:

> Note that both Card LCC Fusion Node Cards and Power Modules are designed to accommodate the ratings below (i.e. both components and PCB traces).

| Characteristic                                               | Value  |
| ------------------------------------------------------------ | ------ |
| **Nodes:** Max number of secondary Nodes (assuming 100mA avg per Node, where load is ) | 30     |
| **Input**: Max supply voltage (limit of 25V capacitor C1)    | 20V    |
| **Input**: Max supply current via CAN Bus network cable (limited by network cable) | 600mA  |
| **Input**: Max supply current via ATX 5557, Spring/Screw Terminal Connector, or DC-005 connector | 3A     |
| **Input**: Max supply current USB-C connector (without 12V regulator, connector limit) | 2A     |
| **Output**: Max 3V3 output current (LM1117-3V3 regulator limitation) | 800mA  |
| **Output**: Max 5V output current (LM2596-5 regulator limitation) | 3A     |
| **Output**: Max 12V output current via LCC Fusion Node Bus Hub(L7812CV limit) | 1500mA |
| **Output**: Max output current to LCC Fusion Node Bus Hub                  | 3A     |
| **Output**: Max output current to ATX 5557 or Spring/Screw Terminal Connector | 3A     |
| **Output**: Max output current via USB-C                     | 2A     |

## How It Works

Power supply input is provided by one of the following:

1. CAN Network Bus cables connected to the LCC Fusion Node Card’s RJ45 CAN Bus connector.

2. ATX 5557 or Terminal Connector Power Input connector on the Power Module board.  Recommend using train layout accessory bus which is typically >12V.

3. USB-C Power Input connector on the Power Module board.  

   >  Recommend a laptop power supply with a USB-C connector with typically provide 18-20V and >3A (>65W) for less than $20 on 
   >
   >  [Amazon](https://www.amazon.com/s?k=power+supply+usb-c&crid=1QOTE1VH1B2IR&sprefix=power+supply+usb-c%2Caps%2C144&ref=nb_sb_noss_1).

### Mounting: 

- Module Module is connected to the top of the LCC Fusion Node Card using pin headers.
- PCB standoffs must be used and screwed in place.

### Power Supplied to LCC Fusion Node Card

The Power Module supplies power to the LCC Fusion Node Card and Node Bus Hub as follows:

1. The **PWR REG** selector allows the input power to converted to either 12V or have the regulator bypassed.  Use this if you want >12V for the LCC Fusion Node Bus Hubsince the selection sets the Node Bus Hub 12V line to either 12V or the power supply voltage.

1. When the PWR REG selection is set to 12V, the L7812CV linear positive voltage regulator IC converts the supply voltage to 12V for use by the Power Module and Node Bus Hub (via the LCC Fusion Node Card).

1. A **LM2596-5** switching voltage regulator supplies 5V power to the LCC Fusion Node Card.

1. A **LM1117-3V3** linear voltage regulator supplies 3.3V power to the LCC Fusion Node Card.

1. Circuit protect against reverse voltage is provide by diodes on each of the output line.

1. Circuit filter is provide for both input and output lines using capacitors.

### Protection

The Power Module ensures stable voltage regulation and protection against various electrical faults for the LCC Fusion Node Card. Below is an overview of each protection component integrated into the Power Module and its role:

| Protected Component         | Protection Component  | Function                                                     | Specifications                                            | Location                                         |
| --------------------------- | --------------------- | ------------------------------------------------------------ | --------------------------------------------------------- | ------------------------------------------------ |
| **Entire Module**           | **PPTC Polyfuse** | Protects from sustained overcurrent conditions by increasing resistance when the current exceeds 3A. Resets once the fault condition is cleared. | **Hold Current:** 3A<br>**Trip Current:** 6A              | In series with the incoming Vcc line             |
| **Entire Module**           | **TVS Diode SMBJ18A** | Protects from high-voltage transients by clamping voltage spikes, preventing them from reaching sensitive components. | **Stand-off Voltage:** 18V<br>**Clamping Voltage:** 29.2V | Across the incoming Vcc and GND lines            |
| **Input/Output Connectors** | **SS310 Diodes**      | Protect against reverse voltage by blocking current flow in the wrong direction. | **Reverse Voltage:** 100V<br>**Forward Current:** 3A      | In series with each input/output power connector |
| **LM2596-5 Regulator**      | **Input Capacitor**   | Filters out high-frequency noise and transient voltage spikes from the input power supply, ensuring stable voltage regulation. | **Value:** 680µF electrolytic                             | Across the input (Vcc) and GND                   |
| **LM2596-5 Regulator**      | **Output Capacitor**  | Filters out high-frequency noise and transient voltage spikes from the output, ensuring stable 5V regulation. | **Value:** 220 µF electrolytic                            | Across the output (5V) and GND                   |
| **L7812CV Regulator**       | **Input Capacitor**   | Filters out high-frequency noise and transient voltage spikes from the input power supply, ensuring stable voltage regulation. | **Value:** 0.33 µF ceramic                                | Across the input (Vcc) and GND                   |
| **L7812CV Regulator**       | **Output Capacitor**  | Filters out high-frequency noise and transient voltage spikes from the output, ensuring stable 12V regulation. | **Value:** 0.1 µF ceramic                                 | Across the output (12V) and GND                  |
| **Ground Bus**              | **48mil Ground Bus**  | Provides a low-resistance path for all protection components, ensuring effective grounding and noise suppression. | **Width:** 48 mil                                         | Used by all protection components                |

### Summary
These protection components work together to safeguard the Power Module from various electrical faults. The polyfuse provides overcurrent protection, the TVS diode clamps high-voltage spikes, and the SS310 diodes protect against reverse voltage. Decoupling capacitors filter out noise and transient voltage spikes, ensuring stable voltage regulation. The Power Module currently has capacitors installed for the LM2596-5 and L7812CV regulators, which help filter the input to the LM1117-3.3V regulator. It is still recommended to install the 2x 10µF capacitors for the LM1117-3.3V regulator to ensure optimal performance. Together, these components ensure the Power Module operates reliably, providing stable 12V, 5V, and 3.3V outputs to the LCC Fusion Node Card.

 ## Components List

PCB for the LCC Fusion Node Card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}Power_Module.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier | Component (Package)                                          | Required?                                             | Purpose                                                      |
| --------------- | ------------------------------------------------------------ | :----------------------------------------------------------- | --------------- |
| C1 | Polymer Solid, 680uF, 25V, SMD | Required | Used by 5V voltage regulator for input filtering. |
| C2 | Polymer Solid, 220uF, 25V, SMD | Required | Used by 5V voltage regulator for input filtering. |
| C3 | Ceramic Capacitor, 0.1uF, 1206 SMD | Required | Used by voltage regulators for output filtering. |
| C4 | Ceramic Capacitor, 33 uF, 1206 SMD | Optional | Used by 12V voltage regulator for input filtering. <br>Required when using 12 voltage regulator (Q1). |
| D1, D4, D5, D6 | SS310 Diode, SMD | Required | Circuit protection from reverse current from the |
| D2, D3 | SS310 Diodes, SMD | Optional | Circuit protection.<br>Required when providing power output (J3, J4, or J5). |
| D7 | SMBJ18A (SMB SMD) | Optional | Protects from high-voltage transients (>29V) |
| F1 | PPTC Polyfuse | Required | Protects from sustained overcurrent conditions (6A trip) |
| J1                  | 5557 ATX RA | Optional | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus network cable. |
| J2 | Spring / Screw 2.54mm Terminal Connector | Optional | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus network cable. |
| J3 | USB-C 4-Pin SMD Socket | Optional | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus network cable. |
| J4 | DC-005 Power Jack | Optional | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus network cable. |
| J5 | USB-C 4-Pin SMD Socket | Optional | Power output connector used to power other 12V+ devices. |
| J6 | Spring / Screw 2.54mm Terminal Connector | Optional | Power output connector used to power other 12V+ devices. |
| J7               | 5557 ATX RA     | Optional | Power output connector used to power other 12V+ devices. |
| J8 | 2-Pin female header | Optional | Power input from LCC Fusion Node Card CAN Bus network cable.  <br>Required when connecting power from CAN Bus network cable. |
| J9 | 4-pin female header | Required | Power output connect to LCC Fusion Node Card. |
| JP1                 | 3-Pin Male Pins                                       | Required | Used to select whether to regulate input voltage to 12V+ or bypass to use power supplied voltage. |
| L1 | Inductor 33uH | Required | Used for 5V voltage regulation. |
| VR1 | LM2596-5.0 IC | Required | 5V voltage regulator (buck) for ESP32 Module and LCC Fusion Node Bus Hub. |
| VR2 | L7812CV | Optional | 12V voltage regulator for LCC Fusion Node Bus Hub. |
| VR3 | LM1117-3V3 IC | Required | 3V3 voltage regulator for LCC Fusion Node Bus Hub. |
| SH1 | [Jumper Cap (2.54mm)](https://www.aliexpress.us/w/wholesale-jumper-caps.html?spm=a2g0o.detail.search.0) | Required | PWR REG selector for setting 12V bypass.  <br>Set to `Bypass` when **NOT** using the 12V power regulator. |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Assembly Instructions

<img src="/assets/images/pcbs/Node_Card/Power_Module_pcb.png" style="zoom:70%; float:right" />Below are the high level steps for assembly of the Output Card:

1. Determine component orientation:
   - Female headers and (ceramic) capacitor components are not polarized and can be installed in either direction.
   - Metal capacitors and diodes are polarized  and must be place in the corrector position.
   - IC’s must be aligned to the correct position using the indicators on the IC and the PCB (refer to  [Soldering Tips](/pcb-soldering/)).
2. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.
3. Use the Power Supply PCB stencil to apply the paste, align the stencil over the PCB using the 2 very small **Tooling Holes** located at the top and bottom of the card.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.
4. Apply soldering paste for all SMD components; 
   - Required:
     - Capacitors (C1, C2, C3, C4)
     - Diodes (D1, D2, D3, D4, D5, D6)
     - Regulators (VR1, VR3)
   - Optional:
     - 12V output (D2, D3)
     - 12V regulator circuit (D4 )
     - Power connectors (J2, J4)
5. Place SMD components into paste.  Note the orientation of each IC.
6. Reflow the solder for the SMD component (refer to  [Soldering Tips](/pcb-soldering/)).
7. Place PTH components (starting with the smaller components).
   1. Required Components:
      1.  Inductor (L1)
      2.  Capacitor (J8)
      3.  3-pin male pins for PWR REG (JP1)
      4.  4-pin female header for power connection to LCC Fusion Node Card (J9)
      5.  2-pin female header for power from LCC Fusion Node Card (J6)
   2. Optional Components:
      1. Power input / output (J1, J2, J3, J4, J5, J6, J7), ***optional when power is provided by LCC Fusion Node Card’s RJ45 CAN connection***
      1. 12V regulator circuit (VR2 )
>  See also: [Soldering Tips](/pcb-soldering/)

## Testing and Verification

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.

2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

3. **Component Orientation**: the IC's are correctly oriented according to the PCB silkscreen or schematic.

### Connectivity Testing

1. **Continuity Check**: Use a multimeter in continuity mode to check for shorts between power rails and ground, and to ensure there are no open circuits in critical connections.

### Power-Up Tests

1. Test the Power Module **before** connecting to a Power Node as follows:
   1. Supply >12V of power to each of the input power connections to be used (J1, J2, J3, and/or J6).  
   2. Set the PWR REG selector (JP1) to `Bypass`.
   3. Use a voltage meter to verify the  3V3 and 5V power at the PRIMARY NODE connector (J7).  
   4. When regulating to 12V, set the PWR REG to `12V` and test for 12V at the PRIMARY NODE connector (J7).  
   5. When providing 12V power to output connectors, test for power at the connectors (J4 and/or J5).
2. Connect the Power Module to a LCC Fusion Node Card and verify the voltages at the LCC Fusion Node Cards pads for the Node Bus Hub.
3. **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

1. Power the LCC Fusion Node Card with the Power Module.
1. Verify that the Node connects to the LCC Node network using an LCC Configuration Tool

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 


## Troubleshooting

- Reference the provided PCB diagrams while testing connections.
- Verify connections between pins using ohm meter.
- When regulated power is not detected, check for input voltage at each of the regulators.
- Test for a ground connection supply GND, output GND, and each of the IC GND pins.

