---
# Core Status Properties
status: active
priority: high
energy: high

# Temporal Properties
created: 2025-08-15
started: 2025-08-15
target: 2025-09-15
completed:

# Context Properties
area: "[[02-AREAS/tech]]"
type: implementation
next-action: "Set up local development environment"
blocked-by:
momentum: building

# Project-specific metadata
github-fork: "https://github.com/ggfevans/daggerheart"
upstream-repo: "https://github.com/Foundryborne/daggerheart"
tech-stack: ["JavaScript", "Foundry VTT", "Node.js", "Rollup", "Gulp", "HTML/CSS"]
project-version: "1.0.4"

# Tags
tags:
  - project
  - open-source
  - daggerheart
  - foundry-vtt
  - javascript
  - contribution
---

# Foundryborne Daggerheart Open Source Contributor Project

## 🎯 Project Objective
Become an effective open source contributor to the Foundryborne Daggerheart implementation for Foundry VTT, making meaningful contributions to improve the system for the community.

## 📚 Project Context

### What is Foundryborne Daggerheart?
- **Purpose**: Community-built Foundry VTT implementation of the Daggerheart TTRPG system
- **Status**: Active development, v1.0.4 released (Care Package 3 - Jumping Capybara)
- **Community**: Not affiliated with Critical Role/Darrington Press, purely community-driven
- **Maturity**: Recently hit v1.0.0 stable release, now in maintenance/improvement phase

### Repository Statistics
- **Stars**: 112
- **Forks**: 37
- **Issues**: 183 closed, 0 currently open (as of search)
- **Recent Activity**: Last update August 15, 2025
- **Languages**: Primarily JavaScript

## 🔧 Technical Setup

### Prerequisites
- [ ] Node.js and npm installed
- [ ] Foundry VTT installed locally
- [ ] Git configured with GitHub account
- [ ] Code editor (VS Code recommended)
- [ ] Basic JavaScript knowledge
- [ ] Understanding of Foundry VTT system development

### Local Development Environment Setup

#### Step 1: Clone Your Fork
```bash
cd ~/dev  # or your preferred development directory
git clone https://github.com/ggfevans/daggerheart.git
cd daggerheart

# Add upstream remote
git remote add upstream https://github.com/Foundryborne/daggerheart.git
git fetch upstream
```

#### Step 2: Install Dependencies
```bash
npm install
```

#### Step 3: Configure package.json
Update the `package.json` file with your local Foundry paths:

```json
{
  "scripts": {
    "start": "concurrently \"rollup -c --watch\" \"node [YOUR_FOUNDRY_PATH]/resources/app/main.js --dataPath=[YOUR_DATA_PATH] --noupnp\" \"gulp\"",
  }
}
```

Replace:
- `[YOUR_FOUNDRY_PATH]` with your Foundry installation path
- `[YOUR_DATA_PATH]` with your Foundry data directory

#### Step 4: Link to Foundry Systems
```bash
# Linux/Mac
ln -snf ~/dev/daggerheart ~/foundrydata/Data/systems/daggerheart

# Windows (run as admin)
mklink /D "C:\Users\[username]\AppData\Local\FoundryVTT\Data\systems\daggerheart" "C:\dev\daggerheart"
```

#### Step 5: Build and Run
```bash
npm start
```

## 📋 Contribution Strategy

### Phase 1: Learning & Exploration (Week 1)
- [x] Fork repository
- [ ] Set up local development environment
- [ ] Successfully build and run the system locally
- [ ] Join the Foundryborne Discord server
- [ ] Read through the wiki documentation
- [ ] Explore the codebase structure
- [ ] Test the system in Foundry VTT
- [ ] Review recent closed issues for context

### Phase 2: First Contributions (Week 2)
- [ ] Look for "good first issue" labels
- [ ] Start with documentation improvements
- [ ] Fix typos or improve comments
- [ ] Add missing JSDoc comments
- [ ] Improve error messages
- [ ] Submit first small PR

### Phase 3: Feature Contributions (Weeks 3-4)
- [ ] Identify missing features from Daggerheart rules
- [ ] Propose feature in Discord/Issues
- [ ] Implement feature with tests
- [ ] Submit PR with detailed description
- [ ] Respond to code review feedback
- [ ] Get first meaningful PR merged

### Phase 4: Regular Contributor (Ongoing)
- [ ] Take on larger features
- [ ] Help review other PRs
- [ ] Assist new contributors
- [ ] Contribute to wiki/documentation
- [ ] Participate in release planning

## 🗂️ Codebase Structure

### Key Directories
```
daggerheart/
├── src/              # Source code
│   ├── actors/       # Character/NPC logic
│   ├── items/        # Item system
│   ├── sheets/       # Character sheets UI
│   └── system/       # Core system logic
├── templates/        # HTML templates
├── styles/          # CSS/SCSS files
├── lang/            # Localization files
├── packs/           # Compendium data
└── system.json      # System manifest
```

