---
title: "SRD Linking - Quick Reference"
tags: 
  - reference
  - cheat-sheet
  - srd-linking
created: 2025-10-24
---

# SRD Linking Quick Reference Card

## Copy-Paste Frontmatter Snippet

```yaml
# Add these fields to your file's frontmatter:

srd-references:
  - "04-RESOURCES/daggerheart-srd/category/Item Name.md"
  - "04-RESOURCES/daggerheart-srd/category/Other Item.md"

srd-categories: [category1, category2]

srd-context:
  - "brief description of relevance"
  - "why this item matters"

srd-notes: |
  Optional longer explanation of how this content
  is used or customized in your campaign.
```

## SRD Category Reference

```
04-RESOURCES/daggerheart-srd/
├── weapons/           → Weapon name.md
├── armor/             → Armor name.md
├── gear/              → Item name.md
├── spells/            → Spell name.md
├── domains/           → Domain name.md
├── subclasses/        → Subclass name.md
├── classes/           → Class name.md
├── ancestries/        → Ancestry name.md
├── adversaries/       → Creature name.md
├── environments/      → Environment name.md
├── contents/          → Mechanic name.md
└── abilities/         → Ability name.md
```

## Content Type Checklist

### Character Sheets
- [ ] Primary domain
- [ ] Secondary domain
- [ ] Subclass
- [ ] Primary weapon
- [ ] Secondary weapon
- [ ] Armor
- [ ] Key spells

### Session Notes  
- [ ] Adversaries encountered
- [ ] Environment/location
- [ ] Spells cast
- [ ] Items found
- [ ] Environmental hazards

### NPCs
- [ ] Primary weapon
- [ ] Armor/protection
- [ ] Key abilities
- [ ] Equipment offered
- [ ] Special gear

### Story Threads
- [ ] Related domains
- [ ] Potential enemies
- [ ] Thematic elements
- [ ] Relevant mechanics

### World Locations
- [ ] Environment type
- [ ] Creatures present
- [ ] Hazards
- [ ] Available gear

### Builds/Tactics
- [ ] Domains compared
- [ ] Subclasses analyzed
- [ ] Spell combinations
- [ ] Weapon synergies

## Quick Copy Paths (Most Common)

```
Weapons:
04-RESOURCES/daggerheart-srd/weapons/Crossbow.md
04-RESOURCES/daggerheart-srd/weapons/Lute.md
04-RESOURCES/daggerheart-srd/weapons/Longsword.md

Armor:
04-RESOURCES/daggerheart-srd/armor/Leather Armor.md
04-RESOURCES/daggerheart-srd/armor/Plate Armor.md
04-RESOURCES/daggerheart-srd/armor/Studded Leather.md

Domains:
04-RESOURCES/daggerheart-srd/domains/Blade.md
04-RESOURCES/daggerheart-srd/domains/Grace.md
04-RESOURCES/daggerheart-srd/domains/Arcana.md
04-RESOURCES/daggerheart-srd/domains/Midnight.md

Spells:
04-RESOURCES/daggerheart-srd/spells/Fireball.md
04-RESOURCES/daggerheart-srd/spells/Healing Light.md
04-RESOURCES/daggerheart-srd/spells/Charm.md
```

## Validation Checklist

Before saving your update:
- [ ] Paths are exact (case-sensitive)
- [ ] All `srd-references` point to existing files
- [ ] `srd-categories` array length makes sense
- [ ] `srd-context` describes each reference
- [ ] No typos in frontmatter YAML
- [ ] Indentation is consistent (2 spaces)

## Workflow: Adding Links in 5 Minutes

1. **Open file** → Note what SRD content it uses
2. **Search vault** → Find exact file paths
3. **Copy paths** → Into srd-references array
4. **Add categories** → weapons, armor, spells, etc.
5. **Describe context** → Brief 1-2 word explanation
6. **Save** → Done!

## Search Patterns for Finding Files

```
# Find a specific item
"Crossbow" OR "Fireball" OR "Blade"

# Find all items in a category
path:04-RESOURCES/daggerheart-srd/weapons/

# Find by partial name
path:weapons "Improved"

# Find related items
"Leather" AND (armor OR gear)
```

## Benefits Unlocked

✅ **One-click** access to SRD mechanics  
✅ **Visual graph** showing campaign relationships  
✅ **Quick lookup** during session prep  
✅ **Equipment tracking** across party  
✅ **Build comparison** analysis  
✅ **Spell inventory** management  

## Common Categories for srd-categories

```yaml
# Pick from these (lowercase):
srd-categories: 
  - weapons
  - armor
  - gear
  - spells
  - domains
  - subclasses
  - classes
  - ancestries
  - adversaries
  - environments
  - mechanics
  - abilities
```

## Typical srd-context Examples

```
# For weapons
srd-context:
  - "primary melee weapon"
  - "ranged option"
  - "backup weapon"

# For armor
srd-context:
  - "main protection"
  - "ceremonial outfit"

# For spells
srd-context:
  - "damage spell"
  - "healing option"
  - "support ability"

# For domains
srd-context:
  - "primary domain choice"
  - "thematic element"
  - "mechanical synergy"
```

## Priority Implementation Order

### Week 1 (Quick Wins)
- [ ] All 4 PC character sheets
- [ ] Last 3 session notes
- [ ] 3 major NPCs

### Week 2 (Deepen)
- [ ] Remaining recent sessions
- [ ] World locations (3-5)
- [ ] Story threads (2-3)

### Week 3+ (Comprehensive)
- [ ] All older sessions (archive older ones)
- [ ] Build guides
- [ ] Full world documentation
- [ ] Rules mastery notes

## Frontmatter Template (Copy-Ready)

```yaml
---
title: "[Your Content]"
tags: [relevant, tags, here]
created: 2025-10-24

# NEW SRD LINKING SECTION
srd-references:
  - "04-RESOURCES/daggerheart-srd/category/Item1.md"
  - "04-RESOURCES/daggerheart-srd/category/Item2.md"

srd-categories: [category1, category2]

srd-context:
  - "context 1"
  - "context 2"

srd-notes: |
  Optional notes about how this content
  integrates with your campaign.
---
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Links not showing in graph | Check frontmatter syntax, reload vault |
| File not found error | Verify exact path, search vault |
| Too many references | Limit to 5-8 most important items |
| YAML indentation error | Use 2 spaces, not tabs |
| Can't find srd file | Search: `"Item Name" path:04-RESOURCES` |

## Reference Documents

- **Full Strategy**: [[srd-linking-strategy]]
- **Implementation Guide**: [[srd-linking-implementation-guide]]
- **Live Example**: [[SRD-Linking-Example]]

## TL;DR

1. Add `srd-references` array to frontmatter
2. List paths to relevant SRD files
3. Add `srd-categories` for filtering
4. Add `srd-context` to explain why
5. Save and check graph view
6. Done!

---

*Quick Reference v1.0*  
*Created: 2025-10-24*  
*Use this as bookmark → copy snippets into your files*
