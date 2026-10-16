# Derived data and collection ledger

Human-authored records live in `content/`; frequently changing or collection-specific data stays here.

- `repository-metrics.json`: project ID → canonical repository, stable GitHub ID, stars, successful collection time, `pushedAt`, archived status, and API source URL. `pushedAt` is GitHub's repository push time, not necessarily the latest code commit. Failed updates preserve the last successful snapshot.
- `repository-covers.json`: optional image candidates discovered from cached upstream READMEs. Includes repository identity, source URL, and README collection time. Discovery does not prove the image is reachable or grant redistribution rights. Manual covers take precedence; failed images fall back to names.
- `collection/project-candidates.json`: repositories discovered from existing directories, with source links.
- `collection/repository-evidence.json`: README, license and Star verification results. `verified` means upstream intake checks passed, not that editorial review or device testing is complete.
- `collection/license-file-evidence.json`: actual LICENSE-file retrieval evidence for manual resolution of unknown or contradictory metadata; collection alone does not approve a license. Explicit README grants are recorded as `verifiedLicense` plus a dated `licenseReview` while retaining the original API metadata.
- `collection/device-candidates.json`: ESPboards device inventory and official-source checks.
- `collection/manufacturer-inventory.json`: per-manufacturer source inventory; counts cover inspected directories only.
- `collection/reviewed-*.json`: editorial records ready to import as independent Markdown files.
- `collection/project-editorial-review.json`: summary and hardware-mapping review notes.
- `collection/reviewed-device-relations.json`: additional exact-model associations with source dates and review reasons. The curator activates each association only after that device has its own Markdown file; it does not infer compatibility from a shared chip.
- `collection/queue.json`, `progress.json`: generated intake state, including reasons for review/exclusion and manufacturer coverage.
- `collection/device-enrichment-evidence.json`, `m5stack-localized-evidence.json`: extracted manufacturer facts and image candidates; extraction is not editorial approval.
- `collection/device-detail-review.json`: reviewed field-update plan. Reapplying it can overwrite the same fields in Markdown; reconcile later manual corrections before another import.
- `collection/device-image-review.json`: exact-model image selections, raster checks, visual review, replacements and rejected-image reasons. Only verified images are eligible for application to MD.
- `collection/device-gallery-review.json`: checks for supplementary gallery assets beyond the cover.
- `collection/device-enrichment-queue.json`: generated coverage and pending reasons for every listed device.
- `collection/device-relation-audit.json`: generated model-name clues, not a hardware-test result.
- `collection/device-compatibility-review.json`: manual context decisions for ambiguous or partial model support.

Manufacturer-specific `*-source-review.json`, `*-image-evidence.json`, seed records, and individual primary-source extracts preserve earlier review evidence. Some are referenced by collectors and reports; do not delete or rename them solely because they look temporary. The authoritative published editorial content remains the Markdown in `content/`; reviewed JSON files are import plans/snapshots, not a second content database.

Raw response bodies and request cooldowns are local-only under `.cache/collection/`. Do not commit credentials, cookies, or personal authentication information. The collectors never discover or read credentials.

Run `pnpm collect:report` for the current human-readable report at `docs/research/collection-progress.md`. No collector deploys or writes to an external application.

Run `pnpm collect:report:all` to also regenerate the catalog, device-enrichment coverage and relation-review clues without online collection. Commands and overwrite boundaries are documented in [the script index](../scripts/README.md).