### Technology Stack
- **Build Tools**: Rollup, Gulp
- **Framework**: Foundry VTT API
- **Languages**: JavaScript (ES6+), HTML, CSS/SCSS
- **Version Control**: Git/GitHub
- **Package Management**: npm

## 🎯 Contribution Areas

### High-Value Contribution Opportunities
1. **Bug Fixes**: Address any reported issues
2. **UI/UX Improvements**: Enhance character sheets and interfaces
3. **Rules Implementation**: Add missing Daggerheart mechanics
4. **Performance Optimization**: Improve system speed
5. **Accessibility**: Add ARIA labels, keyboard navigation
6. **Localization**: Translate to other languages
7. **Documentation**: Improve wiki and code comments
8. **Testing**: Add automated tests
9. **Compendium Content**: Add items, spells, abilities
10. **Module Compatibility**: Ensure compatibility with popular Foundry modules

## 📐 Contribution Guidelines

### Code Style
- Follow existing code patterns
- Use meaningful variable names
- Add JSDoc comments for functions
- Keep functions small and focused
- Test thoroughly before submitting

### Pull Request Process
1. **Create feature branch**: `git checkout -b feature/your-feature-name`
2. **Make changes**: Implement feature/fix
3. **Test locally**: Ensure everything works
4. **Commit with clear message**: `git commit -m "feat: add X functionality"`
5. **Push to fork**: `git push origin feature/your-feature-name`
6. **Create PR**: Use template, reference issues
7. **Respond to feedback**: Address review comments
8. **Celebrate merge**: 🎉

### Commit Message Convention
```
type(scope): description

- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Code restructuring
- test: Testing
- chore: Maintenance
```

## 🤝 Community Engagement

### Discord Participation
- Join the Foundryborne Discord
- Introduce yourself in #introductions
- Ask questions in #development
- Share progress in #showcase
- Help others in #support

### Issue Management
- Check existing issues before creating new ones
- Provide detailed bug reports with steps to reproduce
- Suggest features with use cases
- Comment on issues you're working on

### Code Review Etiquette
- Be constructive and kind
- Explain reasoning for suggestions
- Accept feedback gracefully
- Thank reviewers for their time

## 📚 Learning Resources

### Foundry VTT Development
- [Official Foundry API Docs](https://foundryvtt.com/api/)
- [Foundry VTT Discord #system-development](https://discord.gg/foundryvtt)
- [Foundry System Tutorial](https://foundryvtt.wiki/en/development/guides/SD-tutorial)

### Daggerheart System
- [Official Daggerheart Rules](https://darringtonpress.com/daggerheart/)
- [Foundryborne Wiki](https://github.com/Foundryborne/daggerheart/wiki)
- [System Documentation](https://foundryborne.online/)

### JavaScript/Web Development
- [MDN Web Docs](https://developer.mozilla.org/)
- [JavaScript.info](https://javascript.info/)
- [Rollup Documentation](https://rollupjs.org/)

## 🎯 Success Metrics

### Short-term (1 month)
- [ ] Successfully set up development environment
- [ ] Submit at least 1 merged PR
- [ ] Join and participate in Discord
- [ ] Understand codebase structure

### Medium-term (3 months)
- [ ] 5+ merged PRs
- [ ] Implement a significant feature
- [ ] Help review other contributors' PRs
- [ ] Become recognized in the community

### Long-term (6+ months)
- [ ] Regular contributor status
- [ ] Trusted reviewer for PRs
- [ ] Mentor new contributors
- [ ] Shape project direction

## 🔗 Key Links

### Project Resources
- **Your Fork**: [ggfevans/daggerheart](https://github.com/ggfevans/daggerheart)
- **Upstream Repo**: [Foundryborne/daggerheart](https://github.com/Foundryborne/daggerheart)
- **Project Website**: [foundryborne.online](https://foundryborne.online/)
- **Wiki/Docs**: [GitHub Wiki](https://github.com/Foundryborne/daggerheart/wiki)
- **Discord**: Join via website
- **Releases**: [GitHub Releases](https://github.com/Foundryborne/daggerheart/releases)

### Reference
- **System Manifest**: `https://github.com/Foundryborne/daggerheart/releases/download/1.0.4/system.json`
- **Contributing Guide**: Check repo for `contributing.md`
- **Code of Conduct**: Check repo for `coc.md`

## 📝 Progress Log

### 2025-08-15
- Created project plan
- Forked repository to personal GitHub
- Researched project structure and community

## 📋 Next Steps
1. **Immediate**: Set up local development environment
2. **This Week**: Join Discord, explore codebase
3. **Next Week**: Submit first PR (documentation or small fix)
4. **This Month**: Make first significant contribution

---
*Last Updated: 2025-08-15*