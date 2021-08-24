---
layout: default
title: "Research"
permalink: /research/
author_profile: false
---

<table class="researchtab" style="border:0;">
<colgroup>
<col width="60%" />
<col width="40%" />
</colgroup>
<thead></thead>
<tbody>

<tr>
<td>
<h2>Automating theoretical studies of (electro)chemical reactivity</h2>
High-throughput density functional theory (DFT) studies of molecules have traditionally been limited to relatively stable species - neutral, closed-shell
species, often in gas phase. However, reactions in electrochemical systems often involve radical, charged, and metal-coordinated species
in a solvent environment. To facilitate studies of such complex and reactive systems, I have been developing
methods to automate calculations of reactive ground-state molecules as well as reaction energy barriers (based on
transition-state theory and Marcus theory), allowing for the accurate prediction of reaction thermodynamics and kinetics
from first-principles.<br>
Using the workflows that I have devised and implemented, it is possible to generate <a href="/files/papers/spottesmith_quantum_2021.pdf">large datasets</a>
containing the properties of reactive molecules. Such datasets have already been used by myself and my colleagues to construct <a href="/files/papers/blau_chemically_2021.pdf">massive chemical reaction networks</a>
and to train <a href="/files/papers/wen_bondnet_2021.pdf">neural networks</a>, for instance for the prediction of bond dissociation energies.<br>
I am working to develop a similar dataset of reaction pathways, with the eventual goal of machine learning energy barriers for arbitrary
(electro)chemical reactions with DFT-level accuracy.
</td>
<td>
<div class="project__image">
<img src="/images/high_throughput_reactivity.png" class="project__image" alt="Large datasets of molecular properties calculated using high-throughput density functional theory">
</div>
</td>
</tr>

<tr>
<td>
<h2>Revealing the mechanistic origins of SEI formation</h2>
The solid electrolyte interphase (SEI) is critically important for metal-ion battery function - preventing electrolyte degradation and allowing
reversible cycling - but it is also notoriously difficult to study. I aim to take a new approach to understand how the SEI forms.
Using reaction networks, one can automatically identify thermodynamically and kinetically favorable reaction pathways to SEI products of interest.
My colleagues and I have, for instance, recently taken this approach to understand the formation of the newly proposed organic SEI component <a href="/files/papers/xie_data_driven_2021.pdf">lithium
ethylene monocarbonate</a> (LEMC). With sufficiently comprehensive collection of reaction mechanisms, I then construct microkinetic
models of SEI formation. Such models allow me to observe competition between SEI products and formation pathways and can provide mechanistic
explanations for structural and compositional trends observed in experiment.<br>
To date, most of my research on SEI formation has focused on lithium-ion batteries, but I am currently working to expand my research and explore SEI formation
mechanisms in magnesium-ion batteries.
</td>
<td>
<div class="project__image">
<img src="/images/sei_formation.png" class="project__image" alt="Stochastic studies based on first-principles energy barriers provide mechanistic insight into solid electrolyte interphase formation">
</div>
</td>
</tr>

<!-- TODO: Add a section on product prediction - maybe EcheML logo? -->
<!--
<tr>
<td>
<h2>Predicting electrochemical reaction outcomes</h2>

</td>
<td>
<div class="project__image">
<img src="/images/product_prediction.png" class="project__image" alt="Predicting the products of electrochemical reactions">
</div>
</td>
</tr>
-->
</tbody>
</table>