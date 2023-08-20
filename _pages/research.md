---
layout: default
title: "Research"
permalink: /research/
author_profile: false
---

<table class="researchtab" style="border:0;">
<colgroup>
<col width="70%" />
<col width="30%" />
</colgroup>
<thead></thead>
<tbody>

<tr>
<td>
<h2>Datasets and data science for complex molecular reactivity</h2>
High-throughput density functional theory (DFT) studies of molecules have traditionally been limited to relatively stable species - neutral, closed-shell, and often in the gas phase. However, reaction cascades in domains like electrochemistry often involve radical, charged, and metal-coordinated species
in a solvent environment. To facilitate studies of such complex and reactive systems, I have developed methods to automate calculations of reactive ground-state molecules as well as reaction energy barriers (based on transition-state theory and Marcus theory), allowing for the accurate prediction of reaction thermodynamics and kinetics from first-principles.<br>

Using the workflows that I have devised and implemented, I have generated <a href="/files/papers/spottesmith_quantum_2021.pdf">large</a> <a href="/files/papers/spottesmith_chemical_reaction_2023.pdf">open</a> <a href="/files/papers/spottesmith_database_molecular_2023.pdf">datasets</a> containing the properties of reactive molecules. Much of the data that I have generated is accessible on the <a href="https://materialsproject.org/molecules">Materials Project</a>, making it accessible to computational experts and novices alike!<br>

In addition to providing data as a community resource, I and my colleagues use computational datasets to study reactivity (see below). The data that I generate is also used <a href="/files/papers/wen_bondnet_2021.pdf">within my research group</a> and <a href="https://doi.org/10.1063/5.0083301">elsewhere</a> to train machine learning models.<br>

The eventual goal of this work is to be able to quickly and accurately predict the properties of arbitrary molecules and reactions throughout chemistry and electrochemistry with DFT-level accuracy (or better).
</td>
<td>
<div class="project__image">
<img src="/images/mpcules_flowchart.png" class="project__image" alt="A flowchart showing how tasks (DFT calculations) are transformed to molecules and molecular properties in the Materials Project.">
</div>
</td>
</tr>

<tr>
<td>
<h2>A new approach to exploring reactivity</h2>
Understanding and controlling reactivity is key to a range of technological applications, from manufacturing to transportation and electronics.
Typical theoretical studies of reactions involve low-throughput molecular simulations, using some combination of DFT and reactive or <i>ab initio</i> molecular dynamics.
Recently, there has been growing interest in <a href="/files/papers/wen_chemical_reaction_2023.pdf">chemical reaction networks (CRNs)</a>, which abstract away the complexity of the quantum chemical potential energy surface, allowing for efficient exploration of even very complex reactive spaces.<br>

However, CRNs have not been applied to study electrochemistry until very recently. In part, this is because electrochemical reaction mechanisms are not well understood, making methods based on chemical intuition or reaction templates intractable. 
My colleagues and I develop new methods for constructing and analyzing (electro)chemical CRNs, with the goal of automatically revealing the inner workings of complex chemical processes without prior domain knowledge and without relying heavily on chemical intuition.
Most recently, we have developed tools to generate CRNs based on filters and <a href="/files/papers/barter_predictive_stochastic_2023.pdf">stochastic methods</a> to not only identify pathways to known species of interest but also automatically identify the natural products of CRNs using simple heuristics. With this method, it is now possible to easily and rapidly generate hypotheses for experimental characterization and in-depth mechanistic studies of complex reactive processes (such as those in Li-ion batteries)
using only computed reaction thermodynamics.<br>
As part of ongoing collaborations with the Blau Group at LBNL, I continue to build on the successes of these methods and devise new ways to efficiently explore reactive spaces.
</td>
<td>
<div class="project__image">
<img src="/images/rnmc.png" class="project__image" alt="Stochastic sampling of reaction networks allows for identification of pathways and prediction of products in complex systems where little is initially known.">
</div>
</td>
</tr>

<tr>
<td>
<h2>Revealing the mechanistic origins of electrolyte degradation</h2>
Electrolyte reactivity is one of the major drivers of inefficiency and capacity loss in metal-ion batteries. When uncontrolled, electrolytes can electrochemically react to form gases (which can cause swelling and explosions) or lower the cell lithium inventory. On the other hand, high-performance electrolytes selectively react to form passivation films, called interphases. It is therefore essential to understand how current electrolytes react and predict how electrolyte additves and next-generation components might affect reactivity.<br>

Using DFT, I construct elementary reaction mechanisms to understand possible degradation pathways. For instance, a community college intern and I examined the behavior of <a href="/files/papers/spottesmith_petrocelli_elementary_decomposition_2023.pdf">lithium hexafluorophosphate (LiPF6)</a>, the most common salt used in Li-ion batteries today. We found that the oft-cited hydrolysis mechanism is thermodynamically and kinetically unfavorable at room temperature, while LiPF6 can rapidly react with Lewis bases like lithium carbonate (Li2CO3)!<br>

CRNs can help to understand electrolyte degradation, exploring more broadly and more thoroughly. I recently demonstrated the power of CRNs and DFT to <a href="/files/papers/spottesmith_chemical_reaction_2023.pdf">explain electrolyte degradation in Mg-ion batteries</a>. With no prior knowledge of gaseous or organic decomposition products, I was able to predict what gases would evolve during Mg plating (in agreement with experimental spectra) and indicate how the observed gases out-competed other possible products.
</td>
<td>
<div class="project__image">
<img src="/images/mg_gases.png" class="project__image" alt="Chemical reaction networks help interpret experimental spectra, explaining gas evolution in Mg-ion batteries">
</div>
</td>
</tr>

<tr>
<td>
<h2>Multiscale modeling of energy technologies</h2>
Interphases, which form as a result of electrolyte decomposition in metal-ion batteries, are critically important for allowing reversible cycling and preserving battery capacity. However, they are also notoriously difficult to study. In part, this is because of the disparate time scales involved in interphase formation. Individual reactions occur in picoseconds, while the interphase continues to grow and evolve for hundreds or even thousands of hours.<br>

Multiscale modeling provides an opportunity to access long time scales while retaining the accuracy of atomistic methods. I and my colleagues use a variety of multiscale techniques to analyze battery interphases. Combining reaction mechanisms from CRN analysis in a <a href="/files/papers/spottesmith_kam_towards_mechanistic_2022.pdf">microkinetic simulation</a>, I was able to trace the mechanistic origins of the bilayer interphase structure on the negative electrode of Li-ion batteries and moreover identify how different interphase components might electrochemically degrade over time. In a collaboration with researchers at the National Renewable Energy Laboratory, I helped to develop a <a href="/files/papers/weddle_continuum_level_2023.pdf">continuum-scale model</a> of interphase growth that includes dozens of elementary mechanisms from DFT. This model, the most complex of its kind ever produced, can easily simulate thousands of hours of electrochemical cycling or voltage holds, revealing interphase growth dynamics and gas evolution behavior while also connecting directly to device-level experimental observables like parasitic current.<br>

I am excited to continue pushing the envelope on multiscale modeling in energy storage, leveraging atomistic simulations in device-level models considering both electrodes and accurate (thermal, mass, and charge) transport.
</td>
<td>
<div class="project__image">
<img src="/images/sei_formation.png" class="project__image" alt="Microkinetic studies based on first-principles energy barriers provide mechanistic insight into solid electrolyte interphase formation">
</div>
</td>
</tr>

</tbody>
</table>