import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

start = content.find('const changeSlide = (direction')
end = content.find('const lenis = new Lenis({')
print(content[start:end])
