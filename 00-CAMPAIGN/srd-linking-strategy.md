---
title: "SRD Linking Strategy"
tags: 
  - organization
  - srd
  - metadata
  - reference
created: 2025-10-24
updated: 2025-10-24
category: "campaign-systems"
---

# SRD-to-Campaign Linking Strategy

## Overview
Establish metadata-based connections between campaign notes and SRD reference documents for seamless discovery and relationship management.

## Frontmatter Metadata Schema

### For Campaign Files (All Types)

Add to frontmatter:

```yaml
# Primary linking field - List SRD paths directly
srd-references:
  - "04-RESOURCES/daggerheart-srd/weapons/Wand.md"
  - "04-RESOURCES/daggerheart-srd/spells/Fireball.md"
  - "04-RESOURCES/daggerheart-srd/domains/Arcana.md"

# Category tags for discovery (helps with Base filtering)
srd-categories: 
  - weapons
  - spells
  - domains
  - subclasses
  - adversaries
  - environments

# Reference context (why/how this SRD content is relevant)
srd-context:
  - "weapon used by NPC"
  - "spell in party's arsenal"
  - "domain selection for character"

# Optional: specific SRD versions or notes
srd-notes: |
  Notes about how this content is used or customized
  in the campaign context
```

### For SRD Files (Optional Reciprocal)

Add to frontmatter:

```yaml
# Campaign usage tracking (optional - for popular/frequently-referenced content)
campaign-usage:
  - "01-CHARACTERS/banjo/character-sheet.md"  # Uses this weapon
  - "03-WORLD/npcs/reese-blackwood.md"        # Has access to this
  - "06-RULES-MASTERY/combat-tactics.md"      # Referenced in

# Alternative: Just rely on backlinks for discovery
# (Cleaner - SRD stays pure reference material)
```

## Implementation Patterns by Content Type

### 1. Character Sheets

**Link to:**
- Primary and secondary weapons (weapons/)
- Known spells (spells/)
- Selected domain (domains/)
- Subclass (subclasses/)
- Armor/equipment (gear/)

**Example:**
```yaml
---
tags: 
  - character/pc
  - player/gareth

srd-references:
  - "04-RESOURCES/daggerheart-srd/domains/Blade.md"
  - "04-RESOURCES/daggerheart-srd/subclasses/Troubadour.md"
  - "04-RESOURCES/daggerheart-srd/weapons/Lute.md"
  - "04-RESOURCES/daggerheart-srd/armor/Studded Leather.md"
  - "04-RESOURCES/daggerheart-srd/spells/Inspiring Words.md"

srd-categories: [domains, subclasses, weapons, armor, spells]
srd-context:
  - "primary domain selection"
  - "player subclass"
  - "favored instrument"
  - "equipped armor"
  - "signature spell"
---
```

### 2. NPC Files

**Link to:**
- Equipment they possess or offer
- Spells/abilities they demonstrate
- Adversary stat blocks (if applicable)
- Factions they belong to (if SRD-based)
- Equipment they might trade/sell

**Example:**
```yaml
---
tags:
  - npc/major
  - relationship/ally

srd-references:
  - "04-RESOURCES/daggerheart-srd/weapons/Crossbow.md"
  - "04-RESOURCES/daggerheart-srd/armor/Reinforced Leather.md"
  - "04-RESOURCES/daggerheart-srd/spells/Healing Light.md"

srd-categories: [weapons, armor, spells]
srd-context:
  - "carries as huntmaster"
  - "standard protective gear"
  - "healing ability demonstrated"
---
```

### 3. Session Notes

**Link to:**
- Adversaries encountered (adversaries/)
- Environmental challenges (environments/)
- Items found/used (gear/, weapons/)
- Spells cast in combat (spells/)
- Domains/subclasses used (for mechanical reference)

**Example:**
```yaml
---
tags: session/daggerheart, date/2025-10-24
session-number: 9

srd-references:
  - "04-RESOURCES/daggerheart-srd/adversaries/Craven.md"
  - "04-RESOURCES/daggerheart-srd/environments/Mountain Pass.md"
  - "04-RESOURCES/daggerheart-srd/adversaries/Giant Eagle.md"
  - "04-RESOURCES/daggerheart-srd/spells/Inspiring Words.md"

srd-categories: [adversaries, environments, spells]
srd-context:
  - "final boss encounter"
  - "avalanche escape scene"
  - "combat encounter"
  - "cast by Banjo in support"
---
```

### 4. Story Threads

**Link to:**
- Relevant rule mechanics (contents/)
- Thematic domains (domains/)
- Enemy types that might appear (adversaries/)
- Environmental challenges (environments/)

**Example:**
```yaml
---
tags: story/active

srd-references:
  - "04-RESOURCES/daggerheart-srd/domains/Midnight.md"
  - "04-RESOURCES/daggerheart-srd/contents/The Spotlight.md"
  - "04-RESOURCES/daggerheart-srd/adversaries/Void Creature.md"

srd-categories: [domains, mechanics, adversaries]
srd-context:
  - "thematic connection to corruption arc"
  - "spotlight mechanics for party tension"
  - "potential antagonists for this thread"
---
```

### 5. World/Location Files

**Link to:**
- Environments that match (environments/)
- Creatures/adversaries that inhabit (adversaries/)
- Equipment commonly found (gear/, weapons/)

### 6. Rules Mastery/Builds

