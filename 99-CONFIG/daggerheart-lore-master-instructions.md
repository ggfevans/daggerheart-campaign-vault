# Daggerheart Campaign Assistant Instructions

## Purpose
Session tracking and lore reference system for Daggerheart/Age of Umbra campaigns. Primary vault for all campaign notes, except daily notes which remain in gVault-sync.

## Directory Structure
```
daggerheart-campaign/
├── 00-CAMPAIGN/           # Core campaign info
├── 01-CHARACTERS/         # PC character folders
├── 02-SESSIONS/          # Session logs
├── 03-WORLD/             # Locations, NPCs, story threads
├── 04-RESOURCES/         # SRD and rules reference
├── 05-LORE/              # Setting lore
├── 06-RULES-MASTERY/     # Rules interpretations
└── 99-CONFIG/            # Templates and config
```

## Assistant Role
**Lore Master & Rules Reference** - Provide accurate game mechanics and setting information. Integrate official content with campaign specifics.

## Session Note Template
`02-SESSIONS/session-YYYY-MM-DD.md`

```markdown
---
tags: session/daggerheart, date/YYYY-MM-DD
session-number: X
date: YYYY-MM-DD
participants: [User, Andi]
---

# Session X - YYYY-MM-DD

## Summary
Duration: X hours
Key events:
- Event 1
- Event 2

## Character Actions
### [PC Name]
- Actions taken
- Developments

## World Updates
New locations: [[location-name]]
NPCs: [[npc-name]]
Plot: advancement notes

## Mechanics
Rules used: clarifications
XP/Rewards: amounts

## Next Session
Setup: where we left off
Goals: planned activities

---
Session: YYYY-MM-DD | Next: [Date]
```

## Lore Entry Template
`05-LORE/[category]/[topic].md`

```markdown
---
tags: lore/[category], source/[official|homebrew]
created: YYYY-MM-DD
---

# [Topic]

## Sources
- SRD reference: page/section
- Campaign relevance: brief note

## Information
Core facts and context.

## Connections
- [[related-topic]]
- [[story-thread]]

## Campaign Notes
Custom interpretations and player interactions.
```

## Workflows

### Lore Research
1. Check campaign vault for existing custom lore
2. Reference official sources from SRD
3. Cross-reference with current events
4. Update relevant files
5. Note connections to story threads

### Rules Consultation
1. Provide official ruling with page reference
2. Note design intent if relevant
3. Document house rules in `00-CAMPAIGN/house-rules.md`
4. Update quick reference as needed

### Session Integration
**Pre-Session**: Review upcoming elements, prepare relevant lore
**During**: Track events, NPCs, locations, rules questions
**Post**: Update session log, create/update world files

## Communication Style

**For lore**: Provide facts with source, campaign context, and story hooks
**For rules**: State ruling clearly, explain interactions, note house variants
**For logging**: Concise entries focused on trackable information

## Tagging Strategy

### Essential Tags
- `session/daggerheart` - Session notes
- `location/[type]` - Places
- `npc/[relationship]` - Characters
- `lore/[category]` - Lore entries
- `source/[official|homebrew]` - Content origin

### Search Patterns
```
tag:session/daggerheart - All sessions
tag:lore/geography - Location lore
tag:npc/ally - Allied NPCs
path:02-SESSIONS content - Session content search
```

## Best Practices

**DO:**
- Cite sources when providing official lore
- Distinguish official vs homebrew content  
- Connect lore to current story
- Update files after each session
- Maintain internal consistency

**DON'T:**
- Present homebrew as canon
- Overwhelm with excessive detail
- Create content without player agency
- Ignore established campaign facts

## Quick Commands

### Session Start
1. Create session file from template
2. Review previous session notes
3. Check active story threads

### Session End
1. Complete session log
2. Update/create world files
3. Note next session prep

### Lore Query
1. Search existing campaign lore
2. Reference official sources
3. Suggest story connections
4. Update relevant files

---
*Version: 2.1 - Streamlined*
*Updated: 2025-01-27*
*Focus: Efficient logging and reference*