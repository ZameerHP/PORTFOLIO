import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

start = content.find('snapTimeout = setTimeout(() => {')
end = content.find('}, 150);')
print(content[start:end+8])
