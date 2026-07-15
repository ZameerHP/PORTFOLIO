import re

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
  ShoppingBag, 
  Database, 
  ShieldCheck,
  Rocket,
  MonitorPlay,
  Layers,
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
  { name: "Responsive Development", icon: Smartphone },
  { name: "Smooth Animations", icon: Sparkles },
  { name: "SEO Optimization", icon: Search },
  { name: "Performance Optimization", icon: Zap },
  { name: "AI Integration", icon: Bot },
  { name: "Accessibility", icon: ShieldCheck }
];

const WHAT_I_BUILD = [
  { name: "Business Websites", icon: Globe },
  { name: "Portfolio Websites", icon: MonitorPlay },
  { name: "SaaS Platforms", icon: Layers },
  { name: "Landing Pages", icon: Rocket },
  { name: "E-Commerce Stores", icon: ShoppingBag },
  { name: "AI Applications", icon: Cpu },
  { name: "Admin Dashboards", icon: Database },
  { name: "Custom Web Applications", icon: Code2 }
];

const PROCESS = [
  "Discovery", "Research", "UI / UX Design", "Development", 
  "Animation", "Testing", "Deployment", "Optimization"
];

const STATS = [
  { label: "Projects Completed", value: "50+" },
  { label: "Responsive Design", value: "100%" },
  { label: "Performance Optimized", value: "99/100" },
  { label: "Client Satisfaction", value: "100%" }
];

const FadeIn = ({ children, delay = 0, className = "" }: { children: React.ReactNode, delay?: number, className?: string }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-100px" }}
      transition={{ duration: 1, delay, ease: [0.16, 1, 0.3, 1] }}
      className={className}
    >
      {children}
    </motion.div>
  );
};

