import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Fix Slide 0
bad_slide0 = """                </div>
              </div>
              </ScrollLocker>
            </motion.div>
          )}

          {currentSlide === 1 && ("""

good_slide0 = """                </div>
              </div>
            </motion.div>
          )}

          {currentSlide === 1 && ("""

content = content.replace(bad_slide0, good_slide0)

# Slide 7 was supposed to be:
#             </motion.div>
#           )}
# But because the first match replaced Slide 0, Slide 7 might not have been replaced!
# Let's check if Slide 7 has </ScrollLocker>

with open('src/App.tsx', 'w') as f:
    f.write(content)
