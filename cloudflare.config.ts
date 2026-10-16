import { defineConfig } from "cf/config";

export default defineConfig({
	accountId: "995fe370bbd6d82dfd2770ffa51a2748",
	worker: {
		name: "esp32-sh",
		domains: ["esp32.sh"],
		compatibilityDate: "2026-10-01",
		compatibilityFlags: [
			"nodejs_compat",
		],
		entrypoint: "@tanstack/react-start/server-entry",
	},
});
