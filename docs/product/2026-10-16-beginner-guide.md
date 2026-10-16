# Start Here / 新手指南

Local implementation; no deployment or hardware validation in this change.

## Page structure

`/guides`, `/zh/guides`, `/ja/guides`. The page starts with four project-led recommendations: XiaoZhi voice companion, Cardputer-ADV official demo, DevKitC I/O and Wi-Fi learning, and the complete StackChan robot. Every recommended device links to its internal detail page. Budget labels are relative; original-post prices are not current retail quotes. Wokwi is an optional browser-first entry via Tools.

Ten supplied X posts follow in a single feed, ordered by their `order` field (initially 1–10). Desktop uses three columns, tablet two, and mobile one. Original posts stay in their original language. No separate credit block or full-text republication. Post 7 is explicitly advanced; Muse needs a working app/account, a token and a local build, so it is not presented as a beginner flash-and-go recommendation.

## Independent Markdown records

- `content/guides/posts/*.md`: one embed per file. `id`, localized `title`, canonical X/Twitter `url`, `order`. Filename equals ID.
- `content/guides/picks/*.md`: one recommendation per file. Three-language title/summary/effort, relative `budget` (`low`, `medium`, `high`), `deviceIds`, `projectIds`, an official `resource` link, source URLs, order.
- Both build to ignored `src/generated/guides.json`. Workers never read Markdown at runtime.
- Delete an individual post Markdown file to remove its embed. Picks do not depend on post IDs and survive deletion. Their source URLs remain provenance, even when the corresponding embed is not displayed.
- Delete a pick separately to remove its recommendation. Unknown device/project references fail validation before generated files are written. No database, login or paid API is needed.

Run `pnpm verify`, start `pnpm preview --port 4317`, then run `pnpm check:http`. Original files on the Desktop are research input, not a build dependency. No full tweet text or account credentials are copied into the repository.

## Editorial boundaries

- Lichuang Shizhanpai S3 was missing and is added from the official hardware overview and official XiaoZhi tutorial. That tutorial explicitly documents the device/project relation; the tutorial includes older firmware instructions, so follow current upstream releases rather than pinning that old version in our recommendation.
- Use exact model support. Do not infer Cardputer-ADV support from original Cardputer support, or equate a complete StackChan robot with a bare CoreS3.
- StackChan's factory functionality and community `stack-chan/stack-chan` are separate. The official factory guide is the first action; the community repository is follow-up exploration.
- The DevKitC LED exercise needs an external LED, resistor and wiring; no universal onboard programmable LED or GPIO number is promised.
- MaixCAM2 is not ESP32 and is not recommended as an ESP32 device. Shared-chip assumptions and outdated star/price figures in the posts are not imported as catalog facts.
- Other ideas (WLED, ESPHome, Xteink readers, Muse and custom firmware) remain discoverable in the original posts. They are not all labeled equally easy or mapped to unverified devices.

## Embeds and verification

`XPostEmbed` loads the official `platform.twitter.com/widgets.js` once, when an embed approaches the viewport, and uses `widgets.createTweet`. The original link is server-rendered and remains available if X is blocked, a post is deleted, or the widget fails. Embeds load third-party content from X; no local image proxy is introduced. Three-language UI does not translate original posts.

Content tests cover invalid URLs, duplicate tweet IDs, unknown device references, preservation of generated files on validation failure, and deleting a post independently from recommendations. Local HTTP checks verify all ten source links and translated titles, internal device links, canonical URLs and redirects. These checks do not prove X iframe visual rendering or hardware functionality.

### Local validation result

`pnpm verify` passed (15 TypeScript content tests, 19 Python collection tests and production build). `pnpm check:http` passed all three localized guides and 423 localized device details. An anonymous request to `platform.twitter.com/widgets.js` timed out from this machine, so live X rendering remains unverified; the original-post fallback links are present in server-rendered HTML.
