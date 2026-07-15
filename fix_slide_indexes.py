import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad_slides = """  const slides = [
    { id: "hero", label: "00 // INTRO", name: "Intro" },
    { id: "about", label: "01 // VISION", name: "Vision" },
    { id: "services", label: "02 // CAPABILITIES", name: "Services" },
    { id: "works", label: "03 // SIGNATURE", name: "Works" },
    { id: "testimonials", label: "04 // CLIENTS", name: "Reviews" },
    { id: "pricing", label: "05 // INVESTMENT", name: "Pricing" },
    { id: "faq", label: "06 // INSIGHTS", name: "Contact & FAQ" }
  ];"""

good_slides = """  const slides = [
    { id: "hero", label: "00 // INTRO", name: "Intro" },
    { id: "about", label: "01 // VISION", name: "Vision" },
    { id: "services", label: "02 // CAPABILITIES", name: "Services" },
    { id: "works", label: "03 // SIGNATURE", name: "Works" },
    { id: "skills", label: "04 // EXPERTISE", name: "Skills" },
    { id: "testimonials", label: "05 // CLIENTS", name: "Reviews" },
    { id: "pricing", label: "06 // INVESTMENT", name: "Pricing" },
    { id: "faq", label: "07 // INSIGHTS", name: "Contact & FAQ" }
  ];"""

content = content.replace(bad_slides, good_slides)
content = content.replace('const slideCount = 9;', 'const slideCount = 10;')

# In changeSlide
content = content.replace('const nextSlide = Math.min(6, currentSlide + 1);', 'const nextSlide = Math.min(7, currentSlide + 1);')

# In activeIndex
content = content.replace('activeIndex = Math.min(6, 4 + Math.floor((scrollY - workEndVh * vh) / vh));', 'activeIndex = Math.min(7, 4 + Math.floor((scrollY - workEndVh * vh) / vh));')

# Navbar rendering map
content = content.replace("""              { name: "Services", index: 2 },
              { name: "Works", index: 3 },
              { name: "Pricing", index: 5 }""", """              { name: "Services", index: 2 },
              { name: "Works", index: 3 },
              { name: "Skills", index: 4 },
              { name: "Pricing", index: 6 }""")

# Footer buttons
bad_footer = """                        <button onClick={() => changeSlide(0)} className="hover:text-white text-left transition-colors">Home</button>
                        <button onClick={() => changeSlide(1)} className="hover:text-white text-left transition-colors">About</button>
                        <button onClick={() => changeSlide(2)} className="hover:text-white text-left transition-colors">Services</button>
                        <button onClick={() => changeSlide(3)} className="hover:text-white text-left transition-colors">Works</button>
                        <button onClick={() => changeSlide(4)} className="hover:text-white text-left transition-colors">Reviews</button>
                        <button onClick={() => changeSlide(5)} className="hover:text-white text-left transition-colors">Pricing</button>
                        <button onClick={() => changeSlide(6)} className="hover:text-white text-left transition-colors">Contact</button>"""
good_footer = """                        <button onClick={() => changeSlide(0)} className="hover:text-white text-left transition-colors">Home</button>
                        <button onClick={() => changeSlide(1)} className="hover:text-white text-left transition-colors">About</button>
                        <button onClick={() => changeSlide(2)} className="hover:text-white text-left transition-colors">Services</button>
                        <button onClick={() => changeSlide(3)} className="hover:text-white text-left transition-colors">Works</button>
                        <button onClick={() => changeSlide(4)} className="hover:text-white text-left transition-colors">Skills</button>
                        <button onClick={() => changeSlide(5)} className="hover:text-white text-left transition-colors">Reviews</button>
                        <button onClick={() => changeSlide(6)} className="hover:text-white text-left transition-colors">Pricing</button>
                        <button onClick={() => changeSlide(7)} className="hover:text-white text-left transition-colors">Contact</button>"""

content = content.replace(bad_footer, good_footer)

with open('src/App.tsx', 'w') as f:
    f.write(content)
