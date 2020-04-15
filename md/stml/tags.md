---
title: STML tags
layout: page
---

# Student Mathematical Library
> The AMS undergraduate series, the Student Mathematical Library, is for books that will spark students’ interests in modern mathematics and increase their appreciation for research. Books published in the series emphasize original topics and approaches. The step from mathematical coursework to mathematical research is one of the most important developments in a mathematician’s career. To make the transition successfully, the student must be motivated and interested in doing mathematics rather than merely learning it. They are suitable for honors courses, upper-division seminars, reading courses, or self-study.

{% assign all = site.html_pages | where: 'layout', 'stml' %}
{% assign tags = [] %}

{% for a in all %}
    {% assign tags = tags | concat: a.tags %}
{% endfor %}

{% assign tags = tags | uniq | sort %}

{% for t in tags %}
## {{ t }}
{% for a in all %}
{% if a.tags contains t %}
- [{{ a.title }}]({{ a.url }})
{% endif %}
{% endfor %}
{% endfor %}
