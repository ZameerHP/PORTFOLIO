import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad_skills = """          {currentSlide === 4 && (
            <motion.div
              key="skills-slide"
              custom={{ index: 4, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 5 }}
              className="absolute inset-0 w-full h-full bg-[#0a0a0a]"
            >
              <ScrollLocker
                id="skills-slide-screen"
                className="absolute inset-0 w-full h-full custom-scrollbar"
                onNext={() => changeSlide("next")}
                onPrev={() => changeSlide("prev")}
              >
                <SkillsSection />
              </ScrollLocker>
            </motion.div>
          )}"""

good_skills = """          {currentSlide === 4 && (
            <motion.div
              key="skills-slide"
              custom={{ index: 4, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 5 }}
              className="absolute inset-0 w-full h-full bg-[#0d0d0d]"
              id="skills-slide-screen"
            >
              <SkillsSection />
            </motion.div>
          )}"""

content = content.replace(bad_skills, good_skills)

with open('src/App.tsx', 'w') as f:
    f.write(content)
