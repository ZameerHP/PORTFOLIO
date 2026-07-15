import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Let's find lenis initialization useEffect
target = "const lenis = new Lenis({"
if target in content:
    content = content.replace(target, "if ('scrollRestoration' in history) { history.scrollRestoration = 'manual'; }\n    window.scrollTo(0, 0);\n\n    " + target)
else:
    print("Could not find Lenis init")

with open('src/App.tsx', 'w') as f:
    f.write(content)
