# {{ name|upper }}

{{ description }}

> **• DOMAINS:** [{{ domain_1 }}](../domains/{{ url_encode(domain_1) }}.md) & [{{ domain_2 }}](../domains/{{ url_encode(domain_2) }}.md)  
> **• STARTING EVASION:** {{ evasion }}  
> **• STARTING HIT POINTS:** {{ hp }}  
> **• CLASS ITEMS:** {{ items }}

## {{ name|upper }}’S HOPE FEATURE

***{{ hope_feat_name }}:*** {{ hope_feat_text }}

## CLASS FEATURE{% if class_feats|length > 1 %}S{% endif %}
{% for feat in class_feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
## {{ name|upper }} SUBCLASSES

Choose either the **[{{ subclass_1 }}](../subclasses/{{ url_encode(subclass_1) }}.md)** or **[{{ subclass_2 }}](../subclasses/{{ url_encode(subclass_2) }}.md)** subclass.

## BACKGROUND QUESTIONS

*Answer any of the following background questions. You can also create your own questions.*
{% for background in backgrounds %}
- {{ background.question }}{% endfor %}

## CONNECTIONS

*Ask your fellow players one of the following questions for their character to answer, or create your own questions.*
{% for connection in connections %}
- {{ connection.question }}{% endfor %}

{{ extras }}
