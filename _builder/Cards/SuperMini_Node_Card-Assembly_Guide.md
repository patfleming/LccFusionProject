---

title: SuperMini Node Card Assembly Guide
typora-root-url: ../..
layout: default
permalink: /:name/
parent: Card Assembly Guides
nav_order: 1
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
  - Device Control
subjects:
  - Hardware
  - Assembly Guides
terms:
  # LCC Fusion Project Terms
  - lcc_fusion_cards
  - lcc_fusion_project
  - lcc_fusion_node_bus

  # LCC Fusion Connect Terms
  - lcc_fusion_node_card

  # NMRA LCC Network Terms
  - lcc_event_monitoring_tool
  - lcc_configuration_tool
  - lcc_event_id

  # Model Railroad Automation Terms
  # Hardware and firmware Terms
  - bus
  - can_network
  - cleaning_pcb
  - component
  - current_limiting_resistor
  - decoupling_capacitor
  - edge_card_connector
  - esd_protection_diode
  - esp32_s3
  - ferrite_bead
  - gpio_expander
  - jumper_caps
  - i2c
  - i2c_bus
  - network_cable
  - polyfuse
  - stencil
  - tvs_diode
---
# SuperMini LCC Fusion Node Card Assembly Guide {#supermini-node_card_assembly}
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

In conjunction with the **LCC Fusion Project** Node Bus Hub, the  SuperMini Node Card provides four (4) LCC compatible Nodes.  Typically, in an LCC Fusion Project project, the  SuperMini Node Card is placed into a LCC Fusion Node Cluster using a Node Bus Hub to connect a **LCC Fusion Node Card**, **Power Module**, and optional **LCC Fusion Project** I/O cards.

{% include terminology.html %}

## Specifications

Specifications for the card include:

| Characteristic                                               |                   |
| ------------------------------------------------------------ | ----------------- |
| Super-Mini ESP32-S3 Development Boards                       | 4                 |
| Max Input / Output Lines                                     | 32                |
| Max Output Per Line                                          | 12mA<sup>2</sup>  |
| Max Input/Output per ESP32-S3                                | 120mA             |
| Minimum Current Draw per SuperMini ESP32-S3 Development Boards (idle CPU, no Wi-Fi, no Bluetooth) | 40mA<sup>1</sup>  |
| Maximum Current Draw per SuperMini ESP32-S3 Development Boards (active Wi-Fi and Bluetooth) | 500mA<sup>1</sup> |
| Maximum Current Draw per Card (4 boards, active with both Wi-Fi and Bluetooth) | 2A                |

1. Maximum current is based on the Node’s firmware configuration (WiFi and BT) and activity (idle/active).  

1. Consider using a  resistor inline with output lines to LEDs to reduce the current draw.  For example, a 150Ω resistor inline with to a Red LED witha forward voltage of 2v reduces the current to about 8.6mA. 

   | Component     | Idle Current (mA) | Active Current (mA) |
   | ------------- | ----------------- | ------------------- |
   | **CPU**       | 40-50             | 50                  |
   | **Bluetooth** | 30                | 60-100              |
   | **Wi-Fi**     | 80-90             | 160-260             |


### How It Works

The SuperMini Node Card allows up to 4 Super-Mini ESP32-S3  boards to be installed in sockets.  Each ESP32 supports 8 I/O lines via a RJ45 socket and I2C to other **LCC Fusion Project** I/O cards.  Each I/O line can be configured independently via the CDI to be digital input, digital output, ADC, touch or PWM.  

The card is connected to the LCC Fusion Node Bus Hub for 5V and 3v3 power, dual I2C, and CAN Network.

Each Super-Mini board can independently use wireless to:

- bridge to the wired CAN Network via the Node Bus Hub
- connect to I/O cards a Node I/O controller
- Bluetooth to LCC Fusion Configuration Tool
- Bluetooth to serial terminal app for monitoring

#### Auto Termination Circuit for CAN Bus

The **LCC Fusion Node Cards** utilize an **automatic CAN bus termination circuit** to ensure proper signal integrity while avoiding manual jumper settings by the end user. The termination is dynamically activated when necessary, preventing signal reflections that can occur at open-ended or improperly terminated CAN bus lines.

