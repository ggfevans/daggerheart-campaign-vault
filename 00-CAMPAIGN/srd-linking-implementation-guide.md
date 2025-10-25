---
title: "SRD Linking Implementation Guide"
tags:
  - tutorial
  - workflow
  - srd-linking
  - frontmatter
created: 2025-10-24
---

# SRD Linking Implementation Guide

Quick reference for adding SRD metadata links to your campaign content.

## Quick Start (3 Steps)

### Step 1: Copy the Template
Use the appropriate template for your content type from the section below.

### Step 2: Find SRD File Paths
Use Vault Search to find relevant SRD content:
- Search for weapon/spell/domain name
- Copy exact file path when you find it
- Paste into `srd-references` array

### Step 3: Add to Your File's Frontmatter
Insert the new fields into your existing frontmatter and save.

## Templates by Content Type

### Character Sheet Template

```yaml
---
# Existing fields (keep these)
title: "Character Name"
tags: [character/pc, player/name, class/rogue]
created: YYYY-MM-DD

# ADD THESE FIELDS:
# Direct references to SRD files this character uses
srd-references:
  - "04-RESOURCES/daggerheart-srd/domains/DomainName.md"
  - "04-RESOURCES/daggerheart-srd/subclasses/SubclassName.md"
  - "04-RESOURCES/daggerheart-srd/weapons/WeaponName.md"
  - "04-RESOURCES/daggerheart-srd/armor/ArmorName.md"

# Categories for filtering and organization
srd-categories: [domains, subclasses, weapons, armor, spells]

# Brief context for each reference (optional but helpful)
srd-context:
  - "primary domain"
  - "player subclass choice"
  - "primary weapon"
  - "equipped armor"
  - "signature spell"

# Longer notes about how SRD content fits into character (optional)
srd-notes: |
  Brief explanation of how this content is used in
  your character's build and strategy.
---
```

### Session Notes Template

```yaml
---
# Existing fields
tags: session/daggerheart, date/YYYY-MM-DD
session-number: X
date: YYYY-MM-DD
participants: [Player1, Player2]

# ADD THESE FIELDS:
srd-references:
  - "04-RESOURCES/daggerheart-srd/adversaries/BossName.md"
  - "04-RESOURCES/daggerheart-srd/environments/LocationName.md"
  - "04-RESOURCES/daggerheart-srd/spells/SpellUsed.md"

srd-categories: [adversaries, environments, spells]

srd-context:
  - "major boss encounter"
  - "combat environment"
  - "spell cast in battle"
---
```

### NPC Template

```yaml
---
# Existing fields
tags: [npc/major, relationship/ally, location/town]
created: YYYY-MM-DD

# ADD THESE FIELDS:
srd-references:
  - "04-RESOURCES/daggerheart-srd/weapons/WeaponName.md"
  - "04-RESOURCES/daggerheart-srd/armor/ArmorName.md"
  - "04-RESOURCES/daggerheart-srd/spells/SpellName.md"

srd-categories: [weapons, armor, spells]

srd-context:
  - "carries as main weapon"
  - "protective equipment"
  - "demonstrated ability"
---
```

### Story Thread Template

```yaml
---
# Existing fields
tags: story/active, plot-thread

# ADD THESE FIELDS:
srd-references:
  - "04-RESOURCES/daggerheart-srd/domains/DomainName.md"
  - "04-RESOURCES/daggerheart-srd/adversaries/EnemyType.md"
  - "04-RESOURCES/daggerheart-srd/environments/LocationName.md"

srd-categories: [domains, adversaries, environments]

srd-context:
  - "thematic connection"
  - "potential antagonists"
  - "story setting"
---
```

### Build/Rules Mastery Template

```yaml
---
# Existing fields
title: "Build Analysis: Troubadour"
tags: [build-guide, optimization, reference]

# ADD THESE FIELDS:
srd-references:
  - "04-RESOURCES/daggerheart-srd/domains/Blade.md"
  - "04-RESOURCES/daggerheart-srd/domains/Grace.md"
  - "04-RESOURCES/daggerheart-srd/subclasses/Troubadour.md"
  - "04-RESOURCES/daggerheart-srd/spells/InspiringsWords.md"
  - "04-RESOURCES/daggerheart-srd/weapons/Lute.md"

srd-categories: [domains, subclasses, spells, weapons]

srd-context:
  - "primary domain choice"
  - "secondary domain"
  - "subclass analyzed"
  - "key spell synergy"
  - "instrument weapon"
---
```

## How to Find SRD File Paths

### Method 1: Search in Vault
1. Open Vault Search (Cmd+Shift+F or Ctrl+Shift+F)
2. Search for the item name: `"Wand" OR "Fireball"`
3. Look for result in `04-RESOURCES/daggerheart-srd/`
4. Click the file
5. Copy the path from the file header or status bar

### Method 2: Browse Structure
1. Open vault file explorer
2. Navigate to `04-RESOURCES/daggerheart-srd/`
3. Browse categories: `weapons/`, `spells/`, `domains/`, etc.
4. Find the file
5. Use file's full path

