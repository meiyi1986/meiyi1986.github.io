---
layout: archive
title: "Genetic Programming & Automated Algorithm Design"
permalink: /research/genetic-programming/
excerpt: "Research by Prof. Yi Mei on genetic programming hyper-heuristics that automatically design scheduling, routing and decision rules."
author_profile: true
---

<p class="theme-lead">Instead of hand-crafting an algorithm for every new problem, can we let the computer <b>learn the algorithm itself</b>? My research uses <b>genetic programming (GP)</b> to automatically design heuristics — compact, interpretable decision rules that make fast, high-quality decisions in dynamic and uncertain environments such as factories, delivery fleets, cloud data centres and traffic networks.</p>

<section class="home-stats page-highlights" aria-label="Highlights">
  <div class="home-stat"><span class="home-stat__value">160+</span><span class="home-stat__label">papers on GP &amp; algorithm design</span></div>
  <div class="home-stat"><span class="home-stat__value">6</span><span class="home-stat__label">best / outstanding paper awards in this area</span></div>
  <div class="home-stat"><span class="home-stat__value">1st</span><span class="home-stat__label">book on hyper-heuristics for production scheduling (Springer, 2021)</span></div>
  <div class="home-stat"><span class="home-stat__value">Humies</span><span class="home-stat__label">Silver Award 2023 for human-competitive results</span></div>
</section>

<nav class="pub-jump" aria-label="On this page">
  <a href="#introduction"><i class="fas fa-lightbulb" aria-hidden="true"></i> Introduction</a>
  <a href="#contributions"><i class="fas fa-star" aria-hidden="true"></i> Contributions</a>
  <a href="#output"><i class="fas fa-chart-bar" aria-hidden="true"></i> Research output</a>
</nav>

<a name="introduction"></a>
<h2>Introduction</h2>

<h3>Why learn heuristics?</h3>
<p>Many real-world decisions must be made <b>in real time</b> while the situation keeps changing: new jobs arrive at a factory, machines break down, customer demands and travel times are uncertain. Exact optimisation is too slow to re-run at every change, and hand-designed rules (such as <i>shortest processing time first</i>) need years of expert trial and error and rarely fit every scenario.</p>
<p><b>Hyper-heuristics</b> address this by searching the space of <i>heuristics</i> rather than the space of solutions. A GP hyper-heuristic (GPHH) evolves a priority function that is applied whenever a decision is needed — which job a machine should process next, which task a vehicle should serve next, or which server should host a container.</p>

<div class="theme-split">
<figure class="theme-figure">
<svg class="theme-svg theme-svg--narrow" viewBox="0 0 340 230" role="img" aria-labelledby="tree-t"><title id="tree-t">A dispatching rule as a GP tree: PT + WINQ / NOR</title><line x1="170" y1="38" x2="90" y2="118" class="svg-edge"/><line x1="170" y1="38" x2="250" y2="118" class="svg-edge"/><line x1="250" y1="118" x2="200" y2="196" class="svg-edge"/><line x1="250" y1="118" x2="300" y2="196" class="svg-edge"/><circle cx="170" cy="38" r="21" class="svg-fn"/><text x="170" y="43" text-anchor="middle" class="svg-fn-text">+</text><circle cx="90" cy="118" r="21" class="svg-term"/><text x="90" y="123" text-anchor="middle" class="svg-term-text">PT</text><circle cx="250" cy="118" r="21" class="svg-fn"/><text x="250" y="123" text-anchor="middle" class="svg-fn-text">÷</text><circle cx="200" cy="196" r="21" class="svg-term"/><text x="200" y="201" text-anchor="middle" class="svg-term-text">WINQ</text><circle cx="300" cy="196" r="21" class="svg-term"/><text x="300" y="201" text-anchor="middle" class="svg-term-text">NOR</text><text x="14" y="226" class="svg-axis">function</text><circle cx="6" cy="222" r="5" class="svg-fn"/><circle cx="82" cy="222" r="5" class="svg-term"/><text x="90" y="226" class="svg-axis">terminal (job / machine feature)</text></svg>
<figcaption><b>Figure 1.</b> A scheduling rule represented as a GP tree. Inner nodes are operators; leaves are features of the current state, such as processing time (PT), work in the next queue (WINQ) and number of operations remaining (NOR). The rule computes a priority <code>PT + WINQ / NOR</code> for every waiting job.</figcaption>
</figure>
<div class="theme-split__text">
<h3>Why genetic programming?</h3>
<ul>
<li><b>Flexible representation</b> — rules are programs of any shape, so GP can discover new structures rather than only tuning parameters.</li>
<li><b>Interpretable output</b> — an evolved rule is a readable formula that domain experts can inspect, trust and adjust.</li>
<li><b>Fast at decision time</b> — evaluating a formula takes microseconds, so it can react immediately to changes.</li>
<li><b>Learns from simulation</b> — rules are trained offline on many simulated scenarios and then reused on unseen ones.</li>
</ul>
</div>
</div>

