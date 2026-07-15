import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace setMousePosition with useMotionValue
old_state = '  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });'
new_state = '''  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);
  const smoothX = useSpring(mouseX, { stiffness: 450, damping: 28, mass: 0.6 });
  const smoothY = useSpring(mouseY, { stiffness: 450, damping: 28, mass: 0.6 });'''
content = content.replace(old_state, new_state)

old_effect = '''  // Track Mouse movement for luxury lag cursor
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      setMousePosition({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);'''
new_effect = '''  // Track Mouse movement for luxury lag cursor
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      mouseX.set(e.clientX);
      mouseY.set(e.clientY);
    };
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);'''
content = content.replace(old_effect, new_effect)

old_cursor = '''      {/* LUXURY CUSTOM CURSOR */}
      <motion.div
        animate={{
          x: mousePosition.x - (cursorType === "view" ? 40 : 8),
          y: mousePosition.y - (cursorType === "view" ? 40 : 8),
          scale: cursorType === "hover" ? 2 : cursorType === "view" ? 1 : 1,
        }}
        transition={{ type: "spring", stiffness: 450, damping: 28, mass: 0.6 }}
        className={`fixed pointer-events-none z-50 rounded-full flex items-center justify-center font-mono text-[9px] font-bold uppercase transition-colors duration-700 ${
          cursorType === "view" 
            ? "w-20 h-20 bg-[#ff4f1d] text-white tracking-widest" 
            : cursorType === "hover"
            ? "w-4 h-4 bg-white/20 border border-white"
            : "w-4 h-4 bg-[#ff4f1d] border border-transparent"
        }`}
        id="custom-luxury-cursor"
      >'''
new_cursor = '''      {/* LUXURY CUSTOM CURSOR */}
      <motion.div
        style={{
          x: smoothX,
          y: smoothY,
          marginLeft: cursorType === "view" ? -40 : -8,
          marginTop: cursorType === "view" ? -40 : -8,
        }}
        animate={{
          scale: cursorType === "hover" ? 2 : cursorType === "view" ? 1 : 1,
        }}
        transition={{ type: "spring", stiffness: 450, damping: 28, mass: 0.6 }}
        className={`fixed top-0 left-0 pointer-events-none z-50 rounded-full flex items-center justify-center font-mono text-[9px] font-bold uppercase transition-colors duration-700 ${
          cursorType === "view" 
            ? "w-20 h-20 bg-[#ff4f1d] text-white tracking-widest" 
            : cursorType === "hover"
            ? "w-4 h-4 bg-white/20 border border-white"
            : "w-4 h-4 bg-[#ff4f1d] border border-transparent"
        }`}
        id="custom-luxury-cursor"
      >'''
content = content.replace(old_cursor, new_cursor)

old_floating = '''              {/* Floating Image Preview */}
              <motion.div
                className="fixed pointer-events-none z-[100] hidden md:block"
                animate={{
                  x: mousePosition.x + 20,
                  y: mousePosition.y + 20,
                  opacity: hoveredServiceImage ? 1 : 0,
                  scale: hoveredServiceImage ? 1 : 0.95,
                }}
                transition={{
                  opacity: { duration: 0.3, ease: "easeOut" },
                  scale: { duration: 0.3, ease: "easeOut" },
                  x: { type: "spring", stiffness: 150, damping: 20, mass: 0.5 },
                  y: { type: "spring", stiffness: 150, damping: 20, mass: 0.5 }
                }}
              >'''
new_floating = '''              {/* Floating Image Preview */}
              <motion.div
                className="fixed top-0 left-0 pointer-events-none z-[100] hidden md:block"
                style={{ x: smoothX, y: smoothY, marginLeft: 20, marginTop: 20 }}
                animate={{
                  opacity: hoveredServiceImage ? 1 : 0,
                  scale: hoveredServiceImage ? 1 : 0.95,
                }}
                transition={{
                  opacity: { duration: 0.3, ease: "easeOut" },
                  scale: { duration: 0.3, ease: "easeOut" }
                }}
              >'''
content = content.replace(old_floating, new_floating)

# Now fix Logo
old_logo = '''        {/* Left Logo */}
        <div 
          onClick={() => changeSlide(0)}
          onMouseEnter={() => setCursorType("hover")}
          onMouseLeave={() => setCursorType("default")}
          className={`cursor-pointer hover:opacity-80 transition-opacity pointer-events-auto ${currentSlide === 1 || currentSlide === 2 ? "text-black" : "text-white"} ${currentSlide === 2 ? "opacity-0 pointer-events-none" : "opacity-100"}`}
          id="nav-logo"
        >
          {currentSlide === 3 ? (
            <div className="flex flex-col ml-12 md:ml-24 mt-4 md:mt-8 gap-2">
              <span className="font-bebas font-[900] text-[48px] md:text-[80px] leading-none tracking-tight">SELECTED PROJECTS</span>
              <span className="font-display font-[500] text-[20px] md:text-[32px] text-[#ff4f1d] leading-none tracking-wide ml-2 md:ml-4">our signature</span>
            </div>
          ) : (
            <span className="font-bebas font-[900] text-[34px] leading-none tracking-normal">
              {currentSlide === 1 ? "ABOUT US" : currentSlide === 0 ? "zamy dev" : ""}
            </span>
          )}
        </div>'''
        
new_logo = '''        {/* Left Logo */}
        <div 
          onClick={() => changeSlide(0)}
          onMouseEnter={() => setCursorType("hover")}
          onMouseLeave={() => setCursorType("default")}
          className={`cursor-pointer hover:opacity-80 transition-opacity pointer-events-auto ${currentSlide === 1 || currentSlide === 2 || currentSlide === 3 ? "text-black" : "text-white"} ${currentSlide === 2 ? "opacity-0 pointer-events-none" : "opacity-100"}`}
          id="nav-logo"
        >
          {currentSlide === 3 ? (
            <div className="flex flex-col">
              <span className="font-bebas font-[900] text-[34px] leading-none tracking-normal">SELECTED PROJECTS</span>
              <span className="font-display font-[500] text-[18px] text-black leading-none tracking-wide mt-1">our signature</span>
            </div>
          ) : (
            <span className="font-bebas font-[900] text-[34px] leading-none tracking-normal">
              {currentSlide === 1 ? "ABOUT US" : currentSlide === 0 ? "zamy dev" : ""}
            </span>
          )}
        </div>'''
content = content.replace(old_logo, new_logo)

with open('src/App.tsx', 'w') as f:
    f.write(content)
