---
title: Power-CAN Card Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Card Assembly Guides
nav_order: 1
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_cards
  - lcc_fusion_project
  - lcc_fusion_node_bus

  # LCC Fusion Connect Terms
  - lcc_fusion_node_card
  - lcc_fusion_io_cards
  - hw_communications_address
  - hw_communications_bus

  # NMRA LCC Network Terms
  # Model Railroad Automation Terms
  # Hardware and firmware Terms
  - bus
  - can_network
  - can_termination
  - cleaning_pcb
  - component
  - decoupling_capacitor
  - edge_card_connector
  - esp32_s3
  - jumper_caps
  - i2c
  - i2c_bus
  - network_cable
  - polyfuse
  - stencil

---

# Power-CAN Card Assembly Guide {#power-can_card_assembly}

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

In conjunction with the **LCC Fusion Project** the **Power-CAN** provides both power and CAN Networking to the **Node Bus Hub**.  The Power-CAN Card is inserted into the Node Bus Hub:

- providing 3V3, 5V and 12V for use by other LCC Fusion Project Nodes and breakout cards
- connecting wired CAN Network connections for LCC Fusion Project Nodes

> One Power-CAN Card is required per Node Bus Hub for providing the required power.  Multiple Power-CAN Cards per Node Bus Hub is not supported.

The Power-CAN Card accommodates several methods of connecting different types of power.   Refer to the [Planning for Node Power](/planning-node-power/) for descriptions of possible use cases and recommendations for supplying power to the LCC Fusion Node Card.

{% include terminology.html %}

## Specifications

Specifications for the Power-CAN Card include:

> Note that Power-CAN Card are designed to accommodate the ratings below (i.e. both components and PCB traces).

| Characteristic                                               | Value |
| ------------------------------------------------------------ | ----- |
| **Nodes:** Max number of Nodes (assuming 100mA avg per Node, where load is ) | 30    |
| **Input**: Max supply voltage (limit of 25V capacitor C1)    | 20V   |
| **Input**: Max supply current via CAN Bus network cable (limited by network cable’s 2 power wires) | 1.2A  |
| **Input**: Max supply current via ATX 5557, Spring/Screw Terminal Connector, or DC-005 connector | 3A    |
| **Input**: Max supply current USB-C connector (without 12V regulator, connector limit) | 2A    |
| **Output**: Max 3V3 output current (LM1117-3V3 regulator limitation) | 800mA |
| **Output**: Max 5V output current (LM2596-5 regulator limitation) | 3A    |
| **Output**: Max 12V output current via LCC Fusion Node Bus Hub(L7812CV limit) | 1.5A  |
| **Output**: Max output current to LCC Fusion Node Bus Hub| 3A    |
| **Output**: Max output current to ATX 5557 or Spring/Screw Terminal Connector | 3A    |
| **Output**: Max output current via USB-C                     | 2A    |

## How It Works

Power supply input is provided by one of the following connectors:

