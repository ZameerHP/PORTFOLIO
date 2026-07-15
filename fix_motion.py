import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'import { motion, AnimatePresence } from "motion/react";',
    'import { motion, AnimatePresence, useMotionValue, useTransform, useMotionTemplate } from "motion/react";'
)

content = content.replace(
    '  const [splitProgress, setSplitProgress] = useState<number>(0);',
    '  const splitProgress = useMotionValue(0);'
)

content = content.replace(
    '      setSplitProgress(progress);',
    '      splitProgress.set(progress);'
)

with open('src/App.tsx', 'w') as f:
    f.write(content)
