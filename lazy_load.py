import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace static imports with lazy ones
old_imports = '''import { ContactModal } from "./components/ContactModal";
import { SkillsSection } from "./components/SkillsSection";'''
new_imports = '''import { Suspense, lazy } from "react";
const ContactModal = lazy(() => import('./components/ContactModal').then(module => ({ default: module.ContactModal })));
const SkillsSection = lazy(() => import('./components/SkillsSection').then(module => ({ default: module.SkillsSection })));'''

content = content.replace(old_imports, new_imports)

# Wrap usages in Suspense
content = content.replace('<SkillsSection />', '<Suspense fallback={null}><SkillsSection /></Suspense>')
content = content.replace('<ContactModal isOpen={isContactOpen} onClose={() => setIsContactOpen(false)} />', '<Suspense fallback={null}><ContactModal isOpen={isContactOpen} onClose={() => setIsContactOpen(false)} /></Suspense>')

with open('src/App.tsx', 'w') as f:
    f.write(content)

