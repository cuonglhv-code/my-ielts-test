const fs = require('fs');
const file = 'src/pages/vocabulary/vocabulary.js';
let text = fs.readFileSync(file, 'utf8');
text = text.replace('"extra": "spell n. As a noun, it means "a period of time""', '"extra": "spell n. As a noun, it means \'a period of time\'"');
fs.writeFileSync(file, text, 'utf8');
console.log('Fixed syntax error');
