#!/usr/bin/env node
import readline from 'readline';

const rl = readline.createInterface({ input: process.stdin, terminal: false });

let inputData = '';
rl.on('line', (line) => { inputData += line; });

rl.on('close', () => {
  try {
    if (!inputData.trim()) {
      process.stdout.write('[Context Recovery]: Initializing...');
      return;
    }

    const session = JSON.parse(inputData);

    const model = session.model?.display_name || 'Claude';
    const usedPct = session.context_window?.used_percentage ?? 0;
    const totalCost = session.cost?.total_cost_usd ?? 0.00;

    const usedInt = Math.round(usedPct);
    const filled = Math.floor(usedInt * 10 / 100);
    const bar = '#'.repeat(filled) + '-'.repeat(10 - filled);

    let status = 'OK';
    if (usedPct > 80) status = 'HIGH';
    else if (usedPct > 50) status = 'MED';

    process.stdout.write(`${model}  [${bar}] ${usedInt}% used | $${totalCost.toFixed(2)} | ${status}`);
  } catch (err) {
    process.stdout.write(`[Context Recovery Error]: ${err.message}`);
  }
});
