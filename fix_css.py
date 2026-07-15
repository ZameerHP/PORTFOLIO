import re

with open('src/index.css', 'r') as f:
    content = f.read()

content = content.replace('overflow-x: hidden;', 'overflow-x: hidden;\n  box-sizing: border-box;')
content = content.replace('html {', 'html, body {\n  overflow-x: hidden;\n  width: 100%;\n  box-sizing: border-box;\n}\n\nhtml {')

with open('src/index.css', 'w') as f:
    f.write(content)