**Why Termination is Important:**
- The CAN bus requires **120Ω termination resistors** at both ends of the network to prevent **signal reflections**. These reflections can cause data corruption and reduce communication reliability. Without termination, the CAN signals can bounce back along the cable, interfering with valid data transmissions.
- The **auto termination** circuit monitors the CAN bus and automatically activates termination at the network endpoints, ensuring proper signal termination without user intervention.

**How It Works:**

- The auto termination circuit uses two **BSS138 MOSFETs** to control the connection of **two 60Ω resistors** and a **47nF capacitor** across the CAN lines.
  

**Circuit Breakdown:**

1. **CAN-H and CAN-L Termination:**
   - The termination consists of **two 60Ω resistors** connected in series between **CAN-H** and **CAN-L**. The junction between these resistors is connected to **GND** through a **47nF capacitor** to filter noise and improve signal integrity.
   
2. **BSS138 MOSFET Control:**
   - The two **BSS138 MOSFETs** control the connection of the **60Ω resistors**. When the MOSFETs are turned on, the resistors and capacitor are connected to the CAN bus, providing the required termination.
   - The **sources** of the MOSFETs are connected to the ends of the two 60Ω resistors, while the **drains** are connected to **CAN-H** and **CAN-L** respectively.

3. **Activation via Comparator:**
   - The **gates** of the MOSFETs are controlled by a **comparator (LM393)**, which monitors the CAN bus voltage levels.
   - The comparator is set with a **2.4V reference voltage** from a Zener diode to detect when the CAN bus reaches the appropriate voltage levels for termination.
   - When the bus voltage meets the termination condition, the **MOSFET gates** are activated, and the termination circuit is connected.

4. **Capacitor and Noise Filtering:**
   - The **47nF capacitor** at the junction of the two resistors is connected to **GND**. This capacitor filters out high-frequency noise, ensuring stable CAN bus communication even in the presence of electrical interference.

**Advantages:**
- **Dynamic Activation**: The termination circuit is automatically activated only when needed, preventing unnecessary load on the CAN bus during normal operation.
- **Simplified Installation**: Users do not need to manually configure jumpers or worry about termination placement. The circuit automatically handles termination at the network endpoints.
- **Improved Signal Integrity**: The use of **MOSFETs** ensures that termination resistors and the capacitor are only engaged when required, preventing reflections and maintaining optimal signal quality.
### Protection 

The SuperMini LCC Fusion Node Card integrates multiple Super-Mini ESP32-C3 boards and includes robust protection components to ensure reliable operation. Below is an overview of each protection element integrated into the SuperMini LCC Fusion Node Card and its role:

