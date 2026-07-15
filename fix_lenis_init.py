import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

target = """    const lenis = new Lenis({
      duration: 1.4,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: "vertical",
      gestureOrientation: "vertical",
      smoothWheel: true,
      wheelMultiplier: 1.1,
      touchMultiplier: 1.5,
    });
    lenisRef.current = lenis;"""

good = """    const lenis = new Lenis({
      duration: 1.4,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: "vertical",
      gestureOrientation: "vertical",
      smoothWheel: true,
      wheelMultiplier: 1.1,
      touchMultiplier: 1.5,
    });
    lenisRef.current = lenis;
    lenis.scrollTo(0, { immediate: true });"""

if target in content:
    content = content.replace(target, good)
else:
    print("Could not find lenis init")

with open('src/App.tsx', 'w') as f:
    f.write(content)