<figure class="theme-figure">
<svg class="theme-svg" viewBox="0 0 760 270" role="img" aria-labelledby="flow-t flow-d"><title id="flow-t">GP hyper-heuristic workflow</title><desc id="flow-d">Offline, a population of candidate rules is evaluated in simulated dynamic scenarios and evolved; online, the best rule makes real-time decisions.</desc><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="svg-arrowhead"/></marker></defs><rect x="6" y="6" width="476" height="258" rx="10" class="svg-region"/><text x="22" y="30" class="svg-region-title">OFFLINE · learn the heuristic</text><rect x="506" y="6" width="248" height="258" rx="10" class="svg-region svg-region--online"/><text x="522" y="30" class="svg-region-title">ONLINE · use the heuristic</text><rect x="24" y="52" width="196" height="64" rx="6" class="svg-box"/><text y="80.5" text-anchor="middle" class="svg-label"><tspan x="122.0" dy="0">1. Population of</tspan><tspan x="122.0" dy="17">candidate rules (GP trees)</tspan></text><rect x="266" y="52" width="196" height="64" rx="6" class="svg-box"/><text y="80.5" text-anchor="middle" class="svg-label"><tspan x="364.0" dy="0">2. Evaluate each rule in</tspan><tspan x="364.0" dy="17">simulated dynamic scenarios</tspan></text><rect x="145" y="170" width="196" height="64" rx="6" class="svg-box"/><text y="198.5" text-anchor="middle" class="svg-label"><tspan x="243.0" dy="0">3. Select &amp; vary</tspan><tspan x="243.0" dy="17">(crossover, mutation)</tspan></text><path d="M220,84 L262,84" class="svg-arrow" marker-end="url(#arr)"/><path d="M364,116 Q364,150 322,170" class="svg-arrow" marker-end="url(#arr)"/><path d="M164,170 Q122,150 122,120" class="svg-arrow" marker-end="url(#arr)"/><rect x="526" y="52" width="208" height="64" rx="6" class="svg-box svg-box--accent"/><text y="80.5" text-anchor="middle" class="svg-label"><tspan x="630.0" dy="0">Best evolved rule</tspan><tspan x="630.0" dy="17">(compact, interpretable)</tspan></text><rect x="526" y="170" width="208" height="64" rx="6" class="svg-box"/><text y="198.5" text-anchor="middle" class="svg-label"><tspan x="630.0" dy="0">Real-time decisions: rank</tspan><tspan x="630.0" dy="17">waiting jobs / vehicles / tasks</tspan></text><path d="M462,84 L522,84" class="svg-arrow" marker-end="url(#arr)"/><path d="M630,116 L630,166" class="svg-arrow" marker-end="url(#arr)"/></svg>
<figcaption><b>Figure 2.</b> How a GP hyper-heuristic works. The heuristic is learned offline by evolving a population of candidate rules evaluated in simulation; after a number of generations, the best rule is deployed online to make real-time decisions.</figcaption>
</figure>

<a name="contributions"></a>
<h2>My Contributions</h2>
<p>With my students and collaborators, I have developed GP methods that learn better heuristics, learn them faster, make them easier to understand, and apply them to new domains. Click a title to read the paper, or <i>list entry</i> to see it in my publication list.</p>

