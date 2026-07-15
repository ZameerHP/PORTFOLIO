import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

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
              <div className="absolute top-28 left-6 right-6 md:left-12 md:right-12 flex flex-col md:flex-row justify-between items-start md:items-end gap-2 z-[60] pointer-events-none" id="reveal-header-labels">
                <div className="space-y-1">
                  <span className="font-mono text-xs tracking-widest uppercase text-[#ff4f1d] block">
                    03 // OUR SIGNATURE WORK
                  </span>
                  <h3 className="font-display text-2xl md:text-3xl font-black uppercase tracking-widest text-black">
                    SELECTED PROJECTS
                  </h3>
                </div>
                <div className="font-mono text-[10px] tracking-widest uppercase text-black/40">
                  ESTABLISHED IN 2026
                </div>
              </div>

              {PROJECTS.map((project, idx) => {
                let styles = {};
                if (idx === 0) {
                  const p0 = Math.min(100, splitProgress) / 100;
                  styles = {
                    opacity: p0,
                    transform: `translateY(${(1 - p0) * 80}px) scale(${0.9 + p0 * 0.1})`,
                    zIndex: 9
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
                    className="absolute inset-0 flex items-center justify-center will-change-transform"
                    style={styles}
                  >
                    <div className="relative w-[90%] md:w-[80%] h-[70vh] max-h-[800px] rounded-[18px] overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.15)] group transition-all duration-700 hover:scale-[1.02] hover:shadow-[0_30px_60px_rgba(0,0,0,0.25)] pointer-events-auto">
                      <img 
                        src={project.image} 
                        alt={project.title}
                        className="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
                        referrerPolicy="no-referrer"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent pointer-events-none" />
                      
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

                      <div className="absolute bottom-0 left-0 right-0 p-8 md:p-12 pointer-events-none text-white z-10">
                        <h3 className="font-display text-4xl md:text-6xl font-black uppercase tracking-tight mb-2">
                          {project.title}
                        </h3>
                        <p className="font-sans text-lg md:text-xl text-white/80 max-w-2xl">
                          {project.description}
                        </p>
                      </div>
                    </div>
                  </div>
                );
              })}
              
              <div className="absolute inset-0 flex items-center justify-center pointer-events-none z-[10]" style={{ opacity: splitProgress >= 100 ? 0 : 1 }}>
                <div className="font-display font-black text-[22vw] leading-none text-black uppercase tracking-tighter flex">
                  <span style={{ transform: `translateX(calc(-${(Math.min(100, splitProgress) / 100) * 100}vw))` }} className="will-change-transform">W</span>
                  <span style={{ transform: `translateX(calc(-${(Math.min(100, splitProgress) / 100) * 50}vw))` }} className="will-change-transform">O</span>
                  <span style={{ transform: `translateX(calc(${(Math.min(100, splitProgress) / 100) * 50}vw))` }} className="will-change-transform">R</span>
                  <span style={{ transform: `translateX(calc(${(Math.min(100, splitProgress) / 100) * 100}vw))` }} className="will-change-transform">K</span>
                </div>
              </div>

            </motion.div>
          )}"""

# We need to replace from {currentSlide === 3 && ( to the next {currentSlide === 4 && (
start_idx = content.find('{currentSlide === 3 && (')
end_idx = content.find('{currentSlide === 4 && (')
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + slide_3_new + '\n\n' + content[end_idx:]
else:
    print("Could not find boundaries")

with open('src/App.tsx', 'w') as f:
    f.write(content)
