---
title: "SRD Linking System - Index"
tags: 
  - index
  - srd-linking
  - organization
created: 2025-10-24
---

# SRD-to-Campaign Linking System

## 📚 Complete Documentation Suite

Your campaign vault now includes a complete system for creating frontmatter metadata links between your campaign content and the Daggerheart SRD.

### Core Documents

#### 1. **[[srd-linking-strategy]]** (Start Here for Understanding)
**What it is**: Comprehensive strategy document explaining the complete linking system

**Contains**:
- Overview of metadata schema
- Implementation patterns for each content type (characters, NPCs, sessions, etc.)
- Discovery workflows
- Integration with Bases
- Maintenance guidelines

**Read this when**: You want to understand the *why* behind the system

---

#### 2. **[[srd-linking-implementation-guide]]** (Start Here for Doing)
**What it is**: Step-by-step practical guide with templates and examples

**Contains**:
- Template snippets for each content type
- How to find SRD file paths
- Practical examples (before/after)
- Batch update workflows
- Troubleshooting guide

**Read this when**: You're ready to add links to your files

---

#### 3. **[[SRD-Linking-Quick-Reference]]** (Bookmark This)
**What it is**: One-page cheat sheet for quick reference

**Contains**:
- Copy-paste frontmatter snippet
- SRD category reference
- Content type checklist
- Common file paths
- Quick workflow (5 minutes)

**Use this when**: You're actively adding links and need quick lookups

---

#### 4. **[[SRD-Linking-Example]]** (See It In Action)
**What it is**: Live example using Reese Blackwood NPC

