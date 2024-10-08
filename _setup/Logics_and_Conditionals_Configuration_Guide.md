---
title: Logics and Conditionals Configuration
typora-root-url: ..
layout: minimal
permalink: /:name/
parent: Signaling Configuration Guides
nav_order: 2
use_cases:
  - Node Cluster Setup
  - Signaling Systems
  - Train Detection
  - System Configuration
  - Hardware Testing & Maintenance
---

# Logics and Conditionals Configuration Guide {#logics_and_conditionals_configuration}
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
## **Introduction to Logics and Conditionals Configuration**

The Logics and Conditionals Configuration feature is designed to streamline and automate signal control within your model railroad setup. By allowing users to define logical conditions under which specific actions are taken, this powerful tool ensures that your railroad operates smoothly and efficiently.

**Logic & Conditional The Basics**

Logics can be expressed as a statement in the form of `If X then A else B`.  Below, we’ll explore this statement a little further.

> **If** `X`: Logic’s conditional using Condition(s) and operators
>
> - **Then** `A`: Logic’s **Action** when conditional is **True**
> - **Else** `B`: Logic’s **Action** when conditional is **False**

Let’s now look at a few examples of Logics, conditionals and actions applied to signaling.

| Use Case                                 | Condition                             | Logic’s Action When Conditional is True | Logic’s Action When Conditional is False |
| ---------------------------------------- | ------------------------------------- | --------------------------------------- | ---------------------------------------- |
| Setting of a mainline 2-Lamp Signal Head | Downstream block occupancy = occupied | Set Aspect to ‘Stop’                    | Set Aspect to ‘Clear’                    |
|                                          |                                       |                                         |                                          |
|                                          |                                       |                                         |                                          |

**Expanding Capabilities through Grouping**

To handle more intricate scenarios that require checking multiple conditions simultaneously, Logics and their associated Conditionals can be grouped. This grouping functionality allows for the creation of complex control schemes that can evaluate several different conditions before executing an action. Whether it's managing track occupancy, signal aspects, or route settings, grouping Logics and Conditionals provides the flexibility needed to accommodate a wide range of operational requirements.

**Multiple Groups for Comprehensive Control**

Moreover, the ability to configure multiple groups of Logics and Conditionals opens up even greater possibilities for customization and control. Each group can be dedicated to managing a specific set of controls or a particular mast, enabling users to tailor the behavior of their model railroad to precise specifications. For example, one group could be responsible for controlling the signals at a busy junction, while another might manage the track switches in a different area of the layout. This multi-group approach not only enhances the granularity of control but also allows for more nuanced and detailed management of the railroad's operational dynamics.

In essence, the expanded capabilities of the Logics and Conditionals Configuration tool empower users to create more sophisticated and responsive control systems for their model railroads. By leveraging the power of grouping and multiple control sets, enthusiasts can ensure that their railroads reflect the complexity and precision of real-world operations.





## Overview of Logics and Conditionals Configuration

**Key Configuration Features:**

- **Description**: Assign a functional tag or description for each logic conditional to identify its purpose and role within the system.
- **Group Functionality of Logic**: Determine the logic's interaction within a collective set, opting for `Blocked (Logic is not processed)` (default), `Group (Logic is part of a group of logics)`  (for combined operations), or `Last (logic is last or the only logic in a group)` to finalize a group evaluation.   
- **Condition Configuration**: Define one or two Conditions for the conditional.  Conditions can detect Event ID being produced or changes in track circuit’s reported speed. Conditions are crucial for determining the specific conditions that activate the logic.
- **Logic Operator Configuration**: Choose the conditional’s logical operator used to evaluate a condition of either true or false.
- **Logic Flow Configuration** Choose how the logic group is to be processed, opting for whether to send an Event ID or not and whether to continue processing logics within the group or immediately start processing the next group.
- **Logic Action Timing Configuration** Choose the timing for the logics action, opting for immediate or a delay.
- **Actions Configuration**: Configure one or more actions, including what triggers the action and the Event ID to be produced.

