const fs = require('fs');
const text = fs.readFileSync('src/pages/vocabulary/vocabulary.js', 'utf8');
const errIdx = 385402;
console.log(text.substring(errIdx - 80, errIdx + 80));
