import { resolve } from 'node:path'
import type { Plugin } from 'vite'
import { buildCatalog } from './content.ts'

export function contentPlugin(): Plugin {
  let root = process.cwd()
  return {
    name: 'esp32-markdown-catalog',
    configResolved(config) { root = config.root; buildCatalog(root, true) },
    configureServer(server) {
      const directory = resolve(root, 'content')
      const metadata = [resolve(root, 'data/repository-metrics.json'), resolve(root, 'data/repository-covers.json'), resolve(root, 'data/project-intake-overrides.json')]
      server.watcher.add([directory, ...metadata])
      const refresh = (file: string) => {
        if (!(file.startsWith(directory + '/') && file.endsWith('.md')) && !metadata.includes(file)) return
        try {
          buildCatalog(root, true)
          server.ws.send({ type: 'full-reload' })
        } catch (error) {
          const message = error instanceof Error ? error.message : String(error)
          server.config.logger.error(message)
          server.ws.send({ type: 'error', err: { message, stack: '', plugin: 'esp32-markdown-catalog' } })
        }
      }
      server.watcher.on('add', refresh).on('change', refresh).on('unlink', refresh)
      server.httpServer?.once('close', () => {
        server.watcher.off('add', refresh).off('change', refresh).off('unlink', refresh)
      })
    },
  }
}
