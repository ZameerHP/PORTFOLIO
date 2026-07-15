import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Fix the missing {currentSlide === X
# Currently it looks like:
#           }
#           
#           0 && (
#             <motion.div ...

content = re.sub(r'\n(\s*)(\d) && \(', r'\n\1{currentSlide === \2 && (', content)

with open('src/App.tsx', 'w') as f:
    f.write(content)
