# {{ name|upper }}

***Tier {{ tier }} {{ type }}***  
*{{ description }}*  
**Impulses:** {{ impulses }}

> **Difficulty:** {{ difficulty }}  
> **Potential Adversaries:** {{ potential_adversaries }}

## FEATURES
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}