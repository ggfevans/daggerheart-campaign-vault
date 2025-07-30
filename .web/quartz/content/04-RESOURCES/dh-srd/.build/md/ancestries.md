# {{ name|upper }}

{{ description }}

## ANCESTRY FEATURES
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