1. RJ45 socket(s) connected to network cable (typically wired for both CAN Network and power as follows:

| Wire # | Wire Color          | Function         |
| ------ | ------------------- | ---------------- |
| 1      | White/Orange Stripe | CAN High (CAN H) |
| 2      | Orange              | CAN Low (CAN L)  |
| 3      | White/Green Stripe  | Power (V+)       |
| 4      | Blue                | Ground (GND)     |
| 5      | White/Blue Stripe   | Undefined        |
| 6      | Green               | Undefined        |
| 7      | White/Brown Stripe  | Power (V+)       |
| 8      | Brown               | Ground (GND)     |

3. ATX 5557 or Terminal Connector Power Input connectors on the Power-CAN Card.  Recommend using train layout accessory bus which is typically >12V.

4. USB-C Power Input connector on the Power-CAN Card.  

   >  Recommend a laptop power supply with a USB-C connector with typically provide 18-20V and >3A (>65W) for less than $20 on 
   >
   >  [Amazon](https://www.amazon.com/s?k=power+supply+usb-c&crid=1QOTE1VH1B2IR&sprefix=power+supply+usb-c%2Caps%2C144&ref=nb_sb_noss_1).

#### Power Supplied to Node Bus Hub

The Power-CAN supplies power to the Node Bus Hub as follows:

1. The **PWR REG** selector allows the input power to converted to either 12V or have the regulator bypassed.  Use this if you want >12V for the LCC Fusion Node Bus Hubsince the selection sets the Node Bus Hub 12V line to either 12V or the power supply voltage.

1. When the PWR REG selection is set to 12V, the L7812CV linear positive voltage regulator IC converts the supply voltage to 12V for use by the both the Power-CAN Card and the Node Bus Hub.

1. A **LM2596-5** switching voltage regulator supplies 5V power to the Node Bus Hub.

1. A **LM1117-3V3** linear voltage regulator supplies 3.3V power to the Node Bus Hub.

1. Current overload is provided by two resettable fuses.

1. Circuit protect against reverse voltage is provide by diodes on each of the output line.

1. Circuit filter is provide for both input and output lines using capacitors.

### Protection

The Power-CAN Card ensures stable voltage regulation and protection against various electrical faults for the LCC Fusion Node Card. Below is an overview of each protection component integrated into the Power-CAN Card and its role:

| Protected Component         | Protection Component             | Function                                                     | Specifications                                               | Location                                            |
| --------------------------- | -------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------- |
| **Entire Power-CAN Card**   | **Fast Blow Fuse**               | Protects from current overflow                               | **Hold Current:** 3A                                         | In series with the incoming Vcc line                |
| **Entire Power-CAN Card**   | **Resettable Fuses**             | Protects from sustained overcurrent conditions by increasing resistance when the 3V3 or 5V current exceeds 1.5A. Resets once the fault condition is cleared. | **Hold Current:** 1.5A                                       | In series with the 5V, 3V3 output lines             |
| **Entire Power-CAN Card**   | **TVS Diode SMBJ18A**            | Protects from high-voltage transients by clamping voltage spikes, preventing them from reaching sensitive components. | **Stand-off Voltage:** 18V<br>**Clamping Voltage:** 29.2V    | Across the incoming Vcc and GND lines               |
| **Input/Output Connectors** | **SS310 Diodes**                 | Protect against reverse voltage by blocking current flow in the wrong direction. | **Reverse Voltage:** 100V<br>**Forward Current:** 3A         | In series with each input/output power connector    |
| **CAN Connection**          | **PESD1CAN Diodes**              | Protect against ESD (Electrostatic Discharge) from the CAN network lines | **Reverse Stand-off Voltage (Vr):** 24V<br/>**Clamping Voltage (Vc):** 40V | Across each I2C (CAN-H, CAN-L) input line and GND   |
| **CAN Connection**          | **BLM31PG121SN1L Ferrite Beads** | CAN Network Bus Data Line Noise Suppression Ferrite Bead     |                                                              | In series with the CAN network lines (CAN-H, CAN-L) |
| **LM2596-5 Regulator**      | **Input Capacitor**              | Filters out high-frequency noise and transient voltage spikes from the input power supply, ensuring stable voltage regulation. | **Value:** 680µF electrolytic                                | Across the input (Vcc) and GND                      |
| **LM2596-5 Regulator**      | **Output Capacitor**             | Filters out high-frequency noise and transient voltage spikes from the output, ensuring stable 5V regulation. | **Value:** 220 µF electrolytic                               | Across the output (5V) and GND                      |
| **L7812CV Regulator**       | **Input Capacitor**              | Filters out high-frequency noise and transient voltage spikes from the input power supply, ensuring stable voltage regulation. | **Value:** 0.33 µF ceramic                                   | Across the input (Vcc) and GND                      |
| **L7812CV Regulator**       | **Output Capacitor**             | Filters out high-frequency noise and transient voltage spikes from the output, ensuring stable 12V regulation. | **Value:** 0.1 µF ceramic                                    | Across the output (12V) and GND                     |
| **Ground Bus**              | **48mil Ground Bus**             | Provides a low-resistance path for all protection components, ensuring effective grounding and noise suppression. | **Width:** 48 mil                                            | Used by all protection components                   |

### Summary

These protection components work together to safeguard the Power-CAN Card from various electrical faults. The polyfuse provides overcurrent protection, the TVS diode clamps high-voltage spikes, and the SS310 diodes protect against reverse voltage. Decoupling capacitors filter out noi/se and transient voltage spikes, ensuring stable voltage regulation. The Power-CAN Card currently has capacitors installed for the LM2596-5 and L7812CV regulators, which help filter the input to the LM1117-3.3V regulator. It is still recommended to install the 2x 10µF capacitors for the LM1117-3.3V regulator to ensure optimal performance. Together, these components ensure the Power-CAN Card operates reliably, providing stable 12V, 5V, and 3.3V outputs to the LCC Fusion Node Card.

 ## Components List

PCB for the Power-CAN Card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}Power-CAN_Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

| Component Identifier | Count | Type                    | Value           | Package         | Required?                                                    | Purpose                                                      |
| -------------------- | ----- | ----------------------- | --------------- | --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| C1                   | 1     | Polymer Solid Capacitor | 680uF, 10V      | 6x12mm, PTH     | Required                                                     | Used by 5V voltage regulator for input filtering             |
| C2                   | 1     | Polymer Solid Capacitor | 220µF, 10V      | 6.3x5.8mm , SMD | Required                                                     | Used by 5V voltage regulator for input filtering             |
| C3                   | 1     | Ceramic Capacitor       | 0.1uF           | 1206 SMD        | Optional                                                     | Used by 12V voltage regulator for input filtering (Required when using 12V voltage regulator (Q1)) |
| C4                   | 1     | Ceramic Capacitor       | 0.33uF Tantalum | 3216 SMD        | Optional                                                     | Used by 12V voltage regulator for input filtering (Required when using 12V voltage regulator (VR1)) |
| D1 - D4              | 4     | Diode                   | SS310           | SMD             | Optional                                                     | Circuit protection (Required when providing power input (J1, J2, J3, or J4)) |
| D5                   | 1     | TVS Diode                   | SMBJ18A         | SMB SMD         | Optional                                                     | Protects from high-voltage transients (>29V)                 |
| D6                   | 1     | Diode                   | SS310           | SMD             | Required                                                     | Required by LM2596                                           |
| D7, D11, D12         | 3     | Diode                   | SS310           | SMD             | Required                                                     | Circuit protection for reverse voltage from the LCC Fusion Node Bus Hub |
| D8, D9               | 2     | Diode                   | SS310           | SMD             | Required                                                     | Circuit protection from reverse current from the output lines |
| D10                  | 1     | Diode                   | SS310           | SMD             | Optional                                                     | Circuit protection (Required when providing input power from CAN (J8 or J9)) |
| D13, D14             | 2     | Diode                   | ESD PESD1CAN        | SOT-23 SMD      | Required                                                     | I2C data bus electrostatic discharge (ESD) protection        |
| FH1                  | 1     | Fuse Holder             | 1808 (/w 3A)    | n/a             | Optional when bypassed (JP2)                                 | Protects from sustained overcurrent conditions               |
| F1                   | 1     | Resettable Fuse         | 1.5A            | 1206 SMD        | Required                                                     | Protects from sustained overcurrent conditions               |
| FB1, FB2             | 2     | Ferrite Bead            | BLM31PG121SN1L  | 1206 SMD        | Required                                                     | CAN Network Bus Data Line Noise Suppression Ferrite Bead     |
| J1                   | 1     | Connector               | 5557 ATX RA     | PTH             | Optional                                                     | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus cable |
| J2                   | 1     | Connector               | Spring/Screw    | 2.54mm pitch    | Optional                                                     | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus cable |
| J3                   | 1     | Connector               | USB-C Socket    | 4-Pin SMD       | Optional                                                     | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus cable |
| J4                   | 1     | Connector               | Power Jack      | DC-005          | Optional                                                     | Power input connector to power the LCC Fusion Node Card when power is **not** being supplied via the CAN Network Bus cable |
| J5                   | 1     | Connector               | USB-C Socket    | 4-Pin SMD       | Optional                                                     | Power output connector used to power other 12V+ devices      |
| J6                   | 2     | Connector               | Spring/Screw    | 2.54mm pitch    | Optional                                                     | Power output connector used to power other 12V+ devices      |
| J7                   | 1     | Connector               | 5557 ATX RA     | PTH             | Optional                                                     | Power output connector used to power other 12V+ devices      |
| J8, J9               | 2     | RJ45 Socket             | 8P8C            | PTH             | Optional                                                     | Network cable connector for Power and CAN. See notes above for required cable wiring |
| J10, J11             | 4     | Spring/Screw            | 2.54mm pitch    | Optional        | CAN Network connection for use with CANable Module, or direct wiring |                                                              |
| J12                  | 3     | Spring/Screw            | 2.54mm pitch    | Optional        | CAN Network connection for use with CANable Module, or direct wiring |                                                              |
| J13                  | 1     | JST XH Socket           | 2P, 2.54mm      | Optional        | Battery connection from Battery Card                         |                                                              |
| JP1                  | 1     | Male Header             | 3-Pin, 2.54mm   | PTH             | Required                                                     | Used to select whether to regulate input voltage to 12V+ or bypass to use power supplied voltage |
| JP2                  | 1     | Male Header             | 2-Pin, 2.54mm   | PTH             | Optional                                                     | Used to bypass the inline 3A fast blow fuse (FH1)            |
| L1                   | 1     | Inductor                | 33uH            | PTH             | Required                                                     | Used for 5V voltage regulation                               |
| R1, R2               | 2     | Resistor                | 750Ω            | 1206 SMD        | Optional                                                     | Required when using a CAN Adapter. Limits current to optocoupler (LEDs). Use 750Ω to limit current to 5mA |
| U1, U2               | 2     | Optocoupler             | 6N137           | DIP8 PTH        | Optional                                                     | Required when using a CAN Adapter to provide Windows protection from the CAN network |
| VR1                  | 1     | Voltage Regulator       | L7812CV         | TO-220 PTH      | Optional                                                     | 12V voltage regulator for LCC Fusion Node Bus Hub            |
| VR2                  | 1     | Voltage Regulator       | LM2596-5.0      | TO-263 KTT, SMD | Required                                                     | 5V voltage regulator (buck) for ESP32 Development Board and Node Bus Hub |
| VR3                  | 1     | Voltage Regulator       | LM1117-3V3      | SMD             | Required                                                     | 3V3 voltage regulator for Node Bus Hub                       |
| SH1                  | 1     | Jumper Cap              | 2.54mm pitch    | N/A             | Required                                                     | PWR REG selector for setting 12V bypass. Set to `Bypass` when **NOT** using the 12V power regulator |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

Below are the high level steps for assembly of the Output Card:

1. Determine component orientation:

   - Female headers and (ceramic) capacitor components are not polarized and can be installed in either direction.
   - Metal capacitors and diodes are polarized  and must be place in the corrector position.
   - IC’s must be aligned to the correct position using the indicators on the IC and the PCB (refer to  [Soldering Tips](/pcb-soldering/)).

2. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

3. Use the Power Supply PCB stencil to apply the paste, align the stencil over the PCB using the 2 very small **Tooling Holes** located at the top and bottom of the card.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

   <div style="text-align: center;">
     <img src="/assets/images/pcbs/Power-CAN_Card/Power-CAN_Card_pcb.png" style="zoom:50%;" />
   </div>


   ### Solder SMD Components

   >  Reference the PCB’s diagram above. 
   >
   >  **Note** To enlarge the image for better viewing or printing, from a web browser either zoom in (cntl + ), or right click on the image above and open in a new tab, then left click to enlarge the image.

   1. Apply soldering paste for all SMD components; 
   2. Place SMD components into paste.  Refere to table for whether components are required and their orientation.
   3. Reflow the solder for the SMD component (refer to  [Soldering Tips](/pcb-soldering/)).


| Designator (value)            | Required?                                                    | Orientation                                                  |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| C1 (680uF)                    | Yes                                                          | Anode positioned toward PCB **top** edge                         |
| C2 (220uF)                    | Yes                                                          | Anode positioned toward PCB **top** edge                         |
| C3 (0.33uF)                   | Yes                                                          | Cathode end has a brown line and positioned towards PCB **bottom** edge |
| C4 (0.1uF)                    | When using VR1                                               | None                                                         |
| D1-D4, D9, D10 (SS310 )       | When NOT using CAT network cable for power.                  | Anode towards top of board                                   |
| D5 (SMBJ18A)                  | Yes                                                          | Anode positioned toward PCB **top** edge                         |
| D6, D7, D8, D11, D12 (SS310 ) | Yes                                                          | Cathode end has a white line and positioned towards PCB **bottom** edge |
| D13, D14 (PESD1CAN )          | Yes                                                          | Fits only one way                                            |
| FH1 (Fuse Holder /w 3A)       | Optional                                                     | None                                                         |
| F1 (Resettable Fuse, 3.5A)    | Yes                                                          | None                                                         |
| FB1, FB2                      | Yes                                                          | None                                                         |
| J3, J5 (USB-C Socket)         | When using USB cables for power input (J3) or power output (J5) | Connection towards top of board                              |
| VR2 (LM2596-5.0)              | Yes                                                          | Fits only one way                                            |
| VR3 (LM1117-3V3 IC)           | Yes                                                          | Fits only one way                                            |

### Solder PTH Components

>  Reference the PCB’s diagram above. 
>
>  **Note** To enlarge the image for better viewing or printing, from a web browser either zoom in (cntl + ), or right click on the image above and open in a new tab, then left click to enlarge the image.

Place PTH components (starting with the smaller components).

> See also: [Soldering Tips](/pcb-soldering/)

| Designator                                                   | Required?                                           | Orientation                                |
| ------------------------------------------------------------ | --------------------------------------------------- | ------------------------------------------ |
| J1 (5557 ATX RA), <br>J2 (Spring / Screw Terminal Connector), <br>J4 ( DC-005) | When not using other power inputs (J3, J8, or J9)   | GND pin is marked on board with square pad |
| J6, (Spring / Screw Terminal Connector), <br/> J7 (5557 ATX RA) | When using power ouput                              | GND pin is marked on board with square pad |
| J8, J9 (RJ45 socket)                                         | When power or CAN is provided vit CAT network cable | Fits only one way                          |
| J10, J11, J12 (Spring / Screw Terminal Connector)            | When using CANable USB to CAN adapter               | GND pin is marked on board with square pad |
| J13 (JST XH Socket )                                         | When using **Battery Card**                         | GND pin towards top of board               |
| JP1 (3-Pin Male Header)                                      | Yes                                                 | None                                       |
| JP2 (2-Pin Male Header)                                      | Optional (use when bypassing 3A fuse)               | None                                       |
| L1 ( 33uH )                                                  | Yes                                                 | None                                       |
| U1, U2 (6N137 )                                              | When using CANable USB to CAN adapter               | Yes                                        |
| VR1 (L7812CV )                                               | When regulating 12V output                          | Heat sink towards top of board             |


## Testing and Verification

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.

2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

3. **Component Orientation**: the IC's are correctly oriented according to the PCB silkscreen or schematic.

### Connectivity Testing

1. **Continuity Check**: Use a multimeter in continuity mode to check for shorts between power rails and ground, and to ensure there are no open circuits in critical connections.

### Power-Up Tests

1. Test the Power=CAN Card **before** connecting to a Power Node as follows:
   1. Supply >12V of power to each of the input power connections to be used (J1, J2, J3, and/or J6).  
   2. Set the PWR REG selector (JP1) to `Bypass`.
   3. Use a voltage meter to verify the  3V3 and 5V power at the PRIMARY NODE connector (J7).  
   4. When regulating to 12V, set the PWR REG to `12V` and test for 12V at the PRIMARY NODE connector (J7).  
   5. When providing 12V power to output connectors, test for power at the connectors (J4 and/or J5).
2. **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

1. Power the LCC Fusion Node Card with the Power-CAN Card.
1. Verify that the Node connects to the LCC Node network using an LCC Configuration Tool


## Troubleshooting

- Reference the provided PCB diagrams while testing connections.
- Verify connections between pins using ohm meter.
- When regulated power is not detected, check for input voltage at each of the regulators.
- Test for a ground connection supply GND, output GND, and each of the IC GND pins.

