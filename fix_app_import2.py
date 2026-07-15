import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add import
import_statement = 'import { SkillsSection } from "./components/SkillsSection";\n'
content = content.replace('import { ContactModal } from "./components/ContactModal";', 'import { ContactModal } from "./components/ContactModal";\n' + import_statement)

with open('src/App.tsx', 'w') as f:
    f.write(content)
