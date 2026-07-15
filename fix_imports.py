import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace('import { motion, AnimatePresence, useMotionValue, useTransform, useMotionTemplate } from "motion/react";', 'import { motion, AnimatePresence, useMotionValue, useTransform, useMotionTemplate, useSpring } from "motion/react";')

with open('src/App.tsx', 'w') as f:
    f.write(content)
