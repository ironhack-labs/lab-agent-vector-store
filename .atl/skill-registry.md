# Skill Registry

**Delegator use only.** Any agent that launches sub-agents reads this registry to resolve compact rules, then injects them directly into sub-agent prompts. Sub-agents do NOT read this registry or individual SKILL.md files.

See `_shared/skill-resolver.md` for the full resolution protocol.

## User Skills

| Trigger | Skill | Path |
|---------|-------|------|
| a11y audit, WCAG compliance, screen reader support, keyboard navigation, make accessible | accessibility | ~/.agents/skills/accessibility/SKILL.md |
| creating, opening, or preparing PRs for review | branch-pr | ~/.config/opencode/skills/branch-pr/SKILL.md |
| PRs over 400 lines, stacked PRs, review slices | chained-pr | ~/.config/opencode/skills/chained-pr/SKILL.md |
| design, create, generate banner; social media, ads, website heroes | ckm:banner-design | ~/.claude/skills/ckm-banner-design/SKILL.md |
| branded content, tone of voice, marketing assets, brand compliance, style guides | ckm:brand | ~/.agents/skills/ckm-brand/SKILL.md |
| design logo, create CIP, generate mockups, build slides, design banner, generate icon | ckm:design | ~/.claude/skills/ckm-design/SKILL.md |
| design tokens, systematic design, brand-compliant presentations | ckm:design-system | ~/.agents/skills/ckm-design-system/SKILL.md |
| create strategic HTML presentations with Chart.js, design tokens, responsive layouts | ckm:slides | ~/.agents/skills/ckm-slides/SKILL.md |
| building user interfaces, implementing design systems, shadcn/ui, Tailwind CSS | ckm:ui-styling | ~/.agents/skills/ckm-ui-styling/SKILL.md |
| writing guides, READMEs, RFCs, onboarding, architecture, or review-facing docs | cognitive-doc-design | ~/.config/opencode/skills/cognitive-doc-design/SKILL.md |
| PR feedback, issue replies, reviews, Slack messages, or GitHub comments | comment-writer | ~/.config/opencode/skills/comment-writer/SKILL.md |
| library docs, framework APIs, code examples, setup questions | context7-mcp | ~/.claude/skills/context7-mcp/SKILL.md |
| editing opencode configuration: opencode.json, .opencode/, agents, subagents, skills | customize-opencode | <built-in> |
| analyze Stitch projects, synthesize DESIGN.md files | design-md | ~/.agents/skills/design-md/SKILL.md |
| UI polish, component design, animation decisions, invisible details | emil-design-eng | ~/.agents/skills/emil-design-eng/SKILL.md |
| transform vague UI ideas into polished, Stitch-optimized prompts | enhance-prompt | ~/.agents/skills/enhance-prompt/SKILL.md |
| API syntax questions, configuration options, version migration, library-specific debugging | find-docs | ~/.agents/skills/find-docs/SKILL.md |
| build web components, pages, artifacts, posters, landing pages, dashboards | frontend-design | ~/.agents/skills/frontend-design/SKILL.md |
| git add, commit, push, finish session, commit and push | git-session-finalize | ~/.config/opencode/skills/git-session-finalize/SKILL.md |
| Go tests, go test coverage, Bubbletea teatest, golden files | go-testing | ~/.config/opencode/skills/go-testing/SKILL.md |
| creating GitHub issues, bug reports, or feature requests | issue-creation | ~/.config/opencode/skills/issue-creation/SKILL.md |
| judgment day, dual review, adversarial review, juzgar | judgment-day | ~/.config/opencode/skills/judgment-day/SKILL.md |
| convert Stitch designs into Vite + React components | react:components | ~/.claude/skills/react-components/SKILL.md |
| generate walkthrough videos from Stitch projects | remotion | ~/.agents/skills/remotion/SKILL.md |
| improve SEO, optimize for search, fix meta tags, structured data, sitemap | seo | ~/.agents/skills/seo/SKILL.md |
| integrate shadcn/ui components, component discovery, installation, customization | shadcn-ui | ~/.agents/skills/shadcn-ui/SKILL.md |
| new skills, agent instructions, documenting AI usage patterns | skill-creator | ~/.config/opencode/skills/skill-creator/SKILL.md |
| Stitch design work: prompt enhancement, design system synthesis, screen generation | stitch-design | ~/.claude/skills/stitch-design/SKILL.md |
| iteratively build websites using Stitch with autonomous baton-passing loop | stitch-loop | ~/.agents/skills/stitch-loop/SKILL.md |
| plan, build, create, design, implement, review, fix, improve UI/UX code | ui-ux-pro-max | ~/.agents/skills/ui-ux-pro-max/SKILL.md |
| implementation, commit splitting, chained PRs, keeping tests and docs with code | work-unit-commits | ~/.config/opencode/skills/work-unit-commits/SKILL.md |

