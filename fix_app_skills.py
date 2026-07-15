import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad = """          {currentSlide === 4 && (
            <SkillsSection slideDirection={slideDirection} />
          )}"""

good = """          {currentSlide === 4 && (
            <motion.div
              key="skills-slide"
              custom={{ index: 4, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 5 }}
              className="absolute inset-0 w-full h-full bg-[#0a0a0a] flex flex-col justify-center overflow-hidden"
              id="skills-slide-screen"
            >
              <SkillsSection />
            </motion.div>
          )}"""

content = content.replace(bad, good)

with open('src/App.tsx', 'w') as f:
    f.write(content)
