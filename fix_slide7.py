import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

bad = """                </footer>
              </div>
            </motion.div>
          )}
        </AnimatePresence>"""

good = """                </footer>
              </div>
              </ScrollLocker>
            </motion.div>
          )}
        </AnimatePresence>"""

content = content.replace(bad, good)

with open('src/App.tsx', 'w') as f:
    f.write(content)
