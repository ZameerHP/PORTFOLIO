import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_code = """      if (!isScrollingProgrammatically) {
        clearTimeout(snapTimeout);
        snapTimeout = setTimeout(() => {
          const currentScroll = lenis.scroll;
          let snapTarget = 0;

                              const numProjects = PROJECTS.length;
          const workEndVh = 3 + numProjects + 1;
          if (currentScroll < 3 * vh) {
            snapTarget = Math.round(currentScroll / vh) * vh;
          } else if (currentScroll >= 3 * vh && currentScroll < workEndVh * vh) {
            // DO NOT SNAP DURING SPLIT REVEAL OR CARD STACKING
            snapTarget = currentScroll;
          } else {
            const offsetScroll = currentScroll - workEndVh * vh;
            const slideIndexAfter4 = Math.round(offsetScroll / vh);
            snapTarget = workEndVh * vh + slideIndexAfter4 * vh;
          }

          snapTarget = Math.min(9 * vh, Math.max(0, snapTarget));

          isScrollingProgrammatically = true;
          lenis.scrollTo(snapTarget, { 
            duration: 1.4,
            onComplete: () => {
              isScrollingProgrammatically = false;
            }
          });
        }, 150);
      }"""

content = content.replace(old_code, "")

with open('src/App.tsx', 'w') as f:
    f.write(content)
