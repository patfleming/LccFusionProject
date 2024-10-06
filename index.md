---
title: LCC Fusion Project
layout: home
nav_order: 1
---

{:toc}

> For optimal viewing, please access the HTML version of this documentation for enhanced features and interactivity: [Documentation (html)](index.html).

## Introduction

- Brief overview of the LCC Fusion Project.
- Purpose and target audience (model railroad hobbyists).
- Key features and benefits of using this project.
- [LCC Q&A](/LCC-Q-and-A)

## Roles and Responsibilities

The LCC Fusion Project is targetted at a broad spectrum of topics including hardware and firmware, that impacts layout automation planning, design, and implementation.  This typically requires skills from one or more people.  Below is a roles and repsonsibility summary and its relationship to this project and its documentation.

Use documentation’s navigation area and the [Explore Subjects](/subjects/) page to find documentation based on your role.

Note that responsibilities listed below may well be implemented by a single person as they plan, design, and implement a own layout.  In other situations, the repsonsibilities my shared across model train club members, each working together.

  

| Role                | Responsibility                                               | [Subject Areas](/subjects/)                                       |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Layout Architect    | Focuses on the high-level design and planning of model railroad layouts. The Layout Architect considers the operational logic, thematic consistency, and overall aesthetic. They are responsible for the blueprint of the layout, integrating various components and systems to achieve a cohesive design. | Quick Start Guides<br> Planning For LCC<br> Layout Architect |
| Layout Engineer     | Specializes in the technical and practical aspects of building and maintaining the layout. The Layout Engineer works on the implementation of the design, including track laying, wiring, and the integration of control systems. They ensure that the layout operates smoothly and reliably. | Quick Start Guides<br> Layout Deployment                     |
| System Integrator   | Acts as a bridge between hardware and firmware components of the LCC Fusion Project. The System Integrator ensures seamless communication between control systems, sensors, actuators, and user interfaces. They are key in troubleshooting issues and optimizing system performance. | Layout Deployment                                            |
| firmware Developer  | Develops and maintains the firmware that powers the LCC Fusion Project, including firmware for hardware devices and applications for control and monitoring. The firmware Developer is focused on creating user-friendly, efficient, and robust firmware solutions | Layout Deployment                                            |
| Hardware Specialist | Expert in the selection, assembly, and configuration of hardware components within the LCC Fusion system. The Hardware Specialist advises on the best practices for electronic component selection and helps troubleshoot hardware-related issues. | PCB Build<br> Builder Tips<br> Hardware<br> Cards<br> Breakout Boards |
| DIY Hobbyist        | Enthusiasts who are interested in building and customizing their model railroad layouts with a hands-on approach. DIY Hobbyists look for guidance on projects that they can undertake themselves, leveraging the flexibility of the LCC Fusion Project to personalize their layouts. | Planning for LCC                                             |
| Educator            | Uses the LCC Fusion Project as a teaching tool to introduce students to concepts of electronics, programming, and system design within the context of model railroading. Educators seek resources that can be used to facilitate learning in workshops, classes, or individual projects | Planning for LCC                                             |



## Project Overview

- Detailed description of what the project is.
- Explanation of how it integrates with model railroading.
- Highlight the unique aspects or advantages of your project.

## Hardware Requirements

- List of required components (PCBs, sensors, etc.).
- Sources or recommendations for obtaining these components.

## PCB Assembly Guide

- See Hardware Assembly Guides
- Step-by-step instructions for assembling the PCBs.
- Include any already completed sections here.
- High-quality images or diagrams to assist in assembly.

## Configuration and Setup

- See [An Introduction to the CDI Configuration Tool] (@ref introduction_cdi_configuration_tool)
- See [Configuration (CDI) Guides]({{site.setup_dir}}index/})
- Detailed instructions on how to configure the PCBs.
- Explanation of firmware requirements, if any.
- Guide on how to connect the PCBs to the model railroad setup.

## Connecting the PCBs

