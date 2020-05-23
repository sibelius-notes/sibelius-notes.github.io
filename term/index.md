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

    /*
      You want a simple and fancy tooltip?
      Just copy all [data-tooltip] blocks:
    */
    [data-tooltip] {
      position: relative;
      z-index: 10;
    }

    /* Positioning and visibility settings of the tooltip */
    [data-tooltip]:before,
    [data-tooltip]:after {
      position: absolute;
      visibility: hidden;
      opacity: 0;
      left: 50%;
      bottom: calc(100% + 5px);
      pointer-events: none;
      transition: 0.2s;
      will-change: transform;
    }

    /* The actual tooltip with a dynamic width */
    [data-tooltip]:before {
      content: attr(data-tooltip);
      padding: 10px 18px;
      min-width: 50px;
      max-width: 300px;
      width: max-content;
      width: -moz-max-content;
      border-radius: 6px;
      font-size: 14px;
    /*   font-size: 0.73rem; */
      background-color: rgba(59, 72, 80, 0.9);
      background-image: linear-gradient(30deg,
        rgba(59, 72, 80, 0.44),
        rgba(59, 68, 75, 0.44),
        rgba(60, 82, 88, 0.44));
      box-shadow: 0px 0px 24px rgba(0, 0, 0, 0.2);
      color: #fff;
      text-align: center;
      white-space: pre-wrap;
      transform: translate(-50%, -5px) scale(0.5);
    }

    /* Tooltip arrow */
    [data-tooltip]:after {
      content: '';
      border-style: solid;
      border-width: 5px 5px 0px 5px;
      border-color: rgba(55, 64, 70, 0.9) transparent transparent transparent;
      transition-duration: 0s; /* If the mouse leaves the element,
                                  the transition effects for the
                                  tooltip arrow are "turned off" */
      transform-origin: top;   /* Orientation setting for the
                                  slide-down effect */
      transform: translateX(-50%) scaleY(0);
    }

    /* Tooltip becomes visible at hover */
    [data-tooltip]:hover:before,
    [data-tooltip]:hover:after {
      visibility: visible;
      opacity: 1;
    }
    /* Scales from 0.5 to 1 -> grow effect */
    [data-tooltip]:hover:before {
      transition-delay: 0.3s;
      transform: translate(-50%, -5px) scale(1);
    }
    /* Slide down effect only on mouseenter (NOT on mouseleave) */
    [data-tooltip]:hover:after {
      transition-delay: 0.5s; /* Starting after the grow effect */
      transition-duration: 0.2s;
      transform: translateX(-50%) scaleY(1);
    }
    /*
      That's it.
    */






    /*
      If you want some adjustability
      here are some orientation settings you can use:
    */

    /* LEFT */
    /* Tooltip + arrow */
    [data-tooltip-location="left"]:before,
    [data-tooltip-location="left"]:after {
      left: auto;
      right: calc(100% + 5px);
      bottom: 50%;
    }

    /* Tooltip */
    [data-tooltip-location="left"]:before {
      transform: translate(-5px, 50%) scale(0.5);
    }
    [data-tooltip-location="left"]:hover:before {
      transform: translate(-5px, 50%) scale(1);
    }

    /* Arrow */
    [data-tooltip-location="left"]:after {
      border-width: 5px 0px 5px 5px;
      border-color: transparent transparent transparent rgba(55, 64, 70, 0.9);
      transform-origin: left;
      transform: translateY(50%) scaleX(0);
    }
    [data-tooltip-location="left"]:hover:after {
      transform: translateY(50%) scaleX(1);
    }



    /* RIGHT */
    [data-tooltip-location="right"]:before,
    [data-tooltip-location="right"]:after {
      left: calc(100% + 5px);
      bottom: 50%;
    }

    [data-tooltip-location="right"]:before {
      transform: translate(5px, 50%) scale(0.5);
    }
    [data-tooltip-location="right"]:hover:before {
      transform: translate(5px, 50%) scale(1);
    }

    [data-tooltip-location="right"]:after {
      border-width: 5px 5px 5px 0px;
      border-color: transparent rgba(55, 64, 70, 0.9) transparent transparent;
      transform-origin: right;
      transform: translateY(50%) scaleX(0);
    }
    [data-tooltip-location="right"]:hover:after {
      transform: translateY(50%) scaleX(1);
    }



    /* BOTTOM */
    [data-tooltip-location="bottom"]:before,
    [data-tooltip-location="bottom"]:after {
      top: calc(100% + 5px);
      bottom: auto;
    }

    [data-tooltip-location="bottom"]:before {
      transform: translate(-50%, 5px) scale(0.5);
    }
    [data-tooltip-location="bottom"]:hover:before {
      transform: translate(-50%, 5px) scale(1);
    }

    [data-tooltip-location="bottom"]:after {
      border-width: 0px 5px 5px 5px;
      border-color: transparent transparent rgba(55, 64, 70, 0.9) transparent;
      transform-origin: bottom;
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
        <div class="label label--category search-item tooltip">
        <a href="{{ c.url }}" class="post-tag"  data-tooltip="{{ c.feature_text | split: '|' | last | strip_html }}"
       data-tooltip-location="top">{{ c.title }}</a>
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
