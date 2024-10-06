---
title: Gerber Files
layout: default
nav_order: 5
use_cases:
  - PCB Design & Assembly
  - Node Cluster Setup
---

# Gerber Files Collection

These are Gerber (zip) files for each of the LCC  Fusion Cards and Breakout Boards.  Upload these files to a PCB fabrication site such as JLCPCB to produce your own boards or use with the LCC Fusion Project.

Here are the available Gerber ZIP files:

<ul>
  {% for file in site.static_files %}
    {% comment %}Check if the file's path includes the specific directory structure we're interested in{% endcomment %}
    {% if file.path contains 'builder/GerberFiles/' %}
      {% comment %}Generate the link using the file's path, removing the underscore{% endcomment %}
      <li><a href="{{ site.baseurl }}/{{ file.path | remove: '_' }}">{{ file.name }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
