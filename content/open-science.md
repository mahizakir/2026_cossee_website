+++
title = "Open Science"
type = "page"
+++

<style>
  .os-page {
    margin: 0 auto;
    max-width: 1120px;
    padding: 6px 0 38px;
  }

  .os-hero {
    display: grid;
    gap: 24px;
    grid-template-columns: minmax(0, 1.2fr) minmax(280px, 0.8fr);
    align-items: start;
    margin-bottom: 30px;
  }

  .os-kicker {
    color: var(--ualberta-green);
    display: inline-block;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 0.16em;
    margin-bottom: 12px;
    text-transform: uppercase;
  }

  .os-hero h2 {
    color: var(--ualberta-green-deep);
    font-size: 46px;
    line-height: 1.05;
    margin: 0 0 16px;
    max-width: 12ch;
  }

  .os-lead {
    color: #334638;
    font-size: 18px;
    line-height: 1.82;
    margin: 0 0 14px;
  }

  .os-sublead {
    color: #5c6b61;
    font-size: 15px;
    line-height: 1.75;
    margin: 0;
  }

  .os-focus {
    background: linear-gradient(145deg, rgba(232, 240, 232, 0.95) 0%, rgba(247, 246, 239, 0.96) 100%);
    border: 1px solid rgba(39, 93, 56, 0.12);
    border-radius: 24px;
    box-shadow: 0 18px 44px rgba(29, 71, 42, 0.08);
    padding: 24px;
  }

  .os-focus h3 {
    color: var(--ualberta-green-deep);
    font-size: 24px;
    line-height: 1.2;
    margin: 0 0 12px;
  }

  .os-focus p {
    color: #405346;
    font-size: 15px;
    line-height: 1.75;
    margin: 0 0 16px;
  }

  .os-chip-list {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  .os-chip {
    background: rgba(255, 255, 255, 0.84);
    border: 1px solid rgba(39, 93, 56, 0.1);
    border-radius: 999px;
    color: #2e4a3a;
    display: inline-flex;
    font-size: 13px;
    font-weight: 700;
    line-height: 1.4;
    padding: 8px 12px;
  }

  .os-grid {
    display: grid;
    gap: 18px;
    grid-template-columns: repeat(12, minmax(0, 1fr));
  }

  .os-card {
    background: #ffffff;
    border: 1px solid rgba(39, 93, 56, 0.1);
    border-radius: 22px;
    box-shadow: 0 12px 30px rgba(20, 34, 25, 0.05);
    padding: 22px;
  }

  .os-card--span-4 { grid-column: span 4; }
  .os-card--span-5 { grid-column: span 5; }
  .os-card--span-6 { grid-column: span 6; }
  .os-card--span-7 { grid-column: span 7; }
  .os-card--span-12 { grid-column: span 12; }

  .os-card h3 {
    color: var(--ualberta-green-deep);
    font-size: 24px;
    line-height: 1.2;
    margin: 0 0 12px;
  }

  .os-card h4 {
    color: #214132;
    font-size: 20px;
    line-height: 1.25;
    margin: 0 0 10px;
  }

  .os-card p {
    color: #45584c;
    font-size: 15px;
    line-height: 1.8;
    margin: 0 0 14px;
  }

  .os-card p:last-child {
    margin-bottom: 0;
  }

  .os-list {
    display: grid;
    gap: 10px;
    margin: 0;
    padding: 0;
  }

  .os-list li {
    background: rgba(232, 240, 232, 0.58);
    border-radius: 14px;
    color: #345042;
    list-style: none;
    padding: 12px 14px;
  }

  .os-list strong {
    color: #1f3d2b;
  }

  .os-note {
    background: #f7f3e7;
    border: 1px solid rgba(120, 99, 40, 0.14);
    border-radius: 18px;
    color: #645536;
    font-size: 14px;
    line-height: 1.7;
    padding: 16px 18px;
  }

  .os-links {
    display: grid;
    gap: 12px;
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .os-link-card {
    background: linear-gradient(180deg, #ffffff 0%, #f4f7f1 100%);
    border: 1px solid rgba(39, 93, 56, 0.1);
    border-radius: 18px;
    padding: 18px;
  }

  .os-link-card strong {
    color: var(--ualberta-green-deep);
    display: block;
    font-size: 18px;
    line-height: 1.3;
    margin-bottom: 8px;
  }

  .os-link-card p {
    color: #526258;
    font-size: 14px;
    line-height: 1.65;
    margin: 0;
  }

  @media (max-width: 991px) {
    .os-hero,
    .os-card--span-4,
    .os-card--span-5,
    .os-card--span-6,
    .os-card--span-7 {
      grid-template-columns: 1fr;
      grid-column: span 12;
    }

    .os-links {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 767px) {
    .os-page {
      padding-bottom: 18px;
    }

    .os-hero h2 {
      font-size: 34px;
      max-width: none;
    }

    .os-lead {
      font-size: 16px;
    }

    .os-links {
      grid-template-columns: 1fr;
    }
  }
</style>

<div class="os-page">
  <section class="os-hero">
    <div>
      <span class="os-kicker">Open Science</span>
      <h2>Open science as research practice, not an afterthought.</h2>
      <p class="os-lead">
        Open science at COSSEE is not a side theme. It shapes how projects are planned, how decisions are documented, how evidence is shared, and how research communities are built across ecology and evolution.
      </p>
      <p class="os-sublead">
        The aim is to make research more trustworthy, reusable, and collaborative by treating transparency as part of everyday scientific work rather than something added once a study is finished.
      </p>
    </div>

    <aside class="os-focus">
      <h3>What open science means at COSSEE</h3>
      <p>
        For COSSEE, open science is not just about posting code or data. It includes planning research clearly, creating reusable records of methods and decisions, building living and updateable syntheses, and supporting workflows that make research easier to inspect, repeat, and extend.
      </p>
      <div class="os-chip-list">
        <span class="os-chip">Registrations</span>
        <span class="os-chip">Registered reports</span>
        <span class="os-chip">Protocols</span>
        <span class="os-chip">Transparent workflows</span>
        <span class="os-chip">Living syntheses</span>
        <span class="os-chip">Shared standards</span>
      </div>
    </aside>
  </section>

  <div class="os-grid">
    <section class="os-card os-card--span-7">
      <h3>What this looks like in practice</h3>
      <ul class="os-list">
        <li><strong>Planning studies clearly:</strong> making hypotheses, methods, and analytical choices visible early.</li>
        <li><strong>Using registrations and protocols:</strong> creating stable public records when they strengthen the research process.</li>
        <li><strong>Supporting registered reports:</strong> shifting evaluation toward design quality and reasoning rather than novelty alone.</li>
        <li><strong>Building reusable synthesis projects:</strong> designing reviews, maps, and meta-analyses that can be revisited, updated, and extended.</li>
        <li><strong>Linking transparency with inclusion:</strong> connecting open practice with clearer credit, broader participation, and collaborative community building.</li>
      </ul>
    </section>

    <section class="os-card os-card--span-5">
      <h3>Why it matters</h3>
      <p>
        Better science is not only about producing results. It is also about making the reasoning, design, and workflow behind those results easier to evaluate.
      </p>
      <p>
        In ecology and evolution, where studies can be heterogeneous, context-dependent, and difficult to replicate directly, open science helps make evidence easier to interpret, compare, update, and reuse.
      </p>
    </section>

    <section class="os-card os-card--span-4">
      <h4>Registrations</h4>
      <p>
        Registrations help make the logic of a study visible before results reshape the story. They are especially useful for clarifying research questions, hypotheses, design decisions, and planned analyses.
      </p>
    </section>

    <section class="os-card os-card--span-4">
      <h4>Registered Reports</h4>
      <p>
        Registered reports move peer review earlier in the research process so studies are judged on design strength, clarity, and reasoning before outcomes are known.
      </p>
    </section>

    <section class="os-card os-card--span-4">
      <h4>Published Protocols</h4>
      <p>
        Protocols provide detailed, citable records of how studies and syntheses will be conducted. They are especially useful for complex reviews, evidence maps, and collaborative projects.
      </p>
    </section>

    <section class="os-card os-card--span-6">
      <h3>Research culture and shared standards</h3>
      <p>
        Open science also depends on how people work together. At COSSEE, this includes reproducible workflows, better reporting, clearer research records, shared standards, and infrastructure that others can inspect and build on.
      </p>
      <p>
        In that sense, open science is tied not only to tools, but also to research culture: how projects are organised, how decisions are recorded, and how contributions remain legible over time.
      </p>
    </section>

    <section class="os-card os-card--span-6">
      <h3>Community and infrastructure</h3>
      <p>
        Open science grows through broader ecosystems of repositories, societies, software, and training networks. COSSEE treats these communities and infrastructures as part of the research process rather than separate support layers.
      </p>
      <div class="os-note">
        At COSSEE, open science is closely connected to evidence synthesis, meta-research, and methodological development. These are not separate tracks. They reinforce one another.
      </div>
    </section>

    <section class="os-card os-card--span-12">
      <h3>Read more</h3>
      <div class="os-links">
        <a class="os-link-card" href="/protocols/">
          <strong>Protocols</strong>
          <p>See how COSSEE approaches registrations, registered reports, and protocol-based planning.</p>
        </a>
        <a class="os-link-card" href="/resources/">
          <strong>Resources</strong>
          <p>Browse societies, hubs, tools, and networks connected to open science and synthesis work.</p>
        </a>
        <a class="os-link-card" href="/research/">
          <strong>Research Overview</strong>
          <p>Explore how open science connects with COSSEE's broader research themes, methods, and workflows.</p>
        </a>
      </div>
    </section>
  </div>
</div>