## Compact Rules

Pre-digested rules per skill. Delegators copy matching blocks into sub-agent prompts as `## Project Standards (auto-resolved)`.

### accessibility
- All images must have alt text; decorative images use `alt="" role="presentation"`
- Target WCAG 2.2 Level AA compliance at minimum
- Ensure keyboard navigation: all interactive elements reachable via Tab
- Use semantic HTML: `<nav>`, `<main>`, `<header>`, `<footer>`, proper heading hierarchy
- Color contrast ratio ≥4.5:1 for normal text, ≥3:1 for large text
- Forms: every input has associated `<label>`, errors announced with `aria-describedby`

### branch-pr
- Every PR MUST link an approved issue via `Closes/Fixes/Resolves #N`
- Every PR MUST have exactly one `type:*` label
- Branch names: `^(feat|fix|chore|docs|style|refactor|perf|test|build|ci|revert)/[a-z0-9._-]+$`
- Conventional commits: `type(scope): description` — no `Co-Authored-By` trailers
- PR body MUST contain: linked issue, PR type, summary, changes table, test plan, contributor checklist

### chained-pr
- Split PRs over 400 changed lines unless maintainer accepts `size:exception`
- Each chained PR: clear start/end, prior dependencies, follow-up work, dependency diagram
- Feature Branch Chain: child #1 targets tracker branch; later children target immediate parent
- Never mix chain strategies after user chooses one
- Verify each PR independently: CI, tests, docs, clean diff

### ckm:banner-design
- Use images from the MCP, not code-generated or text-based visuals
- Every image must have `safe` search flag and no text in the prompt (per Gemini API)
- Provide multiple art direction options (minimalist, gradient, bold typography, etc.)
- Specify exact platform dimensions (e.g., Facebook 1200×630, Instagram 1080×1080)

### ckm:brand
- Define brand voice: tone, vocabulary, personality traits
- Maintain visual identity: color palette, typography, logo usage, imagery
- Messaging frameworks: taglines, value propositions, audience-specific messaging
- Track brand assets centrally; enforce consistency across all touchpoints

### ckm:design
- Brand identity: logo design (55 styles via Gemini AI), color systems, typography
- CIP (Corporate Identity Program): 50 deliverables, mockups, templates
- Slides: HTML presentations with Chart.js, responsive layouts
- Banners: 22 styles for social/ads/web/print; icons: 15 styles, SVG via Gemini 3.1 Pro

### ckm:design-system
- Three-layer tokens: primitive → semantic → component
- CSS variables as the implementation layer; spacing/typography scales must be systematic
- Component specs: variants, states, accessibility baked in
- Slides: strategic presentations using design tokens for consistency

### ckm:slides
- Use HTML + Chart.js for interactive, responsive presentations
- Design tokens: consistent colors, typography, spacing across slides
- Copywriting formulas: PAS (Problem-Agitate-Solve), AIDA, storytelling arcs
- Adapt slide strategy to audience and context (pitch, report, education)

