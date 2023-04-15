---
layout: archive
title: "Resources"
permalink: /resources/
author_profile: true
---

## Code

- My GitHub <a href="https://github.com/meiyi1986/GPJSS">repository</a>: **genetic programming hyper-heuristics for evolving dispatching rules for job shop scheduling**.
- My GitHub <a href="https://github.com/meiyi1986/gpucarp">repository</a>: **meta-heuristic and hyper-heuristic algorithms for uncertain arc routing problem**.
- My GitHub <a href="https://github.com/meiyi1986/gporienteering">repository</a>: **genetic programming hyper-heuristic algorithms for stochastic orienteering problem**.
- <a href="https://www.mathworks.com/matlabcentral/fileexchange/45783-the-cc-gdg-cmaes-algorithm">MATLAB code</a> for <a href="https://dl.acm.org/doi/abs/10.1145/2791291?casa_token=_nRe8q8sA0MAAAAA:dW1amTncfliDrBJvstKeXB7wccHs1SrSLyaKi75T2QsNUy3_P82a5NkIOxD06M8tRjrGQoglcP15cA">A Competitive Divide-and-Conquer Algorithm for Unconstrained Large-Scale Black-Box Optimization</a>, *ACM Transactions on Mathematical Software*, 2016
- The ECJ Java library: <a href="https://cs.gmu.edu/~eclab/projects/ecj/">https://cs.gmu.edu/~eclab/projects/ecj/</a>. Highly recommeded if using GP.
- The gplearn Python library for GP: <a href="http://gplearn.readthedocs.io/en/stable/">http://gplearn.readthedocs.io/en/stable</a>.
- The DEAP Python library for GP: <a href="https://deap.readthedocs.io/en/master/">https://deap.readthedocs.io/en/master/</a>.
- MicroGP (Python): <a href="https://squillero.github.io/microgp4/">https://squillero.github.io/microgp4/</a>.
- Jenetics (Java): <a href="https://jenetics.io/">https://jenetics.io/</a>.
- Inspyred (Python): <a href="https://aarongarrett.github.io/inspyred/">https://aarongarrett.github.io/inspyred/</a>.
- Open BEAGLE (C++): <a href="http://chgagne.github.io/beagle/">http://chgagne.github.io/beagle/</a>.
- The HyFlex hyper-heuristic framework: <a href="http://www.asap.cs.nott.ac.uk/external/chesc2011/hyflex_description.html">http://www.asap.cs.nott.ac.uk/external/chesc2011/hyflex_description.html</a>
- The EvoHyp hyper-heuristic framwork: <a href="http://titancs.ukzn.ac.za/EvoHyp.aspx">http://titancs.ukzn.ac.za/EvoHyp.aspx</a>
- An automatic model fitting software: <a href="https://www.nutonian.com/products/eureqa/">Eureqa</a>. It has an academic 30-day trial version.

## Datasets

* <b>Job Shop Scheduling</b>
	* <a href="http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html">Taillard's benchmark datasets</a>
* <b>Flexible Job Shop Scheduling</b>
	* <a href="http://people.idsia.ch/~monaldo/fjsp.html">Flexible Job Shop Scheduling datasets</a>
* <b>Capacitated Arc Routing Problem</b>
	* The <a href="/files/data/carp/gdb.zip">gdb</a> dataset: <i>23 small instances (~30 nodes and ~60 required edges)</i>.
	* The <a href="/files/data/carp/val.zip">val</a> dataset: <i>10 groups of medium to large instances (~50 nodes and ~100 required edges). Each group contains 3 or 4 instances (denoted as A, B, C, D), which are based on the same graph but different vehicle capacity.</i>
	* The <a href="/files/data/carp/egl.zip">egl</a> dataset: <i>8 groups of large instances (~150 nodes and ~200 required edges). The former 4 groups (e1 to e4) and the latter 4 groups (s1 to s4) are based on the same graph, but different subsets of required edges. Each group contains 3 instances (denoted as A, B, C), based on the same graph and required edges, but with different vehicle capacity.</i>
	* The <a href="/files/data/carp/EGL-G.zip">EGL-G</a> dataset: <i>2 groups of large instances (~250 nodes and ~400 required edges). Each group contains 5 instances (denoted as A, B, C, D, E), based on the same graph and required edges, but with different vehicle capacity.</i>
	* The <a href="/files/data/carp/BeijingHefei.zip">Beijing&Hefei</a> dataset: <i>2 large datasets, one generated from the road network of Bejing, and the other from Hefei, two big cities in China. Each dataset has 10 instances, with thousands of edges.</i>
	* <a href="/files/data/carp/Instances.zip">Large scale datasets</a>, and the <a href="/files/data/carp/results.zip">best solutions</a> we found.
	* <a href="/files/data/mdcarp.zip">Multi-Depot CARP datasets</a>.
* <b>Vehicle Routing Problems</b>
	* Benchmark instances for different problem variants can be found from <a href="https://w1.cirrelt.ca/~vidalt/en/VRP-resources.html">Dr. T. Vidal's page</a>.
	* A very good <a href="http://vrp.atd-lab.inf.puc-rio.br/index.php/en">CVRP library</a>, with the <a href="http://vrp.atd-lab.inf.puc-rio.br/index.php/en/plotted-instances">plots of instances and solutions</a>.
* <b>Bin Packing Problem</b>
	* A very comprehensive <a href="http://or.dei.unibo.it/library/bpplib">problem library</a>.
* <b>Timetabling Problem</b>
	* A comprehensive <a href="http://www.cs.nott.ac.uk/~pszrq/data.htm">library</a> from University of Nottingham.
	* A <a href="https://www.unitime.org/exam_datasets.php">University Timetabling benchmark website</a>.

## Interesting links

- My [tutorials](https://github.com/meiyi1986/tutorials) in Jupyter Notebook.
- My <b>IEEE CIS Webinar</b>: Genetic Programming Hyper-Heuristics for Combinatorial Optimisation: <a href="https://ieeetv.ieee.org/ieeetv-specials/genetic-programming-hyper-heuristics-for-combinatorial-optimisation-yi-mei-cis-webinar">[Video]</a>
- Xin Yao's Public Lecture: <a href="https://www.youtube.com/watch?v=pcl08XA1REM"> What can evolutionary computation do for you?</a>
- A. E. Eiben's TED talk: <a href="https://www.youtube.com/watch?v=WJX_wAKhg8A">Tech Kangaroos - Evolution at Work</a>
- Keith Downing's TED Talk: <a href="https://www.youtube.com/watch?v=D3zUmfDd79s">Evolutionary computation</a>
- An interesting website about robots learned by evolutionary computation: <a href="https://strandbeest.com">https://strandbeest.com</a>
- Learn to Play Flappy Bird using Cartesian Genetic Programming: <a href="https://github.com/ShuhuaGao/gpFlappyBird">GitHub</a>
- Hyper-heuristic bibliography: <a href="https://mustafamisir.github.io/hh.html">https://mustafamisir.github.io/hh.html</a>
- An interesting **Science** paper "<a href="http://science.sciencemag.org/content/324/5923/81">Distilling Free-Form Natural Laws from Experimental Data</a>", which uses genetic programming to automatically discover natural laws (symbolic regression).
- A **Nature** paper: "<a href="https://www.nature.com/articles/nature14544">From evolutionary computation to the evolution of things</a>"