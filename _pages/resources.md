---
layout: archive
title: "Resources"
permalink: /resources/
author_profile: true
---

<p class="theme-lead">Open-source code, benchmark datasets and tutorials from my research, followed by external libraries and reading I recommend.</p>

<nav class="pub-jump" aria-label="On this page">
  <a href="#my-code"><i class="fab fa-github" aria-hidden="true"></i> My code</a>
  <a href="#my-datasets"><i class="fas fa-database" aria-hidden="true"></i> My datasets</a>
  <a href="#tutorials"><i class="fas fa-chalkboard-teacher" aria-hidden="true"></i> Tutorials &amp; talks</a>
  <a href="#libraries"><i class="fas fa-toolbox" aria-hidden="true"></i> Libraries</a>
  <a href="#benchmarks"><i class="fas fa-table" aria-hidden="true"></i> Benchmarks</a>
  <a href="#reading"><i class="fas fa-book-open" aria-hidden="true"></i> Further reading</a>
</nav>

<h2 id="my-code">My Code</h2>
<p class="section-intro">Implementations of algorithms from my papers. Please cite the corresponding paper if you use them.</p>
<div class="repo-grid">
  <article class="repo-card repo-card--featured">
    <div class="repo-card__head">
      <i class="fab fa-github" aria-hidden="true"></i>
      <a class="repo-card__name" href="https://github.com/meiyi1986/MAENS">MAENS</a>
      <span class="repo-card__lang repo-card__lang--cpp">C++</span>
    </div>
    <p>Memetic Algorithm with Extended Neighbourhood Search for the capacitated arc routing problem, a widely used benchmark algorithm with the large-step Merge-Split operator.</p>
    <div class="repo-card__foot">
      <span class="repo-card__badges"><img src="https://img.shields.io/github/stars/meiyi1986/MAENS?style=flat&amp;label=stars&amp;color=11685f" alt="GitHub stars" loading="lazy"> <img src="https://img.shields.io/github/forks/meiyi1986/MAENS?style=flat&amp;label=forks&amp;color=39538c" alt="GitHub forks" loading="lazy"></span>
      <span class="repo-card__links"><a href="https://github.com/meiyi1986/MAENS">Repository</a> · <a href="https://doi.org/10.1109/TEVC.2009.2023449">Paper (IEEE TEVC 2009)</a></span>
    </div>
  </article>
  <article class="repo-card repo-card--featured">
    <div class="repo-card__head">
      <i class="fab fa-github" aria-hidden="true"></i>
      <a class="repo-card__name" href="https://github.com/meiyi1986/GPJSS">GPJSS</a>
      <span class="repo-card__lang repo-card__lang--java">Java</span>
    </div>
    <p>Genetic programming hyper-heuristics for automatically evolving dispatching rules for (dynamic) job shop scheduling, built on the ECJ library.</p>
    <div class="repo-card__foot">
      <span class="repo-card__badges"><img src="https://img.shields.io/github/stars/meiyi1986/GPJSS?style=flat&amp;label=stars&amp;color=11685f" alt="GitHub stars" loading="lazy"> <img src="https://img.shields.io/github/forks/meiyi1986/GPJSS?style=flat&amp;label=forks&amp;color=39538c" alt="GitHub forks" loading="lazy"></span>
      <span class="repo-card__links"><a href="https://github.com/meiyi1986/GPJSS">Repository</a> · <a href="/research/genetic-programming/">Research theme</a></span>
    </div>
  </article>
  <article class="repo-card">
    <div class="repo-card__head">
      <i class="fab fa-github" aria-hidden="true"></i>
      <a class="repo-card__name" href="https://github.com/meiyi1986/gpucarp">gpucarp</a>
      <span class="repo-card__lang repo-card__lang--java">Java</span>
    </div>
    <p>Meta-heuristics and genetic programming hyper-heuristics that evolve routing policies for the uncertain capacitated arc routing problem; includes the gdb, val and egl datasets.</p>
    <div class="repo-card__foot">
      <span class="repo-card__badges"><img src="https://img.shields.io/github/stars/meiyi1986/gpucarp?style=flat&amp;label=stars&amp;color=11685f" alt="GitHub stars" loading="lazy"> <img src="https://img.shields.io/github/forks/meiyi1986/gpucarp?style=flat&amp;label=forks&amp;color=39538c" alt="GitHub forks" loading="lazy"></span>
      <span class="repo-card__links"><a href="https://github.com/meiyi1986/gpucarp">Repository</a></span>
    </div>
  </article>
  <article class="repo-card">
    <div class="repo-card__head">
      <i class="fab fa-github" aria-hidden="true"></i>
      <a class="repo-card__name" href="https://github.com/meiyi1986/gporienteering">gporienteering</a>
      <span class="repo-card__lang repo-card__lang--java">Java</span>
    </div>
    <p>Genetic programming hyper-heuristics for the stochastic (team) orienteering problem.</p>
    <div class="repo-card__foot">
      <span class="repo-card__badges"><img src="https://img.shields.io/github/stars/meiyi1986/gporienteering?style=flat&amp;label=stars&amp;color=11685f" alt="GitHub stars" loading="lazy"> <img src="https://img.shields.io/github/forks/meiyi1986/gporienteering?style=flat&amp;label=forks&amp;color=39538c" alt="GitHub forks" loading="lazy"></span>
      <span class="repo-card__links"><a href="https://github.com/meiyi1986/gporienteering">Repository</a></span>
    </div>
  </article>
  <article class="repo-card">
    <div class="repo-card__head">
      <i class="fas fa-cube" aria-hidden="true"></i>
      <a class="repo-card__name" href="https://www.mathworks.com/matlabcentral/fileexchange/45783-the-cc-gdg-cmaes-algorithm">CC-GDG-CMAES</a>
      <span class="repo-card__lang repo-card__lang--matlab">MATLAB</span>
    </div>
    <p>Competitive divide-and-conquer algorithm for unconstrained large-scale black-box optimisation, combining global differential grouping with CMA-ES.</p>
    <div class="repo-card__foot">
      <span class="repo-card__badges"></span>
      <span class="repo-card__links"><a href="https://www.mathworks.com/matlabcentral/fileexchange/45783-the-cc-gdg-cmaes-algorithm">Download</a> · <a href="https://doi.org/10.1145/2791291">Paper (ACM TOMS 2016)</a></span>
    </div>
  </article>
  <article class="repo-card">
    <div class="repo-card__head">
      <i class="fab fa-github" aria-hidden="true"></i>
      <a class="repo-card__name" href="https://github.com/meiyi1986/JourneyPlanner">JourneyPlanner</a>
      <span class="repo-card__lang repo-card__lang--java">Java</span>
    </div>
    <p>Earliest-arrival public transit journey planner based on round-based public transit routing (RAPTOR), with GTFS import and an Adelaide example.</p>
    <div class="repo-card__foot">
      <span class="repo-card__badges"><img src="https://img.shields.io/github/stars/meiyi1986/JourneyPlanner?style=flat&amp;label=stars&amp;color=11685f" alt="GitHub stars" loading="lazy"> <img src="https://img.shields.io/github/forks/meiyi1986/JourneyPlanner?style=flat&amp;label=forks&amp;color=39538c" alt="GitHub forks" loading="lazy"></span>
      <span class="repo-card__links"><a href="https://github.com/meiyi1986/JourneyPlanner">Repository</a></span>
    </div>
  </article>
