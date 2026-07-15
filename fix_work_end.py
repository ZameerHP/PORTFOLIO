import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad_work = """      const workScrolls = numProjects; // 3
      const workEndVh = 3 + workScrolls; // 6"""

good_work = """      const workScrolls = numProjects; // 3
      const workEndVh = 3 + workScrolls + 1; // 7"""

content = content.replace(bad_work, good_work)

with open('src/App.tsx', 'w') as f:
    f.write(content)
