import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add willChange for luxury cursor
old_cursor = '''        style={{
          x: smoothX,
          y: smoothY,
          marginLeft: cursorType === "view" ? -40 : -8,
          marginTop: cursorType === "view" ? -40 : -8,
        }}'''
new_cursor = '''        style={{
          x: smoothX,
          y: smoothY,
          marginLeft: cursorType === "view" ? -40 : -8,
          marginTop: cursorType === "view" ? -40 : -8,
          willChange: "transform"
        }}'''
content = content.replace(old_cursor, new_cursor)

# Add willChange for floating image
old_floating = '''                style={{ x: smoothX, y: smoothY, marginLeft: 20, marginTop: 20 }}'''
new_floating = '''                style={{ x: smoothX, y: smoothY, marginLeft: 20, marginTop: 20, willChange: "transform" }}'''
content = content.replace(old_floating, new_floating)

with open('src/App.tsx', 'w') as f:
    f.write(content)
