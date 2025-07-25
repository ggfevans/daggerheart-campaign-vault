# {{ name|upper }}

{{ description }}
{% if spellcast_trait %}
## SPELLCAST TRAIT

{{ spellcast_trait }}
{% endif %}
## FOUNDATION FEATURE{% if foundations|length > 1 %}S{% endif %}
{% for feat in foundations %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
## SPECIALIZATION FEATURE{% if specializations|length > 1 %}S{% endif %}
{% for feat in specializations %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
## MASTERY FEATURE{% if masteries|length > 1 %}S{% endif %}
{% for feat in masteries %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
{{ extras }}
