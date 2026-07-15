import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

bad = """            <motion.div 
              className="flex whitespace-nowrap gap-8 items-center py-4"
              animate={{ x: [0, -1035] }}
              transition={{ repeat: Infinity, ease: "linear", duration: 20 }}
            >
              {[...STACK, ...STACK].map((tech, i) => (
                <div key={i} className="text-2xl md:text-4xl font-display font-bold text-white/5 uppercase tracking-widest hover:text-blue-500/30 transition-colors duration-500 select-none">
                  {tech}
                </div>
              ))}
            </motion.div>"""

good = """            <motion.div 
              className="flex whitespace-nowrap gap-8 items-center py-4 w-max"
              animate={{ x: ["0%", "-50%"] }}
              transition={{ repeat: Infinity, ease: "linear", duration: 20 }}
            >
              {[...STACK, ...STACK, ...STACK, ...STACK].map((tech, i) => (
                <div key={i} className="text-2xl md:text-4xl font-display font-bold text-white/5 uppercase tracking-widest hover:text-blue-500/30 transition-colors duration-500 select-none pr-8">
                  {tech}
                </div>
              ))}
            </motion.div>"""

content = content.replace(bad, good)

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
