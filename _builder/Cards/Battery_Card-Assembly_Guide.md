---
title: Battery Card Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Card Assembly Guides
nav_order: 2
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
subjects:
  - Hardware
  - Assembly Guides
terms:
  # LCC Fusion Project Terms
  - can_network
  - lcc_fusion_cards
  - lcc_fusion_project
  - lcc_fusion_node_bus

  # LCC Fusion Connect Terms
  - lcc_fusion_node_card

  # NMRA LCC Network Terms
  # Model Railroad Automation Terms
  # Hardware and firmware Terms
  - bus
  - edge_card_connector
  - cleaning_pcb
  - component
  - current_limiting_resistor
  - decoupling_capacitor
  - esd_protection_diode
  - esp32_s3
  - ferrite_bead
  - jumper_caps
  - li_po_battery
  - low_voltage_detection
  - polyfuse
  - stencil
  - tvs_diode

---





# Battery Card Assembly Guide {#battery_card_assembly}
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

In conjunction with the **LCC Fusion** LCC Fusion Node Card and a Node Bus Hub, the **Battery Card** is a critical component for the LCC Fusion Project, designed to keep your LCC nodes powered and portable. This card ensures reliable operation of your layout control system by providing a stable, rechargeable power source.

### What It Is

The Battery Card utilizes a 3S Li-Po battery configuration, delivering a maximum output voltage of 12.6V and a capacity of 1000mAh. It features integrated protection circuits, including overcurrent, short circuit, and low voltage safeguards, ensuring both the battery and your devices remain safe during operation.

### When to Use It

Use the Battery Card to maintain continuous and portable power for your LCC nodes in the LCC Fusion Project. This is particularly beneficial when you need to:

- **Ensure Uninterrupted Power**: Keep LCC nodes running smoothly without relying on fixed power supplies.
- **Enhance Portability**: Make your LCC setup portable for demonstrations, testing, or temporary installations.
- **Utilize Rechargeable Convenience**: Easily recharge the battery via USB for repeated use.

### Key Features

- **Stable Voltage Supply**: Provides consistent power for LCC nodes and components.
- **Rechargeable**: USB charging capability for convenience and ease of use.
- **Comprehensive Protection**: Integrated overcurrent, short circuit, and low voltage protections.

### Applications in LCC Fusion Project

- **LCC Node Power Supply**: Reliable power for LCC nodes to ensure smooth operation.
- **Portable Layout Control**: Allows for the mobility of LCC nodes, ideal for demonstrations and temporary setups.
- **Rechargeable Solution**: Simplifies power management with easy recharging, enhancing the flexibility of your LCC system.

The Battery Card is an essential component for anyone looking to keep their LCC nodes powered and portable, ensuring the LCC Fusion Project operates efficiently and reliably in any setting.

{% include terminology.html %}

## Specifications

| Characteristic              | Value         |
| --------------------------- | ------------- |
| Min Output Voltage          | 9.0V          |
| Max Output Voltage          | 12.6V         |
| Max Output Capacity         | 1000mAh       |
| Typical Output Voltage      | 11.1V         |
| Max USB Input Voltage       | 6V            |
| Max USB Input Current       | 1A            |
| Recommended Charge Current  | 500mA         |
| Charge Termination Voltage  | 12.6V         |
| Operating Temperature Range | -20°C to 60°C |
| Storage Temperature Range   | -20°C to 45°C |
| Discharge Cut-off Voltage   | 9.0V          |
| Overcurrent Protection      | Yes           |
| Short Circuit Protection    | Yes           |

**Notes:**

