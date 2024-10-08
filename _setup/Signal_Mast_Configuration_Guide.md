---
title: Signal Masts Configuration Guide
typora-root-url: ..
layout: default
permalink: /:name/
parent: Signaling Configuration Guides
nav_order: 2
use_cases:
  - Learning & Planning
  - Signaling Systems
---

# Signal Masts Configuration Guide {#signal_masts_configuration}
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
## Signal Masts Configuration

The **Signal Masts Configuration** is a foundational element within the **LCC Fusion Project**, specifically designed to manage the intricacies of **Signal Masts** and **Track Circuits**. This configuration ensures precise control over signal aspects, directly influenced by the state of each **Track Circuit**. Unlike broader signaling configurations that incorporate block occupancy and turnout positions, this section narrows its focus to how signal masts interpret and react to track circuit status. The correct setup of signal masts and their corresponding track circuits is crucial for accurate and reliable signal indication, which, in turn, enhances safety and efficiency on model railroads.

## Terminology

For details on specific terms used throughout this document, refer to [Terminology](/terminology/).

Below is a list of signaling terminology used on prototype railroads, some of which is used in the CDI signaling dialogs.

1. **Aspect**: The visual appearance of a signal as seen by the engineer, indicating the status of the track ahead.
2. **Block**: A section of track that only one train can occupy at a time.
3. **Circuit**: An electrical system used to detect the presence or absence of a train on a track section.
4. **Control Point**: A location on the railroad where trains may be routed from one track to another and where signals are typically located.
5. **Distant Signal**: A signal that provides advance warning of the aspect of the next signal.
6. **Downstream Signal**: A signal this ahead of the locomotive along its route 
7. **Head**: The actual light unit on a signal mast that displays the aspect.
8. **Interlocking**: An arrangement of signals and track switches that allow trains to move from one track to another at a junction.
9. **Mast**: The vertical structure that holds one or more signal heads.
10. **Track Circuit Link Address Event ID**: The Event ID used to link a signal mast to a specific track circuit or other masts.
11. **Route Signaling**: A system where signals indicate the route that has been set for a train, not just the condition of the track ahead.
12. **Signal Indication**: The information conveyed by a signal's aspect.
13. **Signal Pass at Danger (SPAD)**: An event where a train passes a stop signal without authorization.
14. **Track Circuit**: An electrical device used to detect the presence of a train on a section of track and convey this information to the signaling system.
15. **Track Speed**: The speed limit authorized by the signal aspect.
16. **Train Detection**: The system that determines if a section of track is occupied by a train.
17. **Train Protection System**: Safety systems designed to stop a train automatically if certain conditions are met, such as passing a signal at danger.
18. **Turnout**: A turnout, also known as a "points" or a "switch," is a mechanical installation enabling railway trains to be guided from one track to another at a railway junction. A basic turnout has a straight path (the main line) and a divergent path, allowing a train to move from one track to another. It consists of the actual switch mechanism, which includes the rails, tie plates, and operating rods that move the rails to switch the track.
19. **Rule to Aspect Mapping**: The process of assigning specific operational rules to signal aspects.
20. **Event ID**: A unique identifier for an event within the signaling system, such as the change of an aspect.
21. **Lamp Brightness**: The intensity of a signal head's light, controlled by varying the power supplied to the LED.
22. **Glow Effect Duration**: The time it takes for a light to ramp up to full brightness and dim down, simulating the behavior of a tungsten bulb.
23. **Signal Fade**: The gradual change in signal aspect appearance, mimicking the dimming or brightening of a light source.

## Configuration Summary

To configure an signaling for use with LCC Fusion Project, follow these steps, as outlined in the documentation that follows:

1. **Connect to LCC Fusion Node Card**: Ensure the PWM Card is properly connected to an LCC LCC Fusion Node Card. The system supports up to 16 Masts Cards per LCC LCC Fusion Node Cluster, expanding your control capabilities across numerous output devices.
2. Set the card configuration selections, see below and [Setting hardware communications](/hw-communications-configuration/) for details.
3. Connect to signal masts using the Signal Masts Breakout Board.

## PWM Card Hardware Configuration Details

Refer to the PWM Card and the Signal Masts Breakout Board for details on configuring the hardware for use with controling devices such as signal lamp LEDs.

## Signal Masts Configuration

**Signal Masts Configuration **is performed via the LCC Configuration Tool.  Configuration requires configuring the **Rules to Aspect** and **Track Circuits** as shown below.  Refer to the configuration tool dialog on the right.

### Rules to Aspect Configuration

<img src="{{ site.baseurl }}/assets/images/setup/Signal_Masts_CDI.png" style="zoom:0%;float:right" />Rules configuration panel used for setting up rules related to signal masts within the LCC Fusion Project. The summary of the dialog fields is as follows:

