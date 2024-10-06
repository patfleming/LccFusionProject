---
title: LED Resistor Selection
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Builder's Resources & Tips
use_cases:
  - PCB Design & Assembly
  - Automation Deployment
  - Device Control
  - Learning & Planning
---
# Choosing the Right Resistor for LEDs {#Resistor_Selection}

## Introduction

Several of our cards are designed to connect directly to LEDs. Selecting the appropriate current-limiting resistor for the circuit connected to the LED is crucial. The IO Card, for instance, supports outputs of both 5V and 12V (for the entire card), allows for the use of resistors of varying values, and offers the option to bypass the resistor entirely.  

#### LED Illumination 

For layout automation, including various signal types, it's important to select a brightness level that is visible yet not excessively bright, to mimic the realistic lighting of homes, businesses, and actual railway signals. For an outdoor light from the 1950s (resembling tungsten bulbs), you might aim for a yellowish light that covers about 6 feet, translating to less than an inch in HO scale.

To determine the card configuration, start with an online LED resistor calculator, available in the References section ([LED Resistor Calculator](@ref led-calculator)).

The choice of current-limiting resistor is influenced by the LED's current requirement (measured in mA). Brighter LEDs require higher current, typically up to 20mA for full brightness. The relationship between the resistor value, current, and LED brightness is linear. Doubling the resistor value cuts the current and brightness by half.

#### LED Color (Hue)

The forward voltage of an LED depends on its color. Red, Yellow, Green, and Orange LEDs typically require about 2V, whereas White and Blue LEDs need around 3.6V.

> The LED's color is a factor in resistor selection to ensure consistent brightness.

#### Configuring LEDs: Series vs Parallel

LEDs connected in series experience a voltage drop, as the total supply voltage is divided equally among them. Our LED calculator can help with configurations involving multiple LEDs in series.  

> Be aware that if one LED in a series fails, the entire circuit is disrupted, turning off all LEDs.

In a parallel arrangement, LEDs receive the full supply voltage, but the supply current increases as LEDs are added.  Maintaining LED brightness request each of the LEDs to have it's own current limiting resistor.  Thus, the current limiting resistor bypass switch (SW1, SW2) corresponding to the output line should be set ON when using parallel  resistor-LED pairs with 

> Adding a second LED in parallel typically results in a 50% reduction in brightness per LED. Halving the resistor value can maintain the original brightness.

#### Example Configurations

The table below shows calculated values for Vcc, resistor, and LED brightness for a single LED connected in series on a card output line, using the [LED Calculator](led-calculator):

| Vcc  | LED Color               | Resistor (&Omega;) | LED Brightness (%) | Current (mA) |
| :--: | ----------------------- | :----------------: | :----------------: | :----------: |
|  5   | Red/Yellow/Green/Orange |  150 / 750 / 1.5k  |   100 / 50 / 10    |  20 / 10 /2  |
|  5   | White/Blue              |   70/ 140 / 700    |   100 / 50 / 10    | 20 / 10 / 2  |
|  12  | Red/Yellow/Green/Orange |   500 / 1k / 5k    |   100 / 50 / 10    | 20 / 10 / 2  |
|  12  | White/Blue              |  420 / 840 / 4.2k  |   100 / 50 / 10    | 20 / 10 / 2  |

### References

@anchor led-calculator

1. [LED Resistor Calculator (Circuit Digest)](https://circuitdigest.com/calculators/led-resistor-calculator)