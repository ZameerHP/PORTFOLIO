import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace('h-[36px]', 'h-[44px]')

with open('src/App.tsx', 'w') as f:
    f.write(content)