**Contains**:
- Real example frontmatter (Reese's equipment links)
- Explanation of each field
- Benefits this enables
- Step-by-step discovery workflow
- Common questions answered

**Read this when**: You want to see concrete examples before implementing

---

## 🎯 Quick Start Path

### For Impatient Users (5 Minutes)
1. Open [[SRD-Linking-Quick-Reference]]
2. Copy the frontmatter snippet
3. Add to one character sheet
4. Save and check graph view
5. Repeat for other characters

### For Methodical Users (30 Minutes)
1. Read [[SRD-Linking-Strategy]] sections 1-2 (overview)
2. Read [[srd-linking-implementation-guide]] section "Practical Examples"
3. Review [[SRD-Linking-Example]] to see pattern
4. Start with character sheets (highest priority)
5. Reference [[SRD-Linking-Quick-Reference]] as you work

### For Comprehensive Understanding (1-2 Hours)
1. Read entire [[srd-linking-strategy]]
2. Work through [[srd-linking-implementation-guide]] with real files
3. Review [[SRD-Linking-Example]] section "How It Works"
4. Plan your implementation phases
5. Reference docs as you execute

---

## 📋 Frontmatter Fields Summary

### Required Fields (Minimum)
```yaml
srd-references:
  - "04-RESOURCES/daggerheart-srd/category/Item.md"

srd-categories: [category1, category2]
```

### Recommended Fields
```yaml
srd-references:
  - "04-RESOURCES/daggerheart-srd/category/Item.md"

srd-categories: [category1, category2]

srd-context:
  - "why this reference matters"
```

### Optional Enhancement
```yaml
srd-notes: |
  Longer explanation of how this SRD content is used
  or customized in your specific campaign context.
```

---

## 🚀 Implementation Priority Guide

### Phase 1: Character Sheets (Highest ROI)
**Time**: 30-45 minutes for 4 characters  
**Benefit**: Quick access to all PC builds and mechanics  
**Files to update**: 
- Banjo (Gareth's character)
- Vaerenth (Andi's character)
- Augustus (Mark's character)
- Aster (Luie's character)

**What to link**: Domains, subclasses, weapons, armor, key spells

### Phase 2: Recent Sessions (High Engagement)
**Time**: 15-20 minutes per session  
**Benefit**: Immediate context for ongoing campaigns  
**Files to update**: Sessions 6-9 (most recent)  
**What to link**: Adversaries encountered, environments, spells cast

### Phase 3: Major NPCs (Campaign Context)
**Time**: 10-15 minutes per NPC  
**Benefit**: Quick reference for NPC capabilities  
**Files to update**: Reese Blackwood, other key NPCs  
**What to link**: Equipment, abilities, services offered

### Phase 4: World & Story (Deep Integration)
**Time**: Variable  
**Benefit**: Thematic connections and comprehensive context  
**Files to update**: Locations, story threads, building guides  
**What to link**: Environments, creatures, mechanics

---

## 🔍 Discovery Methods After Implementation

### Via Graph View
```
1. Open Graph View (top right)
2. Search for "Troubadour" 
3. See all files using this subclass
4. Expand nodes to see connections
```

### Via Vault Search
```
Search: "srd-references:*"
Result: All files with SRD linking
```

### Via File Links
```
1. Open character sheet
2. Click srd-references link
3. Instantly jump to SRD content
4. Use graph to see who else uses it
```

### Via Bases (If Using)
```
Create Base filter: contains(srd-categories, "weapons")
Group by: player-name
See: All PC weapons organized by character
```

---

## 💡 Key Concepts

### What Gets Linked?
- **Campaign content** (characters, NPCs, sessions, locations, stories)
- **→ References**
- **→ SRD content** (weapons, spells, domains, adversaries, environments)

### Why Link?
- **One-click access** from campaign to mechanics
- **Graph relationships** show usage patterns
- **Discovery** - Find all uses of specific items
- **Consistency** - Everyone uses same reference
- **Campaign impact** - See what's actually used

### How It Works?
- **Frontmatter metadata** (YAML) in your campaign files
- **Points to** SRD file paths
- **Creates** discoverable connections in Obsidian
- **Requires** no plugins (works with graph, search, etc.)
- **Optional** integration with Bases for views

---

## 📊 Expected Benefits Timeline

### Immediate (First Session)
- Faster prep: Quick access to NPC/enemy stats
- Better reference: Don't hunt for weapon mechanics
- Cleaner notes: No duplicated stat blocks

### Short-term (Weeks 1-2)
- Pattern recognition: See what items party uses most
- Quick builds: Reference similar character builds
- Session prep: 20% faster due to quick lookups

### Medium-term (Weeks 2-4)
- Campaign intelligence: Understand equipment distribution
- Strategic planning: See optimization opportunities
- Player communication: Point to official SRD for rulings

### Long-term (Ongoing)
- Knowledge base: Comprehensive campaign-SRD relationship map
- Archive value: Future reference for similar campaigns
- System mastery: Deep understanding of game mechanics
- Community resource: Shareable documentation pattern

---

## ⚙️ Technical Details

### File Format
- **Type**: YAML frontmatter metadata
- **Location**: Top of each .md file (between `---` markers)
- **Syntax**: Standard Obsidian frontmatter
- **Compatibility**: Works with all Obsidian features

### Path Format
```
04-RESOURCES/daggerheart-srd/[category]/[Item Name].md
```

### Categories Available
```
weapons, armor, gear, spells, domains, subclasses,
classes, ancestries, adversaries, environments,
contents, abilities, and more
```

---

## 🔗 Maintenance Schedule

### Daily (During Prep)
- Reference srd-references when planning sessions
- Check graph for related content

### Weekly (Session Prep)
- Add srd-references to next session's encounters
- Update NPC equipment if changed

### Monthly (Maintenance)
- Review all active campaign files
- Check for missing standard links
- Update completed sessions with final references

### Quarterly (Deep Audit)
- Full consistency check
- Update archived sessions
- Refine category organization
- Archive old content

---

## 🎓 Learning Resources

### Concepts to Understand
1. **Frontmatter metadata** - YAML in .md files
2. **Obsidian graph view** - Relationship visualization
3. **File paths** - Exact references to SRD content
4. **Backlinks** - How files reference each other

### External Resources
- Obsidian Help: https://help.obsidian.md/
- YAML Syntax: https://yaml.org/

### Within This Project
- [[srd-linking-strategy]] - Deep dive into strategy
- [[srd-linking-implementation-guide]] - Hands-on walkthrough
- [[SRD-Linking-Example]] - Real-world example

---

## ❓ FAQ

**Q: Do I need to link everything?**  
A: No! Start with characters/sessions/NPCs. Expand from there.

**Q: Can I start with just one character?**  
A: Absolutely! Great way to test the system.

**Q: Will this slow down Obsidian?**  
A: No - frontmatter is efficient and improves organization.

**Q: Can I stop using this system?**  
A: Yes - just don't add new srd-references fields. Existing links stay.

**Q: What if SRD content changes?**  
A: File paths won't change. Update path if file is renamed.

**Q: Do I need Bases or plugins?**  
A: No - works standalone. Plugins enhance but aren't required.

---

## 📝 Implementation Checklist

- [ ] Read [[srd-linking-strategy]] overview
- [ ] Review [[SRD-Linking-Example]] for concrete example
- [ ] Bookmark [[SRD-Linking-Quick-Reference]]
- [ ] Start Phase 1: Add links to character sheets
- [ ] Test graph view - verify links work
- [ ] Move to Phase 2: Recent session notes
- [ ] Continue with Phase 3: Major NPCs
- [ ] Plan Phase 4: Deep integration

---

## 📞 Support & Questions

**Not sure where to start?**  
→ Read [[SRD-Linking-Example]] first

**Want to understand the full system?**  
→ Study [[srd-linking-strategy]]

**Ready to implement?**  
→ Use [[srd-linking-implementation-guide]] + [[SRD-Linking-Quick-Reference]]

**Need quick facts?**  
→ Bookmark [[SRD-Linking-Quick-Reference]]

---

## 🎉 Success Indicators

You'll know the system is working when:

✅ You can click from NPC to equipment in seconds  
✅ Graph view shows interesting relationships  
✅ Session prep is 15-20% faster  
✅ You rarely search for basic mechanics anymore  
✅ Campaign files feel more connected  
✅ New players can explore SRD from campaign content  

---

**System Created**: 2025-10-24  
**Status**: Ready for Implementation  
**Next Step**: Read [[SRD-Linking-Example]] → Start with Phase 1

---

## Document Navigation

| Document | Purpose | Best For |
|----------|---------|----------|
| **This Index** | Overview of entire system | First-time orientation |
| **[[srd-linking-strategy]]** | Strategic deep-dive | Understanding the why |
| **[[srd-linking-implementation-guide]]** | Tactical how-to | Actually doing the work |
| **[[SRD-Linking-Example]]** | Concrete demonstration | Seeing it in action |
| **[[SRD-Linking-Quick-Reference]]** | Cheat sheet | Bookmarked reference |