export const SkillsSection = () => {
  return (
    <div className="relative w-full min-h-screen pt-32 pb-32 px-6 md:px-12 lg:px-24 text-white selection:bg-blue-500/30">
      
      {/* Background Elements (No overflow-hidden on main container to allow scrolling) */}
      <div className="absolute inset-0 pointer-events-none z-0 overflow-hidden">
        <div className="absolute top-[-10%] left-1/2 -translate-x-1/2 w-[80vw] h-[50vh] bg-blue-600/10 rounded-full blur-[150px] mix-blend-screen opacity-50"></div>
        <div className="absolute bottom-[-10%] right-[-10%] w-[50vw] h-[50vh] bg-indigo-600/10 rounded-full blur-[150px] mix-blend-screen opacity-30"></div>
        <div className="absolute inset-0 bg-[url('https://transparenttextures.com/patterns/cubes.png')] opacity-[0.02]"></div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto flex flex-col gap-32 md:gap-40">
        
        {/* 1. Hero Header */}
        <div className="flex flex-col items-center text-center mt-12 md:mt-24">
          <FadeIn>
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-mono tracking-widest uppercase mb-8 shadow-[0_0_20px_rgba(59,130,246,0.15)]">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Skills & Expertise</span>
            </div>
          </FadeIn>
          <FadeIn delay={0.1}>
            <h1 className="text-5xl md:text-7xl lg:text-8xl font-display font-medium leading-[0.9] tracking-tighter mb-8 text-white drop-shadow-2xl">
              SKILLS & <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">EXPERTISE</span>
            </h1>
          </FadeIn>
          <FadeIn delay={0.2}>
            <p className="text-lg md:text-xl text-neutral-400 max-w-2xl mx-auto font-sans leading-relaxed">
              Crafting premium digital experiences through scalable architecture, modern design systems, and flawless animations.
            </p>
          </FadeIn>
          <FadeIn delay={0.3} className="mt-16 w-full max-w-md mx-auto relative flex justify-center">
            <div className="absolute inset-0 bg-blue-500/20 blur-xl rounded-full"></div>
            <div className="h-[1px] w-full bg-gradient-to-r from-transparent via-blue-500/50 to-transparent relative z-10"></div>
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-2 h-2 rounded-full bg-blue-400 shadow-[0_0_10px_#60a5fa] z-20"></div>
          </FadeIn>
        </div>

        {/* 2. Infinite Technology Marquee */}
        <FadeIn delay={0.1} className="w-full overflow-hidden -mx-6 md:-mx-12 lg:-mx-24 px-6 md:px-12 lg:px-24">
          <div className="relative flex overflow-x-hidden group">
            <div className="absolute inset-y-0 left-0 w-32 bg-gradient-to-r from-[#0a0a0a] to-transparent z-10"></div>
            <div className="absolute inset-y-0 right-0 w-32 bg-gradient-to-l from-[#0a0a0a] to-transparent z-10"></div>
            
            <motion.div 
              className="flex whitespace-nowrap items-center py-8 w-max"
              animate={{ x: ["0%", "-50%"] }}
              transition={{ repeat: Infinity, ease: "linear", duration: 25 }}
            >
              {[...STACK, ...STACK, ...STACK, ...STACK].map((tech, i) => (
                <div key={i} className="text-3xl md:text-5xl font-display font-bold text-white/5 uppercase tracking-widest hover:text-blue-500/20 transition-colors duration-500 select-none pr-12 md:pr-16">
                  {tech}
                </div>
              ))}
            </motion.div>
          </div>
        </FadeIn>

        {/* 3. Technology Stack Grid */}
        <div className="flex flex-col gap-16">
          <FadeIn>
            <div className="flex flex-col items-center gap-4">
              <span className="text-xs font-mono uppercase tracking-widest text-blue-400">Core Technologies</span>
              <h2 className="text-3xl md:text-4xl font-display font-medium text-white tracking-tight text-center">Technology Stack</h2>
            </div>
          </FadeIn>
          <div className="flex flex-wrap justify-center gap-4 md:gap-6 max-w-5xl mx-auto">
            {STACK.map((tech, i) => (
              <FadeIn key={i} delay={i * 0.03}>
                <div className="px-6 py-3 md:px-8 md:py-4 rounded-full bg-white/[0.02] border border-white/5 text-neutral-300 font-sans text-sm md:text-base hover:bg-blue-500/10 hover:border-blue-500/30 hover:text-blue-300 hover:-translate-y-1 transition-all duration-300 backdrop-blur-sm shadow-xl shadow-black/20 cursor-default">
                  {tech}
                </div>
              </FadeIn>
            ))}
          </div>
        </div>

        {/* 4. Featured Capabilities */}
        <div className="flex flex-col gap-16">
          <FadeIn>
            <div className="flex flex-col items-center gap-4">
              <span className="text-xs font-mono uppercase tracking-widest text-blue-400">Expertise</span>
              <h2 className="text-3xl md:text-4xl font-display font-medium text-white tracking-tight text-center">Featured Capabilities</h2>
            </div>
          </FadeIn>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 md:gap-8">
            {CAPABILITIES.map((cap, i) => (
              <FadeIn key={i} delay={i * 0.08}>
                <div className="group p-8 md:p-10 rounded-3xl bg-white/[0.02] border border-white/5 hover:border-blue-500/20 transition-all duration-500 backdrop-blur-md hover:-translate-y-2 hover:bg-blue-500/[0.02] hover:shadow-[0_20px_40px_rgba(59,130,246,0.05)] relative overflow-hidden flex flex-col gap-6 h-full cursor-default">
                  <div className="absolute -inset-24 bg-blue-500/10 opacity-0 group-hover:opacity-100 blur-3xl transition-opacity duration-700 rounded-full pointer-events-none"></div>
                  <div className="w-14 h-14 rounded-full bg-white/5 flex items-center justify-center text-neutral-400 group-hover:text-blue-400 group-hover:bg-blue-500/10 transition-colors duration-500 border border-white/5">
                    <cap.icon strokeWidth={1.5} className="w-6 h-6" />
                  </div>
                  <h3 className="text-xl font-display font-medium text-neutral-200 group-hover:text-white transition-colors tracking-tight">{cap.name}</h3>
                </div>
              </FadeIn>
            ))}
          </div>
        </div>

        {/* 5. What I Build & 6. Development Process */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-24 lg:gap-16 pt-8">
          
          {/* What I Build */}
          <div className="flex flex-col gap-12 p-8 md:p-12 rounded-3xl bg-white/[0.01] border border-white/5 backdrop-blur-sm">
            <FadeIn>
              <h2 className="text-2xl font-mono uppercase tracking-widest text-white/80">What I Build</h2>
            </FadeIn>
            <div className="flex flex-col gap-6">
              {WHAT_I_BUILD.map((item, i) => (
                <FadeIn key={i} delay={i * 0.05}>
                  <div className="flex items-center gap-6 group cursor-default">
                    <div className="w-12 h-12 rounded-full bg-white/5 flex items-center justify-center text-neutral-500 group-hover:bg-blue-500/10 group-hover:text-blue-400 group-hover:border-blue-500/20 border border-transparent transition-all duration-500">
                      <item.icon strokeWidth={1.5} className="w-5 h-5" />
                    </div>
                    <span className="text-neutral-300 font-sans text-lg group-hover:text-white transition-colors">{item.name}</span>
                  </div>
                </FadeIn>
              ))}
            </div>
          </div>

          {/* Development Process */}
          <div className="flex flex-col gap-12 p-8 md:p-12 rounded-3xl bg-white/[0.01] border border-white/5 backdrop-blur-sm">
            <FadeIn>
              <h2 className="text-2xl font-mono uppercase tracking-widest text-white/80">Development Process</h2>
            </FadeIn>
            <div className="relative border-l border-white/10 ml-6 flex flex-col gap-10 pb-4">
              {PROCESS.map((step, i) => (
                <FadeIn key={i} delay={i * 0.05} className="relative pl-10 group cursor-default">
                  <div className="absolute left-[-6px] top-1.5 w-3 h-3 rounded-full bg-white/20 group-hover:bg-blue-400 group-hover:scale-150 transition-all duration-500 ring-4 ring-[#0a0a0a]"></div>
                  <div className="text-xs font-mono text-blue-400/50 mb-2 uppercase tracking-widest group-hover:text-blue-400/80 transition-colors">Phase // 0{i + 1}</div>
                  <h3 className="text-2xl font-display font-medium text-neutral-300 group-hover:text-white transition-colors tracking-tight">{step}</h3>
                </FadeIn>
              ))}
            </div>
          </div>

        </div>

        {/* 7. Animated Statistics */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8 md:gap-4 pb-12 pt-16">
          {STATS.map((stat, i) => (
            <FadeIn key={i} delay={i * 0.1} className="flex flex-col items-center text-center gap-4 group cursor-default">
              <div className="text-5xl md:text-6xl font-display font-medium text-white group-hover:text-blue-400 transition-colors duration-500">{stat.value}</div>
              <div className="text-xs font-mono uppercase tracking-widest text-neutral-500 group-hover:text-neutral-300 transition-colors">{stat.label}</div>
            </FadeIn>
          ))}
        </div>

      </div>
      
    </div>
  );
};
"""

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
