---
title: Term
layout: default
feature_text: <h2>Sort by terms</h2>
feature_image: "https://picsum.photos/1300/400?image=989"
---
<main class="main container">
    <div class="content">
        **Parenthetical note** (from CS 246 A0): 1179 is Quest-speak for Fall 2017. The last digit is the month, and the
first three digits, added to 1900, give the year.
        <br>

        *You can click the <b>term heading</b> to view other courses I have audited, which may have incomplete notes and some remarks.*

        <br><br><br>
        <!-- my code -->
        {% assign all_terms = site.posts | map: "term" | uniq %}

        {% for item in all_terms %}
        {% assign courses = site.posts | where: "term", item | where: "hide", false %}
                <div class="typeset" style="border: 1px solid #EEEEEE; padding: 1em; border-radius: 0.3em;">
                    <h1 align="center" style="font-size:2em"><a href="/term/{{ item }}">{{ item | upcase }}</a></h1>
                    <ul>
                        {% for c in courses %}
                        <span class="label label--category"><a href="{{ c.url }}" class="post-tag" style="white-space: nowrap">{{ c.title }}</a></span> &nbsp;&nbsp;
                        {% endfor %}
                    </ul>
                </div>
            <br>
        {% endfor %}
    </div>
</main>