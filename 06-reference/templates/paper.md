---
type: paper
status: unread
citekey: "{{citekey}}"
year: "{% if date %}{{date | format("YYYY")}}{% endif %}"
---

# {{title}}

**Authors:** {% for c in creators %}{{c.firstName}} {{c.lastName}}{% if not loop.last %}, {% endif %}{% endfor %}
**Venue:** {{publicationTitle or proceedingsTitle or itemType}}
**Year:** {% if date %}{{date | format("YYYY")}}{% endif %}
**Zotero:** [open]({{desktopURI}}){% if DOI %} · [DOI](https://doi.org/{{DOI}}){% endif %}{% if URL %} · [URL]({{URL}}){% endif %}

{% if abstractNote %}
## Abstract

{{abstractNote}}
{% endif %}

## TL;DR

## Problem

## Core idea

## Method

## Results

## Baselines / metrics

## Assumptions

## Limitations

## Math

## Follow-up questions

## Links

{% if annotations.length %}
## Zotero annotations

{% for a in annotations %}
{% if a.annotatedText %}> {{a.annotatedText}}{% endif %}
{% if a.imageRelativePath %}
![[{{a.imageRelativePath}}]]
{% endif %}
{% if a.comment %}
**Note:** {{a.comment}}
{% endif %}

---
{% endfor %}
{% endif %}
