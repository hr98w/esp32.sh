# Overnight collection work log

Local review only. No deployment, publishing, authenticated GitHub access, external writes, or computer-use.

## Goal window

Started 2026-10-15 17:17 UTC / 2026-10-16 01:17 Asia/Shanghai. The agreed upper bound is approximately five hours, ending 22:17 UTC / 06:17 local. Finish earlier if the full milestone and final audit pass.

## Checkpoint — 2026-10-15 18:07 UTC

This is an intermediate checkpoint, not a completion report.

- 49 device Markdown files, including verified primary-source links and English/Chinese/Japanese summaries. All 49 independent device URLs returned 200 in local Workers HTTP tests.
- 17 project Markdown files; 15 passed fresh upstream README, Star and open-source-license intake checks. The two original examples still need fresh intake verification. They are not counted as completed projects in the queue report.
- 220 repository candidates from M5Ware and awesome-esp32, with directory provenance. 298 ESPboards source entries, inventoried across 74 manufacturer directories; discovery includes entries that are not ready for publication.
- 20 additional device records staged in `reviewed-devices-supplement.json`, not yet imported as public Markdown. These can be considered after project and UI milestones converge.
- OpenEPaperLink excluded after its README declared CC BY-NC-SA 4.0. Unknown licenses remain in review. No Star values or compatible device IDs were invented.
- Meshtastic hardware documentation reviewed for T-Beam Supreme, T3 S3 and T-Watch S3; source links are recorded on the project relations. Other similarly named devices remain unlinked.

## Implemented and checked so far

- Default English root without locale prefix or default filter parameters; Chinese and Japanese paths; legacy English redirects preserve query parameters.
- Project keyword/tag/device filtering, Star/name/date sorting, searchable manufacturer-grouped sidebar, and collapsed mobile device selector.
- Device catalog search and manufacturer/chip/peripheral filters; standalone device pages and reverse project lookup.
- Source/provenance display, dated Star snapshots, archived flags, and translated listing/contribution explanations. The contribution explanation states that the public source repository is not yet announced.
- Cached README image discovery, manual-image priority and opt-out, name fallback on image failure. A hydration timing issue and a mobile CSS issue were found by browser checks and fixed.
- Local HTTP checks passed for 3 languages, filtering, redirect, 404s and all 49 device URLs. An isolated headless Chrome checked hydrated tag filtering, mobile toggle, layout overflow and blocked-image fallback; no page exceptions. External image URLs were blocked for this check, so image reachability was not certified.
- Six content regression tests and eight anonymous-collection/source-selection tests pass. Type checks and Cloudflare builds passed at checkpoints; a final build and browser/HTTP run remain necessary after the full dataset and latest route metadata changes.

## Current API wait

GitHub anonymous REST quota is exhausted until approximately 2026-10-15 18:20:19 UTC / 02:20:19 local. `resume_projects.py` waits for the recorded server reset and then continues verification. It never reads credentials and never rotates identity or IP. Raw static GitHub retrieval was tried once and failed at transport level; no alternate identities or mirrors were used.

The collector target is 68 verified repositories to allow some editorial exclusions before publishing at least 60 useful projects. Verification is separate from editorial summaries and exact hardware mapping.

## Remaining completion gates

1. Verify enough candidate projects; review their actual READMEs before writing summaries and device relations.
2. Publish at least 60 quality project records with matching Star snapshots and three-language summaries. Recheck both seed projects.
3. Integrate source-backed model relations without inferring compatibility from chip names.
4. Rebuild queue, metrics and cover snapshots; ensure queue included IDs equal the generated public catalog without double counting.
5. Run content/collection tests, type checks, production build, full HTTP checks and hydrated browser checks against the final dataset. Run `python3 scripts/audit-collection.py` successfully.
6. Only after those converge, import selected staged devices or expand projects if useful. Record final counts, remaining review reasons and coverage limits.

`audit-collection.py` currently fails as expected because the project milestone and both original examples are incomplete. Do not mark the goal complete based on intermediate test passes.

## Checkpoint — 2026-10-15 18:15 UTC

- Latest production build, HTTP checks and hydrated browser checks pass with 17 project records and 49 device records. Language switching preserves filters, mobile chooser toggles, blocked covers fall back to names, and localized canonical/hreflang links are present. Final dataset still needs a final run.
- Nine collection/source-selection tests now pass. Source pages without manufacturer assignments are retained as `unknown` rather than rejected or assigned a brand from their titles. Seven such source records remain in review.
- The manufacturer report now separates baseline ESPboards coverage from additional included devices, and links a full device-by-device queue. Twenty-three supplemental records are staged, still unpublished.

