import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# fix splitProgress in changeSlide
content = content.replace(
    'if (currentSlide === 3 && splitProgress < numProjects * 100) {',
    'if (currentSlide === 3 && splitProgress.get() < numProjects * 100) {'
)
content = content.replace(
    'const currentPhase = Math.floor(splitProgress / 100);',
    'const currentPhase = Math.floor(splitProgress.get() / 100);'
)
content = content.replace(
    'if (currentSlide === 3 && splitProgress > 0) {',
    'if (currentSlide === 3 && splitProgress.get() > 0) {'
)
content = content.replace(
    'const currentPhase = Math.ceil(splitProgress / 100);',
    'const currentPhase = Math.ceil(splitProgress.get() / 100);'
)

# fix useEffect dependency
content = content.replace(
    '}, [currentSlide, splitProgress]);',
    '}, [currentSlide]);'
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
