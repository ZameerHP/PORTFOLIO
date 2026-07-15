import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. handleScroll logic
handle_scroll_new = """      if (scrollY < 3 * vh) {
        activeIndex = Math.min(2, Math.floor(scrollY / vh));
        progress = 0;
      } else if (scrollY >= 3 * vh && scrollY < 8 * vh) {
        activeIndex = 3;
        progress = Math.min(400, Math.max(0, ((scrollY - 3 * vh) / vh) * 100));
      } else {
        activeIndex = Math.min(6, 4 + Math.floor((scrollY - 8 * vh) / vh));
        progress = 400;
      }"""
content = re.sub(r'if \(scrollY < 3 \* vh\) \{[\s\S]*?progress = 100;\n      \}', handle_scroll_new, content)

# 2. snapTarget logic
snap_target_new = """          if (currentScroll < 3 * vh) {
            snapTarget = Math.round(currentScroll / vh) * vh;
          } else if (currentScroll >= 3 * vh && currentScroll < 8 * vh) {
            // DO NOT SNAP DURING SPLIT REVEAL OR CARD STACKING
            snapTarget = currentScroll;
          } else {
            const offsetScroll = currentScroll - 8 * vh;
            const slideIndexAfter4 = Math.round(offsetScroll / vh);
            snapTarget = 8 * vh + slideIndexAfter4 * vh;
          }"""
content = re.sub(r'if \(currentScroll < 3 \* vh\) \{[\s\S]*?snapTarget = 4 \* vh \+ slideIndexAfter4 \* vh;\n          \}', snap_target_new, content)

# 3. changeSlide logic
change_slide_new = """    if (typeof direction === "number") {
      if (direction < 3) targetScroll = direction * vh;
      else if (direction === 3) targetScroll = 3 * vh;
      else targetScroll = (8 + direction - 4) * vh;
    } else if (direction === "next") {
      if (currentSlide === 3 && splitProgress < 400) {
        const nextPhase = Math.floor(splitProgress / 100) + 1;
        targetScroll = (3 + nextPhase) * vh;
      } else {
        const nextSlide = Math.min(6, currentSlide + 1);
        if (nextSlide < 3) targetScroll = nextSlide * vh;
        else if (nextSlide === 3) targetScroll = 3 * vh;
        else targetScroll = (8 + nextSlide - 4) * vh;
      }
    } else {
      if (currentSlide === 3 && splitProgress > 0) {
        const prevPhase = Math.ceil(splitProgress / 100) - 1;
        targetScroll = (3 + prevPhase) * vh;
      } else {
        const prevSlide = Math.max(0, currentSlide - 1);
        if (prevSlide < 3) targetScroll = prevSlide * vh;
        else if (prevSlide === 3) targetScroll = 7 * vh; // End of slide 3
        else targetScroll = (8 + prevSlide - 4) * vh;
      }
    }"""
content = re.sub(r'if \(typeof direction === "number"\) \{[\s\S]*?targetScroll = Math\.max\(0, currentSlide - 1\) \* vh;\n      \}', change_slide_new, content)

# 4. Math.min(6 * vh) -> Math.min(10 * vh)
content = content.replace('Math.min(6 * vh, Math.max(0, snapTarget))', 'Math.min(10 * vh, Math.max(0, snapTarget))')

# 5. height: "700vh" -> "1100vh"
content = content.replace('height: "700vh"', 'height: "1100vh"')

with open('src/App.tsx', 'w') as f:
    f.write(content)