## Checkpoint — 2026-10-15 18:43 UTC

- 33 projects now have reviewed three-language summaries, explicit open-source licenses, dated successful Star snapshots, and README provenance. There are 57 documented project/device relations across 25 devices. The milestone audit now fails only the project-count requirement (33 < 60).
- Four source-verified repositories were excluded after editorial review: a Raspberry Pi project, an awesome directory (retained as a discovery source), a Flipper payload collection without confirmed ESP32 support, and a general CAD repository. Two more remain in review for implementation clarity or contradictory license claims. These are not counted toward 60.
- Discovery now includes the cached Awesome M5Stack Cardputer directory: 253 raw repository candidates. Canonical repository aliases merge their source URLs in reports and do not count as distinct public projects.
- A T5 V2.3 touch claim was corrected: the manufacturer sells Basic and Touch options, so the generic record no longer claims a touchscreen. A T7 V1.4 entry stays in review because its vendor link now describes V1.5 with changed GPIO mapping. The legacy T5 entry also stays in review because the linked current wiki describes an ESP32-S3 successor.
- 31 supplementary devices are staged, schema-valid and unpublished. These include the full StackChan robot, distinct from a bare CoreS3, and verified LILYGO screen/modem variants.
- Latest checks pass: 8 content/search tests, 10 collection/source/queue tests, TypeScript, production build, HTTP checks for all 49 device URLs and search/filter routes, and hydrated browser checks with 33 cards. The browser checks now exercise common M5 search spellings, mobile selection/collapse, exact device filtering, Star sort, language preservation, and failed-cover fallback. No page exceptions.
- The API collector remains live and waits for the recorded reset at 2026-10-15 19:20:21 UTC / 03:20:21 local. It will continue toward enough source-verified projects; editorial acceptance remains separate from source verification.

## Checkpoint — 2026-10-15 19:12 UTC

- 34 projects are included. Evil-M5Project was accepted after its full MIT permission notice was inspected in the cached README, despite GitHub not detecting a standalone license. `verifiedLicense` and dated `licenseReview` preserve that source without altering original API metadata.
- 55 supplemental devices are staged and schema-validated. Adafruit and DFRobot coverage has been reviewed against manufacturer guides. Ai-Thinker ESP32-CAM and NodeMCU-32S were checked against vendor documentation explicitly naming the brand; one legacy C3 board remains unconfirmed after its manufacturer URLs returned navigation instead of board specifications. No PDF specifications were inferred from a `.pdf` URL that returned HTML.
- 8 content/search tests and 14 collection/metrics/source/queue tests pass. The metrics tests cover failed-update preservation, repository identity changes, legitimate zero counts, and continued offline processing after a cache miss. Unchanged reviewed records are no longer rewritten on re-import.
- Source coverage is now broken down by discovery directory, and the device report exposes the number of prepared-but-unpublished records separately from included counts.
- The main collector and a separate four-file LICENSE evidence collector wait for the same 19:20:21 UTC reset. Both use the shared host lock, pacing and rate state. License evidence will be reviewed before any intake decision. No alternate identity, IP rotation or authenticated GitHub access is used.

## Checkpoint — 2026-10-15 19:24 UTC

- 53 source-reviewed projects and 51 devices are now included. Seventeen new project records were reviewed from the third anonymous API window; two additional README license declarations brought the total to 53. M5Paper and the complete official StackChan robot were imported early because the new projects explicitly require those exact models. Another 53 staged device records remain unpublished.
- Actual LICENSE evidence resolves NEMO as a choice of GPL-2 or GPL-3. RTSP camera firmware is recorded as GPL-3.0 from its actual LICENSE, with the inconsistent static MIT README badge preserved in the review basis. AWTRIX 3 is excluded for its explicit CC BY-NC-SA noncommercial license. Infiltra remains in review because its README claims MIT while GitHub detects GPL-2.0. ESP32Marauder's license endpoint returned 404; no open-source license was invented.
- New profiles include ClawPuter, MeshCore Cardputer ADV, Plai, an e-paper Home Assistant remote, UIFlow MicroPython, Pngle, an oscilloscope, and others. Device links exclude planned support and distinguish external LoRa/C5 hardware in concise summaries.
- README license review also confirms M5PaperWeather's GPL-3.0 declaration and stackchan-mcp's explicitly described MIT default and GPL-3.0 optional servo sources. Manual decisions retain dated upstream provenance without altering raw API metadata.
- All 8 content/search and 14 collection/source/metrics tests pass; content generation and TypeScript pass. The milestone audit fails only the remaining project count (53 < 60). Final build/HTTP/browser checks remain required against the final dataset.
- The collector is live and waits until 2026-10-15 20:20:23 UTC / 04:20:23 local. Its next batch prioritizes non-M5 projects already found in awesome-esp32 to improve variety. Respecting the shared anonymous API quota; no authenticated or alternate-identity requests.

