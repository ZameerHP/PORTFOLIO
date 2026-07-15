import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

project_card_code = """
const ProjectCard = ({ project, idx, splitProgress }: any) => {
  const transform = useTransform(splitProgress, (v: number) => {
    if (idx === 0) {
      const p0 = Math.min(100, v) / 100;
      return `translateY(${(1 - p0) * 80}px) scale(${0.9 + p0 * 0.1})`;
    } else {
      const startProgress = idx * 100;
      const p = Math.min(100, Math.max(0, v - startProgress)) / 100;
      return `translateY(${(1 - p) * 100}vh)`;
    }
  });

  const opacity = useTransform(splitProgress, (v: number) => {
    if (idx === 0) return Math.min(100, v) / 100;
    return 1;
  });

  return (
    <motion.div 
      className="absolute inset-0 flex items-center justify-center will-change-transform pointer-events-none"
      style={{ transform, opacity, zIndex: 10 + idx }}
    >
      <div className="relative w-[90%] md:w-[85%] lg:w-[80%] h-[75vh] max-h-[800px] rounded-[18px] overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.2)] group transition-all duration-700 hover:scale-[1.01] hover:shadow-[0_30px_60px_rgba(0,0,0,0.3)] pointer-events-auto cursor-pointer">
        <img loading="lazy" decoding="async"
          src={project.image} 
          alt={project.title}
          className="absolute inset-0 w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-black/10 via-transparent to-black/80"></div>
        <div className="absolute bottom-0 left-0 w-full p-8 md:p-12 text-white flex justify-between items-end">
          <div>
            <div className="text-[10px] sm:text-xs font-mono mb-3 uppercase tracking-widest text-neutral-300">
              {project.category}
            </div>
            <h3 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-display font-medium leading-none tracking-tight">
              {project.title}
            </h3>
          </div>
          <div className="w-12 h-12 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center group-hover:bg-white group-hover:text-black transition-colors duration-500">
            <ArrowUpRight className="w-5 h-5" />
          </div>
        </div>
      </div>
    </motion.div>
  );
};
"""

content = content.replace('export default function App() {', project_card_code + '\nexport default function App() {')

with open('src/App.tsx', 'w') as f:
    f.write(content)
print("Inserted ProjectCard")
