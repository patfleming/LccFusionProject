---
title: CDI Configuration Tool
typora-root-url: ..
layout: default
permalink: /:name/
nav_order: 1.1
use_cases:
  - Node Cluster Setup
  - System Configuration
  - Hardware Testing & Maintenance
---
# An Introduction to the CDI Configuration Tool {#introduction_cdi_configuration_tool}
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
## CDI Introduction

Configuration Description Information (CDI) is static information describing the configuration options for an LCC Node.  **CDI Configuration Tools** provide access to the CDI for each of the LCC Nodes in a network.  Access includes seeing and changing the configuration for the Node.  LCC Node firmware typically stores the CDI configuration in permanent memory for quick retrieval. 

There are several options for CDI Configuration Tools:

1. **JRMI** provides the **Configure Nodes** tool integrated into both DecoderPro and PanelPro applications.
2. **Model Railroad System** provides the OpenLCB.exe configuration tool as part of their open source offering.

## Getting Started

Open JRMI's CDI Configuration Tool

1. <img src="{{ site.baseurl }}/assets/images/howto/CDI_VIewer_Open.gif/" style="zoom: 30%; float: right;" />Open **DecoderPro**
2. Click on **OpenLCB_CAN** in the top toolbar
3. Select **Configure Nodes**
4. ***OpenLCB Network Tree*** dialog window opens
5. Click on twisty for the LCC Node to be configured
6. Select **Open Configuration dialog**
7. New window opens showing the CDI for the LCC Node.  
8. Each CDI configuration **segment** is shown with a title and a twisty to open
9. Click on twisty to open and show the CDI 

## References

- [Deepwoods Software's Model Railroad System](https://www.deepsoft.com/home/products/modelrailroadsystem/) ([Robert Heller](https://www.deepsoft.com/~heller/))
- [LCC FAQ Handout](https://www.nmra.org/sites/default/files/standards/lcc_faq_handout.pdf)
- [LCC Standards](https://www.nmra.org/lcc)