- 19:27 UTC: Production build, HTTP checks for all 51 device pages, and hydrated browser checks now pass for the 53-project dataset (8 AI-filter matches, no page exceptions). Desktop/mobile screenshots were inspected; failed covers use the name fallback, no mobile overflow was detected. Only owned preview/headless-browser processes were stopped afterward; the anonymous collector remains running. Final dataset requires another build and route check after expansion.

## Checkpoint — 2026-10-15 19:42 UTC

- 53 projects and 51 devices remain public. Device expansion now has 91 reviewed supplemental records, of which 2 are already public; importing the remaining 89 after the project gate would yield 140 devices.
- Added source-reviewed coverage for all 6 Olimex and all 7 SparkFun models in the checked ESPboards manufacturer baseline, 6 current WEMOS/LOLIN models, 8 Elecrow models, 7 explicit Heltec revisions, and ProS3/Reflow Master Pro. Summaries are original English/Chinese/Japanese text, with no inferred capacity or peripheral features.
- SparkFun intake exposed a real parser omission: Hookup Guide and product-page links were not recognized as primary sources. The collector now recognizes guides, prioritizes documentation over product pages and PDFs, and has a regression test. All 15 collection tests pass.
- Official Olimex category links replace third-party/reseller defaults. Elecrow P4's affiliate redirect is replaced with its directly observed canonical manufacturer URL. ThinkNode M2's misleading old URL slug is not used to infer its processor; the current manufacturer body explicitly documents ESP32-S3. A generic Elecrow Wiki homepage remains insufficient for the miner model.
- Heltec V2/V3/V4 and LoRa chips remain distinct; a GNSS connector is not labeled built-in GNSS. Wireless Shell is a castellated module, not a USB development board. The V2 phaseout is noted from the manufacturer. SparkFun's single-channel LoRa gateway summary retains the official TTN v3 incompatibility note.
- Legacy Unexpected Maker product URLs returning the generic Series[D] homepage stay in review. A dedicated FeatherS3 site failed TLS verification; TLS was not disabled. The original ProS3 and Reflow Master Pro have readable dedicated source facts and are staged separately from newer hardware.
- 25 additional exact-model project relations were reviewed and recorded with source dates and reasons in reviewed-device-relations.json. The curator adds them only when the corresponding device MD exists. Four existing project records gained currently available model relations; deferred relations will activate after the staged import. No same-chip substitution is used.
- The anonymous GitHub collector remains live and waiting until 20:20:23 UTC / 04:20:23 local, with 53 verified projects. The project target and final full-dataset checks are still outstanding.

- 19:45 UTC: Supplemental schema/ID validation confirms 89 unpublished records and an expected combined total of 140 devices across 14 manufacturers. An additional Meshtastic/T-Deck Plus relation was confirmed against both manufacturer SX1262 specifications and the project hardware guide; the original optional-radio T-Deck remains unassociated. The Plus device gained its source-backed LoRa feature. There are now 26 reviewed supplementary relations.

## Final local review — 2026-10-15 23:26 UTC / 2026-10-16 07:26 Shanghai

The original 40-device / 60-project milestone is complete. The task exceeded the planned five-hour window; no further online collection is being performed. The collector reached its verification target and exited. Network rate limits and subsequent transport failures are recorded rather than hidden or treated as editorial exclusions.

### Delivered evidence

