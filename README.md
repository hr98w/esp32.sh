# esp32.sh

**English** | [简体中文](README.zh-CN.md)

Find open-source projects for your ESP32 device at **[esp32.sh](https://esp32.sh/)**.

Browse projects, devices, useful tools, and beginner recommendations. Available in English, Chinese, and Japanese. Built with TanStack Start, React, and Cloudflare Workers; content lives in Markdown, with no database required.

## Development

Requires Node.js 22.12+, pnpm 10, Python 3.10+, and curl.

```sh
pnpm install --frozen-lockfile
pnpm dev                     # http://localhost:3000
pnpm verify                  # Content, types, tests, production build
```

For production HTTP checks, run `pnpm preview --port 4317` and `pnpm check:http` in separate terminals.

## Contributing

Add one Markdown file per entry using the [templates](templates/):

| Content | Directory |
| --- | --- |
| Projects | `content/projects/` |
| Devices | `content/devices/<manufacturer.id>/` |
| Tools | `content/tools/` |
| Beginner recommendations | `content/guides/picks/` |
| X embeds | `content/guides/posts/` |

Write descriptions in English, Chinese, and Japanese. Projects need a README, an explicit open-source license, and at least 10 stars at intake. Device support needs explicit upstream evidence; matching chips alone are insufficient. Covers are optional.

Run `pnpm check`, then open a pull request to [hr98w/esp32.sh](https://github.com/hr98w/esp32.sh). See the [content guide](content/README.md) and [contribution guidelines](CONTRIBUTING.md) for fields and review rules.

## Deployment

Cloudflare Workers Builds deploys `main` after `pnpm verify` passes. See the [deployment guide](docs/operations/deployment.md) for Git integration and manual deployment.

```sh
pnpm exec cf auth login      # When authentication is needed
pnpm verify
pnpm deploy:check            # Dry run
pnpm deploy:built
pnpm check:deployment
```

Configuration: [cloudflare.config.ts](cloudflare.config.ts). Full workflow: [deployment guide](docs/operations/deployment.md).

## Documentation

- [Maintenance](docs/operations/maintenance.md) · [Collection tools](scripts/README.md) · [Collection progress](docs/research/collection-progress.md)
- [Project intake skill](skills/esp32-project-intake/SKILL.md) · [Documentation index](docs/README.md)
