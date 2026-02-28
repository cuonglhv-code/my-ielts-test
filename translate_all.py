import os
import re
import json
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='zh-CN', target='en')

def translate_text(text):
    if not text.strip(): return text
    try:
        # Avoid translating if it's longer than 5000 chars, break it down
        if len(text) > 4500:
            return text
        return translator.translate(text)
    except Exception as e:
        print(f"Error translating: {text[:30]}... - {e}")
        return text

def process_nested_value(val):
    if isinstance(val, str) and contains_chinese(val):
        return translate_text(val)
    elif isinstance(val, list):
        return [process_nested_value(item) for item in val]
    elif isinstance(val, dict):
        return {k: process_nested_value(v) for k, v in val.items()}
    return val

def contains_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def translate_file(path):
    print(f"Processing {path}...")
    try:
        if path.endswith('.json'):
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            data = process_nested_value(data)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        if not contains_chinese(content):
            return

        # Simple regex to find chinese strings in quotes or between html tags
        # For simplicity in this demo, we'll try to find blocks of Chinese text
        # Because we don't want to break code structure, we only translate what's safely identifiable.

        # Find all strings containing Chinese characters
        # This regex looks for quotes containing Chinese
        def replace_match(match):
            original = match.group(0)
            prefix = match.group(1)
            text = match.group(2)
            suffix = match.group(3)
            if contains_chinese(text):
                translated = translate_text(text)
                return f"{prefix}{translated}{suffix}"
            return original

        # Translate double quoted strings containing Chinese
        content = re.sub(r'(")([^"]*[\u4e00-\u9fff][^"]*)(")', replace_match, content)
        # Translate single quoted strings containing Chinese
        content = re.sub(r"(')([^']*[\u4e00-\u9fff][^']*)(')", replace_match, content)
        # Translate text between tags containing Chinese
        content = re.sub(r'(>)([^<]*[\u4e00-\u9fff][^<]*)(<)', replace_match, content)

        # Translate template literal variables with Chinese (basic)
        content = re.sub(r'(`)([^`]*[\u4e00-\u9fff][^`]*)(`)', replace_match, content)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    except Exception as e:
        print(f"Failed to fully process {path}: {e}")

files_with_chinese = []
for root, _, files in os.walk('src'):
    for file in files:
        if file.endswith(('.vue', '.js', '.ts', '.json')):
            path = os.path.join(root, file)
            translate_file(path)

print("Done translating.")
