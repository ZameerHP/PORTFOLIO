with open('src/App.tsx', 'r') as f:
    content = f.read()

start = content.find('const handleScroll = () => {')
end = content.find('const changeSlide = (direction: "next" | "prev" | number) => {')
print(content[start:end])
