import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Slides config
content = content.replace('{ id: "pricing", label: "06 // INVESTMENT", name: "Pricing" },\n    { id: "faq", label: "07 // INSIGHTS", name: "Contact & FAQ" }', '{ id: "faq", label: "06 // INSIGHTS", name: "Contact & FAQ" }')

# 2. Math.min(7, currentSlide + 1) -> Math.min(6, currentSlide + 1)
content = content.replace('Math.min(7, currentSlide + 1)', 'Math.min(6, currentSlide + 1)')

# 3. activeIndex = Math.min(7, 4 + Math.floor((scrollY - workEndVh * vh) / vh)); -> Math.min(6
content = content.replace('activeIndex = Math.min(7, 4 + Math.floor((scrollY - workEndVh * vh) / vh));', 'activeIndex = Math.min(6, 4 + Math.floor((scrollY - workEndVh * vh) / vh));')

# 4. Math.min(10 * vh, Math.max(0, snapTarget)); -> 9 * vh
content = content.replace('Math.min(10 * vh, Math.max(0, snapTarget));', 'Math.min(9 * vh, Math.max(0, snapTarget));')

# 5. Nav links mapping
nav_links_old = '''              { name: "Skills", index: 4 },
              { name: "Pricing", index: 6 }'''
nav_links_new = '''              { name: "Skills", index: 4 }'''
content = content.replace(nav_links_old, nav_links_new)

mobile_nav_links_old = '''                { name: "Works", index: 3 },
                { name: "Skills", index: 4 },
                { name: "Pricing", index: 6 }'''
mobile_nav_links_new = '''                { name: "Works", index: 3 },
                { name: "Skills", index: 4 }'''
content = content.replace(mobile_nav_links_old, mobile_nav_links_new)

footer_nav_links_old = '''                        <button onClick={() => changeSlide(5)} className="hover:text-white text-left transition-colors py-2 block">Reviews</button>
                        <button onClick={() => changeSlide(6)} className="hover:text-white text-left transition-colors py-2 block">Pricing</button>
                        <button onClick={() => changeSlide(7)} className="hover:text-white text-left transition-colors py-2 block">Contact</button>'''
footer_nav_links_new = '''                        <button onClick={() => changeSlide(5)} className="hover:text-white text-left transition-colors py-2 block">Reviews</button>
                        <button onClick={() => changeSlide(6)} className="hover:text-white text-left transition-colors py-2 block">Contact</button>'''
content = content.replace(footer_nav_links_old, footer_nav_links_new)

# 6. Scroll spacer height 1100dvh -> 900dvh
content = content.replace('height: "1100dvh"', 'height: "900dvh"')

with open('src/App.tsx', 'w') as f:
    f.write(content)
