---
title: Firmware Planning Guide
typora-root-url: ..
layout: default
permalink: /:name/
nav_order: 2
use_cases:
  - Learning & Planning
---

# Firmware Planning Guide {#firmware-planning-guide}

Below is a list of available firmware files, categorized by their use case (solution), version, and download links. You can flash the firmware directly to your ESP device by clicking the desired firmware version.

| Solution       | Version |                           Install                            | Description                                                  |
| -------------- | ------- | :----------------------------------------------------------: | ------------------------------------------------------------ |
| Serial Monitor | v1.0.0  | [](#) <esp-web-install-button manifest="https://patfleming.github.io/LccFusionProject/manifests/esp32/serial-monitor/v1.0.0/manifest.json"></esp-web-install-button> | Provides a serial monitor for monitoring LCC Fusion Node messages, including Bluetooth Serial Monitor (phone) app |

## Notes:
- *Browser Support**: Ensure you're using a browser like Chrome or Edge that supports the Web Serial API for flashing ESP devices via USB.
- **Instructions**: Once you connect your ESP device via USB and click the "Download and Flash" button, the firmware will be flashed directly to your device.

<!-- Load the ESP Web Tools Install Button -->

<script
  type="module"
  src="https://unpkg.com/esp-web-tools@10/dist/web/install-button.js?module"
></script>
