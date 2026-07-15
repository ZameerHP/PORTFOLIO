import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad = """className="absolute inset-0 w-full h-full bg-[#0a0a0a] flex flex-col justify-center overflow-hidden"
              id="skills-slide-screen"
            >
              <SkillsSection />"""
              
good = """className="absolute inset-0 w-full h-full bg-[#0a0a0a] overflow-y-auto custom-scrollbar"
              id="skills-slide-screen"
            >
              <SkillsSection />"""
              
content = content.replace(bad, good)

with open('src/App.tsx', 'w') as f:
    f.write(content)
