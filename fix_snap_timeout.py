import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad = "const workEndVh = 3 + numProjects;"
good = "const workEndVh = 3 + numProjects + 1;"

content = content.replace(bad, good)

with open('src/App.tsx', 'w') as f:
    f.write(content)