</div>

<h2 id="my-datasets">My Datasets</h2>
<p class="section-intro">Capacitated arc routing (CARP) benchmark instances used in my research, free to download.</p>
<ul class="data-list">
  <li><a class="data-list__name" href="/files/data/carp/gdb.zip"><i class="fas fa-file-archive" aria-hidden="true"></i> gdb</a><span class="data-list__desc">23 small instances (~30 nodes, ~60 required edges).</span></li>
  <li><a class="data-list__name" href="/files/data/carp/val.zip"><i class="fas fa-file-archive" aria-hidden="true"></i> val</a><span class="data-list__desc">10 groups of medium to large instances (~50 nodes, ~100 required edges); each group has 3–4 instances (A–D) on the same graph with different vehicle capacities.</span></li>
  <li><a class="data-list__name" href="/files/data/carp/egl.zip"><i class="fas fa-file-archive" aria-hidden="true"></i> egl</a><span class="data-list__desc">8 groups of large instances (~150 nodes, ~200 required edges): e1–e4 and s1–s4 use the same graph with different required edges; 3 capacities (A–C) each.</span></li>
  <li><a class="data-list__name" href="/files/data/carp/EGL-G.zip"><i class="fas fa-file-archive" aria-hidden="true"></i> EGL-G</a><span class="data-list__desc">2 groups of large instances (~250 nodes, ~400 required edges), 5 capacities (A–E) each.</span></li>
  <li><a class="data-list__name" href="/files/data/carp/BeijingHefei.zip"><i class="fas fa-file-archive" aria-hidden="true"></i> Beijing &amp; Hefei</a><span class="data-list__desc">Two large datasets generated from the road networks of Beijing and Hefei, 10 instances each with thousands of edges.</span></li>
  <li><a class="data-list__name" href="/files/data/carp/Beullens.zip"><i class="fas fa-file-archive" aria-hidden="true"></i> Beullens</a><span class="data-list__desc">The Beullens et al. CARP benchmark instances.</span></li>
  <li><a class="data-list__name" href="/files/data/carp/Instances.zip"><i class="fas fa-file-archive" aria-hidden="true"></i> Large-scale instances</a><span class="data-list__desc">Large-scale CARP instances, with the <a href="/files/data/carp/results.zip">best solutions</a> we found.</span></li>
  <li><a class="data-list__name" href="/files/data/mdcarp.zip"><i class="fas fa-file-archive" aria-hidden="true"></i> Multi-depot CARP</a><span class="data-list__desc">Multi-depot capacitated arc routing instances.</span></li>
