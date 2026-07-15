import re

with open('src/components/ContactModal.tsx', 'r') as f:
    content = f.read()

content = content.replace('className="absolute top-6 right-6 text-white/50 transition-colors hover:text-white text-xl font-light"', 'className="absolute top-4 right-4 p-3 text-white/50 transition-colors hover:text-white text-xl font-light"')

with open('src/components/ContactModal.tsx', 'w') as f:
    f.write(content)
