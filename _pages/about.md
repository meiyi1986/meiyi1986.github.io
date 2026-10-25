---
permalink: /
title: "Prof. Yi Mei"
hide_title: true
seo_title: "Prof. Yi Mei – Victoria University of Wellington"
excerpt: "Professor at Victoria University of Wellington, researching evolutionary computation, genetic programming, machine learning and combinatorial optimisation."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<!-- ===================== HERO ===================== -->
<section class="home-hero">
  <h1 class="home-hero__name">Prof. Yi Mei</h1>
  <!-- PLACEHOLDER: one- or two-sentence pitch in your own words -->
  <p class="home-hero__tagline">I build AI solutions to learn how to make hard decisions, by evolving interpretable algorithms and policies for scheduling, routing, and resource allocation, and their applications to the real world.</p>

  <p class="home-hero__affiliation">
    Professor<br>
    Programme Director (Computer Science and Computer Graphics)<br>
    School of Engineering and Computer Science (<a href="https://www.wgtn.ac.nz/ecs">SECS</a>)<br>
    Centre for Data Science and Artificial Intelligence (<a href="https://www.wgtn.ac.nz/cdsai">CDSAI</a>)<br>
    Victoria University of Wellington (<a href="https://www.wgtn.ac.nz/">VUW</a>)
  </p>
  <p class="home-hero__affiliation home-hero__affiliation--groups">
    Evolutionary Computation for Combinatorial Optimisation Group (<a href="https://ecs.wgtn.ac.nz/Groups/ECCO/WebHome">ECCO</a>)<br>
    Evolutionary Computation and Machine Learning Research Group (<a href="https://ecs.wgtn.ac.nz/Groups/ECRG/WebHome">ECRG</a>)<br>
    IEEE CIS Taskforce on Evolutionary Scheduling and Combinatorial Optimisation (<a href="https://cis.taskforce.ieee.org/esco/">TESCO</a>)
  </p>
</section>

<!-- ===================== IMPACT STATS ===================== -->
<!-- Google Scholar citations and h-index: edit _data/profile.yml only. Award count: computed from the Grants & Awards page. -->
<section class="home-stats" aria-label="Research impact">
  <div class="home-stat"><span class="home-stat__value">{{ site.data.stats.scholar.citations }}</span><span class="home-stat__label">Google Scholar citations</span></div>
  <div class="home-stat"><span class="home-stat__value">{{ site.data.stats.scholar.h_index }}</span><span class="home-stat__label">h-index</span></div>
  <div class="home-stat"><span class="home-stat__value">{{ site.data.stats.grantsawards.paper_awards }}</span><span class="home-stat__label">best / outstanding paper awards</span></div>
  <div class="home-stat"><span class="home-stat__value">Top 2%</span><span class="home-stat__label">World scientist list, since {{ site.data.profile.top2_since }}</span></div>
</section>

