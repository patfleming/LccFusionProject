---
title: USB to CAN (CANable) Adapter Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Breakout Board Assembly Guides
nav_order: 3
use_cases:
  - Node Cluster Setup
  - PCB Design & Assembly
subjects:
  - Assembly Guides
  - Automation
  - Hardware
  - Signaling
terms:
  # LCC Fusion Project Terms
  # LCC Fusion Connect Terms
  # NMRA LCC Network Terms
  # Model Railroad Automation Terms
  # Hardware and firmware Terms
  - adapter
  - canable
---

# [USB-CAN Adapter](/usb-can-adapter-assembly-guide/)  for Windows  {#usb_can_adapter}
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
This document provides a comprehensive guide on setting up a USB to CAN adapter, specifically the CANable device, for Windows users. Aimed at bridging the gap between your computer and CAN networks, this manual covers the essentials from acquiring a CANable device, updating its firmware to slcan, establishing the hardware connection, configuring JMRI software, to testing the connection with your LCC Node. Whether you're integrating with JMRI for model railroad automation or any other CAN network application, this guide ensures a smooth setup process, enhanced by illustrative images and step-by-step instructions to facilitate your understanding and implementation.

> The Power-CAN Card is specifically designed to support the attachment of the [USB-CAN Adapter](/usb-can-adapter-assembly-guide/) using a USB cable.


{% include terminology.html %}

## Acquiring a [USB-CAN Adapter](/usb-can-adapter-assembly-guide/)  (aka. CANable Device)

- Purchase a CANable Device, an open-source hardware that serves as a USB to CAN adapter, essential for connecting to CAN networks.
- Ensure the device either:
  - Comes pre-installed with slcan firmware (instead of Candlelight firmware), or
  - Is capable of entering DFU Download mode, enabling firmware updates from Candlelight to slcan firmware (detailed below).
