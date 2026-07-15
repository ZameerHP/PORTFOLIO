import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Remove ALL </ScrollLocker>
content = content.replace('              </ScrollLocker>\n', '')
content = content.replace('            </ScrollLocker>\n', '')
content = content.replace('          </ScrollLocker>\n', '')
content = content.replace('</ScrollLocker>', '')

# Now re-add it only at the correct places
# For slide 4:
skills_start = '<ScrollLocker\n                id="skills-slide-screen"'
if skills_start in content:
    # Find the </motion.div> for slide 4
    # The inner content is <SkillsSection />
    old_skills_end = """                <SkillsSection />
            </motion.div>
          )}"""
    
    new_skills_end = """                <SkillsSection />
              </ScrollLocker>
            </motion.div>
          )}"""
    content = content.replace(old_skills_end, new_skills_end)

# For slide 7:
faq_start = '<ScrollLocker\n                id="faq-contact-slide-screen"'
if faq_start in content:
    old_faq_end = """                </footer>
              </div>
            </motion.div>
          )}
        </AnimatePresence>"""
    
    new_faq_end = """                </footer>
              </div>
              </ScrollLocker>
            </motion.div>
          )}
        </AnimatePresence>"""
    content = content.replace(old_faq_end, new_faq_end)

with open('src/App.tsx', 'w') as f:
    f.write(content)
