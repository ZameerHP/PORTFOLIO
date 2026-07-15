import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Update handleScroll
handle_scroll_new = """      const numProjects = PROJECTS.length;
      const workScrolls = numProjects; // 3
      const workEndVh = 3 + workScrolls; // 6

      if (scrollY < 3 * vh) {
        activeIndex = Math.min(2, Math.floor(scrollY / vh));
        progress = 0;
      } else if (scrollY >= 3 * vh && scrollY < workEndVh * vh) {
        activeIndex = 3;
        progress = Math.min(workScrolls * 100, Math.max(0, ((scrollY - 3 * vh) / vh) * 100));
      } else {
        activeIndex = Math.min(6, 4 + Math.floor((scrollY - workEndVh * vh) / vh));
        progress = workScrolls * 100;
      }"""
content = re.sub(r'if \(scrollY < 3 \* vh\) \{[\s\S]*?progress = 400;\n      \}', handle_scroll_new, content)
content = re.sub(r'if \(scrollY < 3 \* vh\) \{[\s\S]*?progress = 300;\n      \}', handle_scroll_new, content)
content = re.sub(r'if \(scrollY < 3 \* vh\) \{[\s\S]*?progress = \d+;\n      \}', handle_scroll_new, content)

# 2. Update snapTarget
snap_target_new = """          const numProjects = PROJECTS.length;
          const workEndVh = 3 + numProjects;
          if (currentScroll < 3 * vh) {
            snapTarget = Math.round(currentScroll / vh) * vh;
          } else if (currentScroll >= 3 * vh && currentScroll < workEndVh * vh) {
            // DO NOT SNAP DURING SPLIT REVEAL OR CARD STACKING
            snapTarget = currentScroll;
          } else {
            const offsetScroll = currentScroll - workEndVh * vh;
            const slideIndexAfter4 = Math.round(offsetScroll / vh);
            snapTarget = workEndVh * vh + slideIndexAfter4 * vh;
          }"""
content = re.sub(r'if \(currentScroll < 3 \* vh\) \{[\s\S]*?snapTarget = 7 \* vh \+ slideIndexAfter4 \* vh;\n          \}', snap_target_new, content)
content = re.sub(r'if \(currentScroll < 3 \* vh\) \{[\s\S]*?snapTarget = \d+ \* vh \+ slideIndexAfter4 \* vh;\n          \}', snap_target_new, content)

# 3. Update changeSlide
change_slide_new = """    const numProjects = PROJECTS.length;
    const workEndVh = 3 + numProjects;
    
    if (typeof direction === "number") {
      if (direction < 3) targetScroll = direction * vh;
      else if (direction === 3) targetScroll = 3 * vh;
      else targetScroll = (workEndVh + direction - 4) * vh;
    } else if (direction === "next") {
      if (currentSlide === 3 && splitProgress < numProjects * 100) {
        const nextPhase = Math.floor(splitProgress / 100) + 1;
        targetScroll = (3 + nextPhase) * vh;
      } else {
        const nextSlide = Math.min(6, currentSlide + 1);
        if (nextSlide < 3) targetScroll = nextSlide * vh;
        else if (nextSlide === 3) targetScroll = 3 * vh;
        else targetScroll = (workEndVh + nextSlide - 4) * vh;
      }
    } else {
      if (currentSlide === 3 && splitProgress > 0) {
        const prevPhase = Math.ceil(splitProgress / 100) - 1;
        targetScroll = (3 + prevPhase) * vh;
      } else {
        const prevSlide = Math.max(0, currentSlide - 1);
        if (prevSlide < 3) targetScroll = prevSlide * vh;
        else if (prevSlide === 3) targetScroll = (workEndVh - 1) * vh; // End of slide 3
        else targetScroll = (workEndVh + prevSlide - 4) * vh;
      }
    }"""
content = re.sub(r'if \(typeof direction === "number"\) \{[\s\S]*?targetScroll = \(7 \+ prevSlide - 4\) \* vh;\n      \}', change_slide_new, content)
content = re.sub(r'if \(typeof direction === "number"\) \{[\s\S]*?targetScroll = \(\d+ \+ prevSlide - 4\) \* vh;\n      \}', change_slide_new, content)

