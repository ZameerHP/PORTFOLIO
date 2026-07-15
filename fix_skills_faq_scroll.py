import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add import
if 'import { ScrollLocker }' not in content:
    content = content.replace('import { SkillsSection } from "./components/SkillsSection";', 'import { SkillsSection } from "./components/SkillsSection";\nimport { ScrollLocker } from "./components/ScrollLocker";')

bad_skills = """          {currentSlide === 4 && (
            <motion.div
              key="skills-slide"
              custom={{ index: 4, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 5 }}
              className="absolute inset-0 w-full h-full bg-[#0a0a0a] overflow-y-auto overflow-x-hidden custom-scrollbar"
              id="skills-slide-screen"
            >
              <SkillsSection />
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

content = content.replace(bad_skills, good_skills)


bad_faq = """          {currentSlide === 7 && (
            <motion.div
              key="faq-contact-slide"
              custom={{ index: 7, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 8 }}
              className="absolute inset-0 w-full h-full bg-[#121212] overflow-y-auto pt-24 pb-12"
              id="faq-contact-slide-screen"
            >"""

good_faq = """          {currentSlide === 7 && (
            <motion.div
              key="faq-contact-slide"
              custom={{ index: 7, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 8 }}
              className="absolute inset-0 w-full h-full bg-[#121212]"
            >
              <ScrollLocker
                id="faq-contact-slide-screen"
                className="absolute inset-0 w-full h-full pt-24 pb-12 custom-scrollbar"
                onNext={() => changeSlide("next")}
                onPrev={() => changeSlide("prev")}
              >"""

content = content.replace(bad_faq, good_faq)


bad_faq_end = """                </div>
              </div>
            </motion.div>
          )}"""

good_faq_end = """                </div>
              </div>
              </ScrollLocker>
            </motion.div>
          )}"""

content = content.replace(bad_faq_end, good_faq_end)

with open('src/App.tsx', 'w') as f:
    f.write(content)