<h3 class="theme-sub"><span class="theme-sub__num">1</span> Learning scheduling heuristics for dynamic job shops</h3>
<p>Our core line of work makes GPHH effective for dynamic (flexible) job shop scheduling: selecting the most useful features, evolving separate <i>routing</i> and <i>sequencing</i> rules together with multi-tree GP, combining rules into ensembles, and guiding the search with surrogate models. This body of work is summarised in our Springer book and two surveys.</p>
<ul class="contrib-list">
  <li><a class="contrib-list__title" href="https://doi.org/10.1007/978-981-16-4859-5">Genetic Programming for Production Scheduling: An Evolutionary Learning Approach</a><span class="contrib-list__venue"><i>Springer</i>, 2021 · <a href="/publications/publication-book.html#zhang2021">list entry</a></span> <span class="contrib-list__note">Book</span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1007/s40747-017-0036-x">Genetic programming for production scheduling: a survey with a unified framework</a><span class="contrib-list__venue"><i>Complex and Intelligent Systems</i>, 2017 · <a href="/publications/publication-journal.html#nguyen2017genetic">list entry</a></span> <span class="contrib-list__note">Survey</span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TETCI.2017.2743758">An efficient feature selection algorithm for evolving job shop scheduling rules with genetic programming</a><span class="contrib-list__venue"><i>IEEE Transactions on Emerging Topics in Computational Intelligence</i>, 2017 · <a href="/publications/publication-journal.html#mei2017efficient">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TCYB.2020.3024849">Evolving Scheduling Heuristics via Genetic Programming with Feature Selection in Dynamic Flexible Job Shop Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Cybernetics</i>, 2021 · <a href="/publications/publication-journal.html#zhang2020evolving">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1162/evco_a_00273">Genetic Programming with Delayed Routing for Multi-Objective Dynamic Flexible Job Shop Scheduling</a><span class="contrib-list__venue"><i>Evolutionary Computation</i>, 2021 · <a href="/publications/publication-journal.html#xu2020genetic">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2021.3056143">Correlation Coefficient based Recombinative Guidance for Genetic Programming Hyper-heuristics in Dynamic Flexible Job Shop Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2021 · <a href="/publications/publication-journal.html#zhang2021correlation">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TCYB.2021.3050141">Collaborative Multifidelity-Based Surrogate Models for Genetic Programming in Dynamic Flexible Job Shop Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Cybernetics</i>, 2022 · <a href="/publications/publication-journal.html#zhang2021collaborative">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2023.3334626">Genetic Programming for Dynamic Flexible Job Shop Scheduling: Evolution With Single Individuals and Ensembles</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2024 · <a href="/publications/publication-journal.html#xu2023genetic2">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2023.3244607">Genetic Programming with Lexicase Selection for Large-scale Dynamic Flexible Job Shop Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2024 · <a href="/publications/publication-journal.html#xu2023genetic">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2023.3255246">Survey on Genetic Programming and Machine Learning Techniques for Heuristic Design in Job Shop Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2024 · <a href="/publications/publication-journal.html#zhang2023survey">list entry</a></span> <span class="contrib-list__note">Survey</span></li>
</ul>

<h3 class="theme-sub"><span class="theme-sub__num">2</span> Multitask learning and knowledge transfer</h3>
<p>Real systems involve many related scheduling or routing scenarios. We showed that learning heuristics for several tasks <b>simultaneously</b> — and transferring knowledge between them — produces better rules with less computation than learning each task separately.</p>
<figure class="theme-figure">
<svg class="theme-svg" viewBox="0 0 700 210" role="img" aria-labelledby="mt-t mt-d"><title id="mt-t">Multitask GP with knowledge transfer</title><desc id="mt-d">Two related scheduling tasks are solved together; promising individuals and building blocks are shared between their populations, while surrogate models cut evaluation cost.</desc><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="svg-arrowhead"/></marker></defs><rect x="20" y="30" width="230" height="120" rx="6" class="svg-region"/><text y="95.0" text-anchor="middle" class="svg-label"><tspan x="135.0" dy="0"></tspan></text><text x="135" y="56" text-anchor="middle" class="svg-region-title">TASK A</text><text x="135" y="76" text-anchor="middle" class="svg-axis">e.g. minimise mean flowtime</text><rect x="450" y="30" width="230" height="120" rx="6" class="svg-region"/><text y="95.0" text-anchor="middle" class="svg-label"><tspan x="565.0" dy="0"></tspan></text><text x="565" y="56" text-anchor="middle" class="svg-region-title">TASK B</text><text x="565" y="76" text-anchor="middle" class="svg-axis">e.g. minimise mean tardiness</text><circle cx="70" cy="110" r="9" class="svg-term"/><circle cx="105" cy="124" r="9" class="svg-term"/><circle cx="140" cy="104" r="9" class="svg-term"/><circle cx="175" cy="122" r="9" class="svg-term"/><circle cx="210" cy="108" r="9" class="svg-term"/><circle cx="500" cy="110" r="9" class="svg-term"/><circle cx="535" cy="124" r="9" class="svg-term"/><circle cx="570" cy="104" r="9" class="svg-term"/><circle cx="605" cy="122" r="9" class="svg-term"/><circle cx="640" cy="108" r="9" class="svg-term"/><circle cx="210" cy="108" r="9" class="svg-fn"/><circle cx="500" cy="110" r="9" class="svg-fn"/><path d="M262,78 C320,40 380,40 440,78" class="svg-arrow" marker-end="url(#arr)"/><path d="M440,112 C380,150 320,150 262,112" class="svg-arrow" marker-end="url(#arr)"/><text x="350" y="40" text-anchor="middle" class="svg-label">transfer promising individuals</text><text x="350" y="166" text-anchor="middle" class="svg-label">share building blocks</text><rect x="250" y="176" width="200" height="30" rx="6" class="svg-box svg-box--accent"/><text y="196.0" text-anchor="middle" class="svg-label"><tspan x="350.0" dy="0">surrogates rank rules cheaply</tspan></text></svg>
<figcaption><b>Figure 3.</b> Multitask GP solves several related tasks at once. Useful individuals and building blocks are transferred between tasks, and surrogate models pre-screen offspring to save expensive simulations.</figcaption>
</figure>
<ul class="contrib-list">
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2021.3065707">Surrogate-Assisted Evolutionary Multitasking Genetic Programming for Dynamic Flexible Job Shop Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2021 · <a href="/publications/publication-journal.html#zhang2020surrogate">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TCYB.2021.3065340">Multitask Genetic Programming Based Generative Hyper-heuristics: A Case Study in Dynamic Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Cybernetics</i>, 2022 · <a href="/publications/publication-journal.html#zhang2021multitask">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2022.3199783">Task Relatedness Based Multitask Genetic Programming for Dynamic Flexible Job Shop Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2023 · <a href="/publications/publication-journal.html#zhang2022task">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TCYB.2022.3196887">Multitask Multiobjective Genetic Programming for Automated Scheduling Heuristic Learning in Dynamic Flexible Job Shop Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Cybernetics</i>, 2023 · <a href="/publications/publication-journal.html#zhang2022multitask">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2022.3169289">Knowledge Transfer Genetic Programming with Auxiliary Population for Solving Uncertain Capacitated Arc Routing Problem</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2023 · <a href="/publications/publication-journal.html#ardeh2022knowledge">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1007/978-3-030-72069-8_9">Knowledge Transfer in Genetic Programming Hyper-heuristics</a><span class="contrib-list__venue"><i>Automated Design of Machine Learning and Search Algorithms</i>, 2021 · <a href="/publications/publication-chapter.html#mei2021knowledge">list entry</a></span> <span class="contrib-list__note">Book chapter</span></li>
</ul>

