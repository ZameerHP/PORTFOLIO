import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace('className="hover:text-white text-left transition-colors"', 'className="hover:text-white text-left transition-colors py-2 block"')

with open('src/App.tsx', 'w') as f:
    f.write(content)
