---
title: Node Bus Hub Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Breakout Board Assembly Guides
nav_order: 1
use_cases:
  - Node Cluster Setup
  - PCB Design & Assembly
subjects:
  - Assembly Guides
  - Hardware
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_node_bus
  - lcc_fusion_cards
  # LCC Fusion Connect Terms
  - lcc_fusion_io_cards
  - lcc_fusion_node_card
  # Hardware and firmware Terms
  - bus
  - cleaning_pcb
  - edge_card_connector
  - jumper_caps
  - network_cable
  - pull_up_resistor
---
# Node Bus Hub Assembly Guide {#node_bus_hub_assembly}
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
The **Node Bus Hub** is a PCB whose primary function is to serve as a backbone for connecting the project's LCC LCC Fusion Node Card with multiple **I/O Cards** (PCBs), allowing them to communicate with each other and work as a unified system. This setup is commonly found in computers, servers, telecommunications equipment, and other electronic systems where modularity and scalability are important.

### Hub Connectors

<img src="{{ site.baseurl }}/assets/images/connectors/Edge_Card_Connector.png" style="zoom:25%;float:right" />All Node Bus Hub PCBs contain one or more **Edge Card Connectors** used to hold the cards in place and provide connectivity to the **LCC Fusion Node Bus Hub**, a set of 12 contacts providing power (GND, 3V3, 5V, 12+V) and communications ( I2C, CAN, and DCC).  Below is the layout of the LCC Fusion Node Bus Hubconnection pabs (left to right, refer to picture on the right):

| **PCB Layer**  | **1** | **2** | **3** | **4** | **5** | **6** |
| ---------- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Top**    | 3V3   | 5V    | 12V   | GND   | SDA0  | SCL0  |
| **Bottom** | SCL1  | SDA1  | CAN-H | CAN-L | DCC1  | DCC2  |

### Hub Expansion

Optionally, Node Bus Hub can provide additional connections for expansion with additional Node Bus Hub as follows (e.g. 6x Hub);

- For connecting to a **remote** Node Bus Hub, network cables (CAT5/6) RJ45 sockets may be provided allowing for daisy chaining over any distance.
- For **direct** connections to adjoining Node Bus Hub(s), sets of connections may be provided on the edges.  

### Hub Expansion Options

| Option                                  | Description                                                  | Advantages                                                   | Disadvantages                                                |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Board-to-Board Connectors (Headers)** | Use headers to connect adjacent hubs directly.               | Secure mechanical and electrical connection; minimal additional components; vertical and horizontal Hub arrangements; No Hub cables required | Limited flexibility in positioning; requires larger foot print |
| **Network Cables**                      | Use standard network cables (e.g., Ethernet cables) to connect hubs. | Flexible positioning; easy to extend the network; uses common cables for communications and power | Requires cabling between Hubs                                |
| **WiFi**                                | Utilize the LCC Fusion I/O Controller Card to provide inter-Hub connections. | No cabling between Hubs; Easy repositioning of Hubs          | Requires an I/O Controller Card and use of one Hub connector; Potential issues with signal range and interference; requires power to the Hub via the I/O Controller Card. |
| **Hybrid Approach**                     | Combine board-to-board connections for nearby hubs and network cables or wireless connections for distant ones. | Balances the stability of wired connections with the flexibility of wireless | Complexity in managing different connection types; potential for signal integrity issues |
| **Modular Network Design**              | Design your hub assemblies to support modular network connections, allowing for easy reconfiguration. | High flexibility and scalability; future-proofing            | Initial design complexity; potential for higher cost         |

{% include terminology.html %}

## Specifications

Specifications for the Node Bus Hub include:

| Characteristic                     | Value        |
| ---------------------------------- | ------------ |
| Max Cards                          | 6            |
| Min Input                          | 1700mA       |
| Input / Output                     | 3V3, 5V, 12V |
| Max Input                          | 35V          |
| Hardware Communication Buses (I2C) | 2            |
| CAN (Controller Area Network)      | 1            |
| DCC (Digital Command Control)      | 1            |
| Expansion Board Connectors         | 4            |

- Power connections for 3V3, 5V, 12V.
- MAX current 1.7A (based on 24 mil trace width, 1oz)
- MAX connectors; 6 (6x Node Bus Hub), 2 (2x Node Bus Hub)
- Indicators (6x Node Bus Hub); 5V (red), I2C data transmit (GRN), I2C data receive (RED)

### How It Works