</ul>

<h2 id="tutorials">Tutorials &amp; Talks</h2>
<div class="repo-grid">
  <article class="repo-card repo-card--featured">
    <div class="repo-card__head">
      <i class="fab fa-github" aria-hidden="true"></i>
      <a class="repo-card__name" href="https://github.com/meiyi1986/tutorials">tutorials</a>
      <span class="repo-card__lang repo-card__lang--jupyter-notebook">Jupyter Notebook</span>
    </div>
    <p>Jupyter notebook tutorials on artificial intelligence, evolutionary computation and optimisation/operations research, such as Bayesian networks, planning and scheduling, and genetic programming.</p>
    <div class="repo-card__foot">
      <span class="repo-card__badges"><img src="https://img.shields.io/github/stars/meiyi1986/tutorials?style=flat&amp;label=stars&amp;color=11685f" alt="GitHub stars" loading="lazy"> <img src="https://img.shields.io/github/forks/meiyi1986/tutorials?style=flat&amp;label=forks&amp;color=39538c" alt="GitHub forks" loading="lazy"></span>
      <span class="repo-card__links"><a href="https://github.com/meiyi1986/tutorials">Repository</a></span>
    </div>
  </article>
  <article class="repo-card">
    <div class="repo-card__head">
      <i class="fas fa-video" aria-hidden="true"></i>
      <a class="repo-card__name" href="https://ieeetv.ieee.org/ieeetv-specials/genetic-programming-hyper-heuristics-for-combinatorial-optimisation-yi-mei-cis-webinar">IEEE CIS Webinar</a>
      <span class="repo-card__lang repo-card__lang--video">Video</span>
    </div>
    <p>Genetic Programming Hyper-Heuristics for Combinatorial Optimisation, an IEEE Computational Intelligence Society webinar.</p>
    <div class="repo-card__foot"><span class="repo-card__badges"></span><span class="repo-card__links"><a href="https://ieeetv.ieee.org/ieeetv-specials/genetic-programming-hyper-heuristics-for-combinatorial-optimisation-yi-mei-cis-webinar">Watch on IEEE.tv</a></span></div>
  </article>
</div>