This configuration is a cornerstone for automated signal management, offering nuanced control over the signal aspects that direct the flow of traffic on your model railroad. By setting up Logics and Conditionals appropriately, you can ensure that signals accurately reflect the state of the tracks, enhancing both the realism and the operational safety of the layout.

## Terminology

For details on specific terms used throughout this document, refer to [Terminology](/terminology/).

Below is a list of signaling terminology used on prototype railroads, some of which is used in the CDI signaling dialogs.

**NMRA LCC Terminology**

- **Event ID**: A unique identifier for an event within the signaling system, such as the change of an aspect.

**Signal Mast Terminology**

- **Mast**: The vertical structure that holds one or more signal heads.
- **Head**: The actual light unit on a signal mast that displays the aspect.
- **Aspect**: The visual appearance of a signal as seen by the engineer, indicating the status of the track ahead.
- **Rule to Aspect Mapping**: The process of assigning specific operational rules to signal aspects.
- **Track Circuit Link Address Event ID**: The Event ID used to link a signal mast to a specific track circuit or other masts.
- **Lamp Brightness**: The intensity of a signal head's light, controlled by varying the power supplied to the LED.
- **Glow Effect Duration**: The time it takes for a light to ramp up to full brightness and dim down, simulating the behavior of a tungsten bulb.
- **Signal Fade**: The gradual change in signal aspect appearance, mimicking the dimming or brightening of a light source.
- **Track Speed**: The speed limit authorized by the signal aspect.
- **Interlocking**: An arrangement of signals and track switches that allow trains to move from one track to another at a junction.
- **Route Signaling**: A system where signals indicate the route that has been set for a train, not just the condition of the track ahead.
- **Signal Indication**: The information conveyed by a signal's aspect.

- **Downstream Signal**: A signal that’s ahead of the locomotive along its route 

**Track Related Terminology**

1. **Block**: A section of track that only one train can occupy at a time.
2. **Track Block**: An electrically isolated section of track that can be monitor for occupancy based on the presence of an electrical current in the rails.
3. **Train Detection**: The system that determines if a section of track is occupied by a train.  The BOD Card provides this functionality.
4. **Circuit**: An electrical system used to detect the presence or absence of a train on a track section.
5. **Track Circuit**: An electrical device used to detect the presence of a train on a section of track and convey this information to the signaling system.
6. **Turnout**: A turnout, also known as a "points" or a "switch," is a mechanical installation enabling railway trains to be guided from one track to another at a railway junction. A basic turnout has a straight path (the main line) and a divergent path, allowing a train to move from one track to another. It consists of the actual switch mechanism, which includes the rails, tie plates, and operating rods that move the rails to switch the track.

## Configuration Summary

To configure an signaling for use with LCC Fusion Project, follow these steps, as outlined in the documentation that follows:

1. **Connect to LCC Fusion Node Card**: Ensure the PWM Card is properly connected to an LCC LCC Fusion Node Card. The system supports up to 16 Masts Cards per LCC LCC Fusion Node Cluster, expanding your control capabilities across numerous output devices.
2. Set the card configuration selections, see below and [Setting hardware communications](/hw-communications-configuration/) for details.
3. Connect to signal masts using the Signal Masts Breakout Board.

## PWM Card Hardware Configuration Details

Refer to the PWM Card and the Signal Masts Breakout Board for details on configuring the hardware for use with controling devices such as signal lamp LEDs.

## Signal Masts Configuration

**Signal Masts Configuration ** is performed via the LCC Configuration Tool.  Configuration requires configuring the **Rules to Aspect** and **Track Circuits** as shown below.  Refer to the configuration tool dialog on the right.

### Rules to Aspect Configuration

<img src="{{ site.baseurl }}/assets/images/setup/Signal_Masts_CDI.png" style="zoom:50%;float:right" />Rules configuration panel used for setting up rules related to signal masts within the LCC Fusion Project. The summary of the dialog fields is as follows:

