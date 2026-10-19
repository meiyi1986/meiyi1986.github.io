---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

My [Google Scholar profile](https://scholar.google.com/citations?user=vTC_7_wAAAAJ) shows <b>12,000+</b> citations and an h-index of <b>56</b>.

<nav class="pub-jump" aria-label="Publication lists">
  <a href="#selected"><i class="fas fa-star" aria-hidden="true"></i> Selected</a>
  <a href="publication-book.html"><i class="fas fa-book" aria-hidden="true"></i> Books</a>
  <a href="publication-journal.html"><i class="fas fa-newspaper" aria-hidden="true"></i> Journal articles</a>
  <a href="publication-conf.html"><i class="fas fa-users" aria-hidden="true"></i> Conference papers</a>
  <a href="publication-chapter.html"><i class="fas fa-bookmark" aria-hidden="true"></i> Book chapters</a>
</nav>

<a name="selected"></a>
<h2>Selected Publications</h2>
<p>A selection of my most cited work, grouped by research area.</p>

<h3 class="pub-group__title">Large-Scale Optimisation</h3>
<p class="pub-group__intro">Decomposing very large problems into smaller, interacting sub-problems so that they can be solved cooperatively.</p>
<ul class="pub-features">
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1109/TEVC.2013.2281543">Cooperative Co-evolution with Differential Grouping for Large Scale Optimization</a></span>
    <span class="pub-feature__authors">M. N. Omidvar, X. Li, <b>Y. Mei</b>, X. Yao</span>
    <span class="pub-feature__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 18(3):378–393, 2014 <span class="news-tag">TEVC Outstanding Paper Award</span></span>
    <p>Introduces <em>differential grouping</em>, which detects interactions between decision variables automatically and uses them to decompose a large-scale problem for cooperative co-evolution. It is widely used as a decomposition method in large-scale black-box optimisation.</p>
  </li>
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1145/2791291">A Competitive Divide-and-Conquer Algorithm for Unconstrained Large-Scale Black-Box Optimization</a></span>
    <span class="pub-feature__authors"><b>Y. Mei</b>, M. N. Omidvar, X. Li, X. Yao</span>
    <span class="pub-feature__venue"><i>ACM Transactions on Mathematical Software</i>, 42(2):13:1–24, 2016</span>
    <p>Combines automatic variable grouping with a powerful sub-problem optimiser in a divide-and-conquer framework, released with an open-source MATLAB implementation.</p>
  </li>
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1109/TEVC.2013.2281503">Cooperative Coevolution with Route Distance Grouping for Large-Scale Capacitated Arc Routing Problems</a></span>
    <span class="pub-feature__authors"><b>Y. Mei</b>, X. Li, X. Yao</span>
    <span class="pub-feature__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 18(3):435–449, 2014</span>
    <p>Brings cooperative co-evolution to large-scale arc routing: <em>route distance grouping</em> uses the distances between routes to decide which parts of the solution should be optimised together.</p>
  </li>
</ul>

<h3 class="pub-group__title">Genetic Programming for Scheduling</h3>
<p class="pub-group__intro">Automatically learning scheduling heuristics for dynamic, uncertain production environments with genetic programming (GP).</p>
<ul class="pub-features">
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1007/s40747-017-0036-x">Genetic Programming for Production Scheduling: A Survey with a Unified Framework</a></span>
    <span class="pub-feature__authors">S. Nguyen, <b>Y. Mei</b>, M. Zhang</span>
    <span class="pub-feature__venue"><i>Complex &amp; Intelligent Systems</i>, 3(1):41–66, 2017</span>
    <p>A survey that organises GP-based hyper-heuristics for production scheduling into a unified framework, covering representations, evaluation, and directions for future research.</p>
  </li>
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1109/TCYB.2020.3024849">Evolving Scheduling Heuristics via Genetic Programming with Feature Selection in Dynamic Flexible Job-Shop Scheduling</a></span>
    <span class="pub-feature__authors">F. Zhang, <b>Y. Mei</b>, S. Nguyen, M. Zhang</span>
    <span class="pub-feature__venue"><i>IEEE Transactions on Cybernetics</i>, 51(4):1797–1811, 2021</span>
    <p>Integrates feature selection into GP so that the evolved routing and sequencing rules use only the most relevant features, giving smaller and more interpretable heuristics without losing effectiveness.</p>
  </li>
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1109/TEVC.2021.3065707">Surrogate-Assisted Evolutionary Multitask Genetic Programming for Dynamic Flexible Job Shop Scheduling</a></span>
    <span class="pub-feature__authors">F. Zhang, <b>Y. Mei</b>, S. Nguyen, M. Zhang, K. C. Tan</span>
    <span class="pub-feature__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 25(4):651–665, 2021</span>
    <p>Learns scheduling heuristics for several related scheduling tasks at once, sharing knowledge between tasks and using surrogate models to cut the computational cost of evaluation.</p>
  </li>
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1109/TEVC.2023.3255246">Survey on Genetic Programming and Machine Learning Techniques for Heuristic Design in Job Shop Scheduling</a></span>
    <span class="pub-feature__authors">F. Zhang, <b>Y. Mei</b>, S. Nguyen, M. Zhang</span>
    <span class="pub-feature__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 28(1):147–167, 2024</span>
    <p>A comprehensive review of how GP and other machine learning techniques are used to design heuristics for job shop scheduling, with a discussion of open challenges.</p>
  </li>
</ul>

<h3 class="pub-group__title">Routing and Logistics</h3>
<p class="pub-group__intro">Memetic and swarm-based algorithms for arc routing and electric vehicle routing.</p>
<ul class="pub-features">
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1109/TCYB.2021.3069942">A Bilevel Ant Colony Optimization Algorithm for Capacitated Electric Vehicle Routing Problem</a></span>
    <span class="pub-feature__authors">Y.-H. Jia, <b>Y. Mei</b>, M. Zhang</span>
    <span class="pub-feature__venue"><i>IEEE Transactions on Cybernetics</i>, 52(10):10855–10868, 2022</span>
    <p>Tackles electric vehicle routing by separating the routing decisions from the charging decisions into two levels, solved with ant colony optimisation.</p>
  </li>
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1109/TEVC.2010.2051446">Decomposition-Based Memetic Algorithm for Multiobjective Capacitated Arc Routing Problem</a></span>
    <span class="pub-feature__authors"><b>Y. Mei</b>, K. Tang, X. Yao</span>
    <span class="pub-feature__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 15(2):151–165, 2011</span>
    <p>Extends memetic search to multi-objective arc routing through decomposition, finding good trade-offs between total cost and makespan.</p>
  </li>
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1109/TEVC.2009.2023449">Memetic Algorithm with Extended Neighborhood Search for Capacitated Arc Routing Problems</a></span>
    <span class="pub-feature__authors">K. Tang, <b>Y. Mei</b>, X. Yao</span>
    <span class="pub-feature__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 13(5):1151–1166, 2009</span>
    <p>Proposes MAENS, a memetic algorithm whose large-step <em>Merge-Split</em> operator explores far beyond traditional local moves. It became a widely used benchmark algorithm for arc routing.</p>
  </li>
</ul>

<h3 class="pub-group__title">Surveys on Evolutionary Machine Learning and Explainable AI</h3>
<p class="pub-group__intro">Overviews that map out emerging research areas.</p>
<ul class="pub-features">
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1080/03036758.2019.1609052">A Survey on Evolutionary Machine Learning</a></span>
    <span class="pub-feature__authors">H. Al-Sahaf, Y. Bi, Q. Chen, A. Lensen, <b>Y. Mei</b>, Y. Sun, B. Tran, B. Xue, M. Zhang</span>
    <span class="pub-feature__venue"><i>Journal of the Royal Society of New Zealand</i>, 49(2):205–228, 2019</span>
    <p>Reviews how evolutionary computation is used across machine learning, including classification, feature selection, clustering, neural architecture search and computer vision.</p>
  </li>
  <li class="pub-feature">
    <span class="pub-feature__title"><a href="https://doi.org/10.1109/TEVC.2022.3225509">Explainable Artificial Intelligence by Genetic Programming: A Survey</a></span>
    <span class="pub-feature__authors"><b>Y. Mei</b>, Q. Chen, A. Lensen, B. Xue, M. Zhang</span>
    <span class="pub-feature__venue"><i>IEEE Transactions on Evolutionary Computation</i>, 27(3):621–641, 2023</span>
    <p>Surveys how GP contributes to explainable AI, both by evolving models that are interpretable by design and by producing explanations for black-box models.</p>
  </li>
</ul>

<h2>Full Publication Lists</h2>

If you need the PDF of any of the papers, please feel free to <a href="mailto:yi.mei@ecs.vuw.ac.nz">contact</a> me.

<ul>
<li><a href="publication-book.html">Authored Books</a></li>
<li><a href="publication-journal.html">Refereed Journal Articles</a></li>
<li><a href="publication-conf.html">Conference Papers</a></li>
<li><a href="publication-chapter.html">Book Chapters</a></li>
</ul>
<hr>