- **Max Output Voltage**: This is the highest voltage provided by the fully charged 3S Li-Po battery.
- **Max Output Capacity**: This represents the battery capacity, which is 1000mAh.
- **Max USB Input Voltage**: The highest voltage that can be safely input through the USB for charging.
- **Max USB Input Current**: The maximum current allowed for charging the battery through the USB input.
- **Min Output Voltage**: The voltage at which the battery is considered fully discharged.
- **Typical Output Voltage**: The nominal voltage of the 3S battery pack.
- **Operating Temperature Range**: The range of temperatures in which the battery can safely operate.
- **Storage Temperature Range**: The recommended temperature range for storing the battery.
- **Charge Termination Voltage**: The voltage at which charging should be terminated to prevent overcharging.
- **Discharge Cut-off Voltage**: The voltage at which the device should stop discharging to prevent battery damage.
- **Recommended Charge Current**: The current recommended for charging to ensure battery longevity.
- **Overcurrent Protection**: Indicates whether the Battery Card has protection against excessive current.
- **Short Circuit Protection**: Indicates whether the Battery Card has protection against short circuits.

### How It Works

The Battery Card for the LCC Fusion Project integrates several key circuits to provide a stable, portable power source for LCC nodes:

1. **Battery Configuration**:
   
   - Utilizes a 3S Li-Po battery pack, delivering a maximum output voltage of 12.6V and a nominal voltage of 11.1V. The voltage drops to 9.0V when fully discharged.
   
2. **Voltage Regulation**:
   - The output from the battery is regulated to provide a consistent 12V supply. Smoothing capacitors (e.g., 220µF) filter noise and stabilize the DC output, ensuring a clean power supply for the LCC nodes.
   
3. **Charging Circuit**:
   - Based on the MCP73831 IC, the charging circuit manages the Li-Po battery charging via USB. The charging current is set by an external resistor connected to the PROG pin, ensuring safe and efficient charging.
   - **Programming Resistor (Rprog)**: Sets the charge current. For example, a 2kΩ resistor sets the charge current to 500mA.
   
4. **Protection Features**:
   
   - **Low Voltage Detection**: Uses an LM393 comparator and a 9V Zener diode to monitor the battery voltage. When the voltage drops below 9V, the comparator triggers an alert to prevent deep discharge.
   
5. **Low Voltage Detection Circuit**:
   - **Voltage Divider**: Scales down the battery voltage to a level suitable for the comparator input.
   - **Comparator (LM393)**: Compares the scaled voltage to a reference voltage (9V) generated by a Zener diode. If the battery voltage falls below 9V, the comparator output changes state, indicating a low battery condition.
   
6. **Integration with LCC Nodes**:
   
   The regulated output is connected via a JST plug directly to the **Power-CAN Card**, ensuring the LCC Fusion Node Cluster receives a stable 12V supply. This allows the nodes to function reliably without reliance on fixed power sources, enhancing portability and flexibility.
   
   When the Battery Card is installed in a **Node Bus Hub**, the batteries are automatically charged via the hub’s 5V connection. The batteries can be charged via a USB cable when the Battery Card is not installed in a LCC Fusion Node Bus Hub Hub.
   
### Protection

| Protected Component     | Protection Component              | Function                                                     | Specifications                                               | Location                                            |
| ----------------------- | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------- |
| **Entire Battery Card** | **Resettable Fuses**              | Protects from sustained overcurrent conditions by increasing resistance when the current exceeds 1.5A and 3A. Resets once the fault condition is cleared. | **Hold Current:** 1.5A and 3.5A                              | In series with the incoming Power line              |
| **Entire Battery Card** | **SS310 Diodes**                  | Protect against reverse voltage by blocking current flow in the wrong direction. | **Hold Current:** 1.5A and 3.5A                              | In series with the incoming Vcc line                |
| **Entire Audio Card**   | **TVS Diode SMBJ18A**             | Protects from high-voltage transients by clamping voltage spikes, preventing them from reaching sensitive components. | **Stand-off Voltage:** 18V **Clamping Voltage:** 29.2V       | Across the incoming Vcc and GND lines               |
| **Audio Amp**           | **Decoupling Capacitors**         | Filters out high-frequency noise and transient voltage spikes from the power supply, ensuring stable voltage to audio amp IC. | **Values:** 0.1 µF ceramic, 10 µF electrolytic or ceramic    | Across Vcc and GND near IC.                         |
| **I2C Lines**           | **Ferrite Bead BLM31PG121SN1L**   | Provides high-frequency noise suppression on the I2C lines.  | **Impedance:** 120 ohms at 100 MHz                           | In series with the SDA and SCL lines of the I2C bus |
| **I2C Lines**           | **ESD Protection Diode PESD1CAN** | Protects the I2C lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V **Clamping Voltage (Vc):** 40V | Across the SDA and SCL lines to GND                 |
| **Power Connections**   | **B240 Diodes**                   | Protect against reverse voltage by blocking current flow in the wrong direction. | **Reverse Voltage:** 100V **Forward Current:** 3A            | In series with battery and output connections.      |

