import Markdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import rehypeRaw from 'rehype-raw'
import rehypeSanitize from 'rehype-sanitize'
import { readmeUrl, type ProjectReadme } from '../lib/project-readme'

export default function ReadmeMarkdown({ readme }: { readme: ProjectReadme }) {
  return <article className="readme-markdown"><Markdown
    remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeRaw, rehypeSanitize]}
    urlTransform={(value, key) => readmeUrl(value, key === 'src', readme)}
    components={{
      a: ({ node: _node, ...props }) => <a {...props} target="_blank" rel="noopener noreferrer" />,
      img: ({ node: _node, src, ...props }) => src ? <img {...props} src={src} loading="lazy" referrerPolicy="no-referrer" /> : null,
    }}
  >{readme.content}</Markdown></article>
}
