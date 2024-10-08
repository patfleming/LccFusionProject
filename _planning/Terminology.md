---
title: Terminology
typora-root-url: ..
layout: default
permalink: /:name/
nav_order: 1
use_cases:
  - Learning & Planning
  - Automation Deployment
  - Device Control
---
# Terminology {#terminology}
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

- Brief overview of the importance of understanding specific terms and acronyms used in the LCC Fusion Project.
- Statement on how this glossary aids in better understanding the documentation and the project as a whole.

## LCC Fusion Project Terms

### CAN Network {#can-network}

**Controller Area Network (CAN)**

The Controller Area Network (CAN) is a robust communication protocol used for real-time data exchange between microcontrollers and devices. Originally developed for automotive systems, it is now widely used in various industries for its reliability, efficiency, and error-checking capabilities. CAN allows multiple devices to communicate on the same network without a host computer. A CAN Network can be wired or wireless. Wired CAN uses 2-wires to form the network, while wireless CAN can be achieved using WiFi or Bluetooth.

### LCC Fusion Project {#lcc-fusion-project}

The **LCC Fusion Project** is a comprehensive system designed for automating and controlling model railroads using the Layout Command Control (LCC) protocol. It integrates various hardware components like the LCC Node and I/O cards with software tools to enhance the realism and operational efficiency of model railroad layouts.

### LCC Fusion Cards {#cards}

<img src="/assets/images/pcbs/Card.png" style="zoom:15%;float:right" />Each card is design to a standard form of width, height, holes for mounting, positioning key, and 12 card edge pads (see pic on right).  This design enables the cards to be installed in card edge connectors mount on the [Node Bus Hub](/node-bus-hub-assembly-guide/), ensuring power and communication connects with the [Node Card](/node-card-assembly-guide/) (also installed in the same [Node Bus Hub](/node-bus-hub-assembly-guide/)).  A positioning key at the bottom of the card insures the card is inserted into the [Node Bus Hub](/node-bus-hub-assembly-guide/) with the correct orientation. 

| **PCB Layer** | **1** | **2** | **3** | **4** | **5** | **6** |
| ------------- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Top**       |  3V3  |  5V   |  12V  |  GND  | SDA0  | SCL0  |
| **Bottom**    | SCL1  | SDA1  | CAN-H | CAN-L | DCC1  | DCC2  |

#### Audio Card {#audio-card}

The **Audio Card** is a component in the LCC Fusion project that converts text messages and .wav files (from SD card) to audio and plays them through connected speakers, using an ESP32 microcontroller and audio amplifiers.

#### Battery Card {#battery-card}

The **Battery Card** is a rechargeable power source in the LCC Fusion project, designed to provide stable, portable power to LCC nodes, ensuring continuous operation and portability.

#### Block Occupancy Detector Card (BOD Card) {#bod-card}

The **BOD Card** is a critical component in the LCC Fusion project, used for detecting the presence of trains within specific track blocks on a model railroad. It monitors track occupancy by detecting current flow between the rails within isolated track sections, and it generates LCC events to signal the occupancy status to other components of the system.

#### PWM Card {#pwm-card}

The **PWM Card** is a component in the LCC Fusion project that uses Pulse Width Modulation (PWM) to control devices like signals and motors. It adjusts the power delivered to a device by varying the duty cycle of the signal, allowing for precise control over trackside accessories.

### LCC Fusion Breakout Boards {#breakout-boards}

