import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_logo = """        {/* Left Logo */}
        <div 
          onClick={() => changeSlide(0)}
          onMouseEnter={() => setCursorType("hover")}
          onMouseLeave={() => setCursorType("default")}
          className={`font-bebas font-[900] text-[34px] leading-none tracking-normal cursor-pointer hover:opacity-80 transition-opacity pointer-events-auto ${currentSlide === 1 || currentSlide === 2 ? "text-black" : "text-white"} ${currentSlide === 2 ? "opacity-0 pointer-events-none" : "opacity-100"}`}
          id="nav-logo"
        >
          {currentSlide === 1 ? "ABOUT US" : currentSlide === 0 ? "zamy dev" : ""}
        </div>"""

new_logo = """        {/* Left Logo */}
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
        </div>"""

content = content.replace(old_logo, new_logo)

with open('src/App.tsx', 'w') as f:
    f.write(content)