1. **Card** (tab): Select the tab for the PWM Card connected to the mast to be configured using a Signal Masts Breakout Board connected to signal lamps (LEDs).
2. **Card Information Configuration**:
   - Define the signal mast card's unique identifiers, such as a reference ID (like a serial number or PCB component label), and add an optional description for the card's purpose or location within the layout.
3. **Card Communications Configuration**:
   - Set the LCC Fusion Cards communication parameters, ensuring they match the card's physical switch or jumper settings for both the bus and address.
4. **Rule to Aspect Mapping Configuration**:
   - **Mast** (tab): select the tab for configuring each of the Masts connected to the Signal Masts Breakout Board.  Up to 8 masts can be connected to each Signal Masts Breakout Board.  A PWM Card is typically connected to 1 Signal Masts Breakout Board.
   - **Mast Operational Mode**: Associate operational modes to signal masts, allowing for independent or linked functioning, and identify masts for easy reference in systems like JMRI.  
   - **Mast Identifier**: Provide a description of the mast, such as the location or purpose of the masts.
   - **Track Circuit Linked Event ID**: Use this Event ID when configuring track circuits by copying this Event ID to the configuration of one of the Track Circuits. This results in a linkage between this mast and the track circuit.  When configuring Logics and Conditionals, the Track Circuit can be used to return the speed previously set by a remote (downsteam) mast when its aspect was set. 
   - **Lamp Fade**: Select the lamp’s fade effect, which controls how the signal's appearance changes, such as mimicking the fade of an incandescent lamp.
   - **Rules Configuration**:  This section defines the rule for the aspect.
     - **Rules**( tab): select the tab for each of the 4 rules to be defined.  Define each rule that match track speed for the mast. 
     - **Rule Name**: Choose a rule name, configure track speed states for the rule, and determine the visual signal aspect, including lamp configuration, phase, and brightness to reflect the rule's track speed.
     - **Rule Track Speed**: Select one of the 8 possible track speed that represent the speed states for the rule being defined.  Note that this is not a literal speed.
     -  **Rule’s Aspect Indicator**: Select the indicator that best represents the intended signal aspect for this rule.
     - **Set Aspect Event ID** is the Event ID that sets the aspect using the lamp(s) configured.   Aspects reset automatically. 
     - **Aspect Set Event ID** is the Event ID that produced once the aspect is set.  This can be used to trigger other signal masts and devices.
     - **Aspect Cleared Event ID** is the Event ID that is produced when aspect is cleared (turned off or changed to another aspect).
   - **Lamps Configuration**:  This section allows specifying which lamps (up to 4) to use for the rule's aspect, including their selection, phase, and brightness.
     - **Lamp** (tab): select the tab for the lamp to be configured.  Aspects may require configuring more than one lamp.
     - **Lamp Selection**: Select which lamp (LED) is used for the aspect.  Each lamp is connected to a Signal Masts Breakout Board `Head` and `Lamp`connector.  Select `UNUSED` for lamps that are not to be configured for the aspect.
     - **Lamp Phase**: Select the lamps `Phase` for the aspect.
     - **Lamp Brightness**: Select the percent of brightness for the lamp. 
     - **Lamp Glow Effect Duration**: Select the duration of the lamp. 

### Track Circuits Configuration

When configuring signals and their corresponding track circuits within a signaling system, you are establishing a relationship between the track circuits and the signals, specifically with respect to the signaling aspects and the speeds they represent. 

The following outlines the steps: 

1. **Configure All Masts**: Initially, set up all signal masts with their respective configurations.  Note that the "Track Circuit Link Event ID" is used later when configuring the Track Circuits.
2. **Link Track Circuits to Masts**: Begin with the mast located furthest downstream and proceed upstream. For each track circuit, copy the corresponding mast's "Track Circuit Link Event ID" into the track circuit’s configuration field. This action establishes a direct link between each mast and its associated track circuit.
3. **Utilize Logics and Conditionals**: After linking, use logics and conditionals to interpret the speeds indicated by downstream track circuits (e.g., 0 for Stop, 1 for Restricting, etc.). These interpretations guide the setting of aspects on masts based on the conditions signaled by downstream track circuit speeds set by a remote (downstream) mast. For example, if a downstream track circuit indicates a speed of 0, the upstream mast should display a 'Stop' aspect.

> Since the Track Circuit to Mast linkage is performed using an LCC Event ID, the mast can be defined and managed from **different LCC Node.**

<img src="{{ site.baseurl }}/assets/images/setup/Track_Circuits_CDI.png" style="zoom:75%; float:right;" />Below is a summary of the Track Circuits Configuration CDI fields (shown in the dialog on the right):

- **Track Circuit (tab)**: There are tabs for up to six circuits, allowing individual configuration for each track circuit.
- **Description**: A field to optionally enter descriptive information about the track circuit or mast.
- **Track Circuit Link Event ID**: This is a crucial field where you enter the Event ID that corresponds to the 'Track Circuit Link Event ID' of a downstream mast. This ID ensures that the aspect shown by the downstream mast influences the track circuit in question.

