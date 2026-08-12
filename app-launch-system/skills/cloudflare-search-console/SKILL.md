---
name: cloudflare-search-console
description: Configure an existing production website on Cloudflare Pages for Google Search Console, Bing Webmaster Tools, and IndexNow. Use when the website already exists and the task is limited to Pages deployment settings, live HTTP checks, search-engine verification, robots.txt, sitemap submission, canonical readiness, or indexing follow-up. Do not use this skill to design or generate the website itself.
---

# Cloudflare Search Console and Bing Webmaster

Connect an already-produced website to Google Search Console and Bing Webmaster Tools from deployment to indexing readiness. Treat the website files as an existing product. Do not redesign pages, rewrite product copy, analyze the Android source, or invent verification data.

## Usage

Use this Skill when the website already exists and the request is about connecting or checking Cloudflare Pages with Google Search Console, Bing Webmaster Tools, or IndexNow:

```text
Use $cloudflare-search-console to connect my existing Cloudflare Pages site to Google Search Console and Bing Webmaster Tools.
Site root: C:\work\AI\sitereportapp
Live URL: https://site.pages.dev/
```

For HTML-file verification, provide Google's exact values:

```text
Filename: google1234567890abcdef.html
Body: google-site-verification: google1234567890abcdef.html
```

For Bing file verification, preserve the exact `BingSiteAuth.xml` content supplied by Bing:

```text
Filename: BingSiteAuth.xml
Body: <?xml version="1.0"?> ...
```

For this project, the normal local checks are:

```powershell
python app-launch-system/scripts/launch.py validate-app-info app-info.yaml
python app-launch-system/scripts/launch.py generate-website --force
python app-launch-system/scripts/launch.py validate-output .
```

After local validation, authorize the Git push or direct Cloudflare deployment separately. Then check the exact live verification URLs, verify Google and Bing properties, submit `sitemap.xml` to both services, and inspect the homepage. If an IndexNow key is configured, submit the homepage and changed public URLs through IndexNow after deployment.

## Workflow

1. Identify the website root, Cloudflare Pages project, production branch, build command, output directory, and public URL. Preserve unrelated user changes.
2. Inspect the existing deployment contract. If the repository has `static-site-manifest.json`, deploy only its listed public files. Never upload Android source, `app-info.yaml`, analysis evidence, locale sources, internal reports, or Skill files.
3. Confirm the public URL exactly. For `https://name.pages.dev/`, use a Google Search Console **URL-prefix property** with the trailing slash and add the matching site in Bing Webmaster Tools. Use a Domain property only when the user controls that domain's DNS zone.
4. Choose each service's verification method: Google HTML tag/file/DNS, or Bing `msvalidate.01`/`BingSiteAuth.xml`. Preserve exact supplied values. Never derive or fabricate a token, filename, or file body.
5. Handle Cloudflare Pages Clean URLs. Official Google `.html` and Bing `.xml` verification files must return `200` at their exact URLs without redirecting. If Pages redirects them, use the supported `_worker.js` handler described in [references/cloudflare-pages.md](references/cloudflare-pages.md).
6. Regenerate or stage deployment output using the existing project command. Confirm `robots.txt` allows crawling and points to the correct absolute sitemap URL, and that `sitemap.xml` contains real URLs.
7. Validate locally: exact verification body, no unresolved tokens, manifest inclusion, no private files, canonical URL, sitemap URL, and local links. Run the project's existing tests and output validators.
8. Deploy only when explicitly authorized. For Git-connected Pages, commit generated public changes and push the configured production branch. For direct Wrangler deployment, confirm `npx wrangler whoami` and deploy only a clean public output directory.
9. Verify the live deployment over HTTP. Check status, redirects, body, content type, robots, sitemap, homepage canonical, and the verification URL. A browser showing a fallback page is not proof that the official verification URL works.
10. Complete the provider workflows manually: verify Google, verify Bing, submit `sitemap.xml` in both webmaster consoles, inspect the homepage and key pages, then use IndexNow for changed URLs when configured. Provider reports may lag behind deployment.

## Scope Boundaries

- Existing website work is out of scope. Do not modify layout, copy, screenshots, routes, ASO, or Android code unless explicitly requested.
- Cloudflare authentication, Git push, Pages settings, DNS, Webmaster console clicks, and IndexNow submissions are external actions. Ask for authorization or provide the exact next action.
- `pages.dev` does not require a custom domain for URL-prefix verification.
- `google-site-verification=TOKEN` is a DNS record value, not HTML file content.
- `BingSiteAuth.xml` is a public root verification file; its XML body must remain byte-for-byte equivalent after whitespace normalization.
- IndexNow keys are public discovery credentials, not ranking signals. The key file must be served from the site root and contain the exact key.
- A file that returns `200` only after a redirect is not verification-ready.

## Completion Criteria

- Cloudflare production deployment contains the intended commit/output.
- `https://site/`, `robots.txt`, and `sitemap.xml` return `200`.
- The exact Google verification URL/tag and Bing verification URL/tag pass their respective checks.
- Search Console and Bing Webmaster property types match the verification methods.
- The remaining manual Search Console action is clearly stated.

## Handoff

Return the live URL, provider property types, verification methods, deployment status, HTTP check results, sitemap path, IndexNow status, and one next manual action. Distinguish local configuration, deployed configuration, and provider-processed data; indexing reports may take hours or days.
