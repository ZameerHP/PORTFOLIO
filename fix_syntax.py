import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad_logic = """      if (scrollY < 3 * vh) {
        activeIndex = Math.min(2, Math.floor(scrollY / vh));
        progress = 0;
      } else if (scrollY >= 3 * vh && scrollY < workEndVh * vh) {
        activeIndex = 3;
        progress = Math.min(workScrolls * 100, Math.max(0, ((scrollY - 3 * vh) / vh) * 100));
      } else {
        activeIndex = Math.min(6, 4 + Math.floor((scrollY - workEndVh * vh) / vh));
        progress = workScrolls * 100;
      } else if (scrollY >= 3 * vh && scrollY < workEndVh * vh) {
        activeIndex = 3;
        progress = Math.min(workScrolls * 100, Math.max(0, ((scrollY - 3 * vh) / vh) * 100));
      } else {
        activeIndex = Math.min(6, 4 + Math.floor((scrollY - workEndVh * vh) / vh));
        progress = workScrolls * 100;
      }"""

good_logic = """      if (scrollY < 3 * vh) {
        activeIndex = Math.min(2, Math.floor(scrollY / vh));
        progress = 0;
      } else if (scrollY >= 3 * vh && scrollY < workEndVh * vh) {
        activeIndex = 3;
        progress = Math.min(workScrolls * 100, Math.max(0, ((scrollY - 3 * vh) / vh) * 100));
      } else {
        activeIndex = Math.min(6, 4 + Math.floor((scrollY - workEndVh * vh) / vh));
        progress = workScrolls * 100;
      }"""

content = content.replace(bad_logic, good_logic)

with open('src/App.tsx', 'w') as f:
    f.write(content)
