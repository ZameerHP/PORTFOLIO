import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# I want to replace:
#                 </footer>
#               </div>
#             </motion.div>
#           )}
#         </AnimatePresence>
# with:
#                 </footer>
#               </div>
#               </ScrollLocker>
#             </motion.div>
#           )}
#         </AnimatePresence>

# Using regex to be safe about spaces
pattern = r'(</footer>\s*</div>\s*)(</motion\.div>\s*\)\}\s*</AnimatePresence>)'
content = re.sub(pattern, r'\1</ScrollLocker>\n            \2', content)

with open('src/App.tsx', 'w') as f:
    f.write(content)
