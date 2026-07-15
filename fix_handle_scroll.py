import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Make sure we got it replaced properly
if 'const numProjects = PROJECTS.length;' not in content:
    print("Replacement failed, applying manually")