The **LCC Fusion Project's Node Bus Hub** is a versatile PCB designed to streamline the connection and management of multiple LCC (Layout Command Control) devices in a model railroad automation setup. Here’s a detailed overview of its features and functionality:

- **Card Edge Connectors:** The Node Bus Hub is equipped with up to 6x 805 card edge 2x6 connectors. These connectors provide parallel connections for multiple critical signals and power lines, including:
  - **3.3V**
  - **5V**
  - **12V**
  - **CAN (Controller Area Network)**
  - **Two I2C (Inter-Integrated Circuit) buses**
  - **DCC (Digital Command Control)**

- **RJ45 Sockets and Pin Headers:** The PCB includes RJ45 sockets and pin headers that allow for easy interconnection of multiple hubs, enabling flexible expansion and connectivity between different parts of the layout.

- **LED Indicators:** The hub features LED indicators for monitoring the I2C bus status. These LEDs provide visual feedback on SDA (Serial Data Line) transfer activity, helping users quickly identify any communication issues.

- **BSS138 Transistor:** A BSS138 MOSFET transistor is integrated into the circuit, assisting with I2C bus communication and particularly with LED status indication. This component ensures reliable signal level shifting and smooth operation of the I2C buses.

- **USB-C Power Option:** For testing purposes without a Power-CAN Card, the Node Bus Hub can be powered via a 5V USB-C connection. This feature includes a power indicator LED and reverse flow protection to prevent any potential damage from incorrect power flow.

- **Communication Protection:** To protect the communication lines, the Node Bus Hub utilizes PESD1CAN protection devices for both I2C buses and the CAN network. These components help safeguard the hub and connected devices from electrostatic discharge (ESD) and other transient voltage spikes.

#### Automatic I2C Line Conditioning

  The **LCC Fusion Node Bus Hub** automatically adjusts I2C line conditioning to ensure robust communication across all connected devices. This feature dynamically engages pullup resistors only when the signal integrity of the I2C lines (SDA and SCL) drops below an acceptable threshold, ensuring clean data signals over longer distances or when multiple devices are connected.

  The I2C line conditioning circuit monitors the voltage levels on the SDA and SCL lines using an **LM393 comparator** and a **PNP transistor (IRLML6402)** to control the engagement of pullup resistors:

  1. **Voltage Monitoring**: 
     - The SDA and SCL lines are continuously monitored by the **LM393 comparator**. The voltage levels are compared against a reference voltage of **2.4V** generated by a **Zener diode**. 
     - If the voltage on the I2C line falls below this threshold, the comparator output triggers the pullup resistors.

  2. **Dynamic Pullup Activation**:
     - When the comparator detects a weak signal, its **output pin** (Pin 1) controls the **base** of the PNP transistor, allowing current to flow through the **emitter** (connected to 3.3V) and **collector** (connected to the SDA or SCL lines through a 2.7kΩ resistor).
     - This action dynamically enables the pullup resistors, boosting the I2C line signal and restoring proper voltage levels.

  3. **Low-Pass Filtering**:
     - A **low-pass filter** (resistor and capacitor) is integrated into the circuit to prevent high-frequency noise from triggering false pullups. This filter ensures that only valid signal drops, such as those caused by long cable runs or multiple devices, are corrected.

  4. **I2C Line Stability**:
     - The circuit is designed to stabilize the I2C lines only when needed, preventing unnecessary pullups that could overload the bus. This method ensures that the I2C communication remains clean without risking excessive pullups, which can affect performance.
     
  5. **Dual I2C Support**:
     - For systems with multiple I2C lines (e.g., two separate I2C buses), each bus has its own monitoring and conditioning circuit, using a separate LM393 comparator, Zener diode, and pullup resistors. This setup ensures that both sets of I2C lines are independently monitored and conditioned as necessary.

  By using this automatic pullup mechanism, the **LCC Fusion Node Bus Hub** ensures optimal performance even in complex layouts with multiple devices and long cable runs, enhancing the reliability of the I2C communication across the network. 

### Connectors

The purpose of the **Node Bus Hub** and its connectors is to facilitate quick and easy connections between the LCC Fusion cards. For setups with requiring expansion, the Node Bus Hub provides connections to additional hubs.