1. **Card** (tab): Slect the tab for the PWM Card connect to the mast to be configured using a Signal Masts Breakout Board connected to signal lamps (LEDs).
2. **Card Information Configuration**:
   - Define the signal mast card's unique identifiers, such as a reference ID (like a serial number or PCB component label), and add an optional description for the card's purpose or location within the layout.
3. **Card Communications Configuration**:
   - Set the LCC Fusion Node Card communication parameters, ensuring they match the card's physical switch or jumper settings for both the bus and address.
4. **Rule to Aspect Configuration**:
   - **Mast** (tab): select the tab for configuring each of the Masts connected to the Signal Masts Breakout Board.  Up to 8 masts can be connected to each breakout board.  A PWM Card is typically connected to 1 breakout board.
   - **Mast Operational Mode**: Associate operational modes to signal masts, allowing for independent or linked functioning, and identify masts for easy reference in systems like JMRI.  
   - **Mast Identifier**: Provide a description of the mast, such as the location or purpose of the masts.
   - **Track Circuit Linked Event ID**: Use this Event ID when configuring track circuits by copying this Event ID to the configuration of one of the Track Circuits. This results in a linkage between this mast and the track circuit.  When configuring Logics and Conditionals, the Track Circuit can be used to return the speed previously set by a remote (downsteam) mast when its aspect was set. 
   - **Fade**: Select the fade effect, which controls how the signal's appearance changes, such as mimicking the fade of an incandescent lamp.
   - **Rules Configuration**:  This section defines the rule for the aspect.
     - **Rules**( tab): select the tab for each of the 4 rules to be defined.  Define each rule that match track speed for the mast. 
     - **Rule Name**: Choose a rule name, configure track speed states for the rule, and determine the visual signal aspect, including lamp configuration, phase, and brightness to reflect the rule's track speed.
     - **Track Speed**: Select one of the 8 possible track speed that represent the speed states for the rule being defined.  Note that this is not a literal speed.
     -  **Aspect Indicator**: Select the indicator that best represents the intended signal aspect for this rule.
     - **Set Aspect Event ID** is the Event ID that sets the aspect using the lamp(s) configured.   Aspects reset automatically. 
     - **Aspect Set Event ID** is the Event ID that produced once the aspect is set.  This can be used to trigger other signal masts and devices.
     - **Aspect Cleared Event ID** is the Event ID that is produced when aspect is cleared (turned off or changed to another aspect).
   - **Lamps Configuration**:  This section allows specifying which lamps (up to 4) to use for the rule's aspect, including their selection, phase, and brightness.
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

#### Using Track Circuits

"When configuring the interaction between two signal masts—A (upstream) and B (downstream)—it's important to establish a clear communication pathway for track conditions that influence signal operations. This is achieved through the 'Track Circuit Link Event ID'. This unique identifier links Mast B to a specific track circuit, which monitors and reports the speed of a section of track. The reported speed from this track circuit is then utilized to determine and set the appropriate aspect at Mast A. This setup ensures that the aspect displayed by Mast A is directly informed by the real-time conditions of the track as detected by the circuit linked to Mast B, enabling accurate and safe signaling based on current track usage and conditions."

Using Mast A and Mast B previously mentioned, let’s see how the track circuit is implemented:

1. **Rules to Aspect Configuration for Mast B**:
   - For Mast B, determine the aspects (e.g., Stop, Proceed, Caution) that it will display under various conditions.
   - Each aspect configured is associated with a unique "Event ID". This "Event ID" serves as a digital signature for the specific aspect and condition it represents.
2. **Linking a Mast to a Track Circuit**:
   - From Mast B’s "Rules to Aspect Configuration", take note of the "Track Circuit Link Event ID" and copy it to a track circuit configuraton.
   - This configuration step using the "Track Circuit Link Event ID" creates a direct link between the track circuit and Mast B.
3. **Logics and Conditionals Configuration**:
   - When configuring the Logic for setting the aspect of Mast A, configure a Condition to test the speed of the track circuit.  For example, if the track circuit is reporting an **Approach** speed for the downstream mast, then aspect for Mast A should be set to **Stop.** 