<h3 class="theme-sub"><span class="theme-sub__num">3</span> New representations: linear and grammar-guided GP</h3>
<figure class="theme-figure">
<svg class="theme-svg" viewBox="0 0 700 220" role="img" aria-labelledby="rep-t rep-d"><title id="rep-t">Tree-based and linear representations</title><desc id="rep-d">The same rule PT + WINQ / NOR shown as a tree and as a linear GP program of register instructions.</desc><text x="150" y="20" text-anchor="middle" class="svg-region-title">TREE-BASED GP</text><line x1="150" y1="52" x2="90" y2="122" class="svg-edge"/><line x1="150" y1="52" x2="210" y2="122" class="svg-edge"/><line x1="210" y1="122" x2="170" y2="190" class="svg-edge"/><line x1="210" y1="122" x2="250" y2="190" class="svg-edge"/><circle cx="150" cy="52" r="21" class="svg-fn"/><text x="150" y="57" text-anchor="middle" class="svg-fn-text">+</text><circle cx="90" cy="122" r="21" class="svg-term"/><text x="90" y="127" text-anchor="middle" class="svg-term-text">PT</text><circle cx="210" cy="122" r="21" class="svg-fn"/><text x="210" y="127" text-anchor="middle" class="svg-fn-text">÷</text><circle cx="170" cy="190" r="21" class="svg-term"/><text x="170" y="195" text-anchor="middle" class="svg-term-text">WINQ</text><circle cx="250" cy="190" r="21" class="svg-term"/><text x="250" y="195" text-anchor="middle" class="svg-term-text">NOR</text><text x="350" y="120" text-anchor="middle" class="svg-big">≡</text><text x="545" y="20" text-anchor="middle" class="svg-region-title">LINEAR GP</text><rect x="420" y="40" width="250" height="150" rx="8" class="svg-code"/><text x="440" y="78" class="svg-code-text">r1 ← WINQ ÷ NOR</text><text x="440" y="108" class="svg-code-text">r0 ← PT + r1</text><text x="440" y="138" class="svg-code-text">return r0</text><text x="545" y="212" text-anchor="middle" class="svg-axis">registers let sub-results be reused (a graph, not a tree)</text></svg>
<figcaption><b>Figure 4.</b> The same rule in tree-based GP and in linear GP. Linear GP stores intermediate results in registers, so sub-expressions can be reused, and grammars can constrain programs to valid, domain-meaningful structures such as if-then-else logic.</figcaption>
</figure>
<p>We introduced linear and grammar-guided linear GP to scheduling, allowing rules with reusable sub-expressions and flow-control logic, and studied how different representations can cooperate.</p>
<ul class="contrib-list">
  <li><a class="contrib-list__title" href="https://doi.org/10.1007/978-3-031-02056-8_11">An Investigation of Multitask Linear Genetic Programming for Dynamic Job Shop Scheduling</a><span class="contrib-list__venue"><i>European Conference on Genetic Programming (EuroGP)</i>, 2022 · <a href="/publications/publication-conf.html#huang2022investigation">list entry</a></span> <span class="badge badge--award">Best Paper Award, EuroGP 2022</span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1145/3583131.3590394">Grammar-guided Linear Genetic Programming for Dynamic Job Shop Scheduling</a><span class="contrib-list__venue"><i>ACM Genetic and Evolutionary Computation Conference (GECCO)</i>, 2023 · <a href="/publications/publication-conf.html#huang2023grammar">list entry</a></span> <span class="badge badge--award">Best Paper Award, GECCO 2023</span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2023.3263871">Multitask Linear Genetic Programming with Shared Individuals and its Application to Dynamic Job Shop Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2024 · <a href="/publications/publication-journal.html#huang2023multitask">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1007/s10710-023-09478-8">Bridging Directed Acyclic Graphs to Linear Representations in Linear Genetic Programming: A Case Study of Dynamic Scheduling</a><span class="contrib-list__venue"><i>Genetic Programming and Evolvable Machines</i>, 2024 · <a href="/publications/publication-journal.html#huang2023bridging">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2024.3353207">Toward Evolving Dispatching Rules With Flow Control Operations By Grammar-Guided Linear Genetic Programming</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2025 · <a href="/publications/publication-journal.html#huang2024toward">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1162/evco.a.25">Cross-Representation Genetic Programming: A Case Study on Tree-based and Linear Representations</a><span class="contrib-list__venue"><i>Evolutionary Computation</i>, 2025 · <a href="/publications/publication-journal.html#huang2025cross">list entry</a></span></li>
