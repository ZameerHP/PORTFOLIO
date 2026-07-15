import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add import
import_statement = 'import { SkillsSection } from "./components/SkillsSection";\n'
content = content.replace('import { Play, Pause, X } from "lucide-react";', 'import { Play, Pause, X } from "lucide-react";\n' + import_statement)

# Add render
render_bad = """          {currentSlide === 5 && (
            <motion.div
              key="testimonials-slide"
"""
render_good = """          {currentSlide === 4 && (
            <SkillsSection slideDirection={slideDirection} />
          )}
          {currentSlide === 5 && (
            <motion.div
              key="testimonials-slide"
"""

content = content.replace(render_bad, render_good)

with open('src/App.tsx', 'w') as f:
    f.write(content)
