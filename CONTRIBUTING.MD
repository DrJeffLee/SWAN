# Git & GitHub Collaboration Guidelines

## Daily Workflow

**Every time you start working on a new feature:**
```bash
git checkout main
git pull origin main
git checkout -b feature/describe-your-feature
```

**When you've made a change :**
```bash
git add .
git commit -m "Brief description of the change. Can be one or two words"
git push origin feature/describe-your-feature
```

**When you're done working on a feature:**
```bash
git add .
git commit -m "Clear description of the feature. Should be one sentence."
git push origin feature/describe-your-work
```

**Then on GitHub:** Create a Pull Request to merge into main (see below)

## Key Rules

1. **Never work directly on main branch** - always create a feature branch
2. **Never push directly to main** - always use Pull Requests  
3. **Always start from updated main** - pull latest changes first
4. **One feature per branch** - keep changes focused
5. **Delete your feature branch after merging** (GitHub will offer this)

## Branch Naming
- `feature/wave-analysis` - new functionality
- `bugfix/calculation-error` - fixing problems
- `docs/update-readme` - documentation changes

## Pull Request Process
1. Push your feature branch to GitHub
2. Create Pull Request (PR) on GitHub  
3. Ask someone to review your code
4. Address any feedback
5. Merge when approved
6. Delete the feature branch

## Getting Help
- **Stuck?** Ask for help immediately - Git problems get worse if ignored
- **Made a mistake?** Don't panic - almost everything in Git can be undone
- **Conflicts?** Ask for help the first few times

## Commands You'll Use Most
```bash
git status          # See what's changed
git pull origin main # Get latest changes
git add .           # Stage your changes  
git commit -m "msg" # Save your changes
git push origin branch-name # Upload to GitHub
```

**Remember:** When in doubt, ask! It's better to check than break something.
