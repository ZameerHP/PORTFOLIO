import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace('{currentSlide === 6 && (', '{currentSlide === 7 && (')
content = content.replace('{currentSlide === 5 && (', '{currentSlide === 6 && (')
content = content.replace('{currentSlide === 4 && (', '{currentSlide === 5 && (')

content = content.replace('custom={{ index: 6, dir: slideDirection }}', 'custom={{ index: 7, dir: slideDirection }}')
content = content.replace('custom={{ index: 5, dir: slideDirection }}', 'custom={{ index: 6, dir: slideDirection }}')
content = content.replace('custom={{ index: 4, dir: slideDirection }}', 'custom={{ index: 5, dir: slideDirection }}')

with open('src/App.tsx', 'w') as f:
    f.write(content)
