---
title: Turnout Card Configuration Guide
typora-root-url: ..
layout: default
permalink: /:name/
parent: Card Configuration Guides
nav_order: 2
use_cases:
  - Node Cluster Setup
  - Device Control
  - System Configuration
---

# Turnout Card Configuration Guide {#turnout_card_configuration}
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

The Turnout Card, in synergy with the **LCC Fusion Node Card** and one of the Turnout breakout boards** , forms the turnout controls functionality of the **LCC Fusion Project** system, facilitating turnout motor control for moving turnout points and detetection of points after being set to closed or open positions. This integration is pivotal for automating track signaling and control, core features in advanced model railroad setups.

## Application Scenarios

Below are detailed scenarios for deploying and configuring the Turnout Card:

| Scenario                    | Turnout Card Setup                                           | Block Breakout Board Setup | CDI Setup                                                    | Installation                                                 |
| --------------------------- | ------------------------------------------------------------ | -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Train Detection for Signals | 1. Adjust COMM BUS jumpers (JP1, JP2) to BUS A.<br>2. Configure COMM ADDR switches (SW1) to 0 (set all switches to OFF). | Not applicable             | 1. Start the LCC CDI configuration tool.<br>2. Access the LCC Node configuration.<br>3. Navigate to the Turnout Card section.<br>4. Enter `01` for **Reference ID**.<br>5. Input `Block 0` for **Description**.<br>Remember to use the predefined Event IDs for scenarios requiring block occupation information, such as signal logic and conditions. | 1. Connect the track blocks' ground (COM) rail to the Block Breakout Board's BLK1 connector.<br>2. Connect the layout's track bus ground (GND, COM) wire to the Block Breakout Board's TRACK BUS (GND, COM) connection.<br>3. Connect one of the turnout breakout boards to the Turnout Card using a network cable.<br>4. Slot the LCC LCC Fusion Node Card and the Turnout Card into a Node Bus Hub. |

## Terminology

For details on specific terms used throughout this document, refer to [Terminology](/terminology/).

## Configuration Summary

To configure an Turnout Card for use with LCC Fusion Project, follow these steps, as outlined in the documentation that follows:

1. **Connect to LCC Fusion Node Card**: Ensure the Turnout Card is properly connected to an LCC LCC Fusion Node Card. The system supports up to 16 Turnout Cards per LCC LCC Fusion Node Cluster, expanding your control capabilities across numerous output devices.
2. Set the card configuration selections, see below and [Setting hardware communications](/hw-communications-configuration/) for details.
3. Connect to turnouts using one of the turnout breakout boards.

### Turnout Card Hardware Configuration Details

This section will cover the specifics of setting up the physical jumpers on the Turnout Card. It includes instructions on how to access the jumpers, detailed explanations of their functions, and guidance on configuring them for various operational modes.

| Label     | PCB Components Indicator | Choices   | Description                                                      |
| :-------- | :----------------- | :----------- | :----------------------------------------------------------- |
| COMM BUS  | JP1, JP2     | A, B | Selects the I2C bus, aligning with firmware settings.  Must match with the firmware configuration (see below). |
| OUTPUT | JP3 | 9V, 12V |Selects the power output to the turnouts. |
| COMM ADDR | SW1                | 0 - 7        |Assigns a unique I2C address within an LCC LCC Fusion Node Cluster.  Each card within an LCC LCC Fusion Node Cluster using the same IC must have a unique address. |

## Turnout Card firmware Configuration for LCC Events

This part will detail the process for configuring the firmware to handle LCC events related to the I/O card. Using the  LCC Configuration Tool, it will outline steps to integrate the card with the LCC Fusion firmware, setting up LCC Event IDs to drive output devices. <img src="{{ site.baseurl }}/assets/images/setup/Turnout_Card_CDI.png" style="zoom:50%;float:right" />

