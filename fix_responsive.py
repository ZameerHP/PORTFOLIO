import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace h-full with h-[100dvh] for main slide containers if any? 
# Wait, the main container is <div className="fixed inset-0 w-full h-full bg-[#0d0d0d] overflow-hidden font-sans">
# The absolute inset-0 already covers it, but we can change h-full to h-[100dvh] or h-full depending on how absolute positioning works (inset-0 implies top:0; bottom:0; which equals 100% height, but fixed inset-0 is better).

# Let's check where h-screen or 100vh is used
content = content.replace('100vh', '100dvh')
content = content.replace('h-screen', 'h-[100dvh]')

# Ensure Hero title has clamp
content = re.sub(r'text-\[8vw\] xl:text-\[110px\]', 'text-[clamp(3rem,10vw,110px)]', content)
content = re.sub(r'text-\[12vw\] md:text-\[100px\]', 'text-[clamp(4rem,12vw,100px)]', content)

with open('src/App.tsx', 'w') as f:
    f.write(content)

with open('src/components/ContactModal.tsx', 'r') as f:
    content = f.read()

content = content.replace('h-screen', 'h-[100dvh]')
# Inputs size
content = content.replace('text-sm', 'text-base')

with open('src/components/ContactModal.tsx', 'w') as f:
    f.write(content)
