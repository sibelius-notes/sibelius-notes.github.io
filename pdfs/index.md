---
layout: home
title: PDF
feature_image: "https://picsum.photos/1300/400?image=989"
feature_text: |
    ## PDF
---



This page contains all pdf files on this site.

<ul>
{% for file in site.static_files %}
  {% if file.extname contains 'pdf' %}
    <li><a href="{{ file.path }}">{{ file.name }}</a></li>
  {% endif %}
{% endfor %}
</ul>