- Find a CANable device by searching ' CANable' on AliExpress: [https://www.aliexpress.us/w/wholesale-canable.html?spm=a2g0o.home.search.0](https://www.aliexpress.us/w/wholesale-canable.html?spm=a2g0o.home.search.0)

## Firmware Update to slcan

To use the CANable device with JMRI, it must be recognized as a virtual COM port by Windows, requiring **slcan** firmware.

Follow these steps to update your CANable device to slcan firmware, ensuring compatibility with JMRI:

1. **Switch to DFU Mode**:
   - Each type of CANable adapter has a unique method of entering into DFU Mode which allows for updating the adapter’s firmware.  To install the Slcan firmware, the adapter **must be placed into DFU mode before connecting the adapter** via USB cable to the Windows computer.
   - Using your adapter’s documentation for updating the firmware, enable DFU (Device Firmware Update) Mode by using one of the following methods:
     - small dip switch located on the adapters PCB with two positions; DFU mode and normal operations mode. 
     - shorting out 2 pins (DFU and 3V3)
     - holding the DFU button during while inserting the adapter into a computer USB port   
2. **Chrome Preparation for Device Recognition**:
   - Execute the ImpulseRC Driver Fixer to allow Chrome to detect the device: [https://canable.io/utilities/ImpulseRC_Driver_Fixer.exe](https://canable.io/utilities/ImpulseRC_Driver_Fixer.exe)
3. **Updating the [USB-CAN Adapter](/usb-can-adapter-assembly-guide/) (CANable) Firmware**:
   - Utilize the CANable.io firmware updater utility to update the adapter firmware to slcan. The firmware update is performed directly through this webpage: [CANable Firmware Updater](https://canable.io/updater/canable1.html).
   
     1. Switch the adapter to DFU mode and connect it to the USB port of a Windows computer.
     2. Access the link above and choose a slcan version from the dropdown menu.
     3. Ensure the device is recognized; if not, confirm it is in DFU mode.
     4. Click the `Connect and Update`button to initiate the firmware update.
     5. In the subsequent popup, select `STM32 BOOTLOADER - Paired` and click `Connect`.
     6. Choose the device's name from the displayed list to proceed.
     7. A message stating `Erasing DFU device memory` will appear; wait during this process.
     8. `Copying data from browser to DFU device` will display next; please wait as the firmware transfers.
     9. A confirmation message, `Wrote 27332 bytes`, indicates the firmware has been successfully updated.
     10. Click `Disconnect`.
     11. Reset the adapter to **exit DFU mode** and return to normal operation.
4. **Return to Normal Operating Mode**:
   - If a switch was utilized for entering DFU Mode, revert the CANable device to its regular (Work) mode after the update.

## [USB-CAN Adapter](/usb-can-adapter-assembly-guide/)  Connection

Establish a connection between the computer's USB port and the LCC Node using a modified CAT network cable as described:

### CAT Cable Modification 

1. Remove the RJ45 plug from one end of the cable to reveal the 8 internal wires.

2. <img src="{{ site.baseurl }}/assets/images/pcbs/Breakout_Boards/CANable/JMRI_CANable_Plug.png" style="zoom:100%;float:right" />On the opposite end, identify the first three wires by looking at the RJ45 plug's back with the tab facing downwards.

3. <img src="{{ site.baseurl }}/assets/images/pcbs/Breakout_Boards/CANable/JMRI_CANable_Connector.png" style="zoom:100%;float:right" />Connect these three wires to the USB to CAN device's screw terminals as follows:

   | Network Cable Wire                    | [USB-CAN Adapter](/usb-can-adapter-assembly-guide/)  Screw Terminal |
   | ------------------------------------- | ------------------------------------------------------------ |
   | 1 (leftmost wire, from left to right) | CAN-L                                                        |
   | 2 (second wire)                       | GND                                                          |
   | 3 (third wire)                        | CAN-H                                                        |

### Final Hardware Setup Steps

Complete the setup by connecting the modified network cable to the USB to CAN device's screw terminals and establishing the connection to the LCC Node as follows:

1. Activate the CAN termination switch to the ON position for this adapter since it is located at one end of the CAN network. It's crucial to also configure a CAN termination at the network's other end, which is most likely to be on an LCC Node, to ensure proper network functionality.
2. <img src="{{ site.baseurl }}/assets/images/howto/CANable_Windows_Device_Manager.png" alt="image-20240504062958691" style="zoom:80%;float:right" />Plug the USB to CAN device into a USB port on the computer.
3. Insert the cable’s RJ45 connector into one of the two CAN network ports on the LCC Node.
4. To determine the Windows COM port used by the adapter open the **Windows Device Manager** and view the COM ports.  The device **CANtact USB/CAN Device (COMx)** should be shown, along with the COM port.  Use this COM port below when configuring JMRI.
5. > Note that ‘modern’ versions Windows will automatically find/install the device driver required to support the USB to CAN device.  For older versions of Windows, following the information found at https://canable.io/getting-started.html#drivers

## JMRI Configuration

To integrate JMRI with the CAN network through a USB to CAN adapter, execute the following instructions:

1. Launch the JMRI DecoderPro application from your Windows system.

2. Navigate to `Edit` -> `Preferences` from the main menu of DecoderPro.

3. <img src="{{ site.baseurl }}/assets/images/pcbs/Breakout_Boards/CANable/JMRI_CANable_Adapter.png" style="zoom:75%;float:right" />Configure a new connection by applying the following parameters:

   - [ ] `System Manufacturer: OpenLCB`

   - [ ] `System Connection: CAN via Lawicell CAN/USB`

   - [ ] `Settings:`
     - [ ] `Serial Port: COMx` (Identify this as the Windows-assigned port upon connecting the USB-CAN device)
       - [ ] `Connection Prefix: M `(default setting)
       - [ ] `Connection Name: ` [Your chosen name]

4. Finalize your settings by clicking the `Save` button located at the bottom-right corner of the Preferences-Connections window.

## Test Connection
After restarting JMRI Decoder Pro, verify the connection spanning from the computer, through the adapter, to the CAN network. This verification can be accomplished by choosing the `OpenLCB` tab from the top menu, followed by `Configure Nodes`. Every LCC Node within the CAN network should be visible in the `Network Tree` dialog.
