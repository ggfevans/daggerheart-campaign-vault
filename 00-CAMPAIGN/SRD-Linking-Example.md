---
title: "SRD Linking - Live Example"
tags:
  - example
  - srd-linking
  - documentation
created: 2025-10-24

# ✨ DEMONSTRATION: Reese Blackwood NPC with SRD Links
# This shows what the updated file frontmatter would look like

# Existing NPC metadata
npc-type: major-npc
relationship: ally
location: last-light
profession: huntmaster

# NEW SRD LINKING SECTION
srd-references:
  - "04-RESOURCES/daggerheart-srd/weapons/Improved Crossbow.md"
  - "04-RESOURCES/daggerheart-srd/armor/Legendary Leather Armor.md"
  - "04-RESOURCES/daggerheart-srd/gear/Hunting Kit.md"
  - "04-RESOURCES/daggerheart-srd/gear/Rope.md"

srd-categories: [weapons, armor, gear]

srd-context:
  - "primary ranged weapon as huntmaster"
  - "protective gear for wilderness work"
  - "professional hunting equipment"
  - "practical survival tool"

srd-notes: |
  As Huntmaster of Last Light, Reese carries professional-grade
  equipment suited to wilderness tracking and monster combat.
  The crossbow reflects skills in ranged hunting, while leather armor
  provides mobility necessary for wilderness exploration.
---

# How SRD Linking Works - Live Demo with Reese Blackwood

## What We Added

Three new frontmatter fields were added to **Reese Blackwood's NPC file**:

1. **`srd-references`** - Direct file paths to relevant SRD content
2. **`srd-categories`** - Category tags for filtering and discovery
3. **`srd-context`** - Brief explanations of each reference's relevance
4. **`srd-notes`** - Optional longer context about how SRD content fits the character

## Benefits This Enables

### For Campaign Management
- **One-click access** to Reese's equipment specs via SRD links
- **Visual context** in graph view showing NPC → equipment relationships
- **Discovery** - See all NPCs using "Improved Crossbow" at a glance

### For Rules Reference
- **Quick lookup** of crossbow mechanics when Reese is in a scene
- **Equipment comparison** - What do other NPCs/characters carry?
- **Consistency** - All references point to same SRD source

### For Campaign Evolution
- **Equipment tracking** - Update once in SRD, reflects everywhere
- **Build analysis** - Compare Reese's equipment to PC builds
- **Adventure planning** - What gear would be useful as loot?

## The References Explained

### Weapon: Improved Crossbow
- **Reason**: Fits a professional huntmaster's toolkit
- **Mechanical link**: Shows Reese's primary combat approach
- **Discovery**: Graph will show "Who carries Improved Crossbow?" → Reese

### Armor: Legendary Leather Armor  
- **Reason**: Balances protection with wilderness mobility
- **Mechanical link**: Shows AC/defense without being heavy
- **Discovery**: Armor comparison view → "What do NPCs wear?"

### Gear: Hunting Kit
- **Reason**: Essential for professional tracker
- **Mechanical link**: Supports wilderness survival mechanics
- **Discovery**: "What gear enables hunting?" → Find Hunting Kit

### Gear: Rope
- **Reason**: Universal tool for wilderness navigation/rescue
- **Mechanical link**: Practical for climbing/traversal challenges
- **Discovery**: Common item with multiple uses

## How to Use This in Your Campaign

### Finding Reese's Equipment
```
From: 03-WORLD/npcs/reese-blackwood.md
→ Click "srd-references" or any listed path
→ Opens Improved Crossbow stats (04-RESOURCES/...)
→ Use for combat mechanics, compare to PC weapons
```

### Graph View Discovery
```
1. Open Graph View
2. Search for "Reese Blackwood"
3. See connected files:
   - Party members (backlinks)
   - Sessions mentioning Reese
   - SRD equipment (srd-references)
4. Visually understand Reese's role in campaign
```

### Base Query Example
```
Filter: contains(path, "npc") AND contains(srd-categories, "weapons")
Result: All NPCs with weapon references
View: "Which NPCs are combat-capable and with what weapons?"
```

## Next Steps: Apply to Your Campaign

### Phase 1: Character Sheets (Highest Priority)
- [ ] Add srd-references to: Banjo, Vaerenth, Augustus, Aster
- [ ] Link their domains, subclasses, weapons, armor
- [ ] Use as quick combat reference during sessions

### Phase 2: Session Notes
- [ ] Add srd-references to adversaries in recent sessions
- [ ] Link environments/locations where combats occurred
- [ ] Track spell usage via spell SRD links

### Phase 3: Major NPCs
- [ ] Add srd-references to key NPCs
- [ ] Link their equipment, abilities, services offered
- [ ] Show NPC-PC equipment relationships

### Phase 4: Deep Integration
- [ ] Story threads with relevant mechanics
- [ ] World locations with thematic SRD connections
- [ ] Build guides comparing multiple options

## Example: How It Works Step-by-Step

**Scenario**: You're prepping Session 10, Reese Blackwood will be in combat

**Old Workflow**:
1. Open Reese's NPC file
2. See "Equipment: [To be established in play]"
3. Remember he's probably carrying a crossbow
4. Search vault for crossbow stats
5. Open Improved Crossbow SRD file
6. Reference damage/range/traits

**New Workflow** (with SRD linking):
1. Open Reese's NPC file
2. See "srd-references" section
3. Click "Improved Crossbow.md"
4. Instantly have all stats
5. See what damage/traits apply to this combat

**Time saved**: ~90 seconds per NPC lookup during prep

## Common Questions

### "Why not just put the weapon stats in the NPC file?"
- **Single source of truth**: One official SRD file for "Improved Crossbow"
- **Consistency**: Everyone uses same mechanics
- **Comparison**: See who else uses this weapon
- **Graph relationships**: Understand equipment distribution

### "Won't this be a lot of metadata to maintain?"
- **Start small**: Just character sheets + recent sessions
- **Copy-paste**: Most characters use standard equipment
- **One-time setup**: Once added, information is stable
- **Backlinks work both ways**: Update visible in graph

### "What if I want to customize equipment?"
- **Keep SRD clean**: Reference standard version in metadata
- **Add customization notes**: In `srd-notes` field explain changes
- **Example**: "Uses Improved Crossbow with custom goblin-bone coating"

### "Does this require any plugins?"
- **No**: Pure frontmatter metadata
- **Optional**: Bases for table views, Dataview for queries
- **Works**: Graph view, backlinks, search all work immediately

## Quick Reference: What to Link by Content Type

| Content Type | Link To | Reason |
|---|---|---|
| **Character Sheet** | Domains, Subclasses, Weapons, Armor, Spells | Shows complete mechanical build |
| **NPC** | Equipment, Abilities, Gear | Shows capabilities and resources |
| **Session Note** | Adversaries, Environments, Spells Cast | Shows what was used in play |
| **Story Thread** | Related Mechanics, Thematic Domains | Shows mechanical connections |
| **World Location** | Environments, Creatures, Gear | Shows what exists in location |
| **Build Guide** | Domains, Subclasses, Spells, Weapons | Shows analyzed options |

## See Also
- [[srd-linking-strategy]] - Detailed strategy and patterns
- [[srd-linking-implementation-guide]] - Step-by-step how-to

---

**This example demonstrates how a simple update creates powerful relationships**  
**between your campaign content and the comprehensive Daggerheart SRD.**

*Created: 2025-10-24*  
*Status: Implementation Ready*
