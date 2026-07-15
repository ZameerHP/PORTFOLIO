import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace('activeIndex = Math.min(7, 5 + Math.floor((scrollY - 5 * vh) / vh));', 'activeIndex = Math.min(6, 4 + Math.floor((scrollY - 4 * vh) / vh));')
content = content.replace('snapTarget = 5 * vh + slideIndexAfter4 * vh;', 'snapTarget = 4 * vh + slideIndexAfter4 * vh;')
content = content.replace('const offsetScroll = currentScroll - 5 * vh;', 'const offsetScroll = currentScroll - 4 * vh;')

# And in snap logic:
content = content.replace('if (currentScroll < 4 * vh) {', 'if (currentScroll < 3 * vh) {')
content = content.replace('} else if (currentScroll >= 4 * vh && currentScroll < 5 * vh) {', '} else if (currentScroll >= 3 * vh && currentScroll < 4 * vh) {')
content = content.replace('snapTarget = currentScroll - 4 * vh < 0.5 * vh ? 4 * vh : 5 * vh;', 'snapTarget = currentScroll - 3 * vh < 0.5 * vh ? 3 * vh : 4 * vh;')
content = content.replace('Math.min(7 * vh, Math.max(0, snapTarget))', 'Math.min(6 * vh, Math.max(0, snapTarget))')

with open('src/App.tsx', 'w') as f:
    f.write(content)
