---
title: Troubleshooting Card Communications
typora-root-url: ..
layout: default
permalink: /:name/
parent: Builder's Resources & Tips
use_cases:
  - PCB Design & Assembly
  - Learning & Planning
  - Hardware Testing & Maintenance
---
# Troubleshooting Hardware Communications {#trouble_shooting_I2C}
{:toc}
## Introduction

When an I2C-enabled card is not detected while monitoring the serial output of the ESP32 Node, consider the following steps:

- **Checking the I2C Data Transmission Indicator**: 
  - Observe the indicator on the Node Bus Hub immediately after rebooting. A flashing light suggests the Node is attempting to establish an I2C connection with the card. 
    - Note: If there is no data transmission, this could indicate an issue with the Node Bus Hub or the LCC Fusion Node Card (either firmware or hardware-related).

- **Configuration Settings**: 
  - Ensure the bus and address settings on the card correspond with the I2C card's CDI configuration. 
  - Be mindful that DIP switches are sensitive to their exact positions, which can affect connectivity.

- **Continuity Checks**:
  - Confirm that both the LCC Fusion Node Card and the I2C-enabled card are inserted into the same Node Bus Hub. Testing different Node Bus Hub connectors can also be helpful. Validate the integrity of the Node Bus Hub itself.
  - Check if the Node Bus Hub's power indicator is on, signifying that power is being supplied from the LCC Fusion Node Card to the Node Bus Hub and its connected cards.
  - Measure 5V at the corresponding IC pin for the I2C address when the DIP switch is set to ON. Refer to the PCB documentation to locate the correct IC pins.
  - Assess the continuity of the I2C communication bus by checking the connections between the SDA/SCL and the corresponding IC pins when jumpers are in place.
