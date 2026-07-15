import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

# I will just replace the first </> that comes right after the </div> for the progress bar.
# Actually, the SkillCard ends with:
#         </div>
#       </div>
#     </>
#   );
# };
# I'll specifically target this pattern in SkillCard

pattern = """        </div>
      </div>
    </>
  );
};

export const SkillsSection"""

replacement = """        </div>
      </div>
    </motion.div>
  );
};

export const SkillsSection"""

content = content.replace(pattern, replacement)

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
