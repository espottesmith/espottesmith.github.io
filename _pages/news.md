---
layout: archive
permalink: /news/
title: "Blog"
author_profile: true
redirect_from:
  - /blog/
---

{% assign numposts = 0 %}
{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.posts %}
{% capture numposts %}{% increment numposts %}{% endcapture %}
{% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
{% if year != written_year %}
{% capture written_year %}{{ year }}{% endcapture %}
{% endif %}
{% include archive-single.html %}
{% endfor %}

{% if numposts == 0 %}
Nothing here yet! Check back to see if I've written any posts.
{% endif %}