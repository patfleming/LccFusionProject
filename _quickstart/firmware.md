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

Below is a list of available firmware files, categorized by their use case (solution), version, and download links. You can download the firmware directly to your ESP device by clicking the desired firmware version.

To update the firmware on your ESP32, follow these simple steps:

1. **Click one of the blue "Connect" buttons from the table below** to begin.
2. **Select the serial port** where your ESP32 is connected from the list, then click the "Connect" button at the bottom.
3. Choose the **"Install..." option** to start the firmware update process.
4. **Click the "Install" button** to begin installing the new firmware.
5. Watch the progress as the current firmware is erased, and the new firmware is copied to your ESP32.
6. Once it's done, click **"Next"**, and you can optionally review the installation log if you'd like.

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
