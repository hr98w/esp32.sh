export const PAGE_SIZE = 24

export function parsePage(value: unknown): number {
  if (typeof value !== 'number' && typeof value !== 'string') return 1
  if (!/^[1-9]\d*$/.test(String(value))) return 1
  const page = Number(value)
  return Number.isSafeInteger(page) ? page : 1
}

export function paginate<T>(items: readonly T[], requestedPage: unknown) {
  const total = items.length
  const pageCount = Math.max(1, Math.ceil(total / PAGE_SIZE))
  const page = Math.min(parsePage(requestedPage), pageCount)
  const offset = (page - 1) * PAGE_SIZE
  return { items: items.slice(offset, offset + PAGE_SIZE), page, pageCount, total, start: total ? offset + 1 : 0, end: Math.min(offset + PAGE_SIZE, total) }
}

/** Keep navigation bounded even when the catalog has thousands of pages. */
export function pageNumbers(page: number, pageCount: number): (number | 'gap')[] {
  const candidates = new Set([1, pageCount, page - 1, page, page + 1])
  if (page <= 3) { candidates.add(2); candidates.add(3) }
  if (page >= pageCount - 2) { candidates.add(pageCount - 1); candidates.add(pageCount - 2) }
  const numbers = [...candidates].filter(n => n >= 1 && n <= pageCount).sort((a, b) => a - b)
  const result: (number | 'gap')[] = []
  for (const n of numbers) {
    const last = result.at(-1)
    if (typeof last === 'number' && n - last > 1) result.push(n - last === 2 ? last + 1 : 'gap')
    result.push(n)
  }
  return result
}
