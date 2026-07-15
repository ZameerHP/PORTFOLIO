import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

old_blur = 'blur-[120px] mix-blend-screen opacity-50'
new_blur = 'blur-[120px] mix-blend-screen opacity-50 transform-gpu will-change-transform'
content = content.replace(old_blur, new_blur)

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)