4. **Operational Outcome**:
   - Now, when Mast B displays an aspect (signaled by the activation of the corresponding Event ID), the Logics and Conditionals configuration for Mast A’s can detect the changes in the track circuit’s reported speed and change the aspects for Mast A.
   - This ensures that the signaling along the track reflects a consistent and logical flow of information, enhancing both safety and efficiency.

This linkage technique ensures that signals are not only aware of local track conditions but also communicate with each other to maintain a coherent and safe flow of rail traffic, particularly in configurations where the decision made at one signal mast (B) directly influences the operational state of another mast (A) upstream.

## Application Scenarios

### BOD Card Configuration

1. <img src="{{ site.baseurl }}/assets/images/setup/BOD_Card_Line_CDI.png" style="zoom:50%; float:right;" />Using a CDI configuration tool, open the BOD Card(s) segment and update as follows:
2. Configure the card’s information  section and the communications  `COMM BUS`and `COMM ADDR` fields to match the corresponding selections on the BOD Card (PCB).
3. Refer to the `Line` tab for the line connected to the track block.  The default value for the `ON Event ID` will be used for setting up the signal masts aspect.  If available  in the configuration tool, use the `Copy` button to copy the Event ID to the clipboard for use later.



### Signal Mast Configuration

1. Using a CDI configuration tool, open the Signal Masts segment and update as follows:

2. Click on the `Card 1` and `Mast 1` tabs.  For this example, the card 1 is connected to a Signal Masts Breakout Board connected to the mast. 

3. Update the `Card Information Configuration` and `Card Communications Configuration` fields. 

4. Update the `Rule to Aspect Mapping Configuraton` as follows:

   <img src="{{ site.baseurl }}/assets/images/Setup/Mast_Rule_Def_CDI.png" style="zoom:70%;" />

| Field                       | Value         | Description                                                  |
| --------------------------- | ------------- | ------------------------------------------------------------ |
| Mast Operational Mode       | `Normal`      | Setting indicates the mast enabled in a nomal mode, not linked to any other masts. |
| Mast Identifier             | <user define> | Enter a value to identify the task.                          |
| Track Circuit Link Event ID | <not used>    | Configuring a track circuit is not needed for this example.  |
| Lamp Fade                   | `None`        | Setting indicates no fading of the lamp                      |



5. Configure the ‘Stop’ rule by configurating the `Rule 1`tab’s fields as shown to the right and detailed below:

<img src="{{ site.baseurl }}/assets/images/Setup/Mast_Rule_Stop_CDI.png" style="zoom:70%;" />



| Field                       | Value                      | Description                                                  |
| --------------------------- | -------------------------- | ------------------------------------------------------------ |
| Mast Operational Mode       | `Normal`                   | Setting indicates the mast enabled in a nomal mode, not linked to any other masts. |
| Mast Identifier             | <user define>              | Enter a value to identify the task.                          |
| Track Circuit Link Event ID | <not used>                 | Configuring a track circuit is not needed for this example.  |
| Lamp Fade                   | `None`                     | Setting indicates no fading of the lamp                      |
| Rules Configuration         | `Rule 1`(tab)              | Configure the the 1st rule                                   |
| Rule Name                   | `0-Stop`                   | Selection identifies the rule being configured               |
| Rule Track Speed            | `Stop`                     | Selection identifies the speed for the track.                |
| Rule’s Aspect Indicator     | `R/R - Stop before Signal` | Selection identifies the aspect to be shown.                 |
| Set Aspect Event ID         | <use default>              | The Event ID to set the aspect.  Used with Logics and Conditionals for setting the aspect. |
| Aspect Set Event ID         | <use default>              | Not used.                                                    |
| Aspect Cleared Event ID     | <use default>              | Not used.                                                    |
| Lamps Configuration         | `Lamp 1` (tab)             | Selection identifies configuration for the first lamp.       |
| Lamp Selection              | `LED_1`                    | Select the LED number associated with the lamp associated the wired mast. |
| Lamp Phase                  | `Steady`                   | Selection indicates the lamp is to remain steadyly lite.     |
| Lamp Brightness             | `50`                       | Selection indicates the lamp is be set a 50% brightness, a good starting point. |
| Lamp Glow Effect Duration   | <use default>              | Selection identifies a normal glow of the lamp.              |

