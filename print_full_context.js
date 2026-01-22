const fs = require('fs');

const data = JSON.parse(fs.readFileSync('analysis_data.json', 'utf8'));
// Process ALL items
const items = data;

const output = [];
items.forEach((item, index) => {
    output.push(`=== TOPIC ${index + 1}: ${item.hotword} ===`);
    output.push(`Hotness: ${item.hotwordnum}`);
    if (item.search_result && item.search_result.references) {
        item.search_result.references.slice(0, 2).forEach(ref => { // Top 2 refs to save space
            output.push(`-- Ref: ${ref.title} --`);
            // Sanitize snippet to simple text
            const snippet = (ref.snippet || ref.content || "").substring(0, 300).replace(/\s+/g, ' ');
            output.push(`Content: ${snippet}`);
            output.push(`Date: ${ref.date}`);
        });
    } else {
        output.push("No search info.");
    }
    output.push("\n");
});

fs.writeFileSync('context_full.txt', output.join('\n'));
console.log("Context saved to context_full.txt");
