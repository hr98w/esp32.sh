import data from '../generated/guides.json'
import type { GuidePick, GuidePost } from './content/schema'
export const guides = data as { posts: GuidePost[]; picks: GuidePick[] }