1. Using the [LCC Configuration Tool]({{ site.baseurl }}/assets/images/howto/CDI_VIewer_Open/) find the LCC Node and open the configuration.
2. Scroll down to the Turnout Card segment and click on the twistie to open the configuration dialog box for the card
3. Select the tab for the specific card to be configured.  Note that  uninstalled cards can be configured for future use.
4. Select the tab for the specific line to be configured.  Note that unconnected lines can be configured for future use.
5. Make changes and click **Write** to save the change.
6. After all changes are made, click **Refresh** to verify changes took affect. 

Below are the card dialog configuration options for this card (refer to diagram on right):

> After changing fields, click the **Write** button to save the changes.

### CDI Summary

The Turnout Card configuration dialog, as shown in the image, provides options for setting up and customizing turnout motor parameters and the associated events that control them. Here's a summary of each section:

1. **Card Information Configuration:**
   - **Reference ID**: A field to enter a unique identifier for the card, such as a serial number or PCB component label.
   - **Description**: A text box to input a description of the card, potentially including its location or role in the layout.
2. **Card Communications Configuration:**
   - **Card Communications Bus**: A dropdown menu to select the communications bus the card will use, which should match the jumper settings on the card itself.
   - **Card Communications Address**: A field to set the card’s communication address, again corresponding to the physical switch settings on the card.
3. **Turnout Configuration:**
   - This section allows configuration of up to eight turnouts, including setting their names and the events that control their positions.
   - **Initial Turnout State at Power-On**: Options for the default state of the turnout motor when power is applied, including 'On' for thrown (open), 'Off' for closed (shut), or 'Previous' to retain the last state before power-down.
4. **Turnout Motor:**
   - **Close Event ID**: Event ID to move the turnout to the closed (shut) position.
   - **Throw (Open) Event ID**: Event ID to move the turnout to the thrown (open) position.
5. **Turnout Points:**
   - **Debounce Duration**: Time to stabilize the turnout points after a change is detected to avoid misreads due to bounce.
   - **Description**: A field for adding a description of the turnout, like its purpose and functionality.
   - **Closed Event ID**: Event ID that is produced when the turnout's points align to the closed position.
   - **Thrown (Open) Event ID**: Event ID that is produced when the turnout's points align to the thrown position.

This configuration interface is essential for integrating turnouts into the LCC network, allowing for the remote operation of turnouts and providing feedback on their positions for automation and control within the model railroad layout.

### Getting Started

Below are practical guidelines for starting out with the Turnout Card configuration:

1. **Utilize Default Event IDs:** Starting with the default Event IDs simplifies the initial setup and minimizes reconfiguration in case of a CDI factory reset. This approach provides consistency and ease of management, especially first leaning LCC or the JMRI Configuration Tool.
2. **Default Values for Debounce and Initial Turnout State:** Use default settings for debounce duration and initial sensor state which offsers a straightforward configuration process and ensures that the system operates predictably right after setup. The default debounce setting helps to avoid false positives from noise, and the default sensor state ensures that the system's initial status is known and consistent.
3. **Simple and Clear Descriptions:** Provide clear descriptions for the card and each line is crucial. The card description should briefly explain its role, while line descriptions should precisely identify which track block is being monitored. This clarity is vital for troubleshooting and for understanding the card’s role within the larger context of the layout.

By following these guidelines, you can achieve a basic yet functional setup that is easier to test and verify. The Turnout Card's design, as the simplest to configure, wire, and test, supports users in quickly getting started with layout automation. Encouraging users to start with these settings also makes the learning curve less steep, and once they're comfortable with the basics, they can delve into more complex customizations if needed.

### CDI Details