<!-- ===================== JOIN ===================== -->
<a name="join"></a>
<div class="notice--info" markdown="1">
**Prospective students:** I am recruiting **PhD, MSc, Honours and Summer Research** students. If your interests align with my [research themes](#research-interests), please [email me](mailto:yi.mei@ecs.vuw.ac.nz) with your CV and transcripts.

<span lang="zh-Hans">**中国国家留学基金委（CSC）联合培养奖学金**：请点击[这里](/vuw-csc/)了解详情。</span>
</div>

<!-- ===================== NEWS ===================== -->
<h2 class="home-section-title">News</h2>
<ul class="news-list">
<li><span class="news-date">2026</span> <span class="news-tag">Award</span> Meng Xu's paper "<a href="https://doi.org/10.1109/MCI.2024.3363970">Genetic Programming and Reinforcement Learning on Learning Heuristics for Dynamic Scheduling: A Preliminary Comparison</a>" won the <b>Outstanding Paper Award</b> of <i>IEEE Computational Intelligence Magazine</i>.</li>
<li><span class="news-date">2026</span> <span class="news-tag">Award</span> Saining Liu's paper "<a href="https://link.springer.com/chapter/10.1007/978-3-032-23604-3_7">Adaptive Curriculum Learning in Genetic Programming–Guided Local Search for Large-Scale Vehicle Routing Problems</a>" won the <b>Best Student Paper Award</b> at <i><a href="https://www.evostar.org/2026/">EvoStar 2026</a></i>.</li>
<li><span class="news-date">2026</span> <span class="news-tag">Recognition</span> Recognised as an <b>Outstanding Associate Editor</b> of <i>IEEE Transactions on Evolutionary Computation</i> for the third consecutive year (2024–2026).</li>
<li><span class="news-date">2025</span> <span class="news-tag">Award</span> Dedy Hendro's paper "<a href="https://ieeexplore.ieee.org/document/11302604">An Investigation of Feature-Grouping for Robust SHAP Explanations in IoT Intrusion Detection</a>" won the <b>Best Student Paper Award</b> at the <i>IEEE International Telecommunication Networks and Applications Conference (ITNAC) 2025</i>.</li>
<li><span class="news-date">2025</span> <span class="news-tag">Award</span> Honoured to receive the Victoria University of Wellington <b>Ki te Pae Research Excellence Award</b>.</li>
</ul>
<nav class="action-row" aria-label="More news">
  <a class="btn-action" href="/grantsawards/"><i class="fas fa-trophy" aria-hidden="true"></i> All grants &amp; awards <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
</nav>

<!-- ===================== RESEARCH THEMES ===================== -->
<!-- Generated by _scripts/research_pages.py -->
<a name="research-interests"></a>
<h2 class="home-section-title">Research Themes</h2>
<div class="theme-cards">
  <article class="theme-card">
    <a class="theme-card__demo" href="/research/evolutionary-combinatorial-optimisation/" aria-hidden="true" tabindex="-1"><svg class="theme-svg theme-card__svg" viewBox="0 0 160 110" role="img" aria-label="Vehicle routes from a depot"><title>Vehicle routes from a depot</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="svg-arrowhead"/></marker></defs><line x1="80" y1="55" x2="30" y2="20" class="svg-road"/><line x1="80" y1="55" x2="25" y2="85" class="svg-road"/><line x1="80" y1="55" x2="135" y2="20" class="svg-road"/><line x1="80" y1="55" x2="140" y2="88" class="svg-road"/><line x1="80" y1="55" x2="80" y2="100" class="svg-road"/><line x1="80" y1="55" x2="80" y2="12" class="svg-road"/><polyline points="80,55 30,20 25,85 80,55" class="svg-route svg-route--1" fill="none"/><polyline points="80,55 135,20 140,88 80,55" class="svg-route svg-route--2" fill="none"/><polyline points="80,55 80,12" class="svg-route svg-route--3" fill="none"/><circle cx="30" cy="20" r="4" class="svg-term"/><circle cx="25" cy="85" r="4" class="svg-term"/><circle cx="135" cy="20" r="4" class="svg-term"/><circle cx="140" cy="88" r="4" class="svg-term"/><circle cx="80" cy="100" r="4" class="svg-term"/><circle cx="80" cy="12" r="4" class="svg-term"/><rect x="72" y="47" width="16" height="16" rx="3" class="svg-fn"/></svg></a>
    <div class="theme-card__body">
      <h3><a href="/research/evolutionary-combinatorial-optimisation/"><i class="fas fa-route" aria-hidden="true"></i> Evolutionary Computation for Combinatorial Optimisation</a></h3>
      <p>Designing evolutionary and memetic algorithms that find high-quality solutions to hard routing, scheduling and allocation problems — and scaling them to very large instances by decomposition.</p>
      <p class="theme-card__contrib"><b>Contributions:</b> MAENS and decomposition-based memetic algorithms for arc routing; differential grouping and cooperative co-evolution for large-scale optimisation (IEEE TEVC Outstanding Paper Award).</p>
      <div class="action-row action-row--compact">
        <a class="btn-action btn-action--small btn-action--primary" href="/research/evolutionary-combinatorial-optimisation/">Explore this theme <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
        <span class="theme-card__count">78 papers</span>
      </div>
    </div>
  </article>
  <article class="theme-card">
    <a class="theme-card__demo" href="/research/genetic-programming/" aria-hidden="true" tabindex="-1"><svg class="theme-svg theme-card__svg" viewBox="0 0 160 110" role="img" aria-label="A GP rule tree"><title>A GP rule tree</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="svg-arrowhead"/></marker></defs><line x1="80" y1="22" x2="40" y2="62" class="svg-edge"/><line x1="80" y1="22" x2="120" y2="62" class="svg-edge"/><line x1="120" y1="62" x2="98" y2="96" class="svg-edge"/><line x1="120" y1="62" x2="142" y2="96" class="svg-edge"/><circle cx="80" cy="22" r="14" class="svg-fn"/><text x="80" y="27" text-anchor="middle" class="svg-fn-text">+</text><circle cx="40" cy="62" r="14" class="svg-term"/><text x="40" y="67" text-anchor="middle" class="svg-term-text">PT</text><circle cx="120" cy="62" r="14" class="svg-fn"/><text x="120" y="67" text-anchor="middle" class="svg-fn-text">÷</text><circle cx="98" cy="96" r="12" class="svg-term"/><text x="98" y="101" text-anchor="middle" class="svg-term-text">W</text><circle cx="142" cy="96" r="12" class="svg-term"/><text x="142" y="101" text-anchor="middle" class="svg-term-text">N</text></svg></a>
    <div class="theme-card__body">
      <h3><a href="/research/genetic-programming/"><i class="fas fa-bolt" aria-hidden="true"></i> Genetic Programming for Real-time Optimisation and Decision-Making</a></h3>
      <p>Evolving compact, interpretable decision rules with genetic programming that react instantly to dynamic events in factories, vehicle fleets, cloud data centres and traffic networks.</p>
      <p class="theme-card__contrib"><b>Contributions:</b> GP hyper-heuristics for dynamic scheduling and routing; the first book on the topic; EuroGP and GECCO Best Paper Awards; HUMIES Silver Award.</p>
      <div class="action-row action-row--compact">
        <a class="btn-action btn-action--small btn-action--primary" href="/research/genetic-programming/">Explore this theme <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
        <span class="theme-card__count">167 papers</span>
      </div>
    </div>
  </article>
  <article class="theme-card">
    <a class="theme-card__demo" href="/research/machine-learning-optimisation/" aria-hidden="true" tabindex="-1"><svg class="theme-svg theme-card__svg" viewBox="0 0 160 110" role="img" aria-label="Learned components in an optimiser"><title>Learned components in an optimiser</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="svg-arrowhead"/></marker></defs><rect x="20" y="14" width="120" height="34" rx="6" class="svg-box svg-box--accent"/><text y="36.0" text-anchor="middle" class="svg-label"><tspan x="80.0" dy="0">optimiser</tspan></text><rect x="8" y="70" width="44" height="28" rx="6" class="svg-box svg-box--gold"/><text y="89.0" text-anchor="middle" class="svg-label svg-small"><tspan x="30.0" dy="0">ML</tspan></text><path d="M30,70 L40,50" class="svg-arrow svg-arrow--gold" marker-end="url(#arr)"/><rect x="58" y="70" width="44" height="28" rx="6" class="svg-box svg-box--gold"/><text y="89.0" text-anchor="middle" class="svg-label svg-small"><tspan x="80.0" dy="0">ML</tspan></text><path d="M80,70 L65,50" class="svg-arrow svg-arrow--gold" marker-end="url(#arr)"/><rect x="108" y="70" width="44" height="28" rx="6" class="svg-box svg-box--gold"/><text y="89.0" text-anchor="middle" class="svg-label svg-small"><tspan x="130.0" dy="0">ML</tspan></text><path d="M130,70 L90,50" class="svg-arrow svg-arrow--gold" marker-end="url(#arr)"/></svg></a>
    <div class="theme-card__body">
      <h3><a href="/research/machine-learning-optimisation/"><i class="fas fa-cogs" aria-hidden="true"></i> Machine Learning and Automated Algorithm Design for Optimisation</a></h3>
      <p>Using machine learning to make optimisers smarter — learning which operator to apply, where to search, and even how to design the algorithm itself.</p>
      <p class="theme-card__contrib"><b>Contributions:</b> Adaptive operator selection; learned and neural neighbourhood search for routing; GP-designed algorithm components; IEEE CIM Outstanding Paper Award; EvoStar 2026 Best Student Paper.</p>
      <div class="action-row action-row--compact">
        <a class="btn-action btn-action--small btn-action--primary" href="/research/machine-learning-optimisation/">Explore this theme <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
        <span class="theme-card__count">112 papers</span>
      </div>
    </div>
  </article>
  <article class="theme-card">
    <a class="theme-card__demo" href="/research/explainable-ai/" aria-hidden="true" tabindex="-1"><svg class="theme-svg theme-card__svg" viewBox="0 0 160 110" role="img" aria-label="Interpretability trade-off"><title>Interpretability trade-off</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="svg-arrowhead"/></marker></defs><line x1="12" y1="98" x2="152" y2="98" class="svg-edge"/><line x1="12" y1="8" x2="12" y2="98" class="svg-edge"/><polyline points="20,20 32,50 52,68 80,80 115,86 145,89" class="svg-front"/><circle cx="20" cy="20" r="4" class="svg-fn"/><circle cx="32" cy="50" r="4" class="svg-fn"/><circle cx="52" cy="68" r="4" class="svg-fn"/><circle cx="80" cy="80" r="4" class="svg-fn"/><circle cx="115" cy="86" r="4" class="svg-fn"/><circle cx="145" cy="89" r="4" class="svg-fn"/><circle cx="52" cy="68" r="9" class="svg-knee"/></svg></a>
    <div class="theme-card__body">
      <h3><a href="/research/explainable-ai/"><i class="fas fa-search" aria-hidden="true"></i> Explainable AI</a></h3>
      <p>Making AI decisions understandable — by evolving models that are interpretable by design, and by explaining the decisions of black-box models.</p>
      <p class="theme-card__contrib"><b>Contributions:</b> Survey on explainable AI by GP; local and counterfactual explanations for evolved policies; interpretability-aware GP; GECCO 2022 Best Paper Award; ITNAC 2025 Best Student Paper.</p>
      <div class="action-row action-row--compact">
        <a class="btn-action btn-action--small btn-action--primary" href="/research/explainable-ai/">Explore this theme <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
        <span class="theme-card__count">18 papers</span>
      </div>
    </div>
  </article>
  <article class="theme-card">
    <a class="theme-card__demo" href="/research/transfer-multitask-lifelong-learning/" aria-hidden="true" tabindex="-1"><svg class="theme-svg theme-card__svg" viewBox="0 0 160 110" role="img" aria-label="Knowledge shared across tasks"><title>Knowledge shared across tasks</title><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="svg-arrowhead"/></marker></defs><rect x="10" y="40" width="40" height="30" rx="6" class="svg-box svg-box--accent"/><text y="60.0" text-anchor="middle" class="svg-label"><tspan x="30.0" dy="0">A</tspan></text><rect x="110" y="40" width="40" height="30" rx="6" class="svg-box svg-box--accent"/><text y="60.0" text-anchor="middle" class="svg-label"><tspan x="130.0" dy="0">C</tspan></text><rect x="60" y="8" width="40" height="30" rx="6" class="svg-box svg-box--accent"/><text y="28.0" text-anchor="middle" class="svg-label"><tspan x="80.0" dy="0">B</tspan></text><path d="M50,48 L60,32" class="svg-arrow" marker-end="url(#arr)"/><path d="M100,32 L110,48" class="svg-arrow" marker-end="url(#arr)"/><path d="M50,62 L106,62" class="svg-arrow" marker-end="url(#arr)"/><rect x="20" y="82" width="120" height="22" rx="6" class="svg-box svg-box--gold"/><text y="98.0" text-anchor="middle" class="svg-label svg-small"><tspan x="80.0" dy="0">shared knowledge</tspan></text></svg></a>
    <div class="theme-card__body">
      <h3><a href="/research/transfer-multitask-lifelong-learning/"><i class="fas fa-project-diagram" aria-hidden="true"></i> Transfer, Multitask, and Lifelong Machine Learning</a></h3>
      <p>Reusing knowledge across related problems so that learning is faster and generalises better — from one task to another, across tasks at once, and over a lifetime of tasks.</p>
      <p class="theme-card__contrib"><b>Contributions:</b> Knowledge-transfer and multitask GP; lifelong learning for optimiser generation and neural routing solvers (IJCAI 2025, ICLR 2026); EuroGP 2022 Best Paper Award.</p>
      <div class="action-row action-row--compact">
        <a class="btn-action btn-action--small btn-action--primary" href="/research/transfer-multitask-lifelong-learning/">Explore this theme <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
        <span class="theme-card__count">34 papers</span>
      </div>
    </div>
  </article>
</div>

Biography
======
Yi Mei is a Professor at the School of Engineering and Computer Science, Victoria University of Wellington, Wellington, New Zealand. 

His research interests include evolutionary computation for combinatorial optimisation, genetic programming, automatic algorithm design, explainable AI, multi-objective optimisation, transfer/multitask learning and optimisation. He has published in top journals in EC and Operations Research (OR) such as IEEE TEVC, IEEE TCYB, EJOR, IEEE Transactions on Services Computing, and ACM Transactions on Mathematical Software. He won an IEEE Transactions on Evolutionary Computation Outstanding Paper Award 2017, GECCO Best Paper Awards in 2022, 2023, 2024, the EuroGP Best Paper Award 2022, and the EvoStar Best Student Paper Award 2026.

He is an Associate Editor of IEEE Transactions on Evolutionary Computation, IEEE Computational Intelligence Magazine, IEEE Transactions on Artificial Intelligence, IEEE Computational Intelligence Letters, Journal of Scheduling, and an Editorial Board Member/Associate Editor of four other international journals. He serves as the Chair of IEEE CIS Evolutionary Computation Technical Committee and Education Portal Subcommittee. He is the Chair of IEEE New Zealand Council. He was the Chair of the IEEE CIS Taskforce on Evolutionary Scheduling and Combinatorial Optimisation. He was the Chair of the IEEE CIS Travel Grant Subcommittee, a Vice-Chair of the IEEE CIS Emergent Technologies Technical Committee, a member of three IEEE CIS Task Forces and two IEEE CIS Technical Committees. He has been recognised as one of the Stanford University/Elsevier <b>World's Top 2% Scientists</b> since 2021. He is a <b>Fellow of Engineering New Zealand</b> and an IEEE Senior Member.

Education
======
* PhD in Computer Science, University of Science and Technology of China, 2010
* MSc in Computer Science, University of Science and Technology of China, 2007
* BSc in Mathematics, University of Science and Technology of China, 2005
