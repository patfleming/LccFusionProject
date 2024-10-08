---
title: Node Card Configuration Guide
typora-root-url: ..
layout: default
permalink: /:name/
parent: Card Configuration Guides
nav_order: 2
use_cases:
  - Node Cluster Setup
  - System Configuration
  - Device Control
---

# LCC Fusion Node Card Configuration Guide {#node_card_configuration}

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



## LCC Fusion Node Card firmware Configuration for LCC Events

This part will detail the process for configuring the firmware to handle LCC events related to the **LCC Fusion Project LCC Fusion Node Card**. Using the  LCC Configuration Tool, it will outline steps to integrate the card with the LCC Fusion firmware, setting up LCC Event IDs to drive output devices. <img src="/_setup{{ site.baseurl }}/assets/images/BOD_Card_CDI.png" style="zoom:50%;float:right" />

1. Using the [LCC Configuration Tool]({{ site.baseurl }}/assets/images/howto/CDI_VIewer_Open/) find the LCC Node and open the configuration.
2. Scroll down to the LCC Fusion Node Card segment and click on the twistie to open the configuration dialog box for the card
3. Select the tab for the specific line to be configured.  Note that unconnected lines can be configured for future use.
4. Make changes and click **Write** to save the change.
5. After all changes are made, click **Refresh** to verify changes took affect. 

Below are the card dialog configuration options for this card (refer to diagram on right):

> After changing fields, click the **Write** button to save the changes.

### Conifguring LCC Fusion Node Card I/O Lines 

The configuration interface dialog (see image on right) for a LCC Fusion Node Card, as presented in the JMRI Configuration Tool, includes several sections that allow for the customization and setup of the RJ45 I/O pins within a model railroad environment:

Here you can assign names and descriptions to individual I/O lines suppported by the LCC Fusion Node Card. Each line corresponds to one of the RJ45 lines for I/O.

1. #### Description:

   1. A field for providing a description for each line, which could detail the function or physical location of the Input/Sensor device connected to that line.

2. #### Initial Line State at Power-On:

   - This setting determines the default state of the output line  when the system is powered on. Options include 'On' for active, 'Off' for inactive, and 'Previous' to retain the state from before the system was last shut down.

3. #### Line Type and Corresponding Fields

   - ##### Digital Input, Output, and I/O

      - Use to turn devices on/off using a digital signal (TTL).  Devices include LEDs, relays, etc.

      - `Pull Up-Down Resistor`

        - **None:** No internal pull-up or pull-down resistor. The pin will be floating when not driven.

          **Pull-Up:** Enables the internal pull-up resistor, pulling the pin to a high state when not driven.

          **Pull-Down:** Enables the internal pull-down resistor, pulling the pin to a low state when not driven.

          **Pull-Up and Pull-Down:** Enables both pull-up and pull-down resistors. This is generally not used but is included for completeness.

        - **Pull-Up and Pull-Down:** Enable both pull-up and pull-down resistors (though this is rarely used, it is technically possible).

      - `Debounce Duration`

        1. For **Input** and **I/O**: This value sets the stabilization wait time before the Ievent is triggered to avoid false detections due to noise. The duration is in increments of 30 milliseconds.
     2. For **Output**: N/A
     
   - `SetOnEvent ID and SetOffEvent ID`
     
     - Used for Digital **Output** and **I/O**, these fields are for entering the Event IDs that are consumed to trigger the digital output line to go High (5V) or Low (0V).
     
   - `OnEvent ID and OffEvent ID`
     
        - Used for Digital **Input** and **I/O**, these fields are for entering the Event IDs that are produced when the line goes High (5V) or Low (0V).

   - ##### PWM Output

      - `Frequency (Hz)` The PWM frequency, which is device-dependent.

      - `Duty Cycle (%)` The PWM duty cycle, expressed as a percentage of the on-time in one cycle. 

      - `PWM Mode`The duration over which the PWM signal varies, creating effects like glowing for LEDs.

        - **NONE**: No special effect. The PWM signal operates normally, suitable for motor or servo control where precise duty cycle control is needed.
        - **SLOW**: Creates a slow, gradual effect over time. Ideal for applications like slow LED fading or other effects that require a longer period.
        - **MEDIUM**: Creates a moderate effect over time. Useful for applications like medium-speed LED pulsing or other effects that require a balanced period.
        - **FAST**: Creates a fast effect over time. Best for applications like rapid LED blinking or other effects that require a short period.

      - `**SetOnEvent ID and SetOffEvent ID:**`

        - These fields are for entering the Event IDs that are consumed to trigger the digital output line to go High (5V) or Low (0V).

        - Below is a summary field’s purpose by PWM device type.

        | **Device Type** | **Frequency (Hz)** | **Duty Cycle (%)** | **PWM Mode**             |
        | --------------- | ------------------ | ------------------ | ------------------------ |
        | **LED**         | 1000               | 0-100 (Brightness) | Slow, Medium, Fast, None |
        | **Motor**       | 1000-20000         | 0-100 (Speed)      | None                     |
        | **Servo**       | 50                 | 5-10 (Position)    | None                     |

   - ##### Touch Input

     - `Sensitivity`
       - **Values:** Low, Medium, High

       - **Description:** Adjusts how responsive the touch sensor is to touch events. Higher sensitivity means the sensor is more responsive to lighter touches.

     - `Threshold`
       - **Values:** Defines the capacitive value that must be exceeded to register a touch event.  Typically in the range of 0 to 4095 (for 12-bit resolution).
       - **Description:** Sets the capacitive value that must be exceeded to register a touch event. A lower threshold makes the sensor more sensitive, while a higher threshold reduces sensitivity to avoid false positives.
     - `OnEvent ID and OffEvent ID:`
       - These fields are for entering the Event IDs that are produced when the line goes High (5V) or Low (0V).

   - ##### ADC (Analog to Digital Converter) Input

      ​	Read analog values from sensors.
      
      - `Number of Levels`: Sets the number of discrete levels the ADC can measure; 512 (9-bit), 1024 (10-bit), 2048 (11-bit), 4096 (12-bit)
      
      - `Max Voltage`: Sets the maximum voltage range for the ADC input; 1.1V, 1.5V, 2.2V, 3.9V
      
         **Trigger Range**
         - `Trigger High:` The high threshold value that will trigger an event when exceeded.
         - `Trigger Low:` The low threshold value that will trigger an event when the reading goes below it.
      
      - `**OnEvent ID and OffEvent ID:**`
      
         - These fields are for entering the Event IDs that are produced when the line is triggered.  That is the analog value is within the **Trigger Range**.