| Component Designator       | **Connector  Label** | Connector Type      | **Connection Number** | **Description**                                              |
| -------------------------- | -------------------- | ------------------- | --------------------- | ------------------------------------------------------------ |
| **J1, J2, J3, J4, J5, J6** | CARD-1 to CARD-6     | Card Edge Connector | 1 - 6                 | Connection to LCC Fusion Cards                               |
| **J7, J8, J11, J12**       | NODE BUS             | Female Header       | n/a                   | Connection to another Node Bus Hub using pin headers         |
| **J9, J10**                | NODE BUS             | RJ45 Socket         | 1/2, 3/4, 5/6, 7/8    | Each pin pair connects between blocks 1 thru 4 for detection of current (  BOD Card) or low voltage (  BLVD Card) |
| **J6**                     | TEST BOARD           | Card Edge           | 1, 2, 3, 4, COM       | Connection to Test Board for connections to the test board track |

### Protection

| **Protected Component**         | **Protection Component**            | **Function**                                                 | **Specifications**                                           | **Location**                                           |
| ------------------------------- | ----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------ |
| **I2C Connection**              | **PESD1CAN Diodes**                 | Protect against ESD (Electrostatic Discharge) from the CAN network lines | **Reverse Stand-off Voltage (Vr):** 24V<br/>**Clamping Voltage (Vc):** 40V | Across each I2C line (SDA, SCL) input line and GND     |
| **CAN Connection**              | **PESD1CAN Diodes**                 | Protect against ESD (Electrostatic Discharge) from the CAN network lines | **Reverse Stand-off Voltage (Vr):** 24V<br/>**Clamping Voltage (Vc):** 40V | Across each CAN line (CAN-H, CAN-L) input line and GND |
| **Power Supply (USB-C Option)** | Reverse Flow Protection             | Prevents damage from incorrect power flow direction.         | Reverse polarity protection                                  | USB-C power input                                      |
| **I2C Buses**                   | Optional 2.7k Ohm Pull-up Resistors | Stabilizes I2C communication by providing additional pull-up resistance. | 2.7k ohm resistors                                           | Activated via jumper cap                               |

 ## Components List

PCB for the card can be ordered from any PCB fabricator using these Gerber Files; 

- [2x-Node Bus Hub]({{site.gerber_dir}}2x-Node_Bus_Hub.zip) (use with up to 2 cards, typically under layout at a remote location)
- [6x-Node Bus Hub]({{site.gerber_dir}}6x-Node_Bus_Hub.zip) (use with up to 6 cards, with expansion capabilities with more 6x Node Bus Hubs, typically used in a central location).  This implementation of the Node Bus Hub also provides:
  - Selection for adding I2C pull-up for long I2C serial connections to improve signal quality.
  - Network cable connections (RJ45) to allow expansion to additional Node Bus Hubs.
  - Connectors (female pin headers) to allow expansion to additional Node Bus Hubs.
  - LED indicators for I2C data transmission for BUS A and BUS B.   A transistor is used to trigger the LEDs to sense data transmissions from the I2C TX (transmission) line going HIGH during data transmissions.
  - 5V power supply connection (USB-C) for providing power when the expansion board is not being powered by a Primary LCC Fusion Node Card (with a Power Module).


