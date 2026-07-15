import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

# Let's just define FadeIn properly!
bad = 'const FadeIn = ({ children, delay = 0, className = "" }: { children: React.ReactNode, delay?: number, className?: string }) => {'
good = 'const FadeIn: React.FC<{ children: React.ReactNode; delay?: number; className?: string; }> = ({ children, delay = 0, className = "" }) => {'

content = content.replace(bad, good)
# also revert my previous partial replacements:
content = content.replace('<div key={i} className="contents"><FadeIn', '<FadeIn key={i}')

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
