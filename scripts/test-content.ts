import { test } from 'node:test'
import assert from 'node:assert/strict'
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, readdirSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { parse, stringify } from 'yaml'
import { projectSubmissionLabel, projectSubmissionUrl, projectSubmissionTemplate } from '../src/lib/submissions.ts'
import { buildCatalog } from './content.ts'
import { matchesQuery, deviceSearchFields } from '../src/lib/search.ts'

const project = {id:'example', name:'Example', repository:'https://github.com/example/project',license:'MIT',kind:'firmware',summary:{zh:'测试',en:'Test',ja:'テスト'},devices:[{deviceId:'maker-board',sourceUrl:'https://github.com/example/project#readme'}],addedAt:'2026-10-16'}
const device = {type:'general-board' as const,id:'maker-board',name:'Board',manufacturer:{id:'maker',name:'Maker'},chip:'ESP32-S3',summary:{zh:'测试',en:'Test',ja:'テスト'},officialUrl:'https://example.com/board'}
const metrics = {repository:project.repository,githubId:123,stars:100,checkedAt:'2026-10-15T17:00:00Z',pushedAt:null,archived:false,sourceUrl:'https://api.github.com/repos/example/project'}
function fixture(run:(root:string)=>void){
  const root=mkdtempSync(join(tmpdir(),'esp32-content-test-'))
  mkdirSync(join(root,'content/projects'),{recursive:true});mkdirSync(join(root,'content/devices/maker'),{recursive:true});mkdirSync(join(root,'data'))
  md(root,'content/projects/example.md',project);md(root,'content/devices/maker/board.md',device)
  try{run(root)}finally{rmSync(root,{recursive:true,force:true})}
}
function md(root:string,path:string,value:unknown){writeFileSync(join(root,path),'---\n'+stringify(value)+'---\n')}
function data(root:string,path:string,value:unknown){writeFileSync(join(root,'data',path),JSON.stringify(value))}

test('unknown hardware and duplicate repository fail rather than publish ambiguous records',()=>fixture(root=>{
  md(root,'content/projects/example.md',{...project,devices:[{deviceId:'not-a-board',sourceUrl:project.repository}]})
  assert.throws(()=>buildCatalog(root),/unknown device/)
  md(root,'content/projects/example.md',project);md(root,'content/projects/duplicate.md',{...project,id:'duplicate'})
  assert.throws(()=>buildCatalog(root),/Duplicate repository/)
}))
test('device identity must match manufacturer directory and translations are mandatory',()=>fixture(root=>{
  md(root,'content/devices/maker/board.md',{...device,manufacturer:{id:'wrong',name:'Wrong'}})
  assert.throws(()=>buildCatalog(root),/manufacturer folder/)
  md(root,'content/devices/maker/board.md',device);md(root,'content/projects/example.md',{...project,summary:{en:'English only'}})
  assert.throws(()=>buildCatalog(root),/summary/)
}))
test('metrics attach without editing Markdown and cannot cross repository identities',()=>fixture(root=>{
  const before=readFileSync(join(root,'content/projects/example.md'),'utf8')
  data(root,'repository-metrics.json',{example:metrics})
  assert.equal(buildCatalog(root,true).projects[0].metrics?.stars,100)
  assert.equal(readFileSync(join(root,'content/projects/example.md'),'utf8'),before)
  data(root,'repository-metrics.json',{example:{...metrics,repository:'https://github.com/another/repo'}})
  assert.throws(()=>buildCatalog(root),/identity mismatch/)
}))
test('confirmed low stars exclude the public view, never delete authored content',()=>fixture(root=>{
  data(root,'repository-metrics.json',{example:{...metrics,stars:9}})
  assert.equal(buildCatalog(root).projects.length,0)
  assert.ok(readFileSync(join(root,'content/projects/example.md'),'utf8'))
  data(root,'repository-metrics.json',{example:{...metrics,stars:10}})
  assert.equal(buildCatalog(root).projects.length,1)
}))
test('manual image wins, opt-out works, automatic image does not mutate Markdown',()=>fixture(root=>{
  data(root,'repository-covers.json',{example:{repository:project.repository,url:'https://example.com/auto.png'}})
  assert.equal(buildCatalog(root).projects[0].cover,'https://example.com/auto.png')
  md(root,'content/projects/example.md',{...project,cover:'/images/manual.png'})
  assert.equal(buildCatalog(root).projects[0].cover,'/images/manual.png')
  md(root,'content/projects/example.md',{...project,autoCover:false})
  assert.equal(buildCatalog(root).projects[0].cover,undefined)
}))
test('failed generation retains the last valid catalog on disk',()=>fixture(root=>{
  buildCatalog(root,true)
  const target=join(root,'src/generated/catalog.json'),before=readFileSync(target,'utf8')
  md(root,'content/projects/example.md',{...project,repository:'http://insecure.example'})
  assert.throws(()=>buildCatalog(root,true))
  assert.equal(readFileSync(target,'utf8'),before)
}))

