import os

content = """import React from "react";
import { motion } from "motion/react";
import { 
  Code2, 
  Figma, 
  Layout, 
  Sparkles, 
  Smartphone, 
  Zap, 
  Search, 
  Bot, 
  Globe, 
  ShieldCheck,
  Cpu
} from "lucide-react";

const STACK = [
  "HTML5", "CSS3", "JavaScript", "TypeScript", "React", "Next.js", 
  "Tailwind CSS", "Framer Motion", "GSAP", "Firebase", "Supabase", 
  "Git & GitHub", "Figma", "Vercel"
];

const CAPABILITIES = [
  { name: "Pixel-Perfect UI", icon: Layout },
  { name: "Premium UI/UX Design", icon: Figma },
  { name: "Responsive Dev", icon: Smartphone },
  { name: "Smooth Animations", icon: Sparkles },
  { name: "Performance Optimization", icon: Zap },
  { name: "AI Integration", icon: Bot }
];

const STATS = [
  { label: "Projects Completed", value: "50+" },
  { label: "Responsive Design", value: "100%" },
  { label: "Performance", value: "99" }
];

const FadeIn: React.FC<{ children: React.ReactNode; delay?: number; className?: string }> = ({ children, delay = 0, className = "" }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: 0.8, delay, ease: [0.16, 1, 0.3, 1] }}
      className={className}
    >
      {children}
    </motion.div>
  );
};

export const SkillsSection = () => {
  return (
    <div className="w-full h-full flex flex-col justify-center items-center px-6 md:px-12 lg:px-24 text-white overflow-hidden bg-[#0d0d0d]">
      
      {/* Background Ambience */}
      <div className="absolute inset-0 pointer-events-none z-0 overflow-hidden">
        <div className="absolute top-1/4 left-1/2 -translate-x-1/2 w-[60vw] h-[60vh] bg-[#ff4f1d]/5 rounded-full blur-[120px] mix-blend-screen opacity-50"></div>
      </div>

      <div className="relative z-10 w-full max-w-7xl mx-auto flex flex-col h-full justify-center gap-12 md:gap-16 pt-20">
        
        {/* Header */}
        <div className="flex flex-col items-start gap-4">
          <FadeIn>
            <span className="font-mono text-xs tracking-widest uppercase text-[#ff4f1d]">
              05 // EXPERTISE
            </span>
          </FadeIn>
          <FadeIn delay={0.1}>
            <h1 className="text-4xl md:text-6xl lg:text-7xl font-display font-black leading-none tracking-tight text-white uppercase">
              TECHNICAL <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#ff4f1d] to-orange-400">ARSENAL</span>
            </h1>
          </FadeIn>
          <FadeIn delay={0.2}>
            <p className="text-sm md:text-base text-white/50 max-w-xl font-sans leading-relaxed">
              Crafting high-end digital experiences using scalable architecture, premium design systems, and flawless animations.
            </p>
          </FadeIn>
        </div>

        {/* Bento Grid */}
        <div className="grid grid-cols-1 md:grid-cols-12 gap-4 md:gap-6">
          
          {/* Capabilities */}
          <div className="col-span-1 md:col-span-8 grid grid-cols-2 md:grid-cols-3 gap-4">
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
          </div>

          {/* Stats */}
          <div className="col-span-1 md:col-span-4 flex flex-col gap-4">
            {STATS.map((stat, i) => (
              <FadeIn key={i} delay={0.4 + (i * 0.1)} className="flex-1">
                <div className="flex flex-col justify-center p-6 rounded-xl bg-[#ff4f1d] text-black h-full group hover:bg-[#e04518] transition-colors duration-500">
                  <div className="text-4xl md:text-5xl font-display font-black leading-none group-hover:scale-105 transition-transform duration-500 origin-left">{stat.value}</div>
                  <div className="text-xs font-mono uppercase tracking-widest text-black/70 mt-2">{stat.label}</div>
                </div>
              </FadeIn>
            ))}
          </div>
        </div>

        {/* Tech Marquee */}
        <FadeIn delay={0.6} className="w-full mt-4 border-t border-white/5 pt-8">
          <div className="relative flex overflow-x-hidden group">
            <div className="absolute inset-y-0 left-0 w-24 bg-gradient-to-r from-[#0d0d0d] to-transparent z-10"></div>
            <div className="absolute inset-y-0 right-0 w-24 bg-gradient-to-l from-[#0d0d0d] to-transparent z-10"></div>
            
            <motion.div 
              className="flex whitespace-nowrap items-center w-max"
              animate={{ x: ["0%", "-50%"] }}
              transition={{ repeat: Infinity, ease: "linear", duration: 30 }}
            >
              {[...STACK, ...STACK, ...STACK, ...STACK].map((tech, i) => (
                <div key={i} className="text-xl md:text-2xl font-display font-bold text-white/10 uppercase tracking-widest hover:text-[#ff4f1d]/50 transition-colors duration-500 select-none pr-12">
                  {tech}
                </div>
              ))}
            </motion.div>
          </div>
        </FadeIn>

      </div>
    </div>
  );
};
"""

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
