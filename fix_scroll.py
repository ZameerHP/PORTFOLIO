import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace('snapTarget = Math.min(9 * vh, Math.max(0, snapTarget));', 'snapTarget = Math.min(10 * vh, Math.max(0, snapTarget));')
content = content.replace('height: "1000vh"', 'height: "1100vh"')
content = content.replace('const slideCount = 10;', 'const slideCount = 11;') # wait what is slideCount used for?

with open('src/App.tsx', 'w') as f:
    f.write(content)