6. Configure the ‘Clear’ rule by configurating the `Rule 2`tab’s fields as shown to the right and detailed below:

<img src="{{ site.baseurl }}/assets/images/Setup/Mast_Rule_Clear_CDI.png" style="zoom:50%; float:left;" />

| Field                     | Value                       | Description                                                  |
| ------------------------- | --------------------------- | ------------------------------------------------------------ |
| Rules Configuration       | `Rule 2`(tab)               | Configure the the 2nd rule (for normal speed)                |
| Rule Name                 | `29-Clear`                  | Selection identifies the rule being configured               |
| Track Speed               | `Clear`                     | Selection identifies the speed for the track.                |
| Aspect Indicator          | `G/R - Proceed on Mainline` | Selection identifies the aspect to be shown for the desired speed. |
| Set Aspect Event ID       | <use default>               | The Event ID to set the aspect.  Used with Logics and Conditionals for setting the aspect. |
| Aspect Set Event ID       | <use default>               | Not used.                                                    |
| Aspect Cleared Event ID   | <use default>               | Not used.                                                    |
| Lamps Configuration       | `Lamp 1` (tab)              | Selection identifies configuration for the first lamp.       |
| Lamp Selection            | `LED_1`                     | Select the LED number associated with the lamp associated the wired mast. |
| Lamp Phase                | `Steady`                    | Selection indicates the lamp is to remain steadyly lite.     |
| Lamp Brightness           | `50`                        | Selection indicates the lamp is be set a 50% brightness, a good starting point. |
| Lamp Glow Effect Duration | <use default>               | Selection identifies a normal glow of the lamp.              |

#### Logics and Conditionals Configuration

For this simple signaling example, we can use just one Logic statement to configure the mast to show the correct aspects for stop or clear based on the track occupancy downstream.

The logic statement looks like this: **IF** (Block is Occupied) **THEN** Set Aspect to `Stop` **ELSE** Set Aspect to `Clear`.

- Since only one logic statement is needed, for the **Logic Group** indicate that the logic is that last one for the group. 
- For the conditional, define use a single Condition (V1) configured to check for the ‘occupied’ Event ID what would be produced by the BOD Card’s configuration for the connected track block that is downstream of the mast. 
- For the **True** action, configure the Event ID for setting the Mast **Stop** aspect, which was previously defined by configuring the Masts `Rule 1`.  
- For the **Flase** action, configure the Event ID for setting the Mast **Clear** aspect, which was previously defined by configuring the Masts `Rule 2`.
- For both actions, configure the action to be performed immediately and to stop processing after the Event ID is sent.

Below are the detailed steps for configuring this example:

1. Using a CDI configuration tool, open the Logics and Conditionals segment and update as follows:
2. Click on the `Logic 1` tab.
3. Set the group processing information and define the conditional as follow:

<img src="{{ site.baseurl }}/assets/images/Setup/Logics_Example.1_Condition_1_CDI.png" style="zoom:70%;" />