## Components List

PCB for the card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}Audio Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram on right for reference):

| Component Identifier | Count | Type                      | Value             | Package                | Required | Purpose                                                  |
| -------------------- | ----- | ------------------------- | ----------------- | ---------------------- | -------- | -------------------------------------------------------- |
| BATT1, BATT2, BATT3  | 3     | Li-Po Battery             | 500mAh, 1000mAh   | 502535, 802540         | Required | Batteries for powering Node Bus Hub                      |
| C1, C2               | 2     | Capacitor                 | 1uF               | 1206 SMD               | Required | Filtering for the charging IC                            |
| D1                   | 1     | Zener Diode               | 9.1V              | 1206 SMD               | Required | Creates a reference voltage determining low battery      |
| D2, D4, D5           | 3     | Diode                     | B240              | SMA, SMD               | Required | Prevents reverse voltage                                 |
| D3                   | 1     | Diode                     | SMAJ5A            | SMB SMD                | Optional | Protects from high-voltage transients (>5V)              |
| D5                   | 1     | Diode                     | PESD1CAN          | SOT-23 SMD             | Optional | I2C data bus electrostatic discharge (ESD)               |
| F1                   | 1     | SK30 PPTC Resettable Fuse | 3A, 12V (or more) | PTH                    | Required | Protects from sustained overcurrent conditions           |
| J1, J2, J3, J4       | 4     | JST XH Socket             | 2P, 2.54mm        | PTH or Spring Terminal | Required | Battery Connections                                      |
| J5                   | 1     | USB-C Socket              | 4-Pin             | SMD                    | Optional | Power output connector used to power other 12V+ devices. |
| LED1                 | 1     | LED                       | Red               | 1206 SMD               | Optional | Low battery indicator (<9.1V)                            |
| LED2                 | 1     | LED                       | Green             | 1206 SMD               | Optional | Charging Indicator                                       |
| LED3                 | 1     | LED                       | Green             | 1206 SMD               | Optional | USB-C Power Indicator                                    |
| R1, R2               | 2     | Resistor                  | 47kΩ              | 1206 SMD               | Required | Voltage Divider for charging circuit input               |
| R3, R4               | 2     | Resistor                  | 10kΩ              | 1206 SMD               | Required | Voltage Divider for charging circuit input               |
| R5                   | 1     | Resistor                  | 1kΩ               | 1206 SMD               | Required | Current-Limiting for diode                               |
| R6, R11, R12         | 3     | Resistor                  | 1kΩ               | 1206 SMD               | Required | Current-Limiting for LEDs                                |
| R7                   | 1     | Resistor                  | 10kΩ              | 1206 SMD               | Required | Voltage Divider for transistor input                     |
| R8                   | 1     | Resistor                  | 47kΩ              | 1206 SMD               | Required | Voltage Divider for transistor input                     |
| R9                   | 1     | Resistor                  | 2kΩ               | 1206 SMD               | Required | Current-Limiting for charging rate                       |
| R10                  | 1     | Resistor                  | 10kΩ              | 1206 SMD               | Required | Current-Limiting for transistor input                    |
| U1                   | 1     | IC                        | LM393             | SO-8, SMD              | Required | Used for detecting low voltage (<9.1v)                   |
| U2                   | 1     | IC                        | MCP73831          | SOT23-5, SMD           | Required | Controls charging current to batteries                   |
| Q1                   | 1     | NPN Transistor            | BSS138            | SOT233, SMD            | Required | Switches output off while charging                       |
| Q2                   | 1     | PNP Transistor            | IRLML6402         | SOT233, SMD            | Required | Switches output off while charging                       |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

 <img src="/assets/images/pcbs/Battery_Card/Battery_Card_pcb.png" style="zoom:50%; float:right" />Below are the high level steps for assembly of the Audio Card:

