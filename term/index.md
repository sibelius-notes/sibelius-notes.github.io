---
title: Term
layout: default
feature_image: "/assets/backpic/piano.jpg"
feature_text: |
    <h2 style="background: rgb(0, 0, 0); background: rgba(0, 0, 0, 0.5); color: white; padding: 10px;">Sort by terms</h2>
---
{% assign all_terms = site.term | reverse %}

{% assign all_terms_in_number = all_terms | map: "term" %}
<style>

    {% for n in all_terms_in_number %}.contner__{{ n }}:before, {% endfor %}
    .tooltip,
    .contner__sources:before,
    .contner__build:before,
    .contner__deploy:before {
      position: absolute;
      left: 0;
      bottom: 100%;
      color: #fff;
      background: #ffb238;
      font-size: 0.9rem;
      padding: 0.25rem 0.75rem;
      border-radius: 2.5px;
    }
    .card,
    .contner__sources div,
    .contner__build div {
      line-height: 2;
      background: #fff;
      padding: 1.2rem 1rem;
      border-radius: 4px;
      box-shadow: 0 2px 10px #e6e6e6;
    }

    .contner {
      margin: 5vh 2.5vw;
      padding: 15vh 0;
      background: #fff;
      border-radius: 5px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .contner svg {
      height: 5rem;
    }
    .contner svg line {
      stroke: #5f39dd;
      stroke-width: 3px;
      stroke-linecap: round;
      stroke-dasharray: 2px 20px;
      animation: animateline 5s linear both infinite;
    }

    /*.contner__sources {
      display: flex;
      border-radius: 8px;
      padding: 1.5rem;
      background: #f9f9f9;
      position: relative;
    }
    .contner__sources:before {
      content: 'data sources';
    }
    .contner__sources div {
      text-align: left;
      margin: 0 1rem;
    }
    .contner__build {
      padding: 10vh 10vw;
      border-radius: 8px;
      background: #f9f9f9;
      position: relative;
    }
    .contner__build:before {
      content: 'build';
    }
    .contner__build div {
      margin: 2rem 0;
    }
    .contner__build div svg {
      width: 4rem;
      height: auto;
      fill: #5f39dd;
    }*/

    {% for n in all_terms_in_number %}.contner__{{ n }}, {% endfor %}
    .contner__deploy {
      width: 100%;
      background: #f9f9f9;
      padding: 1.5rem;
      border-radius: 8px;
      position: relative;
    }
    .contner__deploy:before {
      content: 'deploy';
    }
    {% for t in all_terms %}
    .contner__{{ t.term }}:before {
      content: '{{ t.title }}';
    }
    {% endfor %}

    @media (max-width: 700px) {
      .contner__sources {
        flex-direction: column;
      }
      .contner__sources div {
        margin: 1rem 0;
      }
    }
    @-moz-keyframes animateline {
      from {
        stroke-dashoffset: 0;
      }
      to {
        stroke-dashoffset: -5rem;
      }
    }
    @-webkit-keyframes animateline {
      from {
        stroke-dashoffset: 0;
      }
      to {
        stroke-dashoffset: -5rem;
      }
    }
    @-o-keyframes animateline {
      from {
        stroke-dashoffset: 0;
      }
      to {
        stroke-dashoffset: -5rem;
      }
    }
    @keyframes animateline {
      from {
        stroke-dashoffset: 0;
      }
      to {
        stroke-dashoffset: -5rem;
      }
    }


    .search-container {
      display: flex;
      flex-wrap: wrap;
      /*max-width: 900px;*/
    }

    .search-item {
      padding: 5px 10px;
      /*border: 1px solid grey;*/
      margin: 5px;
      width: 150px;
      flex-basis: 180px;
      flex-grow: initial;
    }
</style>

<main class="main container">
    <div class="content">
<section class="contner">
{% for t in all_terms %}
    <div class="contner__{{ t.term }}">
    {% assign courses = site.posts | where: "term", t.term | where: "hide", false %}
    <div class="search-container">
    {% for c in courses %}
        <div class="label label--category search-item">
        <a href="{{ c.url }}" class="post-tag">{{ c.title }}</a>
        </div>
    {% endfor %}
    </div>

    <div style="text-align:right;position: absolute;bottom: 0; right: 0; font-size:80%; padding-right:1em;">
    <a href="{{ t.url }}" class="post-tag">more courses</a>
    </div>
    </div>
    {% unless t.term == 1179 %}
        <svg viewbox="0 0 10 100">
        <line x1="5" x2="5" y1="0" y2="100"/>
        </svg>
    {% endunless %}
{% endfor %}
</section>
</div>
</main>
