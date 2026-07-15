import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Find slide 3
s3_start = content.find('{currentSlide === 3 && (')
s4_start = content.find('{currentSlide === 4 && (')

if s3_start != -1 and s4_start != -1:
    content = content[:s3_start] + content[s4_start:]
else:
    print("Could not find boundaries")

# Now we have {currentSlide === 4, 5, 6, 7. We need to rename them to 3, 4, 5, 6.
content = content.replace('{currentSlide === 4 && (', '{currentSlide === 3 && (')
content = content.replace('{currentSlide === 5 && (', '{currentSlide === 4 && (')
content = content.replace('{currentSlide === 6 && (', '{currentSlide === 5 && (')
content = content.replace('{currentSlide === 7 && (', '{currentSlide === 6 && (')

# Also rename the custom={{ index: X }} props
content = content.replace('custom={{ index: 4, dir: slideDirection }}', 'custom={{ index: 3, dir: slideDirection }}')
content = content.replace('custom={{ index: 5, dir: slideDirection }}', 'custom={{ index: 4, dir: slideDirection }}')
content = content.replace('custom={{ index: 6, dir: slideDirection }}', 'custom={{ index: 5, dir: slideDirection }}')
content = content.replace('custom={{ index: 7, dir: slideDirection }}', 'custom={{ index: 6, dir: slideDirection }}')

# Navigation buttons
content = content.replace('{ name: "Pricing", index: 6 }', '{ name: "Pricing", index: 5 }')

# In the nav buttons area we have `currentSlide === 1 || currentSlide === 2 || currentSlide === 3` for dark text. 
# Slide 3 is now the split reveal (dark background).
# Let's fix that. Slide 1 and 2 are white background. Slide 3 is dark. 
# Actually, slide 1 is About (white), slide 2 is Services (white). So currentSlide === 1 || currentSlide === 2 is enough.
content = content.replace('currentSlide === 1 || currentSlide === 2 || currentSlide === 3', 'currentSlide === 1 || currentSlide === 2')
content = content.replace('Math.min(7, currentSlide + 1)', 'Math.min(6, currentSlide + 1)')

with open('src/App.tsx', 'w') as f:
    f.write(content)
