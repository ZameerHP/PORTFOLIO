import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

state_search = '  const [isContactOpen, setIsContactOpen] = useState<boolean>(false);'
content = content.replace(state_search, state_search + '\n  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState<boolean>(false);')

with open('src/App.tsx', 'w') as f:
    f.write(content)