| Protected Component                            | Protection Component              | Function                                                     | Specifications                                               | Location                                                     |
| ---------------------------------------------- | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Each Super-Mini ESP32-C3 Development Board** | **Decoupling Capacitors**         | Filters out high-frequency noise and transient voltage spikes from the power supply, ensuring stable voltage for each ESP32-C3. | **Values:** 0.1 µF ceramic, 10 µF electrolytic or ceramic    | Across Vcc and GND near each ESP32-C3                        |
| **CAN Bus (each set)**                         | **Automatic Termination**         | Provides proper termination to prevent signal reflections on the CAN bus. | **Value:** 2x 60 ohms in series (120 ohms)                   | Across CANH and CANL lines, automatically applied based on CAN network voltage while using a low-pass filter to measure peak voltage. |
| **CAN Bus (each set)**                         | **ESD Protection Diode PESD1CAN** | Protects the CAN bus lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Across CANH to GND and CANL to GND                           |
| **I2C Lines**                                  | **Ferrite Bead BLM31PG121SN1L**   | Provides high-frequency noise suppression on the I2C lines.  | **Impedance:** 120 ohms at 100 MHz                           | In series with the SDA and SCL lines of the I2C bus          |
| **I2C Lines**                                  | **ESD Protection Diode PESD1CAN** | Protects the I2C lines from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Across the SDA and SCL lines to GND                          |
| **GPIO to RJ45 Sockets**                       | **Current Limiting Resistor**     | Limits current to protect GPIO pins from accidental shorts.  | **Value:** 150 ohms                                          | In series with each GPIO pin                                 |
| **GPIO to RJ45 Sockets**                       | **ESD Protection Diode PESD1CAN** | Protects two GPIO pins from electrostatic discharge and voltage spikes. | **Reverse Stand-off Voltage (Vr):** 24V<br>**Clamping Voltage (Vc):** 40V | Pin 1 to GPIO1, Pin 2 to GND, Pin 3 to GPIO2                 |
| **GPIO to RJ45 Sockets**                       | **TVS Diode SMAJ5A**              | Clamps high-voltage transients to protect GPIO pins.         | **Stand-off Voltage:** 5V<br>**Clamping Voltage:** 9.2V      | Across each GPIO pin to GND                                  |
| **GPIO to RJ45 Sockets**                       | **RJ45 Sockets**                  | Connect 8 GPIO pins from each Super-Mini ESP32-C3 for I/O purposes. | **Pins:** 8                                                  | Connected to each set of Super-Mini ESP32-C3 pins            |
| **Input Vcc**                                  | **Protected via Power Module**    | The input Vcc is protected by the Power Module, which includes a polyfuse and TVS diode for overcurrent and overvoltage protection. | **PPTC Polyfuse:**<br>**TVS Diode:** SMBJ18A                 | From Power Module to LCC Fusion Node Card Vcc |
| **Ground Bus**                                 | **48mil Ground Bus**              | Provides a low-resistance path for all protection components, ensuring effective grounding and noise suppression. | **Width:** 48 mil                                            | Used by all protection components                            |

### Summary
These protection components work together to safeguard the SuperMini LCC Fusion Node Card from various electrical faults. The decoupling capacitors filter out noise and transient voltage spikes, ensuring stable power for each Super-Mini ESP32-C3. The jumper-selectable termination resistor, made of two 60-ohm resistors in series, ensures proper signal integrity on the CAN bus by allowing termination to be enabled or disabled as needed, while the ESD protection diodes protect the CAN and I2C lines from voltage spikes and electrostatic discharge. The ferrite bead suppresses high-frequency noise on the I2C lines. The current limiting resistors, ESD protection diodes, and TVS diodes protect the GPIO pins connected via the RJ45 sockets from electrostatic discharge, overvoltage, and accidental shorts. The RJ45 sockets facilitate I/O connections from the Super-Mini ESP32-C3. The input Vcc is already protected by the Power Module, which includes a polyfuse, TVS diode, and SS310 diodes for overcurrent and overvoltage protection before reaching the SuperMini LCC Fusion Node Card. Together, these components ensure the SuperMini LCC Fusion Node Card operates reliably in a potentially harsh electrical environment.



 ## Components List

PCB for the LCC Fusion Node Card can be ordered from any PCB fabricator using these [Gerber Files]({{site.gerber_dir}}LCC Fusion Node Card.zip).

[PCB Components](/pcb-parts/) - listing of items used for PCB assembly

[PCB Components](/pcb-components/) - listing of components used for PCB assembly

Below is a list of the PCB components used for this card (see diagram on right for reference): 

