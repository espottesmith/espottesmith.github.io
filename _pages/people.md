---
layout: default
title: "People"
permalink: /people/
---

{% include base_path %}

{% for role in site.roles %}

### {{ role.name }}

{% for item in site.data.people %}
{% assign username = item[0] %}
{% assign person = item[1] %}
{% if person.role == role.key %}
![{{ person.display_name }}]({{ person.image }})
##### {{ person.display_name }}
{% if person.project %}
Project: {{ person.project | markdownify }}
{% endif %}
{% if person.current_position %}
Current Position: {{ person.current_position | markdownify }}
{% endif %}
{% endif %}
{% endfor %}

{% endfor %}