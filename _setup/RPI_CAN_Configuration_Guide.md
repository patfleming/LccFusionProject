---
title: RPI-CAN Card Configuration Guide
typora-root-url: ..
layout: default
permalink: /:name/
parent: Card Configuration Guides
nav_order: 3
use_cases:
  - Node Cluster Setup
  - System Configuration
---

# Setting Up CAN Bus Network on Raspberry Pi (RPI) {#RPI-CAN_config}
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

This section outlines the steps to set up a Raspberry Pi (RPI) for CAN bus support using the MCP2515 module.

## Step 1: Configuring the MCP2515 on RPI

First, configure the MCP2515 for communication in the RPI's Linux environment:

```bash
sudo nano /boot/config.txt
```

This command opens the `config.txt` file using the nano editor. Add the following line at the end of the file:

```bash
dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=25
```

- Ensure the oscillator value corresponds to the one on your MCP2515 module (indicated on the silver oscillator).
- Use interrupt value 25, as the card is designed to utilize RPI pin 25 for the (SPI) interrupt.

> Note: When compiling the ESP32 firmware, ensure the board's CPU Frequency is set to 240 MHz to align with the CAN bus speed.

## Step 2: Auto-Starting the CAN Interface on RPI

Configure the RPI to bring up the CAN interface automatically upon boot:

```bash
sudo nano /etc/network/interfaces
```

Open the network interfaces file and add the following configurations:

```bash
auto can0
iface can0 inet manual
  pre-up /sbin/ip link set can0 type can bitrate 125000 triple-sampling on restart-ms 100
  up /sbin/ifconfig can0 up
  down /sbin/ifconfig can0 down
```

These settings initiate `can0` as the interface with a bitrate of 125k.

## Step 3: Testing the Configuration

To test the setup:

```bash
ifconfig can0
```

1. Run this command in a terminal window to confirm the CAN interface is correctly set up. Look for CAN Bus traffic.

2. <img src="{{ site.baseurl }}/assets/images/pcbs/RPI-CAN_CarRPI-CAN_Status.png" alt="CAN Bus Status" style="zoom:80%; float:right" />Here an example of the `ifconfig` output, showing active CAN communications on CAN0 with data transmission.
   - If encountering errors, check all connections, reboot both RPI and ESP32, and retest.
   - Persistent issues may require rechecking configuration files, settings, and connections to the MCP2515 module.

## References

1. [Adding CAN to the Raspberry PI](https://www.beyondlogic.org/adding-can-controller-area-network-to-the-raspberry-pi/) - provides information on selection of the MCP2515 board and information used in the design of RPI-CAN Card and Linux configuration.
