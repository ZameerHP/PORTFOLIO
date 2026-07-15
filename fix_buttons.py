import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Fix header nav links tap target
content = content.replace('h-[30px]', 'h-[44px]')

# Fix contact button in header
content = content.replace('h-[30px]', 'h-[44px]')
# wait, let me just check where else h-[30px] is used. Let's just do it directly on the nav buttons.

with open('src/App.tsx', 'w') as f:
    f.write(content)