### Method 3: Quick Reference Categories

**Common SRD paths:**
```
04-RESOURCES/daggerheart-srd/
├── weapons/
│   └── [WeaponName].md
├── spells/
│   └── [SpellName].md
├── domains/
│   └── [DomainName].md
├── subclasses/
│   └── [SubclassName].md
├── adversaries/
│   └── [CreatureName].md
├── armor/
│   └── [ArmorName].md
├── gear/
│   └── [ItemName].md
├── environments/
│   └── [LocationName].md
├── classes/
│   └── [ClassName].md
└── contents/
    └── [MechanicName].md
```

## Practical Examples

### Example 1: Character Update

**BEFORE:**
```yaml
---
title: "Captain Howling Banjo"
tags: [character/pc, player/gareth, class/rogue]
created: 2025-07-20
---

# Captain Howling Banjo
Entertainer bard...
```

**AFTER:**
```yaml
---
title: "Captain Howling Banjo"
tags: [character/pc, player/gareth, class/rogue]
created: 2025-07-20

# NEW FIELDS ADDED:
srd-references:
  - "04-RESOURCES/daggerheart-srd/domains/Blade.md"
  - "04-RESOURCES/daggerheart-srd/domains/Grace.md"
  - "04-RESOURCES/daggerheart-srd/subclasses/Troubadour.md"
  - "04-RESOURCES/daggerheart-srd/weapons/Lute.md"
  - "04-RESOURCES/daggerheart-srd/armor/Studded Leather.md"

srd-categories: [domains, subclasses, weapons, armor]

srd-context:
  - "primary offensive domain"
  - "supportive utility domain"
  - "player's chosen subclass"
  - "primary weapon"
  - "standard armor"
---

# Captain Howling Banjo
Entertainer bard...
```

### Example 2: Session Note Update

**BEFORE:**
```yaml
---
tags: session/daggerheart, date/2025-10-24
session-number: 9
date: 2025-10-24
participants: [Andi, Mark, Luie, Gareth]
---

# Session 9

Defeated Craven...
```

**AFTER:**
```yaml
---
tags: session/daggerheart, date/2025-10-24
session-number: 9
date: 2025-10-24
participants: [Andi, Mark, Luie, Gareth]

# NEW FIELDS ADDED:
srd-references:
  - "04-RESOURCES/daggerheart-srd/adversaries/Craven.md"
  - "04-RESOURCES/daggerheart-srd/environments/Mountain Pass.md"
  - "04-RESOURCES/daggerheart-srd/adversaries/Giant Eagle.md"
  - "04-RESOURCES/daggerheart-srd/spells/Inspiring Words.md"

srd-categories: [adversaries, environments, spells]

srd-context:
  - "final boss defeated"
  - "combat environment"
  - "enemy encountered"
  - "spell cast by Banjo"
---

# Session 9

Defeated Craven...
```

## Workflow Tips

### Batch Adding Links
For multiple characters/sessions:
1. Create a list of which files need updates
2. Open first file
3. Add SRD links using templates above
4. Save and move to next
5. Reuse same srd-references list if similar (copy-paste!)

### Finding All Files Needing Links
Search for files WITHOUT SRD metadata:
```
NOT srd-references:*
```

This shows all campaign files not yet linked to SRD content.

### Verification Checklist
Before saving, verify:
- [ ] File paths are exact (copy-pasted from vault)
- [ ] All paths point to existing SRD files
- [ ] srd-categories matches actual references
- [ ] srd-context array length matches references
- [ ] No typos in frontmatter

## Troubleshooting

### "File not found" error
- Verify exact spelling and case
- Check the path prefix: `04-RESOURCES/daggerheart-srd/`
- Search SRD to confirm file exists

### Links not appearing in graph
- Ensure paths are in frontmatter (between `---` markers)
- Check Obsidian reindexed the vault (File → Cache)
- Try force-refresh: Close and reopen vault

### Too many references?
- Limit to 5-8 most relevant references per file
- Use srd-context to explain why each is important
- Consider moving secondary references to srd-notes

## Advanced: Using in Bases

If you're using Obsidian Bases, you can create queries:

**Show characters by their SRD domains:**
```yaml
Filter: contains(srd-categories, "domains")
Group by: player-name
Sort by: file.name
```

**Find all sessions with specific enemy type:**
```yaml
Filter: contains(srd-references, "Craven")
```

## Integration with Graph View

With proper SRD linking:
1. Open Graph View
2. Search for SRD file (e.g., "Troubadour")
3. See all campaign files using it:
   - Character builds with this subclass
   - Session notes where used
   - Build analysis discussions
   - NPC connections

## Next Steps

1. **Pick one content type** (e.g., all character sheets)
2. **Apply template** to 2-3 files as test
3. **Verify links** appear in graph view
4. **Expand** to other content types
5. **Iterate** based on what's most useful

---

*Implementation Guide v1.0*
*Created: 2025-10-24*
*Last Updated: 2025-10-24*

**See Also:** [[srd-linking-strategy]] for detailed strategy and patterns
