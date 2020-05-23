---
title: Chart
layout: page
---

<style>
    .tooltip,
    .contner__sources:before,
    .contner__build:before,
    .contner__deploy:before {
      position: absolute;
      right: 0;
      bottom: 100%;
      color: #fff;
      background: #ffb238;
      text-transform: uppercase;
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
      text-align: center;
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

    .contner__sources {
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
    }
    .contner__deploy {
      background: #f9f9f9;
      padding: 1.5rem;
      border-radius: 8px;
      position: relative;
    }
    .contner__deploy:before {
      content: 'deploy';
    }
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

</style>

<body>
    <!-- in a wrapping section include different contners for each step of the flow: data sources, build, deploy -->
    <section class="contner">

      <!-- in the sources contner show three cards, side by side, or one atop the other on smaller viewports -->
      <div class="contner__sources">

        <div class="sources--cms">
          <h3>CMSs</h3>
          <p>Contentful, Drupal, WordPress, etc.</p>
        </div>

        <div class="sources--markdown">
          <h3>Markdown</h3>
          <p>Documentation, Posts, etc.</p>
        </div>

        <div class="sources--data">
          <h3>Data</h3>
          <p>APIs, Databases, YAML, JSON, CSV, etc.</p>
        </div>

      </div>

      <!-- include a simple line to divide the contner, and animate it to show a connection between the different contners  -->
      <svg viewbox="0 0 10 100">
        <line x1="5" x2="5" y1="0" y2="100"/>
      </svg>


      <!-- in the build contner show two cards, atop of one another and the first of one showing an SVG icon -->
      <div class="contner__build">

        <div class="build--powered">
          <svg viewbox="0 0 100 100">
            <circle cx="50" cy="50" r="50"/>
          </svg>
          <p>powered by</p>
          <h3>GraphQL</h3>
        </div>

        <div class="build--stack">
            HTML · CSS · React
        </div>

      </div>

      <!-- repeat the svg line to connect the second and third contners as well -->
      <svg viewbox="0 0 10 100">
        <line x1="5" x2="5" y1="0" y2="100"/>
      </svg>

      <!-- in the deploy contner show simply text, without a wrapping card -->
      <div class="contner__deploy">
        <h3>Static Web Host</h3>
        <p>Amazon S3, Netlify, GitHub Pages, Surge.sh, Aerobatic, Now.sh, & many more.</p>
      </div>

    </section>

</body>
