---
title: Explore Subjects
layout: default
permalink: /subjects/
---
# Explore Subjects: A Guide to LCC Fusion Project Documentation
Welcome to the comprehensive list of subjects for the LCC Fusion Project documentation! Whether you're just getting started or seeking specific information on ESP32 hardware, firmware configurations, or model railroad automation, our subject list will help you navigate the wealth of resources available.

> Don't forget to check out **Explore Use Cases**, where documentation is organized by various use cases.

Subjects are curated labels that categorize content based on subject matter, functionality, and key concepts. By exploring subjects, you can easily access related articles, guides, and tutorials without sifting through unrelated content. This approach enhances your learning experience and provides a direct path to the information you need.

Below, you'll find an alphabetically sorted list of all subjects used across our documentation. Click on a subject link to view the documentation related to that topic.

<div id="tags-index">
  {% assign all_docs = site.pages %}

  {% for collection in site.collections %}
    {% assign all_docs = all_docs | concat: collection.docs %}
  {% endfor %}

  {% assign subject_list = all_docs | map: 'subjects' | flatten | compact | uniq %}
  {% assign sorted_subjects = subject_list | sort %}

  {% for subject in sorted_subjects %}
    {% if subject %}
    <h2 id="{{ subject | slugify }}">{{ subject }}</h2>
    <ul>
      {% for doc in all_docs %}
        {% if doc.subjects contains subject %}
          <li><a href="{{ site.baseurl }}{{ doc.url }}">{{ doc.title }}</a></li>
        {% endif %}
      {% endfor %}
    </ul>
​    {% endif %}
  {% endfor %}
</div>
