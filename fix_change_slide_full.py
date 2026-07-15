import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

start = content.find('const changeSlide = (direction')
end = content.find('lenisRef.current.scrollTo(targetScroll, { duration: 1.4 });')
end_full = content.find('};', end) + 2

bad_change = content[start:end_full]

good_change = """const changeSlide = (direction: "next" | "prev" | number) => {
    if (!lenisRef.current) return;
    const vh = window.innerHeight || 800;
    const numProjects = PROJECTS.length; // 3
    const workEndVh = 3 + numProjects + 1; // 7

    let targetScroll = 0;

    if (typeof direction === "number") {
      if (direction < 3) targetScroll = direction * vh;
      else if (direction === 3) targetScroll = 3 * vh;
      else targetScroll = (workEndVh + direction - 4) * vh;
    } else if (direction === "next") {
      if (currentSlide === 3 && splitProgress < numProjects * 100) {
        const currentPhase = Math.floor(splitProgress / 100);
        targetScroll = (3 + currentPhase + 1) * vh;
      } else {
        const nextSlide = Math.min(6, currentSlide + 1);
        if (nextSlide < 3) targetScroll = nextSlide * vh;
        else if (nextSlide === 3) targetScroll = 3 * vh;
        else targetScroll = (workEndVh + nextSlide - 4) * vh;
      }
    } else {
      if (currentSlide === 3 && splitProgress > 0) {
        const currentPhase = Math.ceil(splitProgress / 100);
        targetScroll = (3 + currentPhase - 1) * vh;
      } else {
        const prevSlide = Math.max(0, currentSlide - 1);
        if (prevSlide < 3) targetScroll = prevSlide * vh;
        else if (prevSlide === 3) targetScroll = (workEndVh - 1) * vh;
        else targetScroll = (workEndVh + prevSlide - 4) * vh;
      }
    }

    lenisRef.current.scrollTo(targetScroll, { duration: 1.4 });
  };"""

content = content.replace(bad_change, good_change)

with open('src/App.tsx', 'w') as f:
    f.write(content)
