import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

start_str = '{PROJECTS.map((project, idx) => {'
end_str = '              })}'

start_idx = content.find(start_str)
end_idx = content.find(end_str, start_idx) + len(end_str)

if start_idx != -1 and end_idx != -1:
    replacement = """              {PROJECTS.map((project, idx) => (
                <ProjectCard key={project.id} project={project} idx={idx} splitProgress={splitProgress} />
              ))}"""
    
    content = content[:start_idx] + replacement + content[end_idx:]
    with open('src/App.tsx', 'w') as f:
        f.write(content)
    print("Replaced PROJECTS.map")
else:
    print("Could not find PROJECTS.map bounds")
