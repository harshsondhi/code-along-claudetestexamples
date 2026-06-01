#!/usr/bin/env node
import { readFileSync, appendFileSync, mkdirSync } from "fs";
import { join } from "path";
 
const logDir = join(".claude", "hooks", "logs");
mkdirSync(logDir, { recursive: true });
 
try {
  const input = JSON.parse(readFileSync(0, "utf-8"));
  const toolName = input.tool_name;
  const filePath = input.tool_input?.file_path || "unknown";
  const timestamp = new Date().toISOString();
 
  appendFileSync(
    join(logDir, "file-changes.log"),
    `${timestamp} | ${toolName} | ${filePath}\n`,
  );
} catch {
  // Silent fail -- don't block Claude
}
 
process.exit(0);