test('device search supports maker plus model, full-width text, and common M5 spelling',()=>{
  const board={...device,manufacturer:{id:'m5stack',name:'M5Stack'},name:'Cardputer ADV',aliases:[],features:[],sources:[]}
  const fields=deviceSearchFields(board)
  assert.ok(matchesQuery('M5Stack Cardputer',fields))
  assert.ok(matchesQuery('M5CardputerADV',fields))
  assert.ok(matchesQuery('ＥＳＰ３２－Ｓ３',fields))
  assert.equal(matchesQuery('ESP32 C6',fields),false)
  assert.equal(matchesQuery('Cardputer Seeed',fields),false)
})
test('keyword search matches across fields without inventing a word across boundaries',()=>{
  assert.ok(matchesQuery('Seeed XIAO',['Seeed Studio','XIAO ESP32S3']))
  assert.ok(matchesQuery('   ',['Any device']))
  assert.equal(matchesQuery('cores3',['core','s3']),false)
})

test('device type must be explicitly supplied and use a recognized hardware category',()=>fixture(root=>{
  const {type: _type, ...withoutType} = device
  md(root,'content/devices/maker/board.md',withoutType)
  assert.throws(()=>buildCatalog(root),/type/)
  md(root,'content/devices/maker/board.md',{...device,type:'ESP32-S3'})
  assert.throws(()=>buildCatalog(root),/type/)
}))

test('pagination traverses the complete sorted and filtered catalog without duplicates', async () => {
  const { paginate, PAGE_SIZE } = await import('../src/lib/pagination.ts')
  const { selectProjects, selectDevices } = await import('../src/lib/directory.ts')
  const catalog = buildCatalog(process.cwd(), true)
  const lists: { id: string }[][] = [selectProjects(catalog, { sort: 'stars' }), selectProjects(catalog, { sort: 'name', tag: 'tools' }), selectDevices(catalog, { maker: 'm5stack' })]
  for (const entries of lists) {
    const first = paginate(entries, 1)
    const visited = Array.from({ length: first.pageCount }, (_, i) => paginate(entries, i + 1).items).flat()
    assert.deepEqual(visited.map(p => p.id), entries.map(p => p.id))
    assert.equal(new Set(visited.map(p => p.id)).size, entries.length)
    assert.ok(first.items.length <= PAGE_SIZE)
    const last = paginate(entries, 999999)
    assert.equal(last.page, first.pageCount)
    assert.equal(last.end, entries.length)
  }
  const empty = paginate([], 50)
  assert.deepEqual([empty.page, empty.start, empty.end, empty.items.length], [1, 0, 0, 0])
})

test('untrusted page values are normalized and navigation stays bounded', async () => {
  const { parsePage, pageNumbers } = await import('../src/lib/pagination.ts')
  for (const value of [undefined, null, '', 0, -1, 1.5, 'abc', '1e3', [], {}, Number.MAX_SAFE_INTEGER + 1]) assert.equal(parsePage(value), 1)
  assert.equal(parsePage('42'), 42)
  for (const page of [1, 2, 3, 50, 999, 1000]) {
    const links = pageNumbers(page, 1000)
    assert.ok(links.length <= 9)
    assert.ok(links.includes(page) && links.includes(1) && links.includes(1000))
    const numbers = links.filter((n): n is number => typeof n === 'number')
    assert.equal(new Set(numbers).size, numbers.length)
    assert.deepEqual(numbers, [...numbers].sort((a, b) => a - b))
  }
})

