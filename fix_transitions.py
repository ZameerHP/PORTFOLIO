import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

uplift_new = """  const upliftVariants = {
    initial: (custom: { index: number; dir: "next" | "prev" }) => {
      if (custom.index === 0) {
        return { y: 0, scale: 0.9, opacity: 0.3 };
      } else {
        return { y: "100%", scale: 1, opacity: 1 };
      }
    },
    animate: {
      y: 0,
      scale: 1,
      opacity: 1,
      transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] }
    },
    exit: (custom: { index: number; dir: "next" | "prev" }) => {
      if (custom.index === 0) {
        return { y: 0, scale: 0.9, opacity: 0.3, transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] } };
      } else {
        return { y: "100%", scale: 1, opacity: 1, transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] } };
      }
    }
  };"""

standard_new = """  const standardVariants = {
    initial: (custom: { index: number; dir: "next" | "prev" }) => ({
      y: custom.dir === "next" ? "100%" : "-100%",
      opacity: 0,
      scale: 0.95,
      filter: "blur(10px)",
    }),
    animate: {
      y: 0,
      opacity: 1,
      scale: 1,
      filter: "blur(0px)",
      transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] }
    },
    exit: (custom: { index: number; dir: "next" | "prev" }) => ({
      y: custom.dir === "next" ? "-100%" : "100%",
      opacity: 0,
      scale: 0.95,
      filter: "blur(10px)",
      transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] }
    }),
  };"""

content = re.sub(r'const upliftVariants = \{[\s\S]*?^\s*};\n', uplift_new + '\n\n', content, flags=re.MULTILINE)
content = re.sub(r'const standardVariants = \{[\s\S]*?^\s*};\n', standard_new + '\n\n', content, flags=re.MULTILINE)

with open('src/App.tsx', 'w') as f:
    f.write(content)
