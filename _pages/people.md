---
layout: archive
title: "People"
permalink: /people/
author_profile: true
---

{% for role in site.roles %}

# {{ role.name }}
<table class="peopletab" style="border:0;">
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<thead></thead>
<tbody>
{% for item in site.data.people %}
{% assign username = item[0] %}
{% assign person = item[1] %}
{% if person.role == role.key %}
<tr>
<td>
<div class="author__avatar">
<img src="{{ person.image | prepend: base_path }}" class="author__avatar" alt="{{ person.display_name }}">
</div>
</td>
<td>
<strong>{{ person.display_name }}</strong>
{% if person.project %}
{{ person.project | prepend: "Project: " | markdownify }}
{% endif %}
{% if person.current_position %}
{{ person.current_position | prepend: "Current Position: "| markdownify }}
{% endif %}
</td>
</tr>
{% endif %}
{% endfor %}
</tbody>
</table>
{% endfor %}