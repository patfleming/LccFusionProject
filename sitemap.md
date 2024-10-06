---
title: Sitemap
layout: page
permalink: /sitemap/
---
<h2>Main</h2>
<ul>
  {% for page in site.pages %}
    {% if page.url contains 'assets' or page.url contains 'sitemap' %}
      {% continue %}
    {% endif %}
    <li><a href="{{ site.baseurl }}{{ page.url }}">{{ page.title }}</a></li>
  {% endfor %}
</ul>
{% for collection in site.collections %}
  {% assign docs = collection.docs | default: collection.documents %}
  <h2>{{ collection.label | capitalize }}</h2>
  <ul>
    {% for doc in docs %}
      <li><a href="{{ site.baseurl }}{{ doc.url }}">{{ doc.title | safe }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}