| Field                           | Value                                        | Description                                                  |
| ------------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| Description                     | Main Line Signal Control                     | A label describing the purpose of the logic, such as managing the main line signal. |
| Group Functionality of Logic    | `Last...`                                    | Setting indicates that this is the ‘Last’ logic statement in a group.  In this example, a group of only 1 logic.  All other logics in the table will default to `Blocked` and will be ignored (not used). |
| Condition 1 Configuration       |                                              | The following fields define the logic conditional’s first condition, Condition 1. |
| Condition 1 Source              | `Event ID`                                   | Identifies the source for the condition.  This Logic’s conditional uses an`Event ID` (block’s occupied status) to determine its state for true/false.  The Event ID from the BOD Card configuration is specified below. |
| Condition’s Trigger             | `When Condition's Event ID or Speed Changes` | Selection indicates that the condition’s is triggered by a change in the Event ID which occurs with the BOD Card detects a track occupancy change. |
| Condition’s Track Circuit Speed | <not used>                                   | This is only used condition’s souce is a Track Circuit (`Speed from Track Circuit #`). |
| Condition’s True Event ID       | <Occupied Event ID>                          | Enter an Event ID that triggers this condition to be true.  Use the `On Event ID` value configured for the BOD Card’s block that is produced when the downstream block is occupied.  If possible, simply copy and paste the Event ID found in the BOD Card `Line` associated with the block. |
| Condition’s False Event ID      | <Cleared Event ID>                           | Enter an Event ID that triggers this Condition to be false.  Use the `Off Event ID` value configured for the BOD Card’s block that is produced when the downstream block is cleared (not occupied).  If possible, simply copy and paste the Event ID found in the BOD Card `Line` associated with the block. |
| Logic Operations                | `Condition 1 Only`                           | Indicates how the Logic Conditional is be processed using only Condition 1. |

>  Configuration of `Condition 2` is not required since the conditional only needs one Condition defined.  

4. Configure how the Logic is too be processed when the conditional is true and when it is false.  In both case, since there is only one logic in the group the processing should exit the group and that both actions should be processed immediately.

   <img src="{{ site.baseurl }}/assets/images/Setup/Logics_Example.1_Action_CDI.png" style="zoom:50%; float:left;" />

| Field                   | Value                  | Description                                                  |
| ----------------------- | ---------------------- | ------------------------------------------------------------ |
| Logic’s Flow When True  | `Send then Exit Group` | Setting indicates that processing of the logic group terminates after handling the logic’s **true** condition.  No other logics are necessary for setting the signal mast aspects. |
| Logic’s Flow When False | `Send then Exit Group` | Setting indicates that processing of the logics group terminates after handling the logic’s **false** condition.  No other logics are necessary for setting the signal mast aspects. |
| Action’s Time Delay     | `0`                    | Setting indicates that the logic’s actions should take place immediately, causing the aspect to be set immediately. |
| Action’s Time Interval  | <not used>             | Not used since the `Timing` is set to 0.                     |
| Action Retriggerable    | `No`                   | Setting indicates the logic’s actions can NOT be retriggered again after completion. |

6. Configure two actions, one for when the conditional is true (track block is occupied) and one when the conditional is false.  In both cases, Event IDs are sent to set the appropriate aspect for the mast.

   <img src="{{ site.baseurl }}/assets/images/Setup/Logics_Example.1_Action.1_CDI.png" style="zoom:70%; float:left;" />

| Field                   | Value                     | Description                                                  |
| ----------------------- | ------------------------- | ------------------------------------------------------------ |
| Action(s) Configuration | `Action 1` (tab)          | The first action configured will set the mast aspect for the Rule Name `0-Stop`. |
| Action Trigger          | `Immediately if True `    | Selection indicates the action is to occur immediately if the conditional is **True** (i.e. the block is occupied).  The actual action produces the following Event ID. |
| Action Event ID         | `05.01.01.01.5C.65.06.03` | Enter the `Set Aspect Event ID` from `Mast 1`, `Rule 1` which is configured for `0-Stop` rule with an aspect for a `Stop` speed. |
| Action(s) Configuration | `Action 2` (tab)          | The second action configured will set the mast aspect for the Rule Name `29-Clear`. |
| Action Trigger          | `Immediately if False `   | Selection indicates the action is to occur immediately if the conditional is **False** (i.e. the block is unoccupied).  The actual action produces the following Event ID. |
| Action Event ID         | `05.01.01.01.5C.65.06.02` | Enter the `Set Aspect Event ID` from `Mast 1`, `Rule 2` which is configured for `29-Clear` rule with an aspect for `Normal` speed. |
