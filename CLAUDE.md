# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal portfolio website (ankushkumarsingh.github.io) hosted on GitHub Pages. It's a static website showcasing Ankush Kumar Singh's professional profile and includes interactive data structure visualizations.

## Architecture

**Static Site Structure:**
- Pure HTML/CSS/JavaScript with no build process
- Component-based CSS using CSS custom properties for theming
- Progressive enhancement approach - works without JavaScript
- Mobile-first responsive design

**Main Components:**
- `index.html` - Portfolio homepage with hero, about, experience, projects, and contact sections
- `data-structures.html` - Hub for educational visualizations
- `graph.html`, `graph-v2.html`, `dijkstra.html` - Interactive algorithm visualizations
- `styles.css` - Global styles with dark/light theme support
- `script.js` - Theme toggle, smooth scrolling, form handling, and animations

## Common Commands

**No build process required** - this is a static site deployed directly to GitHub Pages.

**Development workflow:**
```bash
# Open files directly in browser for testing
open index.html

# Python PDF sync utility (optional)
pip install -r requirements.txt
python read_pdf.py

# Deploy changes
git add .
git commit -m "Description of changes"
git push origin master
```

**Git branch:** `master` is the main branch (auto-deploys to GitHub Pages)

## Code Conventions

**CSS:**
- Uses CSS custom properties for theming (--primary-color, --text-color, etc.)
- Apple-inspired design system with SF Pro Display font
- Mobile-first breakpoints
- CSS Grid and Flexbox for layouts

**JavaScript:**
- Vanilla JavaScript (no frameworks)
- Modern ES6+ features
- Event-driven architecture for interactions

**HTML:**
- Semantic HTML5 structure
- BEM-like class naming for components
- Font Awesome 6 for icons

## File Organization

**Portfolio Content:** All in `index.html` with sections for hero, about, experience, projects, contact
**Visualizations:** Separate HTML files (`graph.html`, `dijkstra.html`, etc.) for interactive demos
**Assets:** PDF resume, Python utilities for content sync
**Styling:** Single `styles.css` with comprehensive responsive design
**Interactions:** Single `script.js` for all client-side functionality

## Development Notes

- Changes to `index.html` affect the main portfolio page
- Theme system uses CSS custom properties - modify `:root` and `[data-theme="dark"]` selectors
- New visualizations should follow the pattern of existing graph pages
- PDF sync script (`read_pdf.py`) can update website content from resume
- All interactive features gracefully degrade without JavaScript