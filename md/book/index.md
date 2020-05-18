---
title: Book tags
layout: page
---


{% assign all = site.html_pages | where: 'layout', 'stml' %}
{% assign tags = [] %}

{% for a in all %}
    {% assign tags = tags | concat: a.tags %}
{% endfor %}

{% assign tags = tags | uniq | sort %}

{% for t in tags %}
### {{ t }}
{% for a in all %}
{% if a.tags contains t %}
- [{{ a.title }}]({{ a.url }})
{% endif %}
{% endfor %}
{% endfor %}
