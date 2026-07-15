import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Fix Loader ZAMEER STUDIO
content = content.replace('<span className="font-mono text-xs tracking-widest text-[#ff4f1d]">ZAMEER STUDIO</span>', '')

# Fix Header Logo
bad_logo = '{currentSlide === 1 ? "ABOUT US" : "ZAMEER STUDIO"}'
good_logo = '{currentSlide === 1 ? "ABOUT US" : ""}'
content = content.replace(bad_logo, good_logo)

with open('src/App.tsx', 'w') as f:
    f.write(content)

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

content = content.replace('TECHNICAL <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#ff4f1d] to-orange-400">ARSENAL</span>', 'SKILLS <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#ff4f1d] to-orange-400"></span>')
# Wait, let's just make it say SKILLS. Or SKILLS in orange?
content = content.replace('SKILLS <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#ff4f1d] to-orange-400"></span>', '<span className="text-transparent bg-clip-text bg-gradient-to-r from-[#ff4f1d] to-orange-400">SKILLS</span>')

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
