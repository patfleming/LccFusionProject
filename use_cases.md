---
title: Explore Use Cases
layout: default
permalink: /use_cases/
---
# Explore Use Cases: A Guide to LCC Fusion Project Documentation

Welcome to the comprehensive list of use cases for the LCC Fusion Project documentation! Whether you're just getting started or looking for specific examples on how to implement ESP32 hardware, firmware configurations, or model railroad automation, our use case list will guide you through the practical applications of our resources.

> Be sure to also check out **Explore Subjects**, which organizes documentation by topic.

Use cases are real-world examples that categorize content based on practical applications, scenarios, and problem-solving methods. By exploring use cases, you can easily find articles, guides, and tutorials that demonstrate how to apply our documentation to your specific needs. This approach enhances your project planning and implementation by providing clear, actionable insights.

Below, you'll find an alphabetically sorted list of all use cases featured in our documentation. Click on a use case link to see related documentation.

<div id="tags-index">
  {% assign all_docs = site.pages %}
  {% for collection in site.collections %}
    {% assign all_docs = all_docs | concat: collection.docs %}
  {% endfor %}

  {% assign use_case_list = all_docs | map: 'use_cases' | flatten | compact | uniq %}
  {% assign sorted_use_cases = use_case_list | sort %}

  {% for use_case in sorted_use_cases %}
    {% if use_case %}
      <h2 id="{{ use_case | slugify }}">{{ use_case }}</h2>
      <ul>
        {% assign use_case_docs = all_docs | where: "use_cases", use_case %}
        {% assign sorted_docs = use_case_docs | sort: 'title' %}
        {% for doc in sorted_docs %}
          <li><a href="{{ site.baseurl }}{{ doc.url }}">{{ doc.title }}</a></li>
        {% endfor %}
      </ul>
​    {% endif %}
  {% endfor %}
</div>