</ul>

<h3 class="theme-sub"><span class="theme-sub__num">4</span> Routing policies under uncertainty</h3>
<p>For arc and vehicle routing with uncertain demands and travel costs, we evolve <b>routing policies</b> that let each vehicle decide its next task on the fly, including collaboration between vehicles, niching and multi-objective trade-offs.</p>
<ul class="contrib-list">
  <li><a class="contrib-list__title" href="https://doi.org/10.1162/evco_a_00267">Genetic Programming Hyper-Heuristics with Vehicle Collaboration for Uncertain Capacitated Arc Routing Problems</a><span class="contrib-list__venue"><i>Evolutionary Computation</i>, 2020 · <a href="/publications/publication-journal.html#maclachlan2019genetic">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1162/evco_a_00256">A Predictive-Reactive Approach with Genetic Programming and Cooperative Coevolution for Uncertain Capacitated Arc Routing Problem</a><span class="contrib-list__venue"><i>Evolutionary Computation</i>, 2020 · <a href="/publications/publication-journal.html#liu2019predictive">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2021.3095261">Genetic Programming with Niching for Uncertain Capacitated Arc Routing Problem</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2022 · <a href="/publications/publication-journal.html#wang2021genetic">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2022.3195165">A Multi-Objective Genetic Programming Algorithm with α dominance and Archive for Uncertain Capacitated Arc Routing Problem</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2023 · <a href="/publications/publication-journal.html#wang2022multi">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2021.3129278">Genetic Programming with Knowledge Transfer and Guided Search for Uncertain Capacitated Arc Routing Problem</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2022 · <a href="/publications/publication-journal.html#ardeh2021genetic">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1007/978-3-032-23604-3_7">Adaptive Curriculum Learning in Genetic Programming–Guided Local Search for Large-Scale Vehicle Routing Problems</a><span class="contrib-list__venue"><i>International Conference on the Applications of Evolutionary Computation (EvoApps)</i>, 2026 · <a href="/publications/publication-conf.html#liu2026adaptive">list entry</a></span> <span class="badge badge--award">Best Student Paper Award, EvoStar 2026</span></li>
</ul>

