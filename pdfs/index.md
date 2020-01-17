---
layout: home
title: PDF
feature_image: "https://picsum.photos/1300/400?image=989"
feature_text: |
    ## PDF
---

{% assign dict = site.static_files | where_exp: 'a', "a.extname contains 'pdf'" | group_by_exp: "a", "a.path | truncate: 5, ''" %}

This page contains all pdf files on this site.

{% for group in dict %}
    <h1>{{ group.name }}...</h1>
    <ul>
        {% for file in group.items %}
            <li><a href="{{ file.path }}">{{ file.name }}</a></li>
        {% endfor %}
    <ul>
{% endfor %}
