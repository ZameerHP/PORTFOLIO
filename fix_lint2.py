import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

# Just change `<FadeIn key={i}` to `<div key={i} className="contents"><FadeIn`
# and `</FadeIn>` to `</FadeIn></div>` inside the map functions.

content = content.replace('<FadeIn key={i} delay={i * 0.03}>', '<div key={i} className="contents"><FadeIn delay={i * 0.03}>')
content = content.replace('<FadeIn key={i} delay={i * 0.08}>', '<div key={i} className="contents"><FadeIn delay={i * 0.08}>')
content = content.replace('<FadeIn key={i} delay={i * 0.05}>', '<div key={i} className="contents"><FadeIn delay={i * 0.05}>')
content = content.replace('<FadeIn key={i} delay={i * 0.05} className="relative pl-10 group cursor-default">', '<div key={i} className="contents"><FadeIn delay={i * 0.05} className="relative pl-10 group cursor-default">')
content = content.replace('<FadeIn key={i} delay={i * 0.1} className="flex flex-col items-center text-center gap-4 group cursor-default">', '<div key={i} className="contents"><FadeIn delay={i * 0.1} className="flex flex-col items-center text-center gap-4 group cursor-default">')

# Close tags. Since some FadeIn have children, we can just replace all </FadeIn> that are inside the map with </FadeIn></div>.
# It's safer to just change the React.ReactNode type to accept key by making FadeIn a standard FunctionalComponent.
