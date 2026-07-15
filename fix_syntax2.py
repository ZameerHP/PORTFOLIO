import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad_decl = """      const numProjects = PROJECTS.length;
      const workScrolls = numProjects; // 3
      const workEndVh = 3 + workScrolls; // 6

            const numProjects = PROJECTS.length;
      const workScrolls = numProjects; // 3
      const workEndVh = 3 + workScrolls; // 6"""

good_decl = """      const numProjects = PROJECTS.length;
      const workScrolls = numProjects; // 3
      const workEndVh = 3 + workScrolls; // 6"""

content = content.replace(bad_decl, good_decl)

with open('src/App.tsx', 'w') as f:
    f.write(content)