Breakout boards are PCBs designed to be placed close to I/O devices, typically under the layout. They provide fast and simple connections to **Cards** through the use of RJ45 sockets, allowing [Network Cable](/terminology/#network-cable) to link to the corresponding **Card**. Most breakout boards are sized to fit into PCB housings, are DIN mountable, and feature holes for 3mm screws or standoffs.

Breakout Boards have specialized connectors and labeling for direct connections to specific I/O devices. For example, the {{site.data.names.block_breakout_board}} is used with the {{site.data.names.bod_card}}, facilitating direct connections to track blocks for block occupancy detection. This allows for streamlined wiring and reliable communication between the I/O devices and control systems.

### LCC Fusion Node Bus {#node-bus}

The **Node Bus** is a key part of the LCC Fusion Project, designed to connect [Node Card](/node-card-assembly-guide/)s and their I/O cards, ensuring they can communicate and receive power properly.

This bus system specifies the types of connections needed, their purposes, and where they should be placed on a PCB. Essentially, the Node Bus makes sure [Node Card](/node-card-assembly-guide/)s and Input Cards can work together smoothly, providing both the power and the means for them to talk to each other.

There are twelve (12) specific connections outlined for the Node Bus:

1. **Power Lines** (GND, 3V3, 5V, 12V) for different power needs.
2. **CAN Bus Lines** (CAN-L, CAN-H) for LCC communications.
3. **I2C Lines** for two sets of hardware buses (SDA0, SCL0, SDA1, SCL1) for data communication.

The setup of the Node Bus is guided by the LCC Fusion Framework’s design, including where the connection pads are located on the edges of the cards.

### LCC Fusion Node Cluster {#node-cluster}

A Node Cluster is a physical configuration that consists of at least a [Node Card](/node-card-assembly-guide/) and optionally additional cards connected via a [Node Bus Hub](/node-bus-hub-assembly-guide/).   A Node Cluster closely equates to an LCC Node as it will appear a configuration tool as an LCC Node.  Note that one or more [Node Card](/node-card-assembly-guide/)s can be configurated within a Node Cluster. 

### Virtual LCC Fusion Node Cluster {#virtual-node-cluster}

<img src="/assets/images/Virtual_LCC_Node_Cluster.png" style="zoom:20%;float:right;" />A Virtual LCC Node Cluster is a configuration utilizing a virtual connection between its [Node Card](/node-card-assembly-guide/) and other LCC Fusion Connect cards.  A Virtual LCC Node Cluster is an alternative to creating multi-Node clusters by allowing a single LCC Node to wirelessly perform I/O communications with multiple I/O cards dispersed throughout a layout.   This allows a scale-up of I/O without the complexity of managing multiple LCC Nodes.  

The virtual cluster consists of at least a **[Node Card](/node-card-assembly-guide/)** connecting wirelessly to an **I/O Controller Card**.   The I/O Controller Card can provide local I/O and/or thru the use a **[Node Bus Hub](/node-bus-hub-assembly-guide/)** can perform I/O to additional cards.  

> I/O boards can be relocated, minor rewiring and no configuration changes.  

The [Node Card](/node-card-assembly-guide/) utilizes ESP-NOW Wi-Fi technology to extend I/O wirelessly to I/O cards, reducing wiring, and providing flexibility in moving cards.  ESP-NOW provides Wi-Fi without the use of an access point, ssid, or password.

### [Node Card](/node-card-assembly-guide/) Types

Within a Node Cluster, there are two types of [Node Card](/node-card-assembly-guide/)s, a single **Primary [Node Card](/node-card-assembly-guide/)** and one or more **Secondary [Node Card](/node-card-assembly-guide/)s**, as follows:

- **Primary [Node Card](/node-card-assembly-guide/)**: This is the first [Node Card](/node-card-assembly-guide/) you'll connect to your system using a [Node Bus Hub](/node-bus-hub-assembly-guide/). It plays a pivotal role by being the initial point of contact to the CAN network and power supply. The Primary [Node Card](/node-card-assembly-guide/) ensures that these critical resources are available to the other [Node Card](/node-card-assembly-guide/)s in the network.  This [Node Card](/node-card-assembly-guide/) must be connected to both a power supply using a **Power Module** and connected to the CAN Network.
- **Secondary [Node Card](/node-card-assembly-guide/)s**: These [Node Card](/node-card-assembly-guide/)s are connected to the same [Node Bus Hub](/node-bus-hub-assembly-guide/) as the Primary [Node Card](/node-card-assembly-guide/), leveraging the CAN network and power distributed through the Primary [Node Card](/node-card-assembly-guide/).  Secondary [Node Card](/node-card-assembly-guide/)s are similar to a Primary [Node Card](/node-card-assembly-guide/), but do not have a Power Module or a CAN Network connection.  Since they can be configured with the same firmware as the Primary [Node Card](/node-card-assembly-guide/), Secondary [Node Card](/node-card-assembly-guide/)s are equally capable but designated as expansions to the primary setup.    

## LCC Fusion Connect Terms

### LCC [Node Card](/node-card-assembly-guide/) {#node-card}

The central card to which the all other cards connect with, facilitating communication and control within the LCC system.  An LCC Fusion Connect [Node Card](/node-card-assembly-guide/) will always have an ESP32 microcontroller unit (MCU) mounted on a PCB (development board).  Typically this is either a ESP32-WROVER on a DevKitC development board, or the Super Mini ESP32-S3 development board.

### I/O Cards {#io-cards}

An **I/O card** collaborates with the **[Node Card](/node-card-assembly-guide/)** to execute input/output operations, enabling control over various devices. The [Node Card](/node-card-assembly-guide/) issues commands via the Node Bus's serial connections (I2C) directly to the integrated circuits (ICs) on the I/O cards. Here's an overview of the types of I/O card communication supports available:

- **MCP23017 I/O Expander Cards (referred to as MCP Cards)**: These cards incorporate the MCP23017 IC to significantly increase the number of I/O pins at the [Node Card](/node-card-assembly-guide/)'s disposal. With the MCP Card, the [Node Card](/node-card-assembly-guide/) gains access to 16 additional pins for input and output purposes, making it a cornerstone in the LCC Fusion Project for enhancing the control over a broader array of devices.
- **PCA9685 PWM Controller Cards (also known as [PWM Card](/pwm-card-assembly-guide/)s)**: These cards are built around the PCA9685 IC, which augments the [Node Card](/node-card-assembly-guide/) with extra PWM pins. The [Node Card](/node-card-assembly-guide/) leverages these [PWM Card](/pwm-card-assembly-guide/)s to manage LEDs and motors, utilizing Pulse Width Modulation (PWM) signals for precise control over LED intensity and motor velocity.
- **ESP32  Based Cards**: Equipped with an ESP32, these cards are tasked with orchestrating the card’s operations through text-based commands. This includes advanced components like the **Node Cluster I/O Controller Card**, **[Sound Card](/sound-card-assembly-guide/)**, and **DCC Card**. Thanks to the ESP32's advanced capabilities, these cards are able to undertake more complex tasks than those possible with MCP or [PWM Card](/pwm-card-assembly-guide/)s, providing a versatile foundation for sophisticated control schemes.
- **NFC Card Reader Card**: These cards are build around the MRFC533 IC used for NFC (RFID) processing.

Each type of card plays a distinct role in the ecosystem, offering specialized functions that, when combined, create a versatile and powerful network for controlling a wide range of devices within the LCC Fusion Project.

### [Output Card](/output-card-assembly-guide/) {#output-card}

A device that manages up to 16 output lines, capable of controlling devices like LEDs and relays at either 5V or 12V.

### HW Communications Bus {#hw-communications-bus}

The hardware pathway for communication between the LCC Fusion Project [Node Card](/node-card-assembly-guide/) and all other LCC Fusion Project cards.  The LCC Node processor supports two serial buses for I2C communications.  Configuration requires alignment of a card’s switch settings with the CDI communications settings using a configuration tool.

The **LCC Fusion Node Bus Hub** automatically adjusts I2C line conditioning to ensure robust communication across all connected devices. This feature dynamically engages pullup resistors only when the signal integrity of the I2C lines (SDA and SCL) drops below an acceptable threshold, ensuring clean data signals over longer distances or when multiple devices are connected.

### HW Communications Address {#hw-communications-address}

A specific hardware communications (I2C) address assigned to LCC Cards for identification and communication within an LCC Node Cluster.

## LCC Fusion Connect Hardware

### Turnout Card {#turnout_card}

The **Turnout Card** is designed to control various turnout motors on a model railroad layout, receiving commands from the **LCC Fusion** network via I2C communication with the **Node Card**, which interfaces with the LCC network. Through various LCC Fusion breakout boards, the card supports **Tortoise™** slow-motion switch machines as well as other stall motors, single and twin-coil switch machines, and servos, offering precise bidirectional control over turnout point movement. It also manages frog polarity to ensure proper track continuity during turnout operations.

In addition to controlling motor direction and speed, the **Turnout Card** can report the status of turnout points (thrown or closed) back to the **Node Card**, enabling real-time monitoring and event handling within the LCC network. The card supports selectable 12V or 9V outputs to accommodate the specific power requirements of different switch machines.

### Turnout Tortoise Switch Machine Breakout Board {#turnout_tortoise_switch_machine_breakout_board}

The **Turnout Tortoise Switch Machine Breakout Board** is designed to interface with the **Turnout Card** using a network cable, providing direct control of **Tortoise™** slow-motion switch machines. This breakout board allows for a quick, direct connection to the **Tortoise™** switch machine with no additional wiring required. It supports daisy-chaining to a second **Turnout Tortoise Breakout Board**, enabling expanded turnout control while reporting turnout point status (thrown or closed) back to the **Turnout Card**. The board also manages frog polarity, ensuring smooth and reliable turnout operations within a model railroad layout.

For further details, refer to the [planning](/turnout_tortoise_switch_machine_breakout_board/planning), [assembly](/turnout_tortoise_switch_machine_breakout_board/assembly), and [configuration](/turnout_tortoise_switch_machine_breakout_board/configuration) guides.

## NMRA LCC Network Terms

### DCC Signal {#dcc-signal} 

The **DCC Signal** refers to the Digital Command Control (DCC) signal used in model railways, which is a form of alternating current that carries both power and digital control signals to the locomotives.

### Event ID {#event-id}

A unique identifier used within the LCC system to trigger actions or changes in the state of connected devices.  An Event ID is a 64-bit number in a dotted decimal format.  For example: 05.01.01.01.5C.65.00.00.  The LCC Node firmware provides default values that can be modified and reused thru the use of a LCC configuration tool such as the one provided by NMRA JMRI application.

### LCC Event Monitoring Tool {#lcc-event-monitoring-tool} 

The **JMRI Event Monitor** is a software tool used in model railroading to monitor and log events within the Layout Command Control (LCC) network, helping operators diagnose and manage their layout.

### LCC Configuration Tool {#lcc-configuration-tool} 

The **LCC Configuration Tool** is a software application used to configure and manage devices within the LCC (Layout Command Control) system. It allows users to set parameters, such as thresholds for voltage detection, and assign LCC Event IDs for specific conditions.

### LCC Node {#lcc-node}

An **LCC Node** is a device or module within the **LCC** that communicates over the **Layout Command Control (LCC)** network to perform specific tasks, such as controlling signals, turnouts, or detecting block occupancy. Each **LCC Node** can send and receive **LCC Events**, which are used to coordinate the operation of various devices on the model railroad. **LCC Nodes** are typically based on microcontrollers, such as the **ESP32**, and are configured using tools like the **LCC Configuration Tool**. Multiple **LCC Nodes** can be connected, allowing for complex automation and control scenarios on the layout.

## Model Railroad Automation Terms
### Accessory Bus {#accessory-bus}

The **Accessory Bus** is a dedicated communication bus in model railway systems used to manage and control accessories such as signals, lighting, turnout motors, and other non-locomotive devices. It operates separately from the main track power and data buses, allowing for independent control of these devices without interfering with train operations. The Accessory Bus is crucial for organizing and simplifying the wiring of layout accessories, ensuring reliable and efficient control of various layout features.

### Track Block {#track-block}

A **track block** is a specific section of railroad track that is electrically isolated from other sections to monitor or control the movement of trains within that block. In model railroading and layout automation, **track blocks** are used to detect the presence of trains, manage signals, and ensure safe and efficient operation of the railway by dividing the layout into manageable sections. Each **track block** can be monitored for occupancy, voltage levels, and other electrical parameters, allowing for precise control and automation.

### Track Bus {#track-bus}

The **Track Bus** is a pair of wires running underneath the layout that delivers power to the track. It is responsible for distributing DCC (Digital Command Control) signals and power across different sections of the layout, ensuring that all parts of the track receive consistent electrical power. The Track Bus typically connects to feeders, which are smaller wires that link the bus directly to the rails. Proper installation of a Track Bus is essential for reliable and smooth operation of model trains, preventing voltage drops and ensuring uniform performance throughout the layout.

In NMRA DCC systems, the two rails are often referred to as **Rail A** and **Rail B**. To maintain consistency in wiring, model railroaders commonly use color-coded wires for the Track Bus:
- **Red** wire is typically connected to **Rail A**.
- **Black** wire is typically connected to **Rail B**.

This color-coding practice helps ensure that the polarity is consistent throughout the layout, reducing the risk of wiring errors and simplifying troubleshooting. 

### Track Isolation and Blocks

Typically, to create isolated sections of track known as "blocks," only one of the two rails (usually **Rail B**) is isolated from the rest of the layout. This isolation allows the DCC system to detect train occupancy, control signals, or automate train movements within that block. The isolated rail is connected to the Track Bus through an occupancy detector or other control electronics, allowing the system to monitor and control trains within that block without interference from other parts of the layout.

Using a correctly installed Track Bus with consistent color coding and proper block isolation is crucial for the reliable operation of DCC systems. It helps to prevent short circuits, ensures accurate train detection, and maintains consistent power across the entire layout.

## Hardware and Software Terms
### Adapter {#adapter}

In the context of electronics and networking, an **Adapter** is a device that allows one type of hardware or connection to be used with another, facilitating communication between different systems. In the LCC Fusion project, the USB-CAN Adapter enables communication between a computer's USB port and a CAN (Controller Area Network) bus, which is commonly used in model railroad automation to control and monitor various devices on the layout.

### Amplifier {#amplifier}

An **Amplifier** is an electronic device that increases the power, voltage, or current of an audio signal. In the context of the LCC Fusion project, amplifiers are used to boost weak audio signals generated by sound modules or other audio sources, ensuring they are strong enough to drive speakers or other output devices. This is crucial in scenarios where clear and loud sound output is needed for effects like train whistles, station announcements, or other audio cues on a model railroad. The amplifier ensures that the audio signal maintains its quality while being amplified to the necessary levels for effective playback.

### Audio Signal {#audio-signal}

An **Audio Signal** refers to an electrical representation of sound, typically as a varying voltage that corresponds to the sound wave. In the context of model railroad automation, audio signals are used to transmit sound information, such as locomotive sounds, ambient noises, or announcements, from sound modules to amplifiers and eventually to speakers. Managing audio signals involves ensuring that they are properly amplified and transmitted without distortion, allowing for clear and accurate sound reproduction on the layout.

### Bridge Rectifier {#bridge-rectifier} 

A **Bridge Rectifier** is a circuit that converts alternating current (AC) into direct current (DC) by using four diodes in a bridge configuration. In the BOD Card and BLVD Card, it converts the AC-like DCC signal from the track into a DC signal for current and  voltage monitoring.

### Bus {#bus} 

In electronics and networking, a **Bus** refers to a communication system that transfers data between various components within a computer or between computers. In the context of model railroad automation, a bus typically refers to the electrical pathways that carry signals and power across different parts of the layout. For example, the **Track Bus** and **Node Bus** are essential components of the LCC system, facilitating reliable communication and power distribution to various nodes and devices on the layout.

### CAN Termination {#can-termination}

**CAN Termination** refers to the practice of placing a resistor at each end of a CAN (Controller Area Network) bus to prevent signal reflections, which can cause communication errors. The termination resistor, typically 120 ohms, matches the impedance of the CAN bus, ensuring that signals are correctly transmitted and received across the network. Proper CAN Termination is essential for maintaining the integrity and reliability of data transmission within a CAN network, especially in model railway automation where consistent communication between nodes is critical.

The **LCC Fusion Node Cards** utilize an **automatic CAN bus termination circuit** to ensure proper signal integrity while avoiding manual jumper settings by the end user. The termination is dynamically activated when necessary, preventing signal reflections that can occur at open-ended or improperly terminated CAN bus lines.

### CANable {#canable}

**CANable** is an open-source USB-to-CAN adapter used for connecting a computer to a CAN bus network. It is often used in model railroad automation projects like LCC Fusion to interface between the computer and the CAN network, allowing for the transmission and reception of CAN messages. CANable is valued for its affordability and compatibility with various operating systems and software, making it a popular choice for DIY automation enthusiasts.

### Charging Circuit {#charging-circuit} 

A **Charging Circuit** is an electronic circuit designed to safely charge batteries by regulating the charging current and voltage. In the Battery Card Assembly, the charging circuit uses an MCP73831 IC to manage the charging process of the Li-Po batteries, ensuring they are charged efficiently and safely.

### Cleaning PCB {#cleaning-pcb} 

**Cleaning a PCB** involves removing contaminants such as flux residues, dust, and oils that can accumulate during assembly and soldering. Proper cleaning of the PCB is crucial to ensure reliable electrical connections and to prevent short circuits or corrosion over time. Techniques for cleaning a PCB include using isopropyl alcohol, specialized PCB cleaning solutions, and compressed air to remove debris and ensure the board is in optimal condition for use.

### Component {#component}

A **Component** refers to any individual part or element that makes up a larger system or device within the LCC Fusion project. Components can include electronic parts such as resistors, capacitors, ICs (integrated circuits), connectors, or even entire assemblies like breakout boards or cards. Each component has a specific function within the system, contributing to the overall performance and functionality of the model railroad automation setup. Proper identification, handling, and installation of components are crucial for the successful operation of the system.

### Current Limiting Resistor {#current-limiting-resistor}

A **Current Limiting Resistor** is used in electronic circuits to restrict the amount of current that can flow through a component, protecting it from damage due to excessive current. In the BOD Card, these resistors protect the optocoupler and other components.

### Decoupling Capacitor {#decoupling-capacitor}

A **Decoupling Capacitor** is used to filter out high-frequency noise and stabilize the power supply voltage in electronic circuits, especially integrated circuits.  For example, in the BOD Card, it ensures a stable voltage supply to the MCP23017.

### Edge Card Connector {#edge-card-connector}

<img src="/assets/images/parts/Edge_Card_Connector.png" style="zoom:25%;float:right" />The [Node Bus Hub](/node-bus-hub-assembly-guide/) is implemented on PCB containing at least one **Edge Card Connector** (see blue connector on the right).  Supported connectors are the 805 Type A, 12P (2x6), with a 3.56mm pin pitch.  The Node Bus connections are connected to the connector’s 12 pins.  Connecting multiple connectors serially provide power and communications support between multiple cards.

### Ground Plane {#ground_plane}

A **Ground Plane** is a shared electrical reference for all components and power supplies in the system. In the LCC Fusion setup, components and various power sources (track, accessory, etc.) are connected to the same ground plane, ensuring stable power distribution, reducing noise, and providing a consistent return path for currents, improving overall system reliability.

### ESD Protection Diode {#esd-protection-diode}

An **ESD (Electrostatic Discharge) Protection Diode** is used to protect electronic circuits from electrostatic discharge, which can cause damage to sensitive components. In the BOD Card, it protects the I2C lines from ESD events.

### Ferrite Bead {#ferrite-bead}

A **Ferrite Bead** is a (inductive) passive electronic component used to suppress high-frequency noise in electronic circuits.  Used by many of the cards on the I2C lines to reduce interference and ensure reliable communication.

### Flyback Diode {#flyback-diode}

A **flyback diode** is a diode placed across an inductive load, such as a relay or motor, to protect against voltage spikes generated when the current is suddenly interrupted. It allows the current to safely dissipate, preventing damage to other components.

### GPIO Expander {#gpio-expander} 

A **GPIO Expander** is a device that increases the number of General Purpose Input/Output (GPIO) pins available to a microcontroller. The MCP23017, used in the BLVD Card, serves as a GPIO expander, enabling it to monitor multiple track blocks. 

### I2C Bus {#i2c-bus}

A communication protocol used for connecting and configuring devices within the LCC Node cluster, allowing multiple cards to communicate.

### I2C (Inter-Integrated Circuit) {#i2c} 

**I2C** is a communication protocol that allows multiple devices (such as microcontrollers and peripherals) to communicate with each other over a two-wire bus. In the context of the LCC Fusion project, I2C is used for communication between different cards, such as the Audio Card and Node Card, enabling them to exchange data like text messages and control signals. 

### I2S (Inter-IC Sound) {#i2s} 

**I2S** is a serial bus interface standard used for connecting digital audio devices. It allows the transmission of audio data between components such as microcontrollers, digital-to-analog converters (DACs), and audio amplifiers. In the LCC Fusion project, I2S is used to transmit audio signals from the ESP32 to the audio amplifier, ensuring high-quality audio playback.

### Jumper {#jumper}

A small connector used to close, open, or bypass electrical circuits on the [Output Card](/output-card-assembly-guide/), used for configuring voltage and communication settings.

### Li-Po Battery {#li-po-battery} 

A **Li-Po Battery** refers to a lithium polymer battery pack configured in a series arrangement with three cells, resulting in a nominal voltage of 11.1V and a maximum fully charged voltage of 12.6V. This battery configuration is commonly used in portable electronic devices for providing a stable, high-capacity power source.

### MCP23017 {#mcp23017} 

The **MCP23017** is a 16-bit I/O expander with I2C interface, allowing for additional input/output pins in microcontroller-based systems. It is used in the many of the LCC Fusion Project cards to interface with an LCC Fusion Node Card via the LCC Fusion Node Bus Hub.

### Network Cable {#network-cable}

A network cable, commonly known as an Ethernet cable, is a physical medium used to connect devices within a network, facilitating the transmission of data between computers, routers, switches, and other networked devices. These cables typically consist of twisted pairs of copper wires and use RJ45 connectors for wired connections in local area networks (LANs).

> **Recommendation:** For applications requiring higher data rates and power transmission, **CAT6** cables are recommended. CAT6 cables can carry more current with less voltage drop compared to older standards, and their increased stiffness makes them more durable and easier to insert into connectors, ensuring a more reliable connection.

### Optocoupler {#optocoupler}

An **Optocoupler** is an electronic component that transfers electrical signals between two isolated circuits using light. It provides electrical isolation, protecting sensitive components from high voltages and noise. In the BOD Card, the optocoupler isolates the track voltage from the MCP23017 GPIO pins.

### Polyfuse {#polyfuse}

**Polyfuse** is a resettable fuse that protects circuits from overcurrent conditions. It increases resistance when the current exceeds a specified limit, limiting the current flow, and automatically resets when the fault condition is cleared.

### Pull-up Resistor {#pull-up-resistor} 

A **Pull-up Resistor** is used in electronic circuits to ensure a terminal is at a high (logic 1) level when it is not actively driven. In the BLVD Card, pull-up resistors are used to ensure the MCP23017 GPIO pins have a defined logic level.

### PWM (Pulse Width Modulation) {#pwm}

Pulse Width Modulation (PWM) is a technique used to control the amount of power delivered to an electronic load by varying the width of the pulses in a pulse train. In model railroad automation, PWM is often used to control the speed of motors, adjust the brightness of LEDs, and manage other devices requiring variable power output. By adjusting the duty cycle (the ratio of the pulse width to the total period), PWM provides precise control over how much power is delivered to the connected device, making it an essential tool for managing various functions in the LCC Fusion project.

### Shield {#shield}

In the context of an ESP32, a **shield** is an additional hardware board or module that can be connected to the ESP32 development board to expand its functionality. Shields are designed to be stackable, allowing multiple shields to be used together, depending on the specific requirements of the project. They typically connect to the ESP32 through its GPIO (General Purpose Input/Output) pins and may include components like sensors, actuators, communication modules, or power management circuits. Shields simplify the process of adding new capabilities to the ESP32 by providing pre-built, plug-and-play hardware that interfaces seamlessly with the main board.

### Stencil {#stencil}

In PCB manufacturing and assembly, a **Stencil** is a thin sheet of material, usually made from stainless steel or polyimide, that is used to apply solder paste to specific areas of the PCB. The stencil has cutouts corresponding to the pads where components will be placed. During the assembly process, the stencil is aligned with the PCB, and solder paste is spread across the stencil, filling the cutouts. When the stencil is removed, the solder paste remains on the designated pads, ready for component placement. Proper use of a stencil ensures that the solder paste is applied accurately, which is critical for reliable solder joints and overall PCB performance.

### Supermini ESP32-S3 Development Board {#supermini-esp32-s3}

The **Supermini ESP32-S3 Development Board** is a compact, high-performance microcontroller board based on the **ESP32-S3** chip, which features dual-core processors with Wi-Fi and Bluetooth LE connectivity. Designed for space-constrained projects, this development board offers a rich set of peripherals, including GPIOs, I2C, SPI, UART, and ADC interfaces, making it ideal for IoT, embedded systems, and wireless communication applications. Its low power consumption and small form factor make it a versatile solution for developing smart devices with advanced wireless capabilities.

### TVS Diode {#tvs-diode} 

A **TVS (Transient Voltage Suppression) Diode** is a protective component that clamps voltage spikes to prevent damage to electronic circuits. In the BLVD Card, TVS diodes are used to protect the circuit from high-voltage transients that could occur on the track.



## Electrical Components

### 6N137 Optocoupler {#6n137}

The **6N137** is a **high-speed optocoupler** with a transistor output. It provides electrical isolation between two circuits while transmitting digital signals at speeds up to **10Mbps**. It operates with a supply voltage of up to **7V** and is commonly used in communication interfaces and data transmission systems.

### 74HC00 NAND Gate {#74hc00}

The **74HC00** is a **quad 2-input NAND gate IC**. It operates from a supply voltage range of **2V to 6V**, making it suitable for a wide range of logic-level applications. Each gate in the IC performs the NAND operation, outputting LOW only when both inputs are HIGH.

### 74HCT14D Schmitt-Trigger {#74hct14d}

The **74HCT14D** is a **hex Schmitt-trigger inverter**. It operates with a supply voltage range of **4.5V to 5.5V** and is designed to convert noisy or slowly changing input signals into clean digital signals. It is commonly used in digital circuits where signal conditioning is required.

### ACS712 Current Sensor {#acs712}

The **ACS712** is a **current sensor IC** that provides accurate current measurement based on the Hall effect. It operates with a supply voltage of **5V** and is available in models capable of sensing **5A, 20A, or 30A**. The output is analog, and the sensor is commonly used in power monitoring and motor control applications.

### BLM31 Ferrite Bead {#blm31}

The **BLM31** (BLM31PG121SN1L) is a **ferrite bead** designed to suppress high-frequency noise in electronic circuits. It is typically used for filtering EMI (Electromagnetic Interference) on power lines and signal lines. The current rating varies by model, but common versions can handle up to **2A** of current and provide impedance of **600Ω** at **100MHz**.

### BSS138 MOSFET {#bss138}

The **BSS138** is an **N-channel MOSFET** used for low-power switching applications. It operates with a **maximum drain-source voltage of 50V** and can handle up to **200mA** of continuous drain current. Its low gate threshold voltage makes it ideal for logic-level switching in microcontroller circuits.

### G5NB-1A-E-5VDC {#g5nb-1a-e-5vdc}

The **G5NB-1A-E-5VDC** is a compact, single-pole single-throw (SPST) non-latching (no state) relay designed for low-power switching applications. It operates with a 5V DC coil and can switch loads up to 10A at 250V AC or 30V DC. This relay is commonly used in control systems and power switching circuits where compactness and reliability are important.

### IRLML6402 MOSFET {#irlml6402}

The **IRLML6402** is a **P-channel logic-level MOSFET**. It has a maximum drain-source voltage of **20V** and can handle up to **3.7A** of continuous drain current. Its low gate threshold voltage allows it to be driven by 3.3V or 5V logic, making it suitable for load switching in low-voltage applications.

### IRLZ44N MOSFET {#irlz44n}

The **IRLZ44N** is an **N-channel logic-level MOSFET**. It can handle a maximum drain-source voltage of **55V** and a continuous drain current of **47A**. Its low gate threshold voltage (1V to 2V) allows it to be driven directly by 3.3V or 5V logic levels, making it ideal for high-current switching applications.

### KBL406 Bridge Rectifier {#kbl406}

The **KBL406** is a **bridge rectifier** used for converting AC input into DC output. It can handle up to **600V** reverse voltage and provides a maximum forward current of **4A**. This component is commonly used in power supply circuits to rectify incoming AC voltage.

### L298N H-Bridge Motor Driver {#l298n}

The **L298N** is a **dual H-bridge motor driver IC** that can drive two DC motors or one stepper motor. It operates with a supply voltage of up to **46V** and can supply up to **2A per channel**. The L298N is commonly used for motor control in robotics and automation projects.

### L7805CV Voltage Regulator {#l7805cv}

The **L7805CV** (LM7805CV) is a **5V linear voltage regulator** that provides a stable **5V output** with up to **1.5A** of output current. Due to its low efficiency, particularly when stepping down from higher input voltages, it is most suitable for **low-current loads**, where its power dissipation and heat generation remain manageable. One of the key advantage is its **simple circuit design**, requiring only **0.01uF** and **0.33uF** capacitors for stable operation. This makes it an effective and easy-to-implement solution for regulating voltage in small electronic components and circuits. The regulator also includes internal current limiting and thermal shutdown protection, enhancing reliability and providing protection against overload conditions.

### L7812CV Voltage Regulator {#l7812cv}

The **L7812CV** (LM7812CV) is a **12V linear voltage regulator** that provides a stable 12V output with up to **1.5A** of output current. It is commonly used in power supplies to regulate the voltage for various electronic components and circuits. It includes internal current limiting and thermal shutdown protection for reliability.  One of the key advantage is its **simple circuit design**, requiring only **0.01uF** and **0.33uF** capacitors for stable operation. This makes it an effective and easy-to-implement solution for regulating voltage in small electronic components and circuits. The regulator also includes internal current limiting and thermal shutdown protection, enhancing reliability and providing protection against overload conditions.

### LM1117-3V3 Voltage Regulator {#lm1117-3v3}

The **LM1117-3V3** is a **3.3V linear voltage regulator** that provides a fixed output of **3.3V** with a dropout voltage as low as **1.2V**. It can supply up to **800mA** of current and is commonly used to regulate the power supply for 3.3V devices such as microcontrollers and sensors.

### LM2574N-5 Voltage Regulator {#lm2574n-5}

The **LM2574N-5** is a **fixed-output 5V step-down (buck) voltage regulator** capable of delivering up to **0.5A** of output current while operating from an input voltage range of **7V to 40V**. It is highly efficient, making it suitable for **higher current loads** and applications where minimizing power loss and heat generation is important. However, the LM2574N-5 requires **larger capacitors**, such as **220uF** and **680uF**, for stable operation, particularly at higher input voltages and loads. Despite the need for larger components, its high efficiency makes it ideal for powering low-power digital circuits from higher voltage supplies while maintaining low heat output and energy efficiency.

### LM2596S-5 Voltage Regulator {#lm2596s-5}

The **LM2596S-5.0** is a **fixed-output 5V step-down (buck) voltage regulator** capable of delivering up to **3A** of output current, making it ideal for applications requiring **higher current loads**. Operating from an input voltage range of **7V to 40V**, this regulator is highly efficient, reducing power loss and heat generation, even when stepping down from higher voltages. However, like other high-current regulators, the **LM2596S-5.0** requires **larger capacitors**, such as **220uF** and **680uF**, for stable operation, particularly under heavier loads and higher input voltages. Its combination of high current capacity and efficiency makes it a popular choice for powering a variety of digital and power-hungry circuits in an energy-efficient manner.

### LM2596S-ADJ Voltage Regulator  {#lm2596s-adj}

The **LM2596S-ADJ** is an **adjustable-output version** of the LM2596S, offering flexibility in output voltage, allowing users to select different voltages by adjusting external resistors. In your use case, the output voltage can be selected between **5V** and **12V** by connecting either a **4.7K** or **10K** resistor, respectively. This makes the LM2596S-ADJ particularly versatile for projects where different voltages are required, without the need for separate regulators. Like the fixed version, it remains highly efficient and suitable for handling higher current loads with appropriate capacitor sizing for stable operation.

### LM393 Comparator {#lm393}

The **LM393** is a **dual comparator** IC with open-collector outputs. It can compare two input voltages and provide a HIGH or LOW output. It operates with a wide supply voltage range of **2V to 36V** and is commonly used in voltage sensing and signal comparison applications.

### M54562FP Transistor Array {#m54562fp}

The **M54562FP** is an **8-channel Darlington transistor array**. It can sink up to **500mA** per channel with a maximum voltage of **50V**. This IC is commonly used for driving high-current loads such as motors, relays, and LED displays. Each channel includes built-in clamping diodes for protection against inductive loads.

### MAX98257A Audio Amp {#max98257a}

The **MAX98257A** is a **class D audio amplifier** that can deliver up to **3.2W** of output power to an 8Ω speaker. It operates with a supply voltage of **2.5V to 5.5V** and is designed for portable applications where power efficiency and low heat dissipation are critical.

### MB6S Bridge Rectifier {#mb6s}

The **MB6S** is a **bridge rectifier** capable of converting AC input to DC output. It can handle a peak reverse voltage of **600V** and a forward current of **0.5A**. It is commonly used in power supply circuits to rectify low to moderate AC voltages into a stable DC supply.

### MCT6H Optocoupler {#mct6h}

The **MCT6H** is an **optocoupler** used for isolating high-voltage circuits from low-voltage control systems. It can handle input forward currents of up to **60mA** and output collector-emitter voltages up to **30V**. It is commonly used in applications that require electrical isolation between different parts of a circuit.

### MCP23017 I/O Expander {#mcp23017}

The **MCP23017** is a **16-bit I/O expander** that communicates over the I2C bus, allowing microcontrollers to control more digital I/O pins than physically available. Each I/O pin can source up to **10mA** or sink up to **25mA**. It operates with a supply voltage range of **1.8V to 5.5V**, making it ideal for extending GPIO capabilities.

### MCP7383T Battery Charger {#mcp7383t}

The **MCP7383T** is a **Li-ion/Li-polymer battery charge management controller**. It operates with an input voltage range of **4.5V to 12V** and supports programmable charge current up to **1A**. It is commonly used for charging single-cell lithium-ion or lithium-polymer batteries in portable devices.

### MFRC523 NFC {#mfrc523}

The **MFRC523** is an **NFC/RFID controller IC** used for reading and writing to RFID tags at **13.56 MHz**. It communicates with microcontrollers via the SPI, I2C, or UART interface and supports MIFARE protocols. It operates with a supply voltage of **2.5V to 3.3V** and can be used in contactless payment systems, access control, and identification applications.

### NE556 Timer {#ne556}

The NE556 timer is an integrated circuit that combines two independent 555 timers into a single 14-pin package. Each timer within the NE556 can be configured for monostable (one-shot) or astable (oscillator) operation, offering versatile timing and pulse generation capabilities. This dual-timer configuration is ideal for applications requiring multiple timing functions, such as sequential timing, pulse width modulation, or frequency generation. Using the NE556 reduces component count and saves space on circuit boards by providing two timers in one compact chip.

### PCA9685 PWM Driver {#pca9685}

The **PCA9685** is a **16-channel PWM driver** IC, commonly used for controlling servos, LEDs, and motors. It operates via an I2C interface and provides **12-bit resolution** for PWM control. The supply voltage range is **2.3V to 5.5V**, making it suitable for use with microcontrollers and low-power

### PESD1CAN TVS Diode {#pesd1can}

The **PESD1CAN** is a **transient voltage suppression (TVS) diode** designed to protect I2C lines and other low-voltage signal lines from electrostatic discharge (ESD) and other voltage spikes. It provides a clamping voltage of **24V** and is commonly used to safeguard communication lines like CAN or I2C.

### Polyfuse {#polyfuse}

A **Polyfuse** is a **resettable fuse** that protects circuits from overcurrent conditions. When the current exceeds the fuse’s rated limit, the Polyfuse increases in resistance and limits the current flow, typically resetting once the current returns to safe levels. Common current ratings range from **250mA to several amps** depending on the model used.

### PT204 Phototransistor {#pt204}

The **PT204** is a **phototransistor** used for detecting light levels. It can operate with a collector-emitter voltage of up to **30V** and a current of **20mA**. The PT204 is commonly used in opto-electronic devices such as light sensors, automatic lighting systems, and infrared detection circuits.

### SMAJ5A TVS Diode {#smaj5a}

The **SMAJ5A** is a **TVS (Transient Voltage Suppression) diode** with a **5V standoff voltage** and can handle a maximum peak pulse power of **400W**. It protects sensitive electronics from voltage transients induced by lightning or other transient voltage events.

### SMBJ18A TVS Diode {#smbj18a}

The **SMBJ18A** is a **TVS (Transient Voltage Suppression) diode** with a **18V standoff voltage** and can handle a maximum peak pulse power of **400W**. It protects sensitive electronics from voltage transients induced by lightning or other transient voltage events.

### SN65HVD233DR CAN Transceiver {#sn65hvd233dr}

The **SN65HVD233DR** is a **CAN bus transceiver** that supports high-speed data transmission up to **1 Mbps**. It operates with a supply voltage of **3.3V** and is used in automotive and industrial communication networks to handle robust and noise-resistant data transfer over long distances.

### SN74HCT14 Schmitt Trigger {#sn74hct14}

The **SN74HCT14** is a hex Schmitt trigger inverter IC that transforms noisy or slow-changing input signals into clean, fast digital outputs. It includes **six independent Schmitt triggers**, each of which takes an input signal and inverts it, producing a stable high or low output. The Schmitt trigger action introduces **hysteresis**, meaning the switching thresholds for high-to-low and low-to-high transitions are different, helping to eliminate noise and debounce input signals like those from mechanical buttons or switches. This makes the **SN74HCT14** ideal for ensuring reliable signal detection in noisy environments or when inputs are subject to fluctuation.

### SS310 Diode {#ss310}

The **SS310** is a **Schottky diode** with a maximum reverse voltage of **100V** and a forward current rating of **3A**. It is known for its fast switching capabilities and low forward voltage drop, making it ideal for high-efficiency power rectification and protection circuits

### TBD62083A Transistor Array {#tbd62083a}

The **TBD62083A** is an **8-channel Darlington sink driver** IC. It is capable of sinking up to **500mA** per channel with a maximum voltage of **50V**. It includes internal clamping diodes to protect against inductive loads, making it suitable for driving motors, relays, or LEDs.

### TC4428 MOSFET {#tc4428}

The **TC4428** is a **dual MOSFET driver** designed to control high-current MOSFETs or other power transistors. It operates with supply voltages up to **18V** and can source/sink currents of **1.5A** per channel. It is ideal for driving MOSFETs in high-speed switching applications, including motor control and power supplies.

### TQ2-5V Relay {#tq2-5v}

The **TQ2-5V** is a miniature dual-pole dual-throw (DPDT) latching (holds state) relay, featuring two sets of changeover contacts. It operates with a 5V DC coil and is designed for high reliability in switching low-level loads or signals. The TQ2-5V is ideal for applications requiring precise signal switching, such as in telecommunications or industrial control systems. It is available in both surface mount (SMD) and through-hole (PTH) versions.

### Zener Diode {#zener-diode}

A **Zener diode** is a type of diode designed to allow current to flow in the reverse direction when the voltage exceeds a specific breakdown voltage, known as the **Zener voltage**. Common Zener voltages range from **3.3V to 12V**, and they are used in voltage regulation and protection circuits.

## Troubleshooting and Support Terms

   - Terms and phrases commonly used in troubleshooting and support documentation.
   - Helps users understand the support materials and guides.
## Appendix and References
   - Any additional resources or references used for the terminology.
   - Links or citations to external sources for in-depth explanations.