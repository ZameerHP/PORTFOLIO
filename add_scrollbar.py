import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

bad = '    </div>\n  );\n};'
good = """      <style>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: rgba(255, 255, 255, 0.02);
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(255, 255, 255, 0.1);
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(59, 130, 246, 0.5);
        }
      `}</style>
    </div>
  );
};"""

content = content.replace(bad, good)

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