- **67 projects**, **140 devices**, **14 manufacturers**, **131 documented project/device relations across 44 devices**. The other devices can have empty related-project lists; the catalog does not imply every device already has a matching project.
- Exactly 67 independent project Markdown files and 140 independent device Markdown files. Devices are in manufacturer folders; projects use stable flat IDs and multiple tags. All have original English/Chinese/Japanese summaries and provenance. Missing or ambiguous hardware relations remain pending.
- All 67 public projects have verified README evidence, explicit open-source license declarations, stable GitHub identities, and successful dated Star snapshots of at least 10. Metrics are separate from authored Markdown. Manual license resolutions retain the original API metadata and their actual source. ReadPaper is listed for its open-source firmware/repository contents, with the upstream separate closed-source browser extension scope noted in its MD.
- Imported the prepared expansion only after the project milestone passed. The final report has no remaining staged records. Adafruit, DFRobot, Olimex, SparkFun, Seeed Studio, and the checked M5Stack baseline are fully covered relative to the inspected ESPboards directory, with additional M5Stack devices from other sources. This is not a claim of ecosystem-wide completeness.
- Queue counts match the public catalog without duplicate canonical repositories. Remaining project intake: 22 needs-review, 57 pending, 31 excluded, 76 discovered. Remaining device intake: 54 needs-review, 30 pending, 86 discovered. Each retains source and reason where processed.
- Public transport errors are resumable pending work. The collector now stops a batch on DNS/connection failures rather than fanning failures across unrelated repositories; a mocked regression test verifies this behavior. No network retry, authentication, alternate identity, IP rotation, mirror, or TLS bypass was used to manufacture missing evidence.

### Final checks

- `pnpm check`: passed content validation, route generation, and TypeScript.
- `pnpm test:content`: **8 passed**.
- `pnpm test:collection`: **16 passed**.
- `WRANGLER_LOG_PATH=.wrangler/logs pnpm build`: passed Cloudflare client and Worker production build. Existing circular-dependency and CSS-sourcemap warnings do not prevent the build.
- `python3 scripts/audit-collection.py`: passed 67 projects / 140 devices, Markdown identity, three languages, sources, README/license/Star evidence and report equality.
- `python3 scripts/check-http.py`: passed all 140 device URLs, three languages, English root/default query behavior, device/tag/filter routes, 301 redirects and 404s.
- `node scripts/check-browser.mjs`: passed hydrated 67-card rendering, Star ordering, tag filtering, locale preservation, mobile chooser search/select/collapse, no horizontal overflow, failed-cover fallback, 140-device rendering, Adafruit manufacturer filtering, and client navigation to the newly linked Feather ESP32-S2 detail. **No page exceptions**.
- Final desktop/mobile screenshots were visually inspected. External GitHub image requests were deliberately blocked in the browser check to verify name-cover fallback; this does not certify every remote image's availability.
- The user's existing `http://localhost:3000/` returned HTTP 200 with all 67 project cards after the changes. Only the owned production preview and isolated headless Chrome used for checking are shut down; the existing development server is preserved.

### Boundaries

No deployment, publication, remote Git write, GitHub issue/PR, message to authors, personal credential use, or hardware testing. No database, account, payment, favorites, collections, AI auto-merge, or authenticated scheduled automation was added. Project cards still open upstream GitHub; independent project pages remain future work. Automatic covers are optional heuristic README candidates with name fallback. Unverified prices and inventory are not filled in.

For continuation, use `README.md`, the generated `collection-progress.md`, `device-intake-queue.md`, and `data/collection/queue.json`. Only restart anonymous online collection explicitly when needed; offline commands use cached successful responses.

## 2026-10-16 follow-up: device details and 100 projects

This is a separate local content-enrichment goal, started at 00:02:36 UTC with a two-hour maximum. See [the detailed review report](2026-10-16-content-expansion-review.md) for current evidence and exceptions.

- Expanded 67 to 100 projects. All listed records have dated Star snapshots >= 10, verified README/license evidence, and three-language summaries.
- Kept 140 devices across 14 manufacturers; 120 now have reviewed externally hosted manufacturer photos, 138 have key hardware specifications, and all 140 have resource links. All 35 integrated devices have those three elements.
- Reviewed classifications and 164 project/device relations. Partial StackChan support was removed from chat-stick; documented StopWatch support was added. Unconfirmed exact-model relations were not inferred from chip family.
- Added per-device enrichment coverage and pending reasons, plus source/context/image review ledgers and repeatable offline reports.
- Passed content/type checking, 9 content tests, 19 collection tests, production build, the 100-project/140-device milestone audit, and HTTP checks for all 420 device/language pages, related-project order, and external device image URLs.
- Existing build warnings remain documented. HTTP verification does not prove browser hydration or hardware operation.

Unlike the historical check above, this follow-up did not use computer-use, browser automation, or screenshots of the website. Local contact sheets of downloaded public product photos were used only for image-source QA. No deployment, publication, personal credentials, gh, or R2 configuration was used. The next GitHub reset was beyond this goal's deadline, so its waiter was stopped after reaching 100 listed projects; evidence and pending queues remain available.