<h3 class="theme-sub"><span class="theme-sub__num">5</span> Interpretable and explainable heuristics</h3>
<p>Because the output of GP is a formula, it can be made genuinely understandable. We develop methods to keep evolved rules small, to explain the decisions of complex rules, and we surveyed how GP contributes to explainable AI.</p>
<ul class="contrib-list">
  <li><a class="contrib-list__title" href="https://doi.org/10.1145/3512290.3528723">Local Ranking Explanation for Genetic Programming Evolved Routing Policies for Uncertain Capacitated Arc Routing Problems</a><span class="contrib-list__venue"><i>ACM Genetic and Evolutionary Computation Conference (GECCO)</i>, 2022 · <a href="/publications/publication-conf.html#wang2022local">list entry</a></span> <span class="badge badge--award">Best Paper Award, GECCO 2022</span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2023.3238741">Explaining Genetic Programming-Evolved Routing Policies for Uncertain Capacitated Arc Routing Problems</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2024 · <a href="/publications/publication-journal.html#wang2023explaining">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2022.3225509">Explainable Artificial Intelligence by Genetic Programming: A Survey</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2023 · <a href="/publications/publication-journal.html#mei2022explainable">list entry</a></span> <span class="contrib-list__note">Survey</span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2026.3710449">Balancing Effectiveness and Structural Complexities in Scheduling Heuristics via Multi/Many-objective Multiform Genetic Programming</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2026 · <a href="/publications/publication-journal.html#pang2026balancing">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2026.3660890">Genetic Programming with Model Driven Dimension Repair for Learning Interpretable Appointment Rules</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2026 · <a href="/publications/publication-journal.html#zhang2026genetic">list entry</a></span></li>
</ul>

<h3 class="theme-sub"><span class="theme-sub__num">6</span> GP and reinforcement learning: learning to optimise</h3>
<p>We compare and combine GP with deep reinforcement learning, two complementary ways of learning to make sequential decisions, and extend GP to learn whole sets of trade-off rules.</p>
<ul class="contrib-list">
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/MCI.2024.3363970">Genetic Programming and Reinforcement Learning on Learning Heuristics for Dynamic Scheduling: A Preliminary Comparison</a><span class="contrib-list__venue"><i>IEEE Computational Intelligence Magazine</i>, 2024 · <a href="/publications/publication-journal.html#xu2023genetic3">list entry</a></span> <span class="badge badge--award">Outstanding Paper Award, IEEE CIM 2026</span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1007/s10462-024-11059-9">Learn to Optimise for Job Shop Scheduling: A Survey with Comparison between Genetic Programming and Reinforcement Learning</a><span class="contrib-list__venue"><i>Artificial Intelligence Review</i>, 2025 · <a href="/publications/publication-journal.html#xu2024learn">list entry</a></span> <span class="contrib-list__note">Survey</span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2024.3395699">Niching Genetic Programming to Learn Actions for Deep Reinforcement Learning in Dynamic Flexible Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2026 · <a href="/publications/publication-journal.html#xu2024niching">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2025.3568375">Pareto Set Learning through Genetic Programming for Multi-Objective Dynamic Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2025 · <a href="/publications/publication-journal.html#xu2025pareto">list entry</a></span></li>
</ul>

<h3 class="theme-sub"><span class="theme-sub__num">7</span> New application domains</h3>
<p>The same idea transfers well beyond manufacturing — to cloud and fog computing, traffic signal control, air traffic management, ports, multi-agent path planning, and even to designing components of other algorithms.</p>
<div class="theme-apps">
  <span class="badge">Cloud &amp; fog workflow scheduling</span>
  <span class="badge">Traffic signal control</span>
  <span class="badge">Air traffic flow management</span>
  <span class="badge">Yard crane scheduling</span>
  <span class="badge">Multi-agent path planning</span>
  <span class="badge">Emergency medical services</span>
  <span class="badge">Ant colony optimisation design</span>
</div>
<ul class="contrib-list">
  <li><a class="contrib-list__title" href="https://doi.org/10.1145/3638529.3654037">Learning Traffic Signal Control via Genetic Programming</a><span class="contrib-list__venue"><i>ACM Genetic and Evolutionary Computation Conference (GECCO)</i>, 2024 · <a href="/publications/publication-conf.html#liao2024learning">list entry</a></span> <span class="badge badge--award">Best Paper Award, GECCO 2024</span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2025.3578575">GPLight+: A Genetic Programming Method for Learning Symmetric Traffic Signal Control Policy</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2025 · <a href="/publications/publication-journal.html#liao2025gplight+">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TSC.2023.3249160">Genetic Programming for Dynamic Workflow Scheduling in Fog Computing</a><span class="contrib-list__venue"><i>IEEE Transactions on Services Computing</i>, 2023 · <a href="/publications/publication-journal.html#xu2023genetic1">list entry</a></span></li>
  <li><a class="contrib-list__title" href="/publications/publication-journal.html#sun2024cooperative">Cooperative Coevolution Genetic Programming for Dynamic Joint Workflow Scheduling and Container Scaling in Cloud-Fog Computing</a><span class="contrib-list__venue"><i>IEEE Transactions on Services Computing</i>, 2024 · <a href="/publications/publication-journal.html#sun2024cooperative">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2024.3512552">Genetic Programming with Multi-fidelity Surrogates for Large-scale Dynamic Air Traffic Flow Management</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2025 · <a href="/publications/publication-journal.html#guo2024genetic">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TEVC.2026.3721249">Semantic-Guided Memetic Genetic Programming for Evolving Scheduling Rules for Online Yard Crane Scheduling</a><span class="contrib-list__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 2026 · <a href="/publications/publication-journal.html#jin2026semantic">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1109/TAI.2024.3522861">Learning to Communicate among Agents for Large-scale Dynamic Path Planning with Genetic Programming Hyper-Heuristic</a><span class="contrib-list__venue"><i>IEEE Transactions on Artificial Intelligence</i>, 2025 · <a href="/publications/publication-journal.html#liao2024learning">list entry</a></span></li>
  <li><a class="contrib-list__title" href="https://doi.org/10.1007/s12293-025-00435-9">Automated Design of State Transition Rules in Ant Colony Optimization by Genetic Programming: A Comprehensive Investigation</a><span class="contrib-list__venue"><i>Memetic Computing</i>, 2025 · <a href="/publications/publication-journal.html#lin2025automated">list entry</a></span></li>
