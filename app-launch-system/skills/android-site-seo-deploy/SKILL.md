---
name: android-site-seo-deploy
description: Validate the generated static website and prepare its public file set for SEO and static hosting. Use after website generation when the user explicitly asks for deployment preparation or search verification.
---

# Validate And Prepare A Static Site

Use this skill only after the website generator has produced a root-level static site.

## Workflow

1. Run `python app-launch-system/scripts/launch.py validate-output .` from the project root.
2. Read `static-site-manifest.json` and treat it as the only deployable file list.
3. Keep `app-launch-system/`, `app-info.yaml`, `analysis-evidence.json`, `content/`, `aso/`, `seo-geo/`, and `launch-readiness.yaml` out of the public upload.
4. Confirm `websiteUrl`, canonical URLs, sitemap URLs, and search verification values before publication.
5. Do not deploy or modify Cloudflare, DNS, Search Console, or other external services without an explicit user request.

## Prelaunch Sites

For `releaseStage: prelaunch`, treat the site as a product preview. It may use SEO preparation, but must not claim an available Android download or generate Google Play listing assets.

## Handoff

Report the validation result, the public manifest path, excluded internal paths, and any missing domain or verification values.
