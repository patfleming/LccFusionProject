---
title: Hardware Assembly Guides
typora-root-url: ..
layout: default
permalink: /:name/
nav_order: 1
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
  - Device Control
  - Automation Deployment
has_children: True
---
# Hardware Assembly Guides {#hardware_assembly_guides}

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

The **LCC Fusion Project** hardware consists of **PCBs** that need to be built. Each **PCB assembly guide** provides the necessary information for obtaining the parts needed and steps for building the **PCB**.

Building **PCBs** consists of the following steps:

1. **Ordering the PCB** from a **PCB fabricator** using the provided **PCB design files** called **Gerber** files. A **Gerber file** is a zip file containing the necessary details to create the specific **PCB**. ***[JLCPCB](https://jlcpcb.com/)*** is one of several **PCB fabricators** available. When ordering a **PCB**, consider ordering a stencil for applying solder paste.
2. **Ordering the PCB components** from electronic sources such as [**AliExpress**](https://www.aliexpress.com/). The specific type and quantity of components required for each **PCB** are provided in the assembly guides.
3. **Assembling the PCB** is performed by soldering components to the **PCB** while following the steps and guidelines provided in the **PCB assembly guides**.
4. **Testing the PCB** is performed in a series of steps as outlined below and within each of the assembly guides.

For detailed information on design best practices and considerations, please see the [**PCB Design Guidelines**]() section of our documentation.

## PCB Build Sequence

The following is a recommended order in which to build the PCBs.

1. **Node Bus Hub** is required for providing power and communications between a **Power-CAN Card** and other cards and breakout boards.  Power includes 3V3, 5V, and 12+V.  Communications includes CAN, DCC, and (2) I2C serial buses.  
2. **Power-CAN Card** is required for providing both power and communications for the LCC Fusion **cards** and **breakout boards**.  After building this card,  insert this card into the Node Bus Hub to provide power and communications with other cards and breakout boards.    
3. **SuperMini Node Card** is required to run LCC Node firmware which communicates with the I/O cards and devices.  This card can run from 1 to 4 independent LCC Nodes by installing up to 4 SuperMini ESP32-S3 boards.    The SuperMini Node Card must be inserted into a Node Bus Hub and powered with a Power-CAN Card.  More than one LCC Node can share power and communications provided via the Node Bus Hub. 
4. SuperMini Node Card is required to run the firmware for the LCC Node and to communicate with the I/O cards and devices.  The **Power-CAN Card** must be used in conjunction with the SuperMini Node Card to provide both power and CAN communications.  Both cards should also be inserted into a Node Bus Hub.   

## Creating Layout Automation Solutions

Below is a summary of the many layout automation solutions available using the **LCC Fusion Project** **PCBs** (**cards** and **breakout boards**).

The table below lists the **LCC Fusion Cards** and **LCC Fusion Breakout Boards** to be added to the basic **LCC Fusion Node Cluster** consisting of a **Node Bus Hub** with a **Power-CAN Card** and one or more SuperMini Node Card installed in the hub. Note that each SuperMini Node Card can support up to 4 individual **LCC Fusion Cards** by plugging in 1 to 4 **[SuperMini ESP32-S3](/terminology/#supermini-esp32-s3)** development boards.

| Solution                        | Card Assembly Guides                   | [Breakout Board Assembly Guides         | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| LCC Configuration Tool over BT  | None                                                         | None                                                         | Provide wireless Bluetooth connections LCC Configuration Tools running on Windows and Linux.  LCC Node provides a Bluetooth to CAN bridge.  **Note:** only one Node per cluster requires this bridge. |
| Admin console messages over BT  | None                                                         | None                                                         | Enables Bluetooth Serial Terminal applications to connect to the LCC Node(s) admin console for view system messages. |
| Audio Feedback System           | Audio Card                    | None                                                         | Configured Event ID to message text can be converted to audio and played thru speakers.  Use for audio indication of status or announcements..  For example, announce status after moving turnout points, or an announcement when a train is detected approaching a train station. |
| Direct Device I/O               | None                                                         | None                                                         | Provides up to 32 I/O lines (digital input/output, PWM, ADC, and touch).   LCC Events can control digital output devices (LEDs, etc).  PWM is used to control motors and LED lighting effects.   LCC Events can be produced using digital input, ADC to monitor sensors, or using touch of a finger to a wire/contact point. |
| Battery Backup                  | Battery Card                  | None                                                         | Provide battery backup to LCC Fusion Node Cluster |
| Block Low Voltage / Short Circuit Detection | BLVD Card                     | Block Breakout Board          | Used in detecting low track voltage (<12v) within a block.  Produces LCC Event IDs based on a low voltage detection for up to 8 track blocks.  Breakout boards provides a wire connection to each of the blocks and a wire to the track bus. |
| Block Occupancy Detection       | BOD Card                      | Block Breakout Board          | Used in detecting trains within blocks for signaling, crossings, etc. Produces LCC Event IDs based on block occupancy detection for up to 8 track blocks.  Breakout boards provides a wire connection to each of the blocks and a wire to the track bus. |
| Button Control | Button Card | I/O Breakout Board | Enables up to 16 buttons to connected.  Integrates noise reduction technology (Schmitt Trigger). |
| Control LEDs                    | Output Card                   | IO Breakout Board                                            | Provides up to 16 digital output lines supporting 5V or 12V, up to 500 mA.  Optional GND return line. |
| Control Signals                 | BOD Card PWM Card | Signal Masts Breakout Board<br>Signal Head Breakout Boards | Provides signal control based on block detection.  Controls up to 16x lamps per PWM Card.  Detect up to 8x blocks per BOD Card. |
| Control Turnouts                | Turnout Card                                                 | <ol><li>Turnout Stall Motor Switch Machine Breakout Board<li>Turnout Twin Coils Switch Machine Breakout Board<li>Turnout Single Coil Switch Machine Breakout Board<li>Turnout Servo Stall Motor Switch Machine Breakout Board<li>Turnout Slow Motion Switch Machine Breakout Board<ol> | Control turnouts using LCC Events to throw and close a point sets.  Produces LCC Event after movement is performed. |
| Play Sounds                     | Sound Card                    | None                                                         | Control sounds using LCC Events by starting/stopping the playing of MP3 files.  Manage up to 5x players and speakers per card. |
| Monitor Track Electrical Issues | BOD Card BLVD Card | Block Breakout Board          | The BOD Card is normally used for block occupancy detection, but it also handles current overloads (>1A) caused by shorts by using a auto-resettable fuse to temporarily stop the current until the short is fixed.  The BLVD Card will detect the drop voltage caused by shorts, bad connections, etc. and generated an LCC  Event. |
| Control Stepper Motors          | I/O Card                       | Stepper Motor Breakout Board  | Control stepper motors using LCC Events to set speed, stop, and reverse the motor. |
| Control DC Motors | I/O Card | DC Motor Driver Breakout Board | Control DC motors using LCC Events to set speed and direction. |

## PCB Testing Sequence

## PCB Assembly Guides: From Start to Finish

Below, you'll find links to specific guides for each **LCC Fusion Cards**. included in the **LCC Fusion Project**. These guides are tailored to the unique aspects of assembling each type of **PCB**, yet they all follow the same fundamental principles outlined in our sequence diagram. This consistency ensures that, no matter which **PCB** you're working on, the process remains familiar and straightforward.

<img src="{{ site.baseurl }}/assets/images/pcbs/Sound_Card/Sound_Card_Flow.png" style="zoom:70%;float:right" />Sequence of Activities:

1. **Preparation**: Gathering the necessary tools and components.
2. **Soldering**: Step-by-step instructions for soldering components onto the **PCB**.
3. **Testing**: Guidelines for testing the **PCB** to ensure functionality.
4. **Integration**: Advice on integrating the assembled **PCB** into your **model railroad layout**.
5. **Troubleshooting**: Common issues and how to resolve them.

## Assembly Guides

The assembly guides are organized into the following two categories:

1. **Card Assembly Guides**provide the builder with details on how to assemble the **LCC Fusion Cards** for both the **LCC Fusion Node Card** and the **LCC Fusion Cards**.
2. **Breakout Boards Assembly Guides** provide the builder with details on how to assemble the **LCC Fusion Project** **cards** for both the **LCC Fusion Node Card** and the **LCC Fusion Cards**.

## Additional Materials:

### Supplies

- [**PCB Components**]() - listing of items used for **PCB assembly**
- [**PCB Components**]() - listing of components used for **PCB assembly**

### How To Guides

- [**Builder’s Resources & Tips**]()