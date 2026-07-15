import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad_snap = """          if (currentScroll < 3 * vh) {
            snapTarget = Math.round(currentScroll / vh) * vh;
          } else if (currentScroll >= 3 * vh && currentScroll < workEndVh * vh) {
            // DO NOT SNAP DURING SPLIT REVEAL OR CARD STACKING
            snapTarget = currentScroll;
          } else {
            const offsetScroll = currentScroll - workEndVh * vh;
            const slideIndexAfter4 = Math.round(offsetScroll / vh);
            snapTarget = workEndVh * vh + slideIndexAfter4 * vh;
          }"""

good_snap = """          snapTarget = Math.round(currentScroll / vh) * vh;"""

content = content.replace(bad_snap, good_snap)

# Also fix the manual changeSlide logic to align with workEndVh
bad_change = """    if (typeof direction === "number") {
      targetScroll = direction * vh;
    } else if (direction === "next") {
      if (currentSlide === 4 && splitProgress < 100) {
        lenisRef.current.scrollTo(5 * vh, { duration: 1.4 });
        return;
      }
      targetScroll = Math.min(6, currentSlide + 1) * vh;
    } else {
      if (currentSlide === 4 && splitProgress > 0) {
        lenisRef.current.scrollTo(4 * vh, { duration: 1.4 });
        return;
      }
      targetScroll = Math.max(0, currentSlide - 1) * vh;
    }"""

# We just need simple targetScroll logic since every slide is exactly 1 vh.
# Wait, currentSlide is activeIndex.
# Slide 0..2 (3 slides). Slide 3 is the WORK attach.
# Slides 4..5..6 are projects. Slide 7 is Method...
# Let's check how activeIndex maps to vh.
