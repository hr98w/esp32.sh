export const toolCategories = ['flashing', 'simulation', 'coding-debugging', 'display-assets'] as const
export type ToolCategory = (typeof toolCategories)[number]
