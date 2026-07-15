import re

with open('src/components/SkillsSection.tsx', 'r') as f:
    content = f.read()

bad_start = """export const SkillsSection = ({ slideDirection }: { slideDirection: "next" | "prev" }) => {
  const standardVariants = {
    initial: (custom: { dir: "next" | "prev" }) => ({
      y: custom.dir === "next" ? "100%" : "-100%",
    }),
    animate: {
      y: "0%",
      transition: {
        duration: 1.4,
        ease: [0.16, 1, 0.3, 1],
      },
    },
    exit: (custom: { dir: "next" | "prev" }) => ({
      y: custom.dir === "next" ? "-100%" : "100%",
      transition: {
        duration: 1.4,
        ease: [0.16, 1, 0.3, 1],
      },
    }),
  };

  return (
    <motion.div
      key="skills-slide"
      custom={{ dir: slideDirection }}
      variants={standardVariants}
      initial="initial"
      animate="animate"
      exit="exit"
      style={{ zIndex: 5 }}
      className="absolute inset-0 w-full h-full bg-[#0a0a0a] flex flex-col justify-center overflow-hidden"
      id="skills-slide-screen"
    >"""

good_start = """export const SkillsSection = () => {
  return (
    <>"""

content = content.replace(bad_start, good_start)

bad_end = """    </motion.div>
  );
};"""

good_end = """    </>
  );
};"""

content = content.replace(bad_end, good_end)

with open('src/components/SkillsSection.tsx', 'w') as f:
    f.write(content)