>  See also: [Soldering Tips](/pcb-soldering/)

1. Position the card with the edge connector tabs facing down (see image on right).
2. When using a PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.
3. Install (3) Li-Po batteries
   1. use tie strap thru holes to hold in place
   2. connect batteries to connections (J1-J3)
4. Connect Battery Card output to Power-CAN Card
   1. Install a wired JST XH plug to the battery out connector (J4)
   2. plug into the **Power-CAN Card** battery JST XH connector (J13)

| Designator (value) | Component                     | Required? | Orientation                                                  |
| ------------------ | ----------------------------- | --------- | ------------------------------------------------------------ |
| C1, C2             | 1uF                           | Required  | None                                                         |
| D1                 | 9.1V Zener                    | Required  | Cathode end has a white line and positioned towards the left on the PCB. |
| D2, D4, D5         | B240                          | Required  | Cathode end has a white line and positioned towards the top of the PCB. |
| D3                 | SMAJ5A                        | Optional  | Cathode end has a white line and positioned towards the right side of the PCB. |
| D5                 | PESD1CAN                      | Optional  | None                                                         |
| F1                 | Fuse                          | Required  | None                                                         |
| J1, J2, J3, J4     | JST XH, or Terminal Connector | Required  | None                                                         |
| J5                 | USB-C Socket                  | Optional  | None                                                         |
| LED1 - LED3        | Red, Green LED                | Optional  | Reference back of LED, cathode positions downward on the PCB.<img src="/_builder/Cards/images/LED_Orientation.png" style="zoom: 15%; float: right;" /> |
| R1, R2             | 47k&Omega;                    | Required  | None                                                         |
| R3, R4, R7, R10    | 10k&Omega;                    | Required  | None                                                         |
| R5, R6, R11, R12   | 1k&Omega;                     | Required  | None                                                         |
| R9                 | 2k&Omega;                     | Required  | None                                                         |
| U1                 | LM393                         | Required  | Small dot (pin 1) positioned to upper right corner           |
| U2                 | MCP73831                      | Required  | None                                                         |
| Q1                 | BSS138                        | Required  | None                                                         |
| Q2                 | IRLM6402                      | Required  | None                                                         |

## Testing and Verification

The following test and verifications of the card should be performed after a through inspection of the card's soldering.  Check all of the PTH component pins and SMD pads.  Make sure there are no solder bridges between pins and pads.

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.
2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.
3. **Component Orientation**: the IC's are correctly oriented according to the PCB silkscreen or schematic.

### Connectivity Testing

1. **Continuity Check**: Use a multimeter in continuity mode to check for shorts between power rails and ground, and to ensure there are no open circuits in critical connections.

### Power-Up Tests

1. Charge the batteries

   1. Connect a 5V USB-C charging cord to the **Battery Card**’s `CHARGE IN` USB-C socket (J5) charging port and verify that USB Power LED is ON.  
   2. Insert the **Battery Card** into a **powered** Node Hub

   > If the batteries need charging, then the charging LED should also be ON with either of these power connections.

2. After the batteries are charged:

   1. Disconnect all input power

   2. Verify the output voltage at `BATT OUT` (J4) is > 9V.

      > `BATT OUT` provides voltage only when there is **NO** input power to the Battery Card


### Functional Testing

1. Insert the **Battery Card** into a **Node Bus Hub**
2. Verify that the **Battery Card**’s `LOW BATT` LED is not ON.
3. Insert a **Power-CAN Card** into the same **Node Bus Hub**.
4. Connect the **Battery Card**’s output plug into the **Power-CAN Card**’s `BATT IN` JST XH socket.
5. Insert an **SuperMini LCC Fusion Node Card** into same Node Bus Hub
6. Disconnect the power to the **Power-CAN Card**
7. Verify the **SuperMini LCC Fusion Node Card**’s ESP32 board’s power light is still ON, indicating that it is running (on battery power)

## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

1. [Choosing the Right Resistor for LEDs](/led-card-usage-guide/).

