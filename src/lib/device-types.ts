export const deviceTypes = ['integrated-device', 'functional-board', 'general-board', 'module'] as const
export type DeviceType = (typeof deviceTypes)[number]