<h2 id="libraries">Libraries &amp; Frameworks</h2>
<p class="section-intro">Third-party software for evolutionary computation, genetic programming and hyper-heuristics.</p>
<div class="tool-grid">
  <a class="tool-card" href="https://cs.gmu.edu/~eclab/projects/ecj/"><span class="tool-card__name">ECJ</span><span class="tool-card__lang">Java</span><span class="tool-card__note">Highly recommended for GP</span></a>
  <a class="tool-card" href="https://deap.readthedocs.io/en/master/"><span class="tool-card__name">DEAP</span><span class="tool-card__lang">Python</span></a>
  <a class="tool-card" href="http://gplearn.readthedocs.io/en/stable/"><span class="tool-card__name">gplearn</span><span class="tool-card__lang">Python</span></a>
  <a class="tool-card" href="https://squillero.github.io/microgp4/"><span class="tool-card__name">MicroGP</span><span class="tool-card__lang">Python</span></a>
  <a class="tool-card" href="https://aarongarrett.github.io/inspyred/"><span class="tool-card__name">Inspyred</span><span class="tool-card__lang">Python</span></a>
  <a class="tool-card" href="https://jenetics.io/"><span class="tool-card__name">Jenetics</span><span class="tool-card__lang">Java</span></a>
  <a class="tool-card" href="http://chgagne.github.io/beagle/"><span class="tool-card__name">Open BEAGLE</span><span class="tool-card__lang">C++</span></a>
  <a class="tool-card" href="http://www.asap.cs.nott.ac.uk/external/chesc2011/hyflex_description.html"><span class="tool-card__name">HyFlex</span><span class="tool-card__lang">Java</span><span class="tool-card__note">Hyper-heuristic framework</span></a>
  <a class="tool-card" href="http://titancs.ukzn.ac.za/EvoHyp.aspx"><span class="tool-card__name">EvoHyp</span><span class="tool-card__lang">Java</span><span class="tool-card__note">Hyper-heuristic framework</span></a>
  <a class="tool-card" href="https://www.nutonian.com/products/eureqa/"><span class="tool-card__name">Eureqa</span><span class="tool-card__lang">App</span><span class="tool-card__note">Symbolic regression software</span></a>
</div>

<h2 id="benchmarks">Benchmark Libraries</h2>
<ul class="cv-list cv-list--plain">
  <li><span class="cv-list__year">Job shop scheduling</span><div><a href="http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html">Taillard's benchmark datasets</a></div></li>
  <li><span class="cv-list__year">Flexible job shop scheduling</span><div><a href="http://people.idsia.ch/~monaldo/fjsp.html">Flexible job shop scheduling datasets</a></div></li>
  <li><span class="cv-list__year">Vehicle routing</span><div>Instances for many variants on <a href="https://w1.cirrelt.ca/~vidalt/en/VRP-resources.html">Dr T. Vidal's page</a>; the <a href="http://vrp.atd-lab.inf.puc-rio.br/index.php/en">CVRP library</a> with <a href="http://vrp.atd-lab.inf.puc-rio.br/index.php/en/plotted-instances">plotted instances and solutions</a></div></li>
  <li><span class="cv-list__year">Bin packing</span><div>A comprehensive <a href="http://or.dei.unibo.it/library/bpplib">problem library</a></div></li>
  <li><span class="cv-list__year">Timetabling</span><div>The <a href="http://www.cs.nott.ac.uk/~pszrq/data.htm">University of Nottingham library</a> and the <a href="https://www.unitime.org/exam_datasets.php">UniTime benchmark website</a></div></li>
</ul>

<h2 id="reading">Further Reading</h2>
<ul class="reading-list">
  <li>Xin Yao's public lecture: <a href="https://www.youtube.com/watch?v=pcl08XA1REM">What can evolutionary computation do for you?</a></li>
  <li>A. E. Eiben's TED talk: <a href="https://www.youtube.com/watch?v=WJX_wAKhg8A">Tech Kangaroos – Evolution at Work</a></li>
  <li>Keith Downing's TED talk: <a href="https://www.youtube.com/watch?v=D3zUmfDd79s">Evolutionary computation</a></li>
  <li><a href="https://strandbeest.com">Strandbeest</a>: kinetic sculptures designed with evolutionary computation</li>
  <li>Learning to play Flappy Bird with Cartesian genetic programming: <a href="https://github.com/ShuhuaGao/gpFlappyBird">GitHub</a></li>
  <li>Hyper-heuristic bibliography: <a href="https://mustafamisir.github.io/hh.html">mustafamisir.github.io/hh.html</a></li>
  <li><i>Science</i>: “<a href="http://science.sciencemag.org/content/324/5923/81">Distilling Free-Form Natural Laws from Experimental Data</a>”, discovering natural laws with genetic programming (symbolic regression)</li>
  <li><i>Nature</i>: “<a href="https://www.nature.com/articles/nature14544">From evolutionary computation to the evolution of things</a>”</li>
</ul>
