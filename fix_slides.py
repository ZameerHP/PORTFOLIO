import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad_slides = """  const slides = [
    { id: "hero", label: "00 // INTRO", name: "Intro" },
    { id: "about", label: "01 // VISION", name: "Vision" },
    { id: "services", label: "02 // CAPABILITIES", name: "Services" },
    { id: "works", label: "03 // SIGNATURE", name: "Works" },
    { id: "reveal", label: "04 // SPLIT REVEAL", name: "Split" },
    { id: "how-we-work", label: "05 // FRAMEWORK", name: "Method" },
    { id: "testimonials", label: "06 // CLIENTS", name: "Reviews" },
    { id: "pricing", label: "07 // INVESTMENT", name: "Pricing" },
    { id: "faq", label: "08 // INSIGHTS", name: "Contact & FAQ" }
  ];"""

good_slides = """  const slides = [
    { id: "hero", label: "00 // INTRO", name: "Intro" },
    { id: "about", label: "01 // VISION", name: "Vision" },
    { id: "services", label: "02 // CAPABILITIES", name: "Services" },
    { id: "works", label: "03 // SIGNATURE", name: "Works" },
    { id: "testimonials", label: "04 // CLIENTS", name: "Reviews" },
    { id: "pricing", label: "05 // INVESTMENT", name: "Pricing" },
    { id: "faq", label: "06 // INSIGHTS", name: "Contact & FAQ" }
  ];"""

content = content.replace(bad_slides, good_slides)

with open('src/App.tsx', 'w') as f:
    f.write(content)
