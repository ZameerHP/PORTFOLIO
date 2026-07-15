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
              {/* Central text WO RK */}
              <div className="absolute inset-0 flex items-center justify-center pointer-events-none z-[5]">
                <div className="font-display font-black text-[28vw] md:text-[24vw] leading-none text-[#111111] uppercase tracking-tighter flex items-center justify-center">
                  <span style={{ transform: `translateX(calc(-${(Math.min(100, splitProgress) / 100) * 100}vw))` }} className="will-change-transform">WO</span>
                  <div style={{ width: "240px" }} className="flex-shrink-0 md:w-[320px]" />
                  <span style={{ transform: `translateX(calc(${(Math.min(100, splitProgress) / 100) * 100}vw))` }} className="will-change-transform">RK</span>
                </div>
              </div>

              {/* Central Image (Man Portrait) */}
              <div className="absolute inset-0 flex items-center justify-center pointer-events-none z-[10]">
                <div 
                  className="overflow-hidden will-change-transform shadow-2xl relative"
                  style={{
                    width: `calc(max(240px, 20vw) + (100vw - max(240px, 20vw)) * ${Math.min(100, splitProgress) / 100})`,
                    height: `calc(max(340px, 30vh) + (100vh - max(340px, 30vh)) * ${Math.min(100, splitProgress) / 100})`,
                    borderRadius: `${18 * (1 - (Math.min(100, splitProgress) / 100))}px`,
                  }}
                >
                  <img 
                    src={PORTRAITS.gelPortrait} 
                    alt="Man Portrait"
                    className="w-full h-full object-cover"
                  />
                </div>
              </div>

              {/* The 3 Full-Screen Projects */}
              {PROJECTS.map((project, idx) => {
                const startProgress = (idx + 1) * 100;
                const p = Math.min(100, Math.max(0, splitProgress - startProgress)) / 100;
                
                return (
                  <div 
                    key={project.id}
                    className="absolute inset-0 flex flex-col items-center justify-center text-center will-change-transform pointer-events-auto shadow-[0_-20px_50px_rgba(0,0,0,0.5)]"
                    style={{
                      transform: `translateY(${(1 - p) * 100}vh)`,
                      zIndex: 20 + idx,
                    }}
                  >
                    <img 
                      src={project.image} 
                      alt={project.title}
                      className="absolute inset-0 w-full h-full object-cover"
                    />
                    <div className="absolute inset-0 bg-black/40 pointer-events-none" />
                    
                    <div className="relative z-10 px-6 max-w-5xl mx-auto flex flex-col items-center justify-center">
                      <h3 className="font-display text-4xl md:text-7xl lg:text-[90px] font-black uppercase tracking-tight text-white mb-6 md:mb-8 leading-none">
                        {project.title}
                      </h3>
                      <p className="font-sans text-lg md:text-2xl text-white max-w-3xl leading-relaxed">
                        {project.description}
                      </p>
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
else:
    print("Could not find boundaries")

# Update the spacer matching width in the script to use clamp/max to match the inline CSS precisely if needed,
# But we can just use css vars or a static 240px for the text gap, and max(240px, 20vw) for the image width.
# To make it perfectly align, let's just replace `width: "240px"` with `width: "max(240px, 20vw)"`
content = content.replace('width: "240px"', 'width: "max(240px, 20vw)"')

with open('src/App.tsx', 'w') as f:
    f.write(content)
