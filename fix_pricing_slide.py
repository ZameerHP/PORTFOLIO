import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace currentSlide === 7 with currentSlide === 6
content = content.replace('{currentSlide === 7 && (', '{currentSlide === 6 && (')

# Remove the pricing block
pricing_pattern = re.compile(r'\{\s*currentSlide === 6\s*&&\s*\(\s*<motion\.div\s*key="pricing-slide"[\s\S]*?id="pricing-slide-screen"\s*>[\s\S]*?<\/motion\.div>\s*\)\s*\}\s*\{\s*currentSlide === 6\s*&&\s*\(', re.MULTILINE)
content = re.sub(pricing_pattern, '{currentSlide === 6 && (', content)

with open('src/App.tsx', 'w') as f:
    f.write(content)