### ckm:ui-styling
- Use shadcn/ui components (Radix UI + Tailwind) for accessible, composable UI
- Tailwind utility-first: prefer utility classes over custom CSS; use `@apply` only for repeated patterns
- Dark mode: use `dark:` variant; theme via CSS variables
- Responsive: mobile-first with `sm:`, `md:`, `lg:` breakpoints

### cognitive-doc-design
- Lead with the answer: decision/action/outcome first, context after
- Progressive disclosure: happy path → details → edge cases → references
- Prefer tables, checklists, examples, and templates over dense prose
- PR docs: state what to review first, what's out of scope, link to prev/next PR in chains
- Chunk related info into small sections; use headings for signposting

### comment-writer
- Start with the actionable point; don't recap the whole PR before feedback
- Keep feedback short: 1-3 paragraphs or a tight bullet list; explain WHY technically
- Match thread/user language; in Spanish use Rioplatense (voseo): `podés`, `tenés`, `fijate`
- Avoid pile-ons: focus on highest-value issue, not every tiny preference
- No em dashes — use commas, periods, or parentheses instead

### context7-mcp
- Always resolve library ID first via `resolve-library-id`; prefer version-specific IDs
- Select by name match, benchmark score, snippet count, source reputation (High/Medium preferred)
- Call `query-docs` with the full user question, not keywords
- Retry with `researchMode: true` if first result unsatisfies; do this before falling back to training data

### customize-opencode
- Edit opencode.json, opencode.jsonc, files under .opencode/, or ~/.config/opencode/
- Create/fix agents, subagents, skills, plugins, MCP servers, permission rules
- Do NOT use for user application code or non-opencode projects

### design-md
- Analyze Stitch projects and synthesize semantic design systems
- Output DESIGN.md with design tokens, component specs, and usage patterns
- Focus on semantic meaning, not visual implementation details

### emil-design-eng
- UI polish: micro-interactions, transitions, loading states, empty states, error states
- Component design: every state visible (hover, focus, active, disabled, loading, error)
- Animation: prefer subtle, purposeful animations; avoid gratuitous motion
- Invisible details: focus rings, scroll behavior, keyboard shortcuts, accessibility

### enhance-prompt
- Add UI/UX keywords (glassmorphism, minimalism, bento grid, etc.)
- Inject design system context from project DESIGN.md
- Structure output: layout, components, interactions, animations
- Adapt specificity: vague "dashboard" → "real-time analytics dashboard with KPI cards and charts"

### find-docs
- Resolve library ID via Context7 `resolve-library-id`
- Query with full user question, not keywords; use `researchMode: true` as retry
- Prefer Context7 over web search for library documentation
- Always verify API signatures, config options, and version-specific behavior against current docs

### frontend-design
- Produce distinctive, non-generic AI aesthetics; avoid cookie-cutter designs
- Use creative layouts, intentional whitespace, strong typography hierarchy
- Mobile-first responsive design; test across breakpoints
- Prefer CSS Grid + Flexbox over framework-specific layout hacks

### git-session-finalize
- MUST check git status before staging; review Engram memory for context
- MUST NOT commit secrets, credentials, or .env files
- MUST NOT force push to main branch
- MUST verify push success before completing
- Commit message: concise first line (≤50 chars), imperative mood, active voice

### go-testing
- Prefer table-driven tests: `t.Run(tt.name, ...)` for multiple cases
- Test behavior and state transitions, not implementation trivia
- Use `t.TempDir()` for filesystem tests; skip integration tests with `testing.Short()`
- Golden files must be deterministic; update with `-update` flag, then rerun without
- Bubbletea: test `Model.Update()` directly; use `teatest` only for interactive flows

