---
title: Sending LCCS Events
typora-root-url: ..
layout: default
permalink: /:name/
parent: Builder's Resources & Tips
use_cases:
  - LCC Event Management
  - System Configuration
  - Learning & Planning
  - Hardware Testing & Maintenance
---

# Sending Events Using JMRI {#jmri_sending_events}
{:toc}
## Introduction to Sending Events with JMRI

The JMRI software suite, including DecoderPro and PanelPro, offers a powerful set of tools for model railroad control and automation. Among these tools, the Send Frame feature plays a crucial role during the testing phase of LCC Fusion Project implementations. This feature allows users to manually generate and send LCC events directly to the CAN bus, facilitating the testing and debugging of LCC-enabled devices and systems.

## Detailed Steps for Using the Send Frame Tool

### Launching the Send Frame Tool

The process begins in either the JMRI DecoderPro or PanelPro application. Here's a step-by-step guide to accessing the Send Frame Tool:

1. <img src="/assets/images/howto/JMRI_Send_Frame_Launch.png" style="zoom:75%;float:right" />**Access OpenLCB Options**: Navigate to the top menu bar and locate the "OpenLCB" option. This menu is your gateway to features specifically designed for LCC operations, including the Send Frame tool.
2. **Select Send Frame**: From the dropdown menu, select "Send Frame" to open the tool. This action brings up a separate window dedicated to event generation and management.

### Generating and Sending an LCC Event

Once the Send Frame Tool is open, you can generate an LCC event: 

1. <img src="/assets/images/howto/JMRI_Send_Frame_Send.png" style="zoom:50%;float:right" />**Enter Event ID**: In the tool's interface, you'll find an "Event ID" field. Here, you can manually enter or paste the specific Event ID you wish to generate. The format and structure of Event IDs should adhere to LCC standards, ensuring they are recognized and processed correctly by your layout's devices.
2. **Send the Event**: With the Event ID in place, click on the "Send Event Produced" button. This action sends the event onto the CAN bus, where it can be received by LCC-enabled devices configured to respond to that specific ID.

## Expanding the Use of JMRI for LCC Event Testing

Beyond simply sending events, the JMRI Send Frame Tool can be an invaluable resource for testing the responsiveness and configuration of your model railroad's LCC-enabled devices. By generating specific events, you can verify that each device behaves as expected, reacts to the correct events, and integrates seamlessly with the broader LCC network. This testing phase is critical for troubleshooting potential issues, fine-tuning your system's configuration, and ensuring a smooth operation of your model railroad automation projects.