test('tool intake requires review sources and rejects unverified open-source labels', async () => {
  const { toolSchema } = await import('../src/lib/content/schema.ts')
  const base = { id: 'tool', name: 'Tool', url: 'https://example.com/tool', category: 'flashing', runtime: 'browser', sourceType: 'official-tool', pricing: 'unspecified', order: 1, summary: {en:'A useful tool',zh:'实用工具',ja:'便利なツール'}, requirements: {en:'USB',zh:'USB',ja:'USB'}, sources: [{url:'https://example.com/docs',checkedAt:'2026-10-16T06:00:00Z'}], addedAt:'2026-10-16' }
  assert.equal(toolSchema.safeParse(base).success, true)
  assert.equal(toolSchema.safeParse({...base,sources:[]}).success, false)
  assert.equal(toolSchema.safeParse({...base,sources:[{url:'https://example.com/docs'}]}).success, false)
  assert.equal(toolSchema.safeParse({...base,summary:{en:'Only English'}}).success, false)
  assert.equal(toolSchema.safeParse({...base,sourceType:'open-source',pricing:'free'}).success, false)
  assert.equal(toolSchema.safeParse({...base,sourceType:'open-source',license:'MIT',repository:'https://github.com/example/tool'}).success, true)
})

test('duplicate tools fail without overwriting generated project or tool catalogs', async () => {
  const { buildTools } = await import('./tools.ts')
  const authored = buildTools(process.cwd())[0]
  fixture(root => {
    mkdirSync(join(root,'content/tools'))
    md(root,`content/tools/${authored.id}.md`,authored)
    buildCatalog(root,true)
    const toolSnapshot=readFileSync(join(root,'src/generated/tools.json'),'utf8')
    const projectSnapshot=readFileSync(join(root,'src/generated/catalog.json'),'utf8')
    md(root,'content/tools/duplicate.md',{...authored,id:'duplicate',url:authored.url+'#same-tool'})
    assert.throws(()=>buildCatalog(root,true),/Duplicate tool URL/)
    assert.equal(readFileSync(join(root,'src/generated/tools.json'),'utf8'),toolSnapshot)
    assert.equal(readFileSync(join(root,'src/generated/catalog.json'),'utf8'),projectSnapshot)
    md(root,'content/tools/duplicate.md',{...authored,id:'duplicate',url:'https://example.com/another-tool'})
    assert.equal(buildTools(root).length,2)
    md(root,'content/tools/duplicate.md',{...authored,id:'renamed',url:'https://example.com/another-tool'})
    assert.throws(()=>buildTools(root),/filename must match id/)
  })
})

test('guide posts can be removed without losing curated device/project picks',()=>fixture(root=>{
  mkdirSync(join(root,'content/guides/posts'),{recursive:true})
  mkdirSync(join(root,'content/guides/picks'),{recursive:true})
  const localized={zh:'指南',en:'Guide',ja:'ガイド'}
  const post={id:'one',title:localized,url:'https://x.com/example/status/123',order:1}
  const pick={id:'pick',title:localized,summary:localized,effort:localized,budget:'low',deviceIds:['maker-board'],projectIds:['example'],resource:{label:localized,url:'https://example.com/guide'},sources:[post.url],order:1}
  md(root,'content/guides/posts/one.md',post)
  md(root,'content/guides/picks/pick.md',pick)
  buildCatalog(root,true)
  rmSync(join(root,'content/guides/posts/one.md'))
  buildCatalog(root,true)
  const generated=JSON.parse(readFileSync(join(root,'src/generated/guides.json'),'utf8'))
  assert.equal(generated.posts.length,0)
  assert.equal(generated.picks.length,1)
  const before=readFileSync(join(root,'src/generated/guides.json'),'utf8')
  md(root,'content/guides/picks/pick.md',{...pick,deviceIds:['unknown']})
  assert.throws(()=>buildCatalog(root,true),/unknown guide device/)
  assert.equal(readFileSync(join(root,'src/generated/guides.json'),'utf8'),before)
}))
test('guide post validation rejects unsupported URLs and duplicate tweet identities',()=>fixture(root=>{
  mkdirSync(join(root,'content/guides/posts'),{recursive:true})
  const post={id:'one',title:{zh:'原帖',en:'Post',ja:'投稿'},url:'https://x.com/example/status/123',order:1}
  md(root,'content/guides/posts/one.md',{...post,url:'https://example.com/not-x'})
  assert.throws(()=>buildCatalog(root))
  md(root,'content/guides/posts/one.md',post)
  md(root,'content/guides/posts/two.md',{...post,id:'two',url:'https://twitter.com/other/status/123'})
  assert.throws(()=>buildCatalog(root),/Duplicate X post/)
}))


