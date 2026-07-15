import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

bad = 'className="relative w-full min-h-screen pt-32 pb-24 px-6 md:px-12 lg:px-24 text-white overflow-hidden selection:bg-blue-500/30"'
good = 'className="relative w-full min-h-screen pt-32 pb-24 px-6 md:px-12 lg:px-24 text-white selection:bg-blue-500/30"'
content = content.replace(bad, good)

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