**Link to:**
- Domains compared (domains/)
- Subclasses analyzed (subclasses/)
- Spell combinations (spells/)
- Weapon mechanics (weapons/)
- Environmental interactions (environments/)

## Discovery Workflows

### Finding Campaign Context for SRD Content

**From SRD file:**
1. View file → Check backlinks (right panel or via graph)
2. Graph view will show all campaign files referencing this SRD content
3. See exactly where/how SRD content is used in campaign

### Finding SRD References from Campaign Content

**From campaign file:**
1. Check `srd-references` field in frontmatter
2. Click through to relevant SRD files
3. Use `srd-categories` to filter/organize references

### Creating Base Views for SRD Connections

Create filtering views:

**"Characters with SRD Gear"**
- Filter: `contains(srd-categories, "weapons") OR contains(srd-categories, "armor")`
- Group by: player/character
- Shows character gear inventory linked to SRD

**"Session Adversaries"**
- Filter: `tags CONTAINS "session/daggerheart" AND contains(srd-categories, "adversaries")`
- Sort by: date (desc)
- Shows all enemies faced with direct SRD links

**"Spell Inventory"**
- Filter: `contains(srd-categories, "spells")`
- Group by: character/source
- Complete spell usage across campaign

## Implementation Priority

### Phase 1: High-Impact Links (Complete First)
- [ ] Character sheets → weapons, domains, subclasses, armor
- [ ] Session notes → adversaries, environments, spells cast
- [ ] Major NPCs → equipment, capabilities

### Phase 2: Medium-Priority Links
- [ ] Story threads → thematic domains, related mechanics
- [ ] World locations → environments, inhabitant creatures
- [ ] Gear inventory → specific weapons/armor in use

### Phase 3: Deep Integration
- [ ] Rules mastery → comparative builds and optimizations
- [ ] Combat tactics → specific spell/ability combinations
- [ ] Lore connections → thematic elements across SRD

## Metadata Standards

### Field Values Format
- **srd-references**: Array of exact file paths (use copy from file explorer)
- **srd-categories**: Array of category names (lowercase): weapons, spells, domains, subclasses, armor, gear, adversaries, environments, spells, abilities, contents, subclasses, classes, ancestries
- **srd-context**: Array of brief descriptive strings (1-3 words max)

### Example Complete Entry

```yaml
---
title: "Captain Howling Banjo"
tags:
  - character/pc
  - player/gareth
  - class/rogue

# SRD Linking
srd-references:
  - "04-RESOURCES/daggerheart-srd/domains/Blade.md"
  - "04-RESOURCES/daggerheart-srd/domains/Grace.md"
  - "04-RESOURCES/daggerheart-srd/subclasses/Troubadour.md"
  - "04-RESOURCES/daggerheart-srd/weapons/Lute.md"
  - "04-RESOURCES/daggerheart-srd/armor/Studded Leather.md"
  - "04-RESOURCES/daggerheart-srd/spells/Inspiring Words.md"
  - "04-RESOURCES/daggerheart-srd/spells/Charm.md"

srd-categories: [domains, subclasses, weapons, armor, spells]

srd-context:
  - "primary domain selection"
  - "secondary domain"
  - "player subclass choice"
  - "favored instrument/weapon"
  - "equipped protective gear"
  - "signature support spell"
  - "secondary spell"

srd-notes: |
  Banjo's build emphasizes charm and support magic through
  Troubadour subclass, with Blade/Grace domains providing
  versatile combat options. Relies on lute for instrument
  performance and combat presence.

created: 2025-07-20
updated: 2025-10-24
---
```

## Search Patterns

### Using Vault Search

**Find all campaign items using specific SRD content:**
```
content:"04-RESOURCES/daggerheart-srd/spells/Fireball.md"
```

**Find all references to specific SRD category:**
```
srd-categories:spells
srd-categories:weapons
```

**Find all campaign files with SRD references:**
```
srd-references:*
```

## Graph Visualization Benefits

With proper frontmatter linking:
- **Campaign → SRD edges** show which content is "mechanically active" in campaign
- **SRD ← Campaign backlinks** show usage frequency and context
- **Hub detection** reveals most-used SRD content (powerful items/spells)
- **Category clustering** shows thematic connections

## Integration with Bases

Create a Base for "SRD Reference Mapping":

```yaml
name: "SRD Reference Mapping"
source: 
  - path: "03-WORLD"
  - path: "02-SESSIONS"
  - path: "01-CHARACTERS"
  - path: "06-RULES-MASTERY"

properties:
  - name: "content-type"
    type: "select"
    options: [character, npc, session, location, story-thread, build-guide]
  
  - name: "srd-references"
    type: "text"
  
  - name: "srd-categories"
    type: "multi-select"
    options: [weapons, spells, domains, subclasses, armor, adversaries, environments]
  
  - name: "reference-count"
    type: "number"
    formula: "length(srd-references)"

views:
  - name: "References by Category"
    group: "srd-categories"
    
  - name: "Most Linked SRD Content"
    group: "srd-references"
    sort: "reference-count"

  - name: "Content Type Analysis"
    group: "content-type"
```

## Maintenance Notes

- **Update frequency**: Review SRD links when campaign content changes
- **Consistency**: Use exact file paths (copy-paste from file explorer)
- **Cleanup**: Archive old session links when archiving sessions
- **Validation**: Periodically check for broken references via graph backlinks

---

*Strategy Created: 2025-10-24*
*Purpose: Enable seamless discovery between campaign and SRD content*
*Implementation: Start with Phase 1 (characters and sessions)*
