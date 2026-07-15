import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add useTransforms after useMotionValue
transform_code = """  const splitProgress = useMotionValue(0);
  const woX = useTransform(splitProgress, (v: number) => `calc(-${(Math.min(100, v) / 100) * 80}vw)`);
  const rkX = useTransform(splitProgress, (v: number) => `calc(${(Math.min(100, v) / 100) * 80}vw)`);"""

content = content.replace('  const splitProgress = useMotionValue(0);', transform_code)

bad_wo = """                  <div style={{ transform: `translateX(calc(-${(Math.min(100, splitProgress) / 100) * 80}vw))` }} className="will-change-transform flex items-center">
                    WO
                  </div>"""

good_wo = """                  <motion.div style={{ x: woX }} className="will-change-transform flex items-center">
                    WO
                  </motion.div>"""

bad_rk = """                  <div style={{ transform: `translateX(calc(${(Math.min(100, splitProgress) / 100) * 80}vw))` }} className="will-change-transform flex items-center">
                    RK
                  </div>"""

good_rk = """                  <motion.div style={{ x: rkX }} className="will-change-transform flex items-center">
                    RK
                  </motion.div>"""

content = content.replace(bad_wo, good_wo)
content = content.replace(bad_rk, good_rk)

with open('src/App.tsx', 'w') as f:
    f.write(content)