- Diagrams showing which PCBs get connected together.
- Explanation of the connections and their purposes.
- Troubleshooting tips for common connection issues.

## LCC CDI Configuration Tool Configuration

- Step-by-step guide on configuring the boards using the LCC CDI Configuration Tool.
- Screenshots or diagrams to assist in this process.
- Explanation of different configuration options and their effects.

## Usage and Operation

- Instructions on how to use the system in a model railroad setting.
- Examples or scenarios of the system in action.

## Troubleshooting and Support

- Common issues and their solutions.
- Information on where users can seek help (forums, contact information).

## Contributing to the Project

- Guidelines on how others can contribute to the project.
- Information on open-source licensing and credits.
## Change Log and Updates

- Record of changes and updates made to the project.
- Future plans or upcoming features.

## References

## Acknowledgments

- **BOB** AI (my AI avatar the ChatGPT chatbot developed and hosted from OpenAI.com) - Bob has been relentless has been instrumental in all aspects of this project, from helping with electronic designs and technology, C++ sketchs for the firmware, Windows installer, and the overall layout and documentation
- Robert Heller - for his working examples of both hardware and firmware for LCC Nodes and I/O boards.  His was the inspiration and basis upon which this was built.
- The OpenMRN-Lite development team for macros to help with the CDI design and example code.

## Licenses for LCC Fusion Connect

### Hardware License

This project is licensed under the CERN Open Hardware License Version 2 - Permissive (CERN-OHL-P v2.0).

#### Summary of the License

This license allows you to use and modify this design for any purpose, including commercial, provided that you:

- Attribute the original source of the design to us by including the following copyright notice in all copies or substantial portions of the licensed material:
  
  "Copyright (C) [Year] [Your Name or Organization's Name]. This work is licensed under the CERN OHL-P v2.0."
  
- Include a copy of the license itself with the distributed work. The license text is available at: [https://ohwr.org/cern_ohl_p_v2.txt](https://ohwr.org/cern_ohl_p_v2.txt)

- Indicate if changes were made to the original design, in a way that is trackable from the modified work back to the original source.

#### Applying the License

To apply the CERN OHL-P v2.0 to your work, include a file named `LICENSE` or `LICENSE.txt` in the root of your project source repository, containing the full text of the license, and reference the license in your README as shown here.

For more details on the license, its permissions, conditions, and limitations, please read the full license text at the link provided above.


Based on the copyright notice and license conditions you've provided, it seems you are using a license similar to the BSD 2-Clause "Simplified" License for your firmware. Here is a Markdown (MD) template for the "License" section of your README file that reflects this license. Make sure to replace [firmware Name] with the actual name of your firmware project.

### firmware License

This firmware is licensed under the BSD 2-Clause "Simplified" License.

#### firmware License Summary

##### Copyright

This license permits personal and commercial use, distribution, and modification of the firmware under the following conditions:

- **Redistribution**: Redistribution of source code must retain the above copyright notice, this list of conditions, and the following disclaimer. Redistribution in binary form must reproduce the copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.

- **Disclaimer**: THIS FIRMWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS FIRMWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#### Applying the License

To apply this license to your firmware, include a file named `LICENSE` or `LICENSE.txt` in the root directory of your project source repository, containing the full text of this license. Reference this license in your project's README file as shown here to inform users and contributors of the licensing terms.

For more information on the BSD 2-Clause "Simplified" License, visit [https://opensource.org/licenses/BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause).

## Disclaimer of Liability

LCC Fusion Connect is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort or otherwise, arising from, out of, or in connection with the firmware or the use or other dealings in the firmware/hardware.

The user assumes all responsibility and risk for the use of this firmware/hardware. The information and powered hardware provided are subject to change without notice and should not be construed as a commitment by the author.

Use caution and common sense when working with electrical components and always follow the manufacturer's instructions and safety guidelines. The creator of this project cannot be held responsible for any injuries, damages, or violations of local codes or laws that may arise from the use of this project.

## Contact Information

- Pat Fleming (PatFlemingHTC@gmail.com)