| Component Identifier | Count | Type                    | Value/Description                                            | Package    | Required? | Purpose                                                      |
| -------------------- | ----- | ----------------------- | ------------------------------------------------------------ | ---------- | --------- | ------------------------------------------------------------ |
| BZ1 - BZ4            | 4     | Piezo Active Buzzer     | 9650-5V                                                      | SMD        | Optional  | Buzzer for audio status indicator                            |
| C1, C3, C5, C7, C9   | 5     | Ceramic Capacitor       | 0.1uF                                                        | 1206 SMD   | Required  | IC protection                                                |
| C2, C4, C6, C8       | 4     | Ceramic Capacitor       | 10uF                                                         | 1206 SMD   | Required  | IC protection                                                |
| C9                   | 1     | Ceramic Capacitor       | 0.1uF                                                        | SMD 1206   | Required  | Filters high-frequency noise from CAN signals, smoothing the voltage for the comparator |
| C10                  | 1     | Ceramic Capacitor       | 47nF                                                         | SMD 1206   | Required  | Filters high-frequency noise from CAN-H and CAN-L lines      |
| D1 - D32             | 32    | TVS Diode                   | SMAJ5A                                                       | SMB        | Required  | GPIO pin Transient Voltage Spike (TVS) protection            |
| D33 - D48            | 16    | ESD Diode                   | PESD1CAN                                                     | SOT-23 SMD | Optional  | GPIO pin electrostatic discharge (ESD) protection            |
| D49                  | 1     | ESD Diode                   | PESD1CAN                                                     | SOT-23 SMD | Optional  | CAN Network Bus electrostatic discharge (ESD) protection     |
| D50, D51             | 2     | ESD Diode                   | PESD1CAN                                                     | SOT-23 SMD | Optional  | I2C data bus electrostatic discharge (ESD) protection        |
| D52 - D55            | 4     | Diode                   | SS310                                                        | SMA        | Optional  | Required when installing Buzzer (BZ1)                        |
| FB1, FB2             | 2     | Ferrite Bead            | BLM31PG121SN1L                                               | 1206 SMD   | Required  | CAN Network Bus Data Line Noise Suppression Ferrite Bead     |
| FB3 - FB6            | 4     | Ferrite Bead            | BLM31PG121SN1L                                               | 1206 SMD   | Required  | I2C Data Line Noise Suppression Ferrite Bead                 |
| J1 - J4              | 4     | RJ45 Socket             | 8P8C                                                         | PTH        | Optional  | Network cable (CAT5/6) connection to I/O devices             |
| J5 - J8              | 4     | Female Headers          | 9-Pin                                                        | PTH        | Optional  | Socket for Super-Mini ESP32-S3 development board(s)          |
| JP1 - JP4            | 4     | Male Pin Header         | 3-Pin                                                        | PTH        | Required  | Line 8 selection (GND or I/O line)                           |
| JP5                  | 1     | Male Pin Header         | 2-Pin                                                        | PTH        | Optional  | Used to set the CAN Bus termination using Jumper Caps        |
| Q1, Q2               | 2     | Transistor              | BSS138                                                       | SOT-23     | Required  | Controls CAN connections to terminator                       |
| R1 - R32             | 32    | Resistor                | 120Ω                                                         | 1206 SMD   | Required  | Current limiting protection for GPIO pin                     |
| R33                  | 1     | Resistor                | 1kΩ                                                          | SMD 1206   | Required  | Current limiting for reference voltage                       |
| R34                  | 1     | Resistor                | 100Ω                                                         | SMD 1206   | Requried  | Low Pass Filter for low signal detection                     |
| R35, R36             | 2     | Resistor                | 60Ω                                                          | 1206 SMD   | Required  | CAN network (split) termination circuit                      |
| U1 - U4              | 4     | CAN Transceiver         | SN65HVD233DR                                                 | SMD        | Required  | CAN Transceiver for use with ESP32 to provide CAN communications |
| U5                   | 1     | IC (Voltage Comparator) | LM393 or LM2903N                                             | SO-8, SMD  | Required  | Used for detecting low voltage in the I2C lines (less than 2.4v) |
| SH1 - SH5            | 5     | Jumper Cap              | [Jumper Cap (2.54mm)](https://www.aliexpress.us/w/wholesale-jumper-caps.html?spm=a2g0o.detail.search.0) | 2.54mm     | Required  | Used with CAN Bus Termination. Recommend tall caps for ease of use. |
| ZD1                  | 1     | Zener-Diode             | 2.4V                                                         | BZT52      | Required  | Used for a 2.4V reference voltage                            |
|                      | 1     | Super-Mini ESP32-S3     | 18-Pin Version                                               | SMD        | Required  | MCU (processor) for the SuperMini LCC Fusion Node Card       |

## Tools Required

> [List of recommended tools](/pcb-tools/).

## Safety Precautions

- See [Safety Precautions](/safety-precautions/). 

## Assembly Instructions

<img src="/assets/images/pcbs/Node_Card/supermini-node_Card_pcb.png" style="zoom:40%; float:right" />Below are the high level steps for assembly of the Output Card:

1. Clean PCB with alcohol to remove residue.  See [Cleaning_PCB](/pcb-prep/) for details.

2. Use the SuperMini Node Card’s PCB stencil to apply the paste, align the stencil over the PCB using the 2 Tooling Holes located at the top and bottom of the card.  There are very small holes with no labels or markings.  Use a thick straight pin or wire for the alignment, pushing down into a soft foam surface to hold the pin/wire in place.

3. Apply soldering paste for all SMD components

4. The following table identifies which components are needed for each of the optionally installed ESP32 boards:

   | SuperMini Node | CAN IC | Resistor (optional) | Capacitors | Diodes           |
   | -------------- | ------ | ------------------- | ---------- | ---------------- |
   | 1              | U1     | R1-R8               | C1, C2     | D1-D8. D33-D36   |
   | 2              | U2     | R9-R16              | C3, C4     | D9-D16, D37, D40 |
   | 3              | U3     | R17-R24             | C5, C6     | D17-D24, D41-D44 |
   | 4              | U4     | R25-R32             | C7, C8     | D25-D32, D45-D48 |

5. Use the following to identify component requirements and orientation on the PCB:

   | Component Identifier | Component (Package)               | Required? | Orientation                                                  |
   | -------------------- | --------------------------------- | :-------- | ------------------------------------------------------------ |
   | BZ1 - BZ4            | Piezo Active Buzzer, 9650-5V, SMD | Optional  | None                                                         |
   | C1 - C9              | Capacitor, 0.1uF, 1206 SMD        | Required  | None                                                         |
   | C10                  | Capacitor, 47pF, 1206 SMD         | Required  | None                                                         |
   | D1-D32               | Diode, SMAJ5A, SMB                | Required  | None                                                         |
   | D33 - D51            | Diode, PESD1CAN, SOT-23 SMD       | Optional  | Fit only one way                                             |
   | D52-D55              | Diode, SS310, SMA                 | Optional  | Cathode end has a white line and positioned towards PCB **bottom** edge |
   | J1, J2, J3, J4       | RJ45 socket (8P8C)                | Optional  | Fit only one way                                             |
   | J5, J6, J7, J8       | 9-Pin Female Headers              | Optional  | None                                                         |
   | JP1 - JP5            | Male Pin Headers                  | Required  | None                                                         |
   | R1-R33               | Resistor, 120Ω, 1206 SMD          | Required  | None                                                         |
   | R34                  | Resistor, 100Ω, 1206 SMD          | Required  | None                                                         |
   | R35, R36             | Resistor, 60Ω, 1206 SMD           | Required  | None                                                         |
   | Q1, Q2               | Transistor, BSS138, SOT-23        | Required  | Fit only one way                                             |
   | FB1 - FB6            | Diode, BLM31PG121SN1L, 1206 SMD   | Required  | None                                                         |
   | U1, U2, U3, U4       | SN65HVD233DR IC                   | Required  | Package has small dimple in corner (pin 1) which is position to PCB **top** right edges |
   |                      | Super-Mini ESP32-S3               | Required  | Position Super-Mini ESP32-S3 development board’s USB connector to PCB **right** edge |
   | ZD1                  | 2.4V                              | Required  | Cathode end has a white line and positioned towards PCB **right** edge |

5. Place SMD components into paste.  Note the orientation of each IC.

6. Reflow the solder for the SMD component (refer to  [Soldering Tips](/pcb-soldering/)).

7. Place PTH components (starting with the smaller components).

   - RJ45 Sockets for CAN Wired Communications (J1, J2, J3, J4)

   - CAN Terminator selectors (JP1)

>  See also: [Soldering Tips](/pcb-soldering/)

## Testing and Verification

### Card Configuration

- If the SuperMini LCC Fusion Node Card is at the end of the CAN Bus Network, set the CAN TERM by placing a Jumper Cap on JP1.

### Visual Inspection

1. **Initial Check**: Examine the board for any obvious issues like missing components, solder bridges, or components that are misaligned or not fully seated.

2. **Solder Joint Inspection**: Use a magnifying glass or a microscope to inspect solder joints. Look for cold solder joints, insufficient or excessive solder, or any shorts between pads.

3. **Component Orientation**: the IC's are correctly oriented according to the PCB silkscreen or schematic.

### Connectivity Testing

1. **Continuity Check**: Use a multimeter in continuity mode to check for shorts between power rails and ground, and to ensure there are no open circuits in critical connections.

### Power-Up Tests

1. Assembly a tested Power Module to the LCC Fusion Node Card.
2. **Apply Power** to the Power Module and verify the following:
   1. Use an voltage meeter to check the tabs at the base edge of the LCC Fusion Node Card verifying 3V3, 5V, and 12V+.   If verification fails, there is a component that is not installed correctly, or a solder bridge.
3. Remove the power supply and assembly an DevKit-C Module to the LCC Fusion Node Card.
4. Power up the LCC Fusion Node Card again and verify the red LED power indicator on the DevKit-C Module is on indicating 5V is being supplied to the ESP32.
5. **Check for Hot Components**: Feel for components that are overheating, which could indicate a problem like a short circuit or incorrect component.

### Functional Testing

1. <img src="/assets/images/pcbs/Node_Card/Serial_Menu_Display_CAN_Status.png" style="zoom:70%; float:right" />Using a USB cable, connect the Super-Mini ESP32-S3 module to a computer.
1. Install LCC Fusion Project firmware.
1. Using a serial monitor, verify the firmware starts correctly.
1. Check the LCC Fusion Node Card’s CAN Network connectivity using the Node’s serial monitor menu.
1. Connect the computer to the LCC Fusion Node Card using a CANable Adapter.
1. Run JMRI and connect to the CAN Network.
1. While using the JMRI LCC Configuration Tool, verify that the Node appears in the network of LCC Nodes.


## Troubleshooting

- See [I2C Trouble Shooting](/test-i2c-cards/).

## References

- Super-Mini ESP32-S3 pin assignments.<img src="/assets/images/pcbs/Node_Card/SuperMini_ESP32-S3_pinout.png" alt="image-20240813095602688" style="zoom:70%; float:right" />

| SuperMini Node Connection | SuperMini Node Function      | **Super-Mini ESP32-S3 Pin** |
| ------------------------- | ---------------------------- | --------------------------- |
| CAN IC                    | TX                           | TX                          |
| CAN IC                    | RX                           | RX                          |
| I/O RJ45 (Pin 1)          | Digital I/O, PWM, ADC, Touch | GP1                         |
| I/O RJ45 (Pin 2)          | Digital I/O, PWM, ADC, Touch | GP2                         |
| I/O RJ45 (Pin 3)          | Digital I/O, PWM, ADC, Touch | GP3                         |
| I/O RJ45 (Pin 4)          | Digital I/O, PWM, ADC, Touch | GP4                         |
| I/O RJ45 (Pin 5)          | Digital I/O, PWM, ADC, Touch | GP5                         |
| I/O RJ45 (Pin 6)          | Digital I/O, PWM, ADC, Touch | GP6                         |
| I/O RJ45 (Pin 7)          | Digital I/O, PWM, ADC, Touch | GP7                         |
| I/O RJ45 (Pin 8)          | Digital I/O, PWM, ADC, Touch | GP8                         |
| LCC Fusion Node Bus Hub                 | SCL1                         | GP9                         |
| LCC Fusion Node Bus Hub                 | SCL0                         | GP10                        |
| LCC Fusion Node Bus Hub                 | SDA1                         | GP11                        |
| LCC Fusion Node Bus Hub                 | SDA0                         | GP12                        |
| LCC Fusion Node Bus Hub                 | 3V3                          | 3V3 (OUT)                   |
| n/a                       | n/a                          | 5V                          |
| LCC Fusion Node Bus Hub                 | GND                          | GND                         |
| n/a                       | n/a                          | GP13                        |