# Update Math.min scroll bounds
content = re.sub(r'Math\.min\(\d+ \* vh, Math\.max\(0, snapTarget\)\)', 'Math.min(9 * vh, Math.max(0, snapTarget))', content)

# 4. Update Slide 3 Content
slide_3_new = """          {currentSlide === 3 && (
            <motion.div
              key="reveal-slide"
              custom={{ index: 3, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 4 }}
              className="absolute inset-0 w-full h-full bg-[#F6EEDC] flex flex-col justify-center items-center overflow-hidden"
              id="reveal-slide-screen"
            >
              {/* Central text WORK perfectly together at 0, splits apart as scroll */}
              <div className="absolute inset-0 flex items-center justify-center pointer-events-none z-[5]">
                <div className="font-display font-black text-[22vw] leading-none text-[#111111] uppercase tracking-tighter flex items-center justify-center">
                  <div style={{ transform: `translateX(calc(-${(Math.min(100, splitProgress) / 100) * 80}vw))` }} className="flex will-change-transform">
                    <span>W</span><span>O</span>
                  </div>
                  <div style={{ transform: `translateX(calc(${(Math.min(100, splitProgress) / 100) * 80}vw))` }} className="flex will-change-transform">
                    <span>R</span><span>K</span>
                  </div>
                </div>
              </div>

              {/* The Full-Screen Projects */}
              {PROJECTS.map((project, idx) => {
                let styles = {};
                if (idx === 0) {
                  const p0 = Math.min(100, splitProgress) / 100;
                  styles = {
                    opacity: p0,
                    transform: `translateY(${(1 - p0) * 80}px) scale(${0.9 + p0 * 0.1})`,
                    zIndex: 10
                  };
                } else {
                  const startProgress = idx * 100;
                  const p = Math.min(100, Math.max(0, splitProgress - startProgress)) / 100;
                  styles = {
                    transform: `translateY(${(1 - p) * 100}vh)`,
                    zIndex: 10 + idx,
                  };
                }

                return (
                  <div 
                    key={project.id}
                    className="absolute inset-0 flex items-center justify-center will-change-transform pointer-events-none"
                    style={styles}
                  >
                    <div className="relative w-[90%] md:w-[85%] lg:w-[80%] h-[75vh] max-h-[800px] rounded-[18px] overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.2)] group transition-all duration-700 hover:scale-[1.01] hover:shadow-[0_30px_60px_rgba(0,0,0,0.3)] pointer-events-auto cursor-pointer">
                      <img 
                        src={project.image} 
                        alt={project.title}
                        className="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
                        referrerPolicy="no-referrer"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent pointer-events-none transition-opacity duration-500 group-hover:opacity-90" />
                      
                      <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none z-20">
                        <a 
                          href="#" 
                          target="_blank" 
                          rel="noopener noreferrer"
                          className="pointer-events-auto bg-black text-white px-[34px] py-[16px] rounded-full font-sans font-bold text-sm tracking-wider uppercase transform translate-y-4 group-hover:translate-y-0 transition-all duration-500 hover:scale-105"
                        >
                          VIEW PROJECT
                        </a>
                      </div>

                      <div className="absolute bottom-0 left-0 right-0 p-8 md:p-12 pointer-events-none text-white z-10 flex flex-col gap-3">
                        <h3 className="font-display text-4xl md:text-5xl lg:text-6xl font-black uppercase tracking-tight leading-none">
                          {project.title}
                        </h3>
                        <p className="font-sans text-base md:text-lg lg:text-xl text-white/90 max-w-2xl font-medium">
                          {project.description}
                        </p>
                      </div>
                    </div>
                  </div>
                );
              })}
            </motion.div>
          )}"""

start_idx = content.find('{currentSlide === 3 && (')
end_idx = content.find('{currentSlide === 4 && (')
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + slide_3_new + '\n\n          ' + content[end_idx:]

with open('src/App.tsx', 'w') as f:
    f.write(content)
