---
title: LCC Q & A
typora-root-url: ..
layout: default
permalink: /:name/
nav_order: 1
use_cases:
  - Learning & Planning
  - System Configuration
---

# LCC Q&A {#lcc_q_and_a}

Below are some common questions concerning NMRA Layout Command Control (LCC):

1. **Will LCC work with my DCC layout?** Yes, LCC complements DCC. LCC does not render DCC obsolete; instead, it takes accessory traffic off the DCC bus, allowing locomotive control to remain on the rails.
2. **Can LCC be used on a DC layout?** Yes, LCC can be used with any train control method, including DC. Since LCC is a separate protocol with its own communications, it's compatible with DC systems.
3. **Is LCC bi-directional?** LCC nodes can both send and receive data over the LCC bus, unlike DCC decoders. This allows for functionalities like detectors, turnout feedback, local fascia controls, and more to communicate with each other.
4. **Is LCC high speed?** LCC operates significantly faster than DCC by using the automotive CAN-bus. It has the capacity for extra traffic and can also operate over even faster networks like Ethernet or WiFi.
5. **Do I need a LCC 'Master' unit?** No, LCC is a peer-peer network, meaning any two or more LCC devices can communicate directly without needing a central command station. A computer can facilitate configuration, but it's not essential for operation.
6. **What is NMRA's role in LCC?** NMRA has set the standards for LCC, similar to what they did for DCC. The standards were developed by a group of independent volunteers, modelers, and electronics experts. The NMRA's role is to establish these standards for manufacturers to use license-free.
7. **What makes LCC unique?** Each LCC product is unique, eliminating the need for users to assign and keep track of device addresses. It allows for easy addition of new nodes to existing systems without data collisions and is expandable for future functionalities.
8. **Are LCC products from different manufacturers compatible?** Yes, because of the standards set by NMRA, LCC products from different manufacturers are designed to interoperate.
9. **Are there manufacturers producing LCC products?** Several manufacturers are providing LCC-related products, including TCS Train Control Systems, RR-CirKits, and Deepwoods firmware (MRS).

