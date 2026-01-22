const fs = require('fs');

const data = JSON.parse(fs.readFileSync('analysis_data.json', 'utf8'));
const topMiddle = data.slice(2, 5);

const output = [];
topMiddle.forEach((item, index) => {
    output.push(`=== TOPIC ${index + 3}: ${item.hotword} ===`);
    if (item.search_result && item.search_result.references) {
        item.search_result.references.slice(0, 3).forEach(ref => {
            output.push(`-- Ref: ${ref.title} --`);
            output.push(`Snippet: ${ref.snippet || ref.content.substring(0, 200)}`);
            output.push(`Date: ${ref.date}`);
            output.push('---');
        });
    } else {
        output.push("No search results.");
    }
    output.push("\n");
});
fs.writeFileSync('context.txt', output.join('\n'));

