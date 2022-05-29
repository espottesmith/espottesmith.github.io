---
layout: archive
title: "Software"
permalink: /software/
author_profile: true
---

As part of my research, I develop scientific software, mostly aiming to solve
problems related to computational chemistry, high-throughput simulations, and
chemical reaction networks. Below are listed the main projects that I develop
or contribute to.

<table class="softwaretab" style="border:0;">
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead></thead>
<tbody>
{% for item in site.data.software %}
{% assign codename = item[0] %}
{% assign packdata = item[1] %}
<tr>
<td>
<div class="software__image">
<img src="{{ packdata.image | prepend: base_path }}" class="software__image" alt="{{ packdata.name }}">
</div>
</td>
<td>
<h1><a href="{{ packdata.url }}"> {{ packdata.name | markdownify }} </a></h1>
<h2>{{ packdata.role | prepend: "Role: " | markdownify }}</h2>
{{ packdata.description | markdownify }}
</td>
</tr>
{% endfor %}
</tbody>
</table>