</ul>
<p class="contrib-list__extra"><span class="badge badge--award">HUMIES Silver Award 2023</span> Jordan MacLachlan's work on <a href="https://dl.acm.org/doi/abs/10.1145/3629719.3629720">genetic programming for emergency medical services</a> was recognised for human-competitive results at GECCO 2023.</p>

<a name="output"></a>
<h2>Research Output</h2>
<figure class="theme-figure">
<svg class="theme-svg" viewBox="0 0 720 270" role="img" aria-labelledby="chart-t chart-d"><title id="chart-t">Papers per year</title><desc id="chart-d">Stacked bars of journal articles and conference papers on genetic programming and automated algorithm design, 2014 to 2026.</desc>
<line x1="46" x2="706" y1="222.0" y2="222.0" class="svg-grid"/><text x="38" y="226.0" class="svg-axis" text-anchor="end">0</text>
<line x1="46" x2="706" y1="172.0" y2="172.0" class="svg-grid"/><text x="38" y="176.0" class="svg-axis" text-anchor="end">5</text>
<line x1="46" x2="706" y1="122.0" y2="122.0" class="svg-grid"/><text x="38" y="126.0" class="svg-axis" text-anchor="end">10</text>
<line x1="46" x2="706" y1="72.0" y2="72.0" class="svg-grid"/><text x="38" y="76.0" class="svg-axis" text-anchor="end">15</text>
<line x1="46" x2="706" y1="22.0" y2="22.0" class="svg-grid"/><text x="38" y="26.0" class="svg-axis" text-anchor="end">20</text>
<rect x="55.6" y="222.0" width="31.5" height="0.0" class="svg-bar-j"><title>2014: 0 journal</title></rect>
<rect x="55.6" y="202.0" width="31.5" height="20.0" class="svg-bar-c"><title>2014: 2 conference</title></rect>
<text x="71.4" y="197.0" class="svg-value" text-anchor="middle">2</text>
<text x="71.4" y="239" class="svg-axis" text-anchor="middle">2014</text>
<rect x="106.4" y="222.0" width="31.5" height="0.0" class="svg-bar-j"><title>2015: 0 journal</title></rect>
<rect x="106.4" y="212.0" width="31.5" height="10.0" class="svg-bar-c"><title>2015: 1 conference</title></rect>
<text x="122.2" y="207.0" class="svg-value" text-anchor="middle">1</text>
<text x="122.2" y="239" class="svg-axis" text-anchor="middle">2015</text>
<rect x="157.2" y="222.0" width="31.5" height="0.0" class="svg-bar-j"><title>2016: 0 journal</title></rect>
<rect x="157.2" y="162.0" width="31.5" height="60.0" class="svg-bar-c"><title>2016: 6 conference</title></rect>
<text x="172.9" y="157.0" class="svg-value" text-anchor="middle">6</text>
<text x="172.9" y="239" class="svg-axis" text-anchor="middle">2016</text>
<rect x="208.0" y="202.0" width="31.5" height="20.0" class="svg-bar-j"><title>2017: 2 journal</title></rect>
<rect x="208.0" y="92.0" width="31.5" height="110.0" class="svg-bar-c"><title>2017: 11 conference</title></rect>
<text x="223.7" y="87.0" class="svg-value" text-anchor="middle">13</text>
<text x="223.7" y="239" class="svg-axis" text-anchor="middle">2017</text>
<rect x="258.7" y="212.0" width="31.5" height="10.0" class="svg-bar-j"><title>2018: 1 journal</title></rect>
<rect x="258.7" y="92.0" width="31.5" height="120.0" class="svg-bar-c"><title>2018: 12 conference</title></rect>
<text x="274.5" y="87.0" class="svg-value" text-anchor="middle">13</text>
<text x="274.5" y="239" class="svg-axis" text-anchor="middle">2018</text>
<rect x="309.5" y="212.0" width="31.5" height="10.0" class="svg-bar-j"><title>2019: 1 journal</title></rect>
<rect x="309.5" y="72.0" width="31.5" height="140.0" class="svg-bar-c"><title>2019: 14 conference</title></rect>
<text x="325.2" y="67.0" class="svg-value" text-anchor="middle">15</text>
<text x="325.2" y="239" class="svg-axis" text-anchor="middle">2019</text>
<rect x="360.3" y="192.0" width="31.5" height="30.0" class="svg-bar-j"><title>2020: 3 journal</title></rect>
<rect x="360.3" y="92.0" width="31.5" height="100.0" class="svg-bar-c"><title>2020: 10 conference</title></rect>
<text x="376.0" y="87.0" class="svg-value" text-anchor="middle">13</text>
<text x="376.0" y="239" class="svg-axis" text-anchor="middle">2020</text>
<rect x="411.0" y="162.0" width="31.5" height="60.0" class="svg-bar-j"><title>2021: 6 journal</title></rect>
<rect x="411.0" y="52.0" width="31.5" height="110.0" class="svg-bar-c"><title>2021: 11 conference</title></rect>
<text x="426.8" y="47.0" class="svg-value" text-anchor="middle">17</text>
<text x="426.8" y="239" class="svg-axis" text-anchor="middle">2021</text>
<rect x="461.8" y="162.0" width="31.5" height="60.0" class="svg-bar-j"><title>2022: 6 journal</title></rect>
<rect x="461.8" y="22.0" width="31.5" height="140.0" class="svg-bar-c"><title>2022: 14 conference</title></rect>
<text x="477.5" y="17.0" class="svg-value" text-anchor="middle">20</text>
<text x="477.5" y="239" class="svg-axis" text-anchor="middle">2022</text>
<rect x="512.6" y="152.0" width="31.5" height="70.0" class="svg-bar-j"><title>2023: 7 journal</title></rect>
<rect x="512.6" y="82.0" width="31.5" height="70.0" class="svg-bar-c"><title>2023: 7 conference</title></rect>
<text x="528.3" y="77.0" class="svg-value" text-anchor="middle">14</text>
<text x="528.3" y="239" class="svg-axis" text-anchor="middle">2023</text>
<rect x="563.3" y="112.0" width="31.5" height="110.0" class="svg-bar-j"><title>2024: 11 journal</title></rect>
<rect x="563.3" y="32.0" width="31.5" height="80.0" class="svg-bar-c"><title>2024: 8 conference</title></rect>
<text x="579.1" y="27.0" class="svg-value" text-anchor="middle">19</text>
<text x="579.1" y="239" class="svg-axis" text-anchor="middle">2024</text>
<rect x="614.1" y="122.0" width="31.5" height="100.0" class="svg-bar-j"><title>2025: 10 journal</title></rect>
<rect x="614.1" y="22.0" width="31.5" height="100.0" class="svg-bar-c"><title>2025: 10 conference</title></rect>
<text x="629.8" y="17.0" class="svg-value" text-anchor="middle">20</text>
<text x="629.8" y="239" class="svg-axis" text-anchor="middle">2025</text>
<rect x="664.9" y="132.0" width="31.5" height="90.0" class="svg-bar-j"><title>2026: 9 journal</title></rect>
<rect x="664.9" y="82.0" width="31.5" height="50.0" class="svg-bar-c"><title>2026: 5 conference</title></rect>
<text x="680.6" y="77.0" class="svg-value" text-anchor="middle">14</text>
<text x="680.6" y="239" class="svg-axis" text-anchor="middle">2026</text>
<rect x="54" y="22" width="12" height="12" class="svg-bar-j"/><text x="72" y="32" class="svg-label">Journal articles &amp; books</text>
<rect x="236" y="22" width="12" height="12" class="svg-bar-c"/><text x="254" y="32" class="svg-label">Conference papers</text>
</svg>
<figcaption><b>Figure 5.</b> My papers on GP and automated algorithm design per year (167 in total), identified by title keywords in my <a href="/publications/">publication lists</a>. The 2026 count covers papers published so far this year.</figcaption>
</figure>

<p class="home-more"><a href="/publications/">Full publication list →</a> &nbsp; <a href="/">← Back to home</a></p>