| CDI Group                         | CDI Field                               | Choices           | Comments                                                     |
| --------------------------------- | --------------------------------------- | ----------------- | ------------------------------------------------------------ |
| Card Information Configuration    | Reference ID                            | 0-255             | An optional value for the card’s identifier.  For example, a serial number or PCB component label. |
| Card Information Configuration    | Description                             | Text              | You can optionally enter reference information here to describe this card.  For example, the location and/or purpose of this card with the layout. |
| Card Communications Configuration | Card Communications Bus<sup>1</sup>     | BUS A, BUS B      | Ensure this matches the card’s COMM BUS settings as determined by the jumper positions. |
| Card Communications Configuration | Card Communications Address<sup>1</sup> | 0 - 7             | Ensure this matches the card’s COMM ADDR settings as determined by the switch positions. |
| Turnout Motor Configuration       | Initial Turnout State at Power-On       | OFF, ON, PERVIOUS | Select the default state of the Turnout when the system powers on. Options include 'On' for an thrown state, 'Off' for an closed state, and 'Previous' to retain the turnout state from the last session before shutdown. The default setting is 'Previous'. |
| Turnout Motor Configuration       | Close Event ID                          | Event ID          | Enter the Event ID that will close the turnout points.       |
| Turnout Motor Configuration       | Throw (Open) Event ID                   | Event ID          | Enter the Event ID that will throw (open) the turnout points. |
| Turnout Points Configuration      | Debounce Duration                       | 0-255             | Specify the stabilization wait time before the sensor device is triggered, where unit is 30ms. |
| Turnout Points Configuration      | Description                             | Text              | Enter a short description for this Turnout device for easy identification.  For example, the location and/or purpose of the track block within the layout. |
| Turnout Points Configuration      | Closed Event ID                         | Event ID          | Enter the Event ID that is produced when the turnout points are closed. |
| Turnout Points Configuration      | Thrown (Open) Event ID                  | Event ID          | Enter the Event ID that is produced when the turnout points are thrown (open). |

1. For details on bus and address selections, refer to [HW Communications Configuration](/hw-communications-configuration/)

## Functional Testing

After configuring your Turnout Card and ensuring all hardware connections are properly established, it’s essential to verify the functionality the detection of each track block to ensure your setup works as intended for your model railroad automation. Follow these steps to conduct functional testing:

1. Make all of the **connections** between the LCC Fusion Node Card, Turnout Card, Block Breakout Board, Track Bus (GND) and track block rails.
2. **Verify Device Behavior**: 
   1. Open an **LCC Event Monitoring** tool such as the one provided by JMRI.
   2. Place an locomotive on the rails within the track’s block and turn on the track power.
   3. The configured **On Event ID** for the specific should now appear in the event monitor.
   4. Turning off the track power or removing the locomotive from the track block should produce the configured **Off Event ID**.

3. Repeat the above for each of the Block Breakout Board’s track block connectors.

## Troubleshooting Guide

| Issue                                               | Possible Cause                              | Solution                                                     |
| --------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------ |
| No power to track block                             | Incorrect connections to track              | Verify Track Bus, track block rails, and Block Breakout Board connections.<ol><li>Block Breakout Board not connected to track block’s GND/COM rail. <li> Block Breakout Board not connected to Track Bus GND/COMM connector.<li>Track Bus V+ not connected to track block V+ rail.</ol> |
| Turnout Card block indicator not showing detection. | LCC Fusion Node Card not connecting to Turnout Card.   | <ol><li>Verify that LCC LCC Fusion Node Card is powered up<li>Verify that Turnout Card is seated in the Node Bus Hub connector.<li>Verify via the LCC Node Serial Monitor that the Turnout Card is detected.</ol> |
| Turnout Card is not connecting                      | Incorrect HW Communications Bus and Address | <ol><li>Confirm the HW Communications Bus and Address matches between the card and the configuration tool.  If encountering this, check that the HW Communications Bus and Address settings align between the card and the configuration tool. <li>Utilize the LCC LCC Fusion Node Cluster Serial Monitor to inspect currently detected I2C devices within the LCC LCC Fusion Node Cluster network.</</ol> |

