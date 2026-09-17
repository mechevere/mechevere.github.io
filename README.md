# Mateo Echeverri — personal site

Astro site with M PLUS 1p, white, near-black, and #960601. Fonts are bundled locally.

## Local development

Use Node 24. Run `npm ci`, then `npm run dev`. Validate with `npm run check` and build with `npm run build`.

## Publishing

The deployment workflow `.github/workflows/deploy.yml` builds and publishes to GitHub Pages on every push to `master`, or when manually run from Actions. In repository Settings → Pages, choose GitHub Actions as the source. The site URL is https://mechevere.github.io/.

## Content

Learnings are Markdown files in `src/content/writing/`. Use title, description (for metadata and RSS), date, tags, and draft. Set `draft: true` to exclude an article and its tags from production. The current generic placeholder articles are published to demonstrate the layout; replace them with your writing.

Tags are lowercase words/numbers separated by hyphens. Each tag has a static page at `/learnings/tags/<tag>/`. Lists display only titles and tags. The Reading List is populated via `src/data/reading-list.ts`.

About contains placeholder bio text and a subtle Impressum link. The Impressum uses the owner-provided name and address. Public contact details and any further legal notices should be reviewed as the site scope evolves.

## Offline review

Run `INCLUDE_DRAFTS=true npm run build`, then `python3 scripts/export-preview.py /absolute/path/preview.html`. This bundles pages and fonts into one offline HTML file. Run a normal production build before deploying; the workflow does this automatically.
