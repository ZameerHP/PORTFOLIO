import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace bg-[#0d0d0d] with bg-[#F6EEDC] in slide 3
start_idx = content.find('{currentSlide === 3 && (')
end_idx = content.find('{currentSlide === 4 && (')

slide_3 = content[start_idx:end_idx]

# Modify colors in slide 3
slide_3 = slide_3.replace('bg-[#0d0d0d]', 'bg-[#F6EEDC]')
slide_3 = slide_3.replace('text-white', 'text-black')
slide_3 = slide_3.replace('text-white/40', 'text-black/40')
# Reveal visual status label
slide_3 = slide_3.replace('bg-black/85', 'bg-white/85')
slide_3 = slide_3.replace('text-white/90', 'text-black/90')
slide_3 = slide_3.replace('border-white/10', 'border-black/10')

# Actually, the background revealed on the full screen behind the sliding split text panels
# is bg-[#0a0a0a]. Let's make it a matching light color or maybe just keep it dark since it reveals a portrait?
# If we keep it dark, the portrait stays dark. If we change it, the portrait has a light background.
# Let's change it to bg-[#F6EEDC] as well, or #F0E6D2 (slightly darker sand)
slide_3 = slide_3.replace('bg-[#0a0a0a]', 'bg-[#F6EEDC]')
slide_3 = slide_3.replace('border-white/5', 'border-black/5')
slide_3 = slide_3.replace('from-black/85', 'from-[#F6EEDC]/85')
slide_3 = slide_3.replace('to-black/80', 'to-[#F6EEDC]/80')

content = content[:start_idx] + slide_3 + content[end_idx:]

with open('src/App.tsx', 'w') as f:
    f.write(content)