#### Track Circuit Link Event ID

When configuring the Track Circuit, the "Track Circuit Link Event ID" field is used to establish a connection with an upstream signal mast. This Event ID is crucial for determining how the track circuit responds to signals from the mast that is located upstream, effectively dictating the track circuit's behavior based on the conditions signaled by the upstream mast. By configuring this link, the track circuit is made aware of and can react appropriately to the signaling aspects displayed by the upstream mast, ensuring a cohesive flow of signaling information along the railway.

#### Track Circuits Application Example

When configuring two signal masts, A (upstream) and B (downstream), the communication between them regarding track conditions is crucial for coherent signal operation. This process involves the use of the "Mast Link Address Event ID", a unique identifier that plays a pivotal role in linking the track circuit of Mast A to the aspects displayed by Mast B.

Here’s how this linkage is implemented:

1. **Rules to Aspect Configuration for Mast B**:
   - For Mast B, determine the aspects (e.g., Stop, Proceed, Caution) that it will display under various conditions.
   - Each aspect configured is associated with a unique "Event ID". This "Event ID" serves as a digital signature for the specific aspect and condition it represents.
2. **Copying the Event ID**:
   - From Mast B’s "Rules to Aspect Configuration", take note of the "Event ID" associated with each aspect you wish to link to Mast A’s track circuit.
   - This "Event ID" is what you will use to create a direct link between the track circuit controlled by Mast A and the signal aspect displayed by Mast B.
3. **Track Circuit Configuration for Mast A**:
   - Within Mast A’s "Track Circuit Configuration", locate the field for entering the "Mast Link Address Event ID".
   - Paste or manually enter the "Event ID" from Mast B’s corresponding aspect into this field.
   - By doing so, you establish a connection that tells Mast A’s track circuit to react based on the aspect currently displayed by Mast B.
4. **Operational Outcome**:
   - Now, when Mast B displays an aspect (signaled by the activation of the corresponding Event ID), Mast A’s track circuit recognizes this event and adjusts its signal to drivers accordingly.
   - This ensures that the signaling along the track reflects a consistent and logical flow of information, enhancing both safety and efficiency.

This linkage technique ensures that signals are not only aware of local track conditions but also communicate with each other to maintain a coherent and safe flow of rail traffic, particularly in configurations where the decision made at one signal mast (B) directly influences the operational state of another mast (A) upstream.

## Application Scenarios

Below are detailed scenarios for deploying and configuring the PWM Card for controlling signal masts.  Reference the corresponding PCB using component labels (e.g. SW1, JP1) for the location of the selector or connector.

|      |      |
| ---- | ---- |

| Scenario                  | PWM Card                      | Signal Masts Breakout Board | Wiring                                                       | CDI Setup                                                    |
| ------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Signal Mast ‘Stop’ Aspect | 1. Set COMM BUS selector (JP1, JP2) to BUS A.<br>2. Configure COMM ADDR switches (SW1) to 0 (set all switches to OFF). |                                                            | 1. Connect `Signal Head 1` `Lamps 1-3` (JP1) to a signal using a 4-wire JST XH plug from the signal mast.<br>2. Connect `ACC BUS` connector (J14) to the layout accessory bus.<br>3. Set `LINE 16` selector (JP1) to `OUTPUT` using a jumper cap.  Note that this setting does not require `COMMON OUTPUT` to be configured.<br>4. Connect the Block Breakout Board to the BOD Card using a network cable.<br/>5. Slot the LCC LCC Fusion Node Card and the BOD Card into a Node Bus Hub. | 1. Start the LCC CDI configuration tool.<br>2. Access the LCC Node configuration.<br>3. Navigate to the **Segment: Signaling Configuration** section and select the tab for Card 1.<br>4. Enter `01` for **Reference ID**.<br>5. Enter`Mast 01 before turnout 1` for **Description**.<br>Remember to use the predefined Event IDs for scenarios requiring signal aspect information, such as signal logic and conditions.<br>6. Configure the **Rule to Aspect Configuration** by selecting **Mast 1** tab.<br>7. See below for additional CDI fields for configuring the rule to aspect. |

| Field Name                                                   | Value                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Operational Mode                                             | `Normal`                                                     |
| Mast Identifier                                              | <enter an identifier for the mast>                           |
| Track Speed (Rule 1 tab)                                     | <use default value shown>                                    |
| Appearance-Indicator                                         | <use default value shown>                                    |
| Set Aspect Event ID, Aspect Set Event ID, Aspect Cleared Event ID | <use default values shown>                                   |
| Lamp Selection (Lamp 1 tab)                                  | `LED-1`                                                      |
| Lamp Phase                                                   | <use default value shown>                                    |
| Lamp Brightness                                              | `50` (start with 50% and adjust based on room lighting and LED type) |
| Lamp Duration                                                | <use default value shown>                                    |

