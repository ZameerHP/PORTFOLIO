import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace 8 * vh back to 7 * vh in the scroll logic
content = content.replace('scrollY < 8 * vh', 'scrollY < 7 * vh')
content = content.replace('scrollY - 8 * vh', 'scrollY - 7 * vh')
content = content.replace('currentScroll < 8 * vh', 'currentScroll < 7 * vh')
content = content.replace('currentScroll - 8 * vh', 'currentScroll - 7 * vh')
content = content.replace('8 * vh + slideIndexAfter4', '7 * vh + slideIndexAfter4')
content = content.replace('(8 + direction - 4)', '(7 + direction - 4)')
content = content.replace('(8 + nextSlide - 4)', '(7 + nextSlide - 4)')
content = content.replace('(8 + prevSlide - 4)', '(7 + prevSlide - 4)')

content = content.replace('Math.min(10 * vh, Math.max(0, snapTarget))', 'Math.min(9 * vh, Math.max(0, snapTarget))')
content = content.replace('height: "1100vh"', 'height: "1000vh"')

with open('src/App.tsx', 'w') as f:
    f.write(content)
