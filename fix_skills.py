import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

content = content.replace('grid-cols-2 md:grid-cols-3', 'grid-cols-1 sm:grid-cols-2 lg:grid-cols-3')

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
