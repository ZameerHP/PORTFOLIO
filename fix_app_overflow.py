import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad = 'className="absolute inset-0 w-full h-full bg-[#0a0a0a] overflow-y-auto custom-scrollbar"'
good = 'className="absolute inset-0 w-full h-full bg-[#0a0a0a] overflow-y-auto overflow-x-hidden custom-scrollbar"'
content = content.replace(bad, good)

with open('src/App.tsx', 'w') as f:
    f.write(content)
