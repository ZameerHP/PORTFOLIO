import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

bad = """          <FadeIn>
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono tracking-widest uppercase mb-8 shadow-[0_0_20px_rgba(59,130,246,0.15)]">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Skills & Expertise</span>
            </div>
          </FadeIn>"""

content = content.replace(bad, "")

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
