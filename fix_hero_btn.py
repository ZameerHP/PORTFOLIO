import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace('hover:text-white transition-colors duration-700 drop-shadow-[0_1px_4px_rgba(0,0,0,0.5)]"', 'hover:text-white transition-colors duration-700 drop-shadow-[0_1px_4px_rgba(0,0,0,0.5)] min-h-[44px] py-2"')

with open('src/App.tsx', 'w') as f:
    f.write(content)