[PCB Parts](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for the 6x Node Bus Hub (see diagram on right for reference): 

> Components are all marked as ** Optional ** since the number of connectors, power indictor, I2C data bus indicators, and ESD protection can vary depending on 

| Component Identifier         | Count | Type                      | Value            | Package                            | Required? | Purpose                                                      |
| ---------------------------- | ----- | ------------------------- | ---------------- | ---------------------------------- | :-------: | ------------------------------------------------------------ |
| C1, C4                       | 2     | Ceramic Capacitor         | 0.1uF            | SMD 1206                           | Required  | Conditions/filters the current for the IC (U1, U2).          |
| C2, C3, C5, C6               | 4     | Ceramic Capacitor         | 0.1uF            | SMD 1206                           | Required  | Low Pass Filter for low signal detection                     |
| D1-D3                        | 3     | LED                       | Red              | SMD 1206                           | Optional  | Indicators for PWR (5V) and I2C data transmission (receive (RX) line) |
| D4                           | 1     | Diode                     | SS310            | SMA                                | Optional  | Prevents accidental input V+ from damaging circuits, since USB-C is output-only. |
| D5, D6                       | 2     | ESD Diode                     | PESD1CAN         | SOT-23 SMD                         | Optional  | Required only when using the I2C data bus. Provides I2C electrostatic discharge (ESD) protection. |
| D7                           | 1     | ESD Diode                     | PESD1CAN         | SOT-23 SMD                         | Optional  | Provides CAN Network data bus electrostatic discharge (ESD) protection. |
| J1-J6                        | 6     | Card Edge Connector       | 12P (2x6)        | 3.86mm, 805 Strip Connector Type A | Required  | Connector for inserting cards with card edge connector tabs. Number of connectors varies by Node Bus Hub design. |
| J7, J8, J11, J12<sup>1</sup> | 4     | Female Right Angle Header | 8P, 2.54mm       | -                                  | Optional  | Used for connecting boards via pin headers. Provides direct connection to adjoining Node Bus Hub PCBs for I/O expansion. |
| J9, J10                      | 2     | RJ45 Socket               | 8P8C             | -                                  | Optional  | Required only when connecting hubs together using network cables. Provides network cable (CAT5/6) connection(s) to remote Node Bus Hub PCBs. |
| J13                          | 1     | Male Pin Header           | 2P               | -                                  | Optional  | Used to enable/disable I2C pullups for better reliability within a Node Bus Hub. Typically set once per hub. |
| J14                          | 1     | Connector                 | USB-C, 4P        | -                                  | Optional  | Required only when not using Power-CAN Card for power. Provides 5V power to remote devices. |
| Q1-Q4                        | 4     | Transistor                | IRLML6402        | SOT-23-3                           | Required  | Controlls 2.7k pullup when triggered by comparator           |
| Q5, Q6                       | 2     | Transistor                | BSS138           | SOT-23                             | Optional  | Used to turn on I2C data transmission indicators based on I2C signals. |
| R1                           | 1     | Resistor                  | 1kΩ              | SMD 1206                           | Required  | Current limiting for reference voltage                       |
| R2 - R5                      | 4     | Resistor                  | 100Ω             | SMD 1206                           | Requried  | Low Pass Filter for low signal detection                     |
| R6-R9                        | 4     | Resistor                  | 2.7kΩ            | SMD 1206                           | Required  | I2C Pullup resistors for both sets of SDA/SCL lines. Improves signal quality. |
| R10, R11                     | 2     | Resistor                  | 10kΩ             | SMD 1206                           | Optional  | Current limiting resistors for I2C indicators.               |
| R12                          | 1     | Resistor                  | 1kΩ              | SMD 1206                           | Optional  | Current limiting resistors for power indicator               |
| R13, R14                     | 2     | Resistor                  | 1kΩ              | SMD 1206                           | Optional  | Current limiting resistors for LED I2C indicators.           |
| SH13                         | 1     | Jumper Cap (Shunt)        | 2.54mm           | -                                  | Optional  | Used for setting I2C pullup selection. Recommend tall caps for ease of use. |
| U1-U2                        | 2     | IC (Voltage Comparator)   | LM393 or LM2903N | SO-8, SMD                          | Required  | Used for detecting low voltage in the I2C lines (less than 2.4v) |
| ZD1                          | 1     | Zener-Diode               | 2.4V             | BZT52                              | Required  | Used for a 2.4V reference voltage                            |

1. 8-male header when connecting boards together via pin headers between the optional female headers (J8, J9, J11, J12). Connects to adjoining Node Bus Hub together by connecting the female right angle connectors together.

## Tools Required

The card only requires soldering three sets of PTH female pin headers.  Required tools required are:

- soldering iron
- solder
- tacky putty (hold components while soldering)

> See [List of recommended tools](/pcb-tools/) for more details on these tools.



## Safety Precautions

- See [Safety Precautions](@ref safety_precautions_assembly). 



## Assembly Instructions

See also: [Soldering Tips](/pcb-soldering/)

Here are the step-by-step instructions for assembling the card:

### 6x-Hub

<img src="{{ site.baseurl }}/assets/images/pcbs/Node_Bus_Hub/6x-Node_Bus_Hub_pcb.png" style="zoom: 40%; float: right;" >Use of a SMD soldering stencil is optional since a minimal number of SMD component are installed and can easily be soldered with a soldering iron or soldering air pencil.

Depending on requirements, 1 to 6 connectors can be installed on either side.

#### Solder SMB Components

1. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.
2. Apply solder paste to all SMB pads.
3. Place Components into the paste.’
4. Reflow using hot plate, oven, or hot air pencil.

| Designator (value) | Component    | Required?                                                    | Orientation                                                  |
| ------------------ | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| C1 - C6            | 0.1uF        | Required                                                     | None                                                         |
| D1, D2, D3         | Red LED      | Optional, provides Power and Communications (I2C) Data TX indicators | Reference back of LED, cathode positions downward on the PCB.<img src="/_builder/Breakout_Boards/images/LED_Orientation.png" style="zoom: 15%; float: right;" /> |
| D4                 | SS310        | Required when using Power Indicator (D1)                     | Cathode end has a white line and positioned upward on the PCB. |
| D5, D6, D7         | PESD1CAN     | Optional,  provides ESD protection for Comm (I2C and CAN)    | None                                                         |
| J14                | USB-C Socket | Required when powering 5V via USB-C vs                       | Position socket pointing outward                             |
| R1                 | 1kΩ          | Required                                                     | None                                                         |
| R2 - R5            | 100Ω         | Required                                                     | None                                                         |
| R6-R9              | 2.7kΩ        | Required when using I2C pullups for improved signaling       | None                                                         |
| R10, R11           | 10kΩ         | Required when using Comm (I2C) Data RX/TX status indicators (D2, D3) | None                                                         |
| R12                | 1kΩ          | Required when using Power Indicator (D1)                     | None                                                         |
| R13, R14           | 1kΩ          | Required when using Comm (I2C) Data RX/TX status indicators (D2, D3) | None                                                         |
| Q1 - Q4            | IRLML6402    | Required                                                     | Fits only one way                                            |
| Q5, Q6             | BSS138       | Required when using Comm (I2C) Data RX/TX status indicators (D2, D3) | Fits only one way                                            |
| U1, U2             | LM393        | Required                                                     | IC’s dimple (pin 1) positioned toward PCB **top** edge           |
| ZD1                | Zener 2.4v   | Required                                                     | None                                                         |

#### Solder PTH Components

<img src="{{ site.baseurl }}/assets/images/pcbs/Node_Bus_Hub/6x_Node_Bus_Hub_Placing_Parts.gif" style="zoom: 25%; float: right;" />Solder each card edge connector individually.

> Make sure to seat each connector firmly against the PCB while soldering 1st pin, then heat and reseat the connector.  Finally solder the rest of the connector pins.

| Designator (value) | Component                         | Required?                                                    | Orientation                   |
| ------------------ | --------------------------------- | ------------------------------------------------------------ | ----------------------------- |
| J1 - J6            | 805 Connector                     | Requires at least 2 connectors, placed within white rectangles | None                          |
| J7, J8, J11, J12   | 8-Pin Female Header - Right Angle | Required when connecting boards together for expansion vertically or horizontally using male pins) | Place socket pointing outward |
| J9, J10            | RJ45 Socket                       | Required when connecting boards together for expansion using network cables | Place socket pointing outward |
| J13                | 2-Pin Male Header                 | Required when I2C signal is unstable                         | None                          |

