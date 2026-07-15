import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

old_relative = '<div className="relative min-h-[300px] w-full">'
new_relative = '<div className="w-full">'
content = content.replace(old_relative, new_relative)

old_grid = 'className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 absolute inset-0 pointer-events-auto"'
new_grid = 'className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 pointer-events-auto"'
content = content.replace(old_grid, new_grid)

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)

