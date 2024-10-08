---
title: LCC Event Monitoring
typora-root-url: ..
layout: default
permalink: /:name/
parent: Builder's Resources & Tips
use_cases:
  - LCC Event Management
  - System Configuration
  - Learning & Planning
  - Hardware Testing & Maintenance
---

# Monitoring For Events Using JMRI {#jmri_monitoring_events}
{:toc}
## Introduction to Monitoring for Events with JMRI

The JMRI software suite, including DecoderPro and PanelPro, offers a powerful set of tools for model railroad control and automation. Among these tools, the Traffic Monitor (OpenLCB Monitor) feature plays a crucial role during the testing phase of LCC Fusion Project implementations. This feature allows users to monitor for LCC events, facilitating the testing and debugging of LCC-enabled devices and systems.

## Detailed Steps for Using the Traffic Monitor Tool

### Launching the Traffic Monitor Tool

The process begins in either the JMRI DecoderPro or PanelPro application. Here's a step-by-step guide to accessing the Send Frame Tool:

1. <img src="{{ site.baseurl }}/assets/images/howto/JMRI_Traffic_Monitor_Launch.png" style="zoom:75%;float:right" />**Access OpenLCB Options**: Navigate to the top menu bar and locate the "OpenLCB" option. This menu is your gateway to features specifically designed for LCC operations, including the Traffic Monitor tool.
2. **Select Traffic Monitor**: From the dropdown menu, select "Traffic Monitor" to open the tool. This action brings up a separate window dedicated to event monitoring.

### Monitoring an LCC Event

Once the Traffic Monitor (OpenLCB Monitor) tool is open, you can monitor for LCC events: 

1. <img src="{{ site.baseurl }}/assets/images/howto/JMRI_Traffic_Monitor.png" style="zoom:50%;float:right" />**Monitoring For LCC Node Events** by connecting JMRI to an LCC Node, opening the JMRI CDI Configuration Tool, to configure an LCC Node.  Note the numerious LCC events generated while the LCC Node provides configuration information to the CDI Configuration Tool.  Refer to [Using the CDI Configuration Tool](@ref introduction_cdi_configuration_tool) for details on using the tool.
1. **Monitoring for Specific Events** by triggering a sensor, such as the BOD Card monitoring track block occupancy.  The configured sensors Event ID should be displayed in the monitor.