### **2x**-Hub

1. <img src="/_builder/Breakout_Boards/images/2x-Node_Bus_Hub_pcb.png" style="zoom:50%; float:right" />Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

2. Solder each card edge connector individually.

   > Make sure to seat each connector firmly against the PCB while soldering 1st pin, then heat and reseat the connector.  Finally solder the rest of the connector pins.

   | Designator (value) | Component         | Required?                                                    | Orientation                                                  |
   | ------------------ | ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
   | D1                 | Red LED           | Optional, power status indicator                             | Yes, reference back of LED, cathode positions upward on the PCB.<img src="/_builder/Breakout_Boards/images/LED_Orientation.png" style="zoom: 15%; float: right;" /> |
   | J1 - J2            | 805 Connector     | Requires at least 1 connector, placed within white rectangles | None                                                         |
   | J3, J4             | RJ45 Socket       | Required when connecting boards together for expansion using network cables | Place socket pointing outward from the PCB                   |
   | J5                 | 2-Pin Male Header | Required when I2C signal is unstable                         | None                                                         |
   | R1-R4              | 2.7kΩ             | Required when using I2C pullups for improved signaling       | None                                                         |
   | R5                 | 1kΩ               | Required when using Power Indicator (D1)                     | None                                                         |

## Testing and Verification

The following test and verifications of the card should be performed after a through inspection of the card's soldering.  Check all of the PTH component pins.  Make sure there are no solder bridges between pins.

### Visual Inspection

1. Initial Check: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.
2. Solder Joint Inspection: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

### Power-Up Tests

Refer to the LCC Fusion Node Card for details on testing the LCC Fusion Node Bus Hub


## Troubleshooting

- See [I2C Trouble Shooting](@ref trouble_shooting_I2C).

## References

