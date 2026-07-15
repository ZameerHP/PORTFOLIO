import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# 1. Add mobile menu state
state_search = '  const [isContactOpen, setIsContactOpen] = useState(false);'
if state_search in content:
    content = content.replace(state_search, state_search + '\n  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);')
else:
    print("Could not find isContactOpen state")

# 2. Add Mobile menu toggle button in nav-right-group and the mobile menu overlay
nav_search = '''        {/* Right Nav Links + CTA Button Group */}
        <div className="flex items-center gap-[12px] pointer-events-auto" id="nav-right-group">
          {/* Nav Links on the Right */}
          <div className="hidden lg:flex items-center gap-[8px]" id="nav-links">'''
nav_replace = '''        {/* Right Nav Links + CTA Button Group */}
        <div className="flex items-center gap-[12px] pointer-events-auto" id="nav-right-group">
          {/* Mobile Menu Toggle */}
          <button 
            className={`lg:hidden font-mono text-[11px] font-bold uppercase tracking-widest px-[16px] h-[36px] md:h-[44px] flex items-center justify-center rounded-full transition-all duration-300 ${currentSlide === 1 || currentSlide === 2 || currentSlide === 3 ? "text-black border border-black/20" : "text-white border border-white/20"}`}
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? "CLOSE" : "MENU"}
          </button>
          
          {/* Nav Links on the Right */}
          <div className="hidden lg:flex items-center gap-[8px]" id="nav-links">'''

content = content.replace(nav_search, nav_replace)

# 3. Add Mobile Menu Overlay at the end of the return statement before the closing div
overlay = '''
      {/* MOBILE MENU OVERLAY */}
      <AnimatePresence>
        {isMobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="fixed inset-0 z-[100] bg-[#0d0d0d] p-6 pt-32 flex flex-col pointer-events-auto"
          >
            <div className="flex justify-between items-center absolute top-10 left-6 right-6">
              <span className="font-bebas font-[900] text-[34px] leading-none tracking-normal text-white">MENU</span>
              <button 
                className="font-mono text-[11px] font-bold uppercase tracking-widest text-white px-[16px] h-[36px] flex items-center justify-center rounded-full border border-white/20"
                onClick={() => setIsMobileMenuOpen(false)}
              >
                CLOSE
              </button>
            </div>
            <div className="flex flex-col gap-6 mt-12">
              {[
                { name: "Home", index: 0 },
                { name: "About", index: 1 },
                { name: "Services", index: 2 },
                { name: "Works", index: 3 },
                { name: "Skills", index: 4 },
                { name: "Pricing", index: 6 }
              ].map((item) => (
                <button
                  key={item.name}
                  onClick={() => {
                    changeSlide(item.index);
                    setIsMobileMenuOpen(false);
                  }}
                  className="text-left font-display text-4xl font-bold text-white uppercase tracking-tighter"
                >
                  {item.name}
                </button>
              ))}
              <button 
                className="mt-8 text-left font-display text-4xl font-bold text-[#ff4f1d] uppercase tracking-tighter"
                onClick={() => {
                  setIsContactOpen(true);
                  setIsMobileMenuOpen(false);
                }}
              >
                Let's Talk
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
'''

content = content.replace('{/* CONTACT MODAL POPUP */}', overlay + '\n      {/* CONTACT MODAL POPUP */}')

with open('src/App.tsx', 'w') as f:
    f.write(content)
