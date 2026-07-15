import re
with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Remove import
content = content.replace('import { CinematicWorkSlide } from "./components/CinematicWorkSlide";\n', '')
content = content.replace('<CinematicWorkSlide currentSlide={currentSlide} />', '')

# 2. Update changeSlide boundary
content = content.replace('Math.min(8, currentSlide + 1)', 'Math.min(7, currentSlide + 1)')
# Update handleScroll boundary
content = content.replace('Math.min(8, 5 + Math.floor((scrollY - 5 * vh) / vh))', 'Math.min(7, 5 + Math.floor((scrollY - 5 * vh) / vh))')
# Update snapTarget boundary
content = content.replace('Math.min(8 * vh, Math.max(0, snapTarget))', 'Math.min(7 * vh, Math.max(0, snapTarget))')

# 3. Update Pricing index in Nav
content = content.replace('{ name: "Pricing", index: 7 }', '{ name: "Pricing", index: 6 }')

# 4. Update lenis scroll spacer
content = content.replace('height: "900vh"', 'height: "800vh"')

with open('src/App.tsx', 'w') as f:
    f.write(content)
