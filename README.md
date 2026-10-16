# esp32.sh

**English** | [简体中文](README.zh-CN.md)

Find open-source projects for the ESP32 device you own.

An open-source project and device directory for ESP32: [esp32.sh](https://esp32.sh/). English is served at `/`, Chinese at `/zh`, and Japanese at `/ja`. Each project and device lives in its own Markdown file. Devices are organized by manufacturer; projects can be filtered by tags. Built with TanStack Start, React, and Cloudflare Workers, with deployments managed through `cf`.

## Development and checks

Requires Node.js 22.12+, pnpm 10, Python 3.10+, and curl. Python tools use only the standard library.

```sh
pnpm install --frozen-lockfile
pnpm dev                 # http://localhost:3000/
pnpm verify              # Content, types, tests, and production build; no collection or deployment
```

To check the local production build, run these commands in separate terminals:

```sh
pnpm preview --port 4317
pnpm check:http          # Full device-page and filter checks against localhost:4317
```

## Contributing projects and devices

Each entry is a separate Markdown file. You can add content without changing application code or setting up a database. Start by checking existing entries to avoid duplicate GitHub repositories or device models.

After cloning the repository (or your fork once the public repository is available), create a branch and install dependencies:

```sh
git switch -c content/add-entry
pnpm install --frozen-lockfile
```

### Add a project

Copy the [project template](templates/project.md) into the flat project directory:

```sh
cp templates/project.md content/projects/my-project.md
```

Edit the new file:

- Set a unique, stable lowercase `id` such as `my-project`, the upstream `name`, and the canonical `repository` URL (`https://github.com/owner/repository`). Keep one entry per repository, even if it supports several devices or tags.
- Confirm a readable README, an explicit open-source license, at least **10 GitHub stars** at intake, and an actual connection to ESP32. Record the real license in `license`; do not keep the template's MIT value without checking it.
- Write short, equivalent descriptions in `summary.en`, `summary.zh`, and `summary.ja`. Set `kind` to `firmware`, `application`, `library`, or `framework`; reuse existing `tags` where possible. Use the actual directory intake date for `addedAt` (`'YYYY-MM-DD'`), not the template date.
- Add upstream references to `sources`, for example `sources: [{ url: https://github.com/owner/repository#readme }]`. `checkedAt` is optional; when provided, use the actual ISO timestamp of verification.
- To link an existing device, add its internal `deviceId` and an upstream `sourceUrl` that explicitly supports that model, then set `compatibility: documented`. A matching chip alone is insufficient. If support is uncertain, keep `devices: []` and `compatibility: pending`; explicitly custom-built hardware uses `custom-hardware`.
- A `cover` is optional; omit it when unavailable. Prefer official or upstream HTTPS image URLs. Without a usable image, the project name is displayed.

Do not add Star counts to Markdown or edit generated files. Maintainers verify and update Star snapshots, intake evidence, and review ledgers. The [intake skill](skills/esp32-project-intake/SKILL.md) can also prepare a record from a GitHub link and a short description.

### Add a device

Copy the [device template](templates/device.md) into its manufacturer's folder:

```sh
mkdir -p content/devices/my-maker
cp templates/device.md content/devices/my-maker/my-maker-model.md
```

- Set a unique, stable device `id`, `name`, `manufacturer.id`, `manufacturer.name`, `chip`, and `type`. **The folder must match `manufacturer.id`**. Reuse an existing manufacturer folder when available; filename and ID should match for new entries.
- Choose the actual hardware form: `integrated-device` (an assembled device such as StopWatch), `functional-board` (a board built around peripherals), `general-board` (a general-purpose development board), or `module` (a module intended for integration). The chip is a separate field.
- Fill all three `summary` languages, `officialUrl`, and `sources` with manufacturer documentation. Unbranded products use manufacturer ID `generic`; unresolved manufacturers use `unknown`. A seller is not necessarily the manufacturer.
- `aliases`, `features`, an external `cover`, specifications, resource links, revision notes, and a sourced reference price are optional. Only include facts you can verify; distinguish product revisions and included accessories. See the [StopWatch record](content/devices/m5stack/m5stack-stopwatch.md) for a detailed example.
- Add project support to the relevant **project Markdown**, not the device file. Device pages find those relations automatically. If the device is new, include both files in the same contribution when linking it.

### Check and submit

```sh
pnpm check
```

This checks content fields, duplicate IDs/repositories, device references, and TypeScript; it does not prove license validity or hardware compatibility. No GitHub credentials or Cloudflare login are needed for this check. For content-only contributions, you do not need to deploy the site or run the collection scripts.

Review your diff, commit only the intended content changes, and open a pull request once the public repository is available. Include upstream links and any unresolved support or licensing questions. The repository URL has not been announced yet; content can currently be prepared and reviewed locally. Each accepted Markdown entry appears after the next website deployment.

See [the content field guide](content/README.md) and [contribution policies](CONTRIBUTING.md) for more detail. Do not submit credentials, caches, or generated build output.

## Deployment

```sh
pnpm exec cf auth login  # Sign in on the official page when needed
pnpm verify
pnpm deploy:check        # Check the latest build without uploading
pnpm deploy:built        # Deploy the build that was just verified
pnpm check:deployment    # Read-only HTTPS checks against the local catalog
```

For a shortcut, `pnpm deploy` rebuilds and deploys the application. Configuration lives in [cloudflare.config.ts](cloudflare.config.ts). See the [deployment guide](docs/operations/deployment.md) for the full workflow, domain maintenance, and recovery steps.

## Maintenance

| Task | Start here |
| --- | --- |
| Add a project from text or a GitHub link with Codex | [ESP32 project intake skill](skills/esp32-project-intake/SKILL.md) |
| Add or edit projects and devices | [Content guide](content/README.md), [templates](templates/), [contribution guidelines](CONTRIBUTING.md) |
| Understand the data flow, directory structure, and validation scope | [Maintenance guide](docs/operations/maintenance.md) |
| Expand the catalog, refresh stars, and update review queues | [Collection tools](scripts/README.md), [data ledger guide](data/README.md) |
| Check included and pending records | [Collection progress](docs/research/collection-progress.md), [device enrichment progress](docs/research/device-enrichment-progress.md) |
| Review product decisions, research, and deployment history | [Documentation index](docs/README.md) |
| Hand the project over to a coding agent | [AGENTS.md](AGENTS.md) |

## Content principles

- English and Chinese are equally important. The interface and summaries currently support English, Chinese, and Japanese.
- Projects need a README, an explicit open-source license, and at least 10 GitHub stars at intake. Unclear licenses remain under review.
- Device compatibility requires explicit upstream evidence. A matching chip does not establish model compatibility; this site does not claim hardware testing.
- Images preferably use official external URLs. Missing or failed images fall back to names. R2 image hosting is not configured.
- GitHub stars and README image candidates are stored as snapshots. Page visits do not request GitHub data.
- Project cards currently link directly to GitHub; devices have individual pages. The source repository and submission entry point have not been announced. There is no database, login, payments, favorites, or AI auto-merge.
