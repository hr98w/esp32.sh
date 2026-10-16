import { HeadContent, Scripts, createRootRoute, Link, useRouterState } from '@tanstack/react-router'

import { resolveLocale, htmlLang } from '../lib/i18n'

import appCss from '../styles.css?url'

export const Route = createRootRoute({
  head: () => ({
    meta: [
      {
        charSet: 'utf-8',
      },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1',
      },
      {
        title: 'esp32.sh',
      },
    ],
    links: [
      { rel: 'icon', href: '/favicon.svg', type: 'image/svg+xml' },
      { rel: 'icon', href: '/favicon-32.png', type: 'image/png', sizes: '32x32' },
      { rel: 'icon', href: '/favicon-16.png', type: 'image/png', sizes: '16x16' },
      {
        rel: 'stylesheet',
        href: appCss,
      },
    ],
  }),
  shellComponent: RootDocument,
  notFoundComponent: () => <div className="empty"><h1>404</h1><Link to="/{-$lang}" params={{ lang: undefined }}>esp32.sh →</Link></div>,
})

function RootDocument({ children }: { children: React.ReactNode }) {
  const locale = useRouterState({ select: (state) => state.location.pathname.split('/')[1] })
  return (
    <html lang={htmlLang(resolveLocale(locale))}>
      <head>
        <HeadContent />
        <script defer data-domain="esp32.sh" src="https://plausible.haoran.cv/js/script.outbound-links.js" />
      </head>
      <body>
        {children}

        <Scripts />
      </body>
    </html>
  )
}
