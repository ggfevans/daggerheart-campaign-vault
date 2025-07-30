# {{ name|upper }}

***Tier {{ tier }} {{ type }}***  
*{{ description }}*  
**Motives & Tactics:** {{ motives_and_tactics }}

> **Difficulty:** {{ difficulty }} | **Thresholds:** {{ thresholds }} | **HP:** {{ hp }} | **Stress:** {{ stress }}  
> **ATK:** {{ atk }} | **{{ attack }}:** {{ range }} | {{ damage }}  {% if experience %}
> **Experience:** {{ experience }}{% endif %}

## FEATURES
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}