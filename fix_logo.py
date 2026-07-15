import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad_logo = '{currentSlide === 1 ? "ABOUT US" : ""}'
good_logo = '{currentSlide === 1 ? "ABOUT US" : currentSlide === 0 ? "zamy dev" : ""}'
content = content.replace(bad_logo, good_logo)

with open('src/App.tsx', 'w') as f:
    f.write(content)
