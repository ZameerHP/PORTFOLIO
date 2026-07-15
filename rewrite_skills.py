import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

# Imports: Add useState, AnimatePresence
import_motion_old = 'import { motion } from "motion/react";'
import_motion_new = 'import { motion, AnimatePresence } from "motion/react";\nimport { useState } from "react";'
content = content.replace(import_motion_old, import_motion_new)

# Replace Icons
icons_old = 'Cpu\n} from "lucide-react";'
icons_new = 'Cpu,\n  ArrowRight,\n  ArrowLeft\n} from "lucide-react";'
content = content.replace(icons_old, icons_new)

# Define skills data
skills_old = '''const CAPABILITIES = [
  { name: "Pixel-Perfect UI", icon: Layout },
  { name: "Premium UI/UX Design", icon: Figma },
  { name: "Responsive Dev", icon: Smartphone },
  { name: "Smooth Animations", icon: Sparkles },
  { name: "Performance Optimization", icon: Zap },
  { name: "AI Integration", icon: Bot }
];'''

skills_new = '''const FRONTEND_SKILLS = [
  { name: "HTML", icon: Layout },
  { name: "CSS", icon: Figma },
  { name: "JavaScript", icon: Code2 },
  { name: "Tailwind CSS", icon: Sparkles },
  { name: "React", icon: Smartphone }
];

const BACKEND_SKILLS = [
  { name: "Node.js", icon: Cpu },
  { name: "Express.js", icon: Zap },
  { name: "REST APIs", icon: Globe }
];'''
content = content.replace(skills_old, skills_new)

# Update component definition
comp_old = 'export const SkillsSection = () => {'
comp_new = 'export const SkillsSection = () => {\n  const [skillType, setSkillType] = useState<"frontend" | "backend">("frontend");'
content = content.replace(comp_old, comp_new)

# Update the grid area
grid_old = '''          <div className="col-span-1 md:col-span-8 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {CAPABILITIES.map((cap, i) => (
              <FadeIn key={i} delay={0.3 + (i * 0.05)} className="h-full">
                <div className="group p-6 rounded-xl bg-white/[0.02] border border-white/5 hover:border-[#ff4f1d]/30 transition-all duration-500 hover:bg-[#ff4f1d]/[0.02] flex flex-col gap-4 h-full relative overflow-hidden">
                  <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-100 transition-opacity duration-500">
                     <cap.icon strokeWidth={1} className="w-24 h-24 text-[#ff4f1d] -mt-8 -mr-8 transform rotate-12 group-hover:scale-110 transition-transform duration-700" />
                  </div>
                  <div className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center text-white/50 group-hover:text-[#ff4f1d] group-hover:bg-[#ff4f1d]/10 transition-colors duration-500 border border-white/5 relative z-10">
                    <cap.icon strokeWidth={1.5} className="w-4 h-4" />
                  </div>
                  <h3 className="text-sm md:text-base font-display font-bold text-white/80 group-hover:text-white transition-colors uppercase tracking-wide relative z-10">{cap.name}</h3>
                </div>
              </FadeIn>
            ))}
          </div>'''

grid_new = '''          <div className="col-span-1 md:col-span-8 flex flex-col gap-4">
            <FadeIn delay={0.3}>
              <div className="flex items-center justify-center gap-6 mb-2">
                <AnimatePresence mode="wait">
                  <motion.h2 
                    key={skillType}
                    initial={{ opacity: 0, y: -10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: 10 }}
                    transition={{ duration: 0.3 }}
                    className="text-2xl md:text-3xl font-display font-black tracking-tight text-white uppercase text-center w-40"
                  >
                    {skillType === "frontend" ? "FRONTEND" : "BACKEND"}
                  </motion.h2>
                </AnimatePresence>
                <button 
                  onClick={() => setSkillType(prev => prev === "frontend" ? "backend" : "frontend")}
                  className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center text-white hover:text-black hover:bg-white border border-white/10 transition-colors duration-500 cursor-pointer pointer-events-auto"
                >
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </FadeIn>
            
            <div className="relative min-h-[300px] w-full">
              <AnimatePresence mode="wait">
                <motion.div
                  key={skillType}
                  initial={{ opacity: 0, x: 50 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -50 }}
                  transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
                  className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 absolute inset-0 pointer-events-auto"
                >
                  {(skillType === "frontend" ? FRONTEND_SKILLS : BACKEND_SKILLS).map((cap, i) => (
                    <div key={i} className="group p-6 rounded-xl bg-white/[0.02] border border-white/5 hover:border-[#ff4f1d]/30 transition-all duration-500 hover:bg-[#ff4f1d]/[0.02] flex flex-col gap-4 relative overflow-hidden">
                      <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-100 transition-opacity duration-500">
                         <cap.icon strokeWidth={1} className="w-24 h-24 text-[#ff4f1d] -mt-8 -mr-8 transform rotate-12 group-hover:scale-110 transition-transform duration-700" />
                      </div>
                      <div className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center text-white/50 group-hover:text-[#ff4f1d] group-hover:bg-[#ff4f1d]/10 transition-colors duration-500 border border-white/5 relative z-10">
                        <cap.icon strokeWidth={1.5} className="w-4 h-4" />
                      </div>
                      <h3 className="text-sm md:text-base font-display font-bold text-white/80 group-hover:text-white transition-colors uppercase tracking-wide relative z-10">{cap.name}</h3>
                    </div>
                  ))}
                </motion.div>
              </AnimatePresence>
            </div>
          </div>'''

content = content.replace(grid_old, grid_new)

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
