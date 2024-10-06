---
title: Builder's Resources & Tips
layout: default
permalink: /:name/
nav_order: 3
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
  - Device Control
  - Automation Deployment
has_children: True
---



# Introduction

The following is a set of tips and guides for working the LCC Fusion Project’s PCB building and concepts.

### Utilizing Both BLVD and BOD Cards

To ensure comprehensive monitoring and protection of your model railway system, it is recommended that users install both the Block Low Voltage Detection (BLVD) Card and the Block Occupancy Detection (BOD) Card with polyfuses for all track blocks.

### How They Work Together:

1. **BOD Card with Polyfuse**:
   - **Purpose**: Detects occupancy by measuring current flow and protects against short circuits with a 1.5A polyfuse.
   - **Short Circuit Protection**: The polyfuse trips during a short circuit, significantly reducing current flow and causing a voltage drop.
2. **BLVD Card**:
   - **Purpose**: Monitors the voltage levels across track blocks.
   - **Low Voltage Detection**: Detects when the voltage drops below 12V, which can indicate a short circuit, excessive load, or other issues.

### User Benefit:

- **Enhanced Protection**: The BOD Card protects against short circuits, while the BLVD Card alerts you to low voltage conditions.
- **Comprehensive Monitoring**: Using both cards together ensures you are alerted to both current and voltage-related issues, providing a more robust and reliable monitoring system.

### Installation Recommendation:

- Install a BOD Card with a polyfused for each track block to handle short circuits and detect occupancy.
- Install a BLVD Card for each track block to monitor voltage levels and detect low voltage conditions.
- This dual-card setup ensures that any significant voltage drop, such as from a short circuit, will be detected and addressed promptly.

By using both the BLVD and BOD Cards, you can ensure the safe and efficient operation of your model railway system, with comprehensive protection and monitoring for all track blocks.



