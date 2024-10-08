---
title: SuperMini I/O Status Shield Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Breakout Board Assembly Guides
nav_order: 3
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
  - Hardware Testing & Maintenance
subjects:
  - Hardware
  - Assembly Guides
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_project
  # LCC Fusion Connect Terms
  # NMRA LCC Network Terms
  # Model Railroad Automation Terms
  # Hardware and firmware Terms
  - cleaning_pcb
  - component
  - esp32_s3
  - shield
---
# SuperMini IO Status Shield Assembly Guide {#supermini_io_status_shield_assembly}
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

In conjunction with the **LCC Fusion Project** SuperMini Node Card, the **SuperMini IO Status Shield** provides status for the (8) I/O lines.  The **Shield** is typically used initial testing and deployments as a means of verifying whether or not the I/O lines are producing an output or input signal.  The **Shield** used is optional and must be plugged into one of the  SuperMini Node Card sockets, with a SuperMini ESP32-S3 plugged into the top of the **Shield**.

{% include terminology.html %}

## Specifications

Specifications for the PCB include:

| Characteristic                                    |       |
| ------------------------------------------------- | ----- |
| Max Input / Output Lines Monitored                | 8     |
| Max Input / Output Current (based on M54562FP IC) | 500mA |


### How It Works

The SuperMini Node Card monitors the (8) I/O lines of the SuperMini Node using a transistor to switch an LED on/off based on the state (High/Low) of the corresponding ESP32 GPIO pin.  A current limiting resistor is utilized to protect the LED.  The **Shield** uses the Vcc and GND provided by the  SuperMini Node Card connection to the LCC Fusion Node Bus Hub.

### Design Notes

Implemented as an Arduino **Shield** (plugs in below ESP32 module);

- Reduces number of wire traces
- Allows for easy additional and removal
- Uses transistor array to:
  - reduce components, allowing for fast on/off switching of LED switch based on the input / output line signal levels
  - allows higher current levels for the LEDs

- Uses SMD resistors for consistency of SMD uses with other boards (another option would be a 9-pin Resistor Network, which didn't save space or simplify the wiring).
- LEDs are positioned on PCB's outer edge for visibility

### Protection

The SuperMini IO Status Shield’s protection is provided by the  SuperMini Node Card circuit protection.

 ## Components List

PCB for the SuperMini IO Status Shield can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}SuperMini_IO_Status_Shield.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this PCB: 

| Component Identifier | Count | Type                 | Value       | Package  | Required? | Purpose                                                      |
| -------------------- | ----- | -------------------- | ----------- | -------- | :-------: | ------------------------------------------------------------ |
| LED1-LED8            | 8     | LED                  | Green       | 1206 SMD | Required  | Status indicator that an I/O line’s state is High when lit.  |
| J1, J2               | 2     | 9-Pin Female Headers | Long Legged | -        | Required  | Socket for Super-Mini ESP32-S3 development board(s). Required to allow insertion into the underlying headers. |
| R1-R8                | 8     | Resistor             | 1kΩ         | 1206 SMD | Required  | Current limiting protection for the LEDs.                    |
| Q1                   | 1     | IC                   | M54562FP    | SOP20    | Required  | Darlington transistor array to amplify low-current signals from the (8) ESP32 GPIO pins, enabling driving of LEDs. |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="{{ site.baseurl }}/assets/images/pcbs/Node_Card/SuperMini_IO_Status_Shield_pcb.png" style="zoom:70%; float:right" />Below are the high level steps for assembly of the SuperMini IO Status Shield:

Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

>  See also: [Soldering Tips](/pcb-soldering/)

| Designator (value) | Component          | Required?                                    | Orientation                                                  |
| ------------------ | ------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| J1, J2             | 9-Pin Male Headers | Required                                     | None                                                         |
| R1 - R8            | 1kΩ                | Required                                     | None                                                         |
| LED1 - LED8        | Red LED            | Optional, for daisy chaining breakout boards | Reference back of LED, cathode positions downward on the PCB.<img src="/_builder/Breakout_Boards/images/LED_Orientation.png" style="zoom: 15%; float: right;" /> |
| Q1                 | M54562FP           | Yes                                          | Position with the dimpled end facing on right side (pin 1 is now in the upper right corner). |

## Testing and Verification

### PCB Configuration

- No configuration required.  

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.

2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

3. **Component Orientation**: the IC's and LED’s are correctly oriented according to the PCB silkscreen or schematic.

### Connectivity Testing

1. **Continuity Check**: Use a multimeter in continuity mode to check for continuity between components.

### Power-Up Tests

1.  Install the **Shield** into the female headers of the SuperMini LCC Fusion Node Card.  
2. Install a SuperMini ESP32-S3 module into the female headers of the **Shield**.
3. Install the SuperMini LCC Fusion Node Card into an LCC Fusion Bus Hub.
4. Install a Power-CAN Card in the same bus hub
5. **Apply Power** to the Power-CAN Card.
6. **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

1. Using an LCC Configuration Tool
   1. Configure Event IDs for each of the Node’s input and output lines.  
   1. For output, generate the configured LCC Event ID and verify that the corresponding LED is lite.
   1. For input, temporarily ground each of the I/O pins and verify that the corresponding LED is lite.


## Troubleshooting

- Correct orientation of both the IC and each of the LEDs is the most common issue. 
- Verify that the SuperMini LCC Fusion Node Card is receiving power and that the SuperMini ESP32-S3 module’s LED is lite.  If not, check that the LCC Fusion Power-CAN Card is installed in the same Node Bus Hub and powered.

## References

- Super-Mini LED to ESP32-S3 pin assignments. <img src="{{ site.baseurl }}/assets/images/pcbs/Node_Card/SuperMini_ESP32-S3_pinout.png" alt="image-20240813095602688" style="zoom:70%; float:right" />

| SuperMini IO Status LED | **Super-Mini ESP32-S3 Pin** |
| ----------------------- | --------------------------- |
| LED1                    | GP1                         |
| LED2                    | GP2                         |
| LED3                    | GP3                         |
| LED4                    | GP4                         |
| LED5                    | GP5                         |
| LED6                    | GP6                         |
| LED7                    | GP7                         |
| LED8                    | GP8                         |