test('one bilingual submission form stays distinct from ordinary issues',()=>{
  const directory=join(process.cwd(),'.github/ISSUE_TEMPLATE')
  const config=parse(readFileSync(join(directory,'config.yml'),'utf8'))
  assert.equal(config.blank_issues_enabled,true,'ordinary feedback must remain possible')
  assert.deepEqual(readdirSync(directory).filter(file=>file.endsWith('.yml')&&file!=='config.yml'),[projectSubmissionTemplate])
  const form=parse(readFileSync(join(directory,projectSubmissionTemplate),'utf8'))
  assert.equal(form.name,'提交项目 / Submit a project')
  assert.deepEqual(form.labels,[projectSubmissionLabel])
  const fields=form.body.filter((field:{type:string})=>field.type!=='markdown')
  assert.deepEqual(fields.map((field:{id:string})=>field.id),['repository','reason','device'])
  assert.deepEqual(fields.filter((field:{validations?:{required?:boolean}})=>field.validations?.required).map((field:{id:string})=>field.id),['repository'])
  const url=new URL(projectSubmissionUrl())
  assert.equal(url.pathname,'/hr98w/esp32.sh/issues/new')
  assert.equal(url.searchParams.get('template'),projectSubmissionTemplate)
})

// README rendering uses untrusted upstream content; these are offline fixtures.
import { createElement } from 'react'
import { renderToStaticMarkup } from 'react-dom/server'
import ReadmeMarkdown from '../src/components/readme-markdown.tsx'
import { ProjectReadme as ReadmePanel } from '../src/components/project-readme.tsx'
import { fetchProjectReadme, readmeUrl } from '../src/lib/project-readme.ts'
import { buildSitemap } from '../src/lib/sitemap.ts'
const readmeFixture = {
  content: '', path: 'docs/README.md',
  htmlUrl: 'https://github.com/example/project/blob/feature/docs/README.md',
  rawUrl: 'https://raw.githubusercontent.com/example/project/feature/docs/README.md',
}
test('README links resolve nested paths and repository-root files, rejecting unsafe protocols', () => {
  assert.equal(readmeUrl('../images/demo.png', true, readmeFixture), 'https://raw.githubusercontent.com/example/project/feature/images/demo.png')
  assert.equal(readmeUrl('/images/demo.png', true, readmeFixture), 'https://raw.githubusercontent.com/example/project/feature/images/demo.png')
  assert.equal(readmeUrl('./install.md', false, readmeFixture), 'https://github.com/example/project/blob/feature/docs/install.md')
  assert.equal(readmeUrl('#setup', false, readmeFixture), readmeFixture.htmlUrl + '#setup')
  assert.equal(readmeUrl('javascript:alert(1)', false, readmeFixture), '')
  assert.equal(readmeUrl('data:image/svg+xml,bad', true, readmeFixture), '')
  assert.equal(readmeUrl('mailto:example@example.com', false, readmeFixture), 'mailto:example@example.com')
})
test('README renders GFM and safe HTML while removing scripts, event handlers, iframes and unsafe links', () => {
  const content = '# Title\n\n| A | B |\n| - | - |\n| 1 | 2 |\n\n![demo](../images/demo.png)\n\n<details><summary>More</summary>Text</details>\n<script>alert(1)</script><iframe src="https://evil.example"></iframe><img src="/images/demo.png" onerror="alert(2)" />\n\n[bad](javascript:alert%281%29)'
  const html = renderToStaticMarkup(createElement(ReadmeMarkdown, { readme: { ...readmeFixture, content } }))
  assert.match(html, /<table>/)
  assert.match(html, /<details>/)
  assert.match(html, /raw\.githubusercontent\.com\/example\/project\/feature\/images\/demo.png/)
  assert.doesNotMatch(html, /<script|<iframe|onerror|javascript:/i)
})
test('README SSR renders the localized fallback without requesting GitHub', async () => {
  for (const locale of ['en','zh','ja'] as const) {
    const html = renderToStaticMarkup(createElement(ReadmePanel, { repository: project.repository, locale }))
    assert.match(html, /project-readme-heading/)
    assert.match(html, /https:\/\/github.com\/example\/project#readme/)
  }
  await assert.rejects(fetchProjectReadme(project.repository, new AbortController().signal), /browser-only/)
})
test('README browser transport is anonymous, decodes Unicode, reuses cache and propagates GitHub failures', async (t) => {
  const entries = new Map<string,string>()
  const windowDescriptor = Object.getOwnPropertyDescriptor(globalThis, 'window')
  const storageDescriptor = Object.getOwnPropertyDescriptor(globalThis, 'sessionStorage')
  Object.defineProperty(globalThis, 'window', { configurable: true, value: {} })
  Object.defineProperty(globalThis, 'sessionStorage', { configurable: true, value: { getItem: (key: string) => entries.get(key) ?? null, setItem: (key: string, value: string) => entries.set(key,value) } })
  const fetchMock = t.mock.method(globalThis, 'fetch', async (input: RequestInfo | URL, options?: RequestInit) => {
    assert.equal(input, 'https://api.github.com/repos/example/project/readme')
    assert.equal(options?.credentials, 'omit')
    assert.deepEqual(options?.headers, { Accept: 'application/vnd.github+json' })
    return new Response(JSON.stringify({ ...{path:readmeFixture.path,html_url:readmeFixture.htmlUrl,download_url:readmeFixture.rawUrl}, encoding:'base64', size:20, content:Buffer.from('你好 ESP32 日本語').toString('base64') }))
  })
  try {
    const first = await fetchProjectReadme(project.repository, new AbortController().signal)
    assert.equal(first.content, '你好 ESP32 日本語')
    assert.deepEqual(await fetchProjectReadme(project.repository, new AbortController().signal), first)
    assert.equal(fetchMock.mock.callCount(), 1)
    entries.clear()
    fetchMock.mock.mockImplementation(async () => new Response('', { status:403 }))
    await assert.rejects(fetchProjectReadme(project.repository, new AbortController().signal), /GitHub 403/)
  } finally {
    if (windowDescriptor) Object.defineProperty(globalThis,'window',windowDescriptor); else Reflect.deleteProperty(globalThis,'window')
    if (storageDescriptor) Object.defineProperty(globalThis,'sessionStorage',storageDescriptor); else Reflect.deleteProperty(globalThis,'sessionStorage')
  }
})
test('sitemap scales with catalog entries and includes localized pagination without filter combinations', () => {
  const xml = buildSitemap({ projects:Array.from({length:25},(_,i)=>({id:'p'+i})), devices:[{id:'board'}] })
  assert.equal((xml.match(/<loc>/g) ?? []).length, (4+25+1+1)*3)
  assert.match(xml, /https:\/\/esp32.sh\/zh\/projects\/p24/)
  assert.match(xml, /https:\/\/esp32.sh\/ja\?page=2/)
  assert.match(xml, /hreflang="zh-CN"/)
  assert.doesNotMatch(xml, /device=|tag=|sort=|\/en\//)
})

import { pageMeta, defaultSocialImage } from '../src/lib/seo.ts'
test('social metadata uses localized canonical URLs and the raster brand image without a cover', () => {
  for (const [locale, ogLocale, prefix] of [['en','en_US',''],['zh','zh_CN','/zh'],['ja','ja_JP','/ja']] as const) {
    const meta = pageMeta({ title:'ESP32 & projects', description:'Localized description', path:'/devices', locale, page:2 })
    const values = Object.fromEntries(meta.map(entry => ['property' in entry ? entry.property : 'name' in entry ? entry.name : 'title', 'content' in entry ? entry.content : entry.title]))
    assert.equal(values['og:url'], `https://esp32.sh${prefix}/devices?page=2`)
    assert.equal(values['og:locale'], ogLocale)
    assert.equal(values['og:title'], 'ESP32 & projects')
    assert.equal(values['twitter:description'], 'Localized description')
    assert.equal(values['twitter:card'], 'summary_large_image')
    assert.equal(values['og:image'], defaultSocialImage)
    assert.equal(values['twitter:image'], defaultSocialImage)
    assert.equal(values['og:image:width'], '1200')
  }
})
test('social covers stay external, while missing, insecure or SVG covers use the fallback', () => {
  for (const [image, expected] of [[undefined,defaultSocialImage],['https://cdn.example/board.webp','https://cdn.example/board.webp'],['https://cdn.example/icon.SVG?raw=1',defaultSocialImage],['http://cdn.example/photo.jpg',defaultSocialImage],['/local.jpg',defaultSocialImage]]) {
    const meta = pageMeta({ title:'Board', description:'A board', path:'/devices/board', locale:'en', image })
    assert.equal(meta.find(entry => 'property' in entry && entry.property==='og:image')?.content,expected)
    assert.equal(meta.find(entry => 'name' in entry && entry.name==='twitter:image')?.content,expected)
    if (image===expected) assert.ok(!meta.some(entry => 'property' in entry && entry.property==='og:image:width'))
  }
})