### issue-creation
- Blank issues disabled — MUST use Bug Report or Feature Request template
- Every issue auto-gets `status:needs-review` on creation
- Maintainer MUST add `status:approved` before any PR can be opened
- Questions go to Discussions, NOT issues
- Search existing issues for duplicates before creating

### judgment-day
- Launch TWO blind judges in parallel with identical target and criteria
- Wait for both judges before synthesis; never accept partial verdict
- Classify warnings: `WARNING (real)` only if normal use triggers it; else `WARNING (theoretical)`
- Ask before fixing Round 1 confirmed issues; re-launch both judges after fixes
- Terminal states: `JUDGMENT: APPROVED ✅` or `JUDGMENT: ESCALATED ⚠️`
- After 2 fix iterations with remaining issues, ask user whether to continue

### react:components
- Convert Stitch designs into modular Vite + React components
- Use system-level networking and AST-based validation
- Component architecture: container-presentational pattern
- Design tokens → CSS variables → component props

### remotion
- Generate walkthrough videos from Stitch projects using Remotion
- Smooth transitions, zooming effects, text overlays
- Composition-based rendering: `<Sequence>`, `<AbsoluteFill>`, `<spring>`
- Render with `npx remotion render`

### seo
- Technical SEO: robots.txt, meta robots, XML sitemap, canonical URLs
- Structured data: JSON-LD for rich snippets (Article, Product, FAQ, BreadcrumbList)
- On-page: title tags ≤60 chars, meta descriptions ≤160 chars, heading hierarchy
- Core Web Vitals: LCP ≤2.5s, FID ≤100ms, CLS ≤0.1
- Internal linking: descriptive anchor text, crawlable link structure

### shadcn/ui
- Use `npx shadcn-ui@latest add <component>` to install; components go to `@/components/ui/`
- Components built on Radix UI primitives with Tailwind styling
- Customize via CSS variables in `globals.css`; use `cn()` utility for conditional classes
- Dark mode: use `next-themes` provider with `dark:` Tailwind variants

### skill-creator
- Skills are runtime instruction contracts, NOT human documentation
- Required frontmatter: name, description (≤250 chars, trigger-first, single line)
- Required sections: Activation Contract, Hard Rules, Decision Gates, Execution Steps, Output Contract, References
- Target 180-450 body tokens; move examples/schemas/edge cases into `references/` or `assets/`
- Hard rules must be observable; decision gates cover real forks; output contract states what to return
- References must be local files, stable relative to the skill directory

### stitch-design
- Entry point: prompt enhancement → design system synthesis → screen generation
- Use Stitch MCP for high-fidelity screen generation and editing
- Design system: extract from existing screens, synthesize into DESIGN.md

### stitch-loop
- Autonomous baton-passing loop pattern for iterative website building
- Agent A generates design → Agent B implements → Agent C reviews → loop
- Each iteration: assess, plan, execute, verify

### ui-ux-pro-max
- 50+ styles (glassmorphism, brutalism, minimalism, bento grid, etc.), 161 color palettes
- 57 font pairings, 99 UX guidelines, 25 chart types across 10 stacks
- Color systems: primary, secondary, accent, neutral, semantic (success, warning, error)
- Accessibility: contrast ratios, focus indicators, aria attributes, keyboard navigation
- Animation: prefer CSS transforms and opacity for GPU-accelerated 60fps animations
- Responsive: mobile-first, 4 breakpoints (sm/md/lg/xl), fluid typography with `clamp()`

### work-unit-commits
- Commit by work unit, not by file type; each commit represents one deliverable behavior
- Keep tests with the code they verify; keep docs with the user-visible change
- Each commit: one clear purpose, repo makes sense after applying only this commit, rollback is reasonable
- Approaching 400 changed lines → promote commits into chained PRs
- SDD work units map cleanly: clear start, clear finish, verification, isolated rollback

## Project Conventions

No project-specific convention files found (no AGENTS.md, CLAUDE.md, .cursorrules, GEMINI.md, or copilot-instructions.md detected).
