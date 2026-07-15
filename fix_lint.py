import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

# Replace <FadeIn key={i} ...> with <React.Fragment key={i}><FadeIn ...></FadeIn></React.Fragment>

content = re.sub(r'<FadeIn key=\{i\} (delay=\{[^}]+\})(?: className="([^"]+)")?>', r'<React.Fragment key={i}>\n<FadeIn \1' + r' className="\2">' if r' className="' in r'\2' else r'<React.Fragment key={i}>\n<FadeIn \1>', content)

# I will just write a simpler fix: change the FadeIn definition to include `key?` (no, key is reserved). 
