import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

old_content = """              <div className="w-full max-w-[1600px] mx-auto px-6 md:px-[120px] py-[60px] md:py-[120px]">
                {/* Header */}
                <motion.div
                  initial={{ opacity: 0, y: 40 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 1.4, ease: [0.22, 1, 0.36, 1] }}
                  className="mb-16 md:mb-[80px]"
                >
                  <span className="font-sans font-bold text-[11px] md:text-sm tracking-widest uppercase text-black mb-[30px] block">
                    SERVICES
                  </span>
                  <h2 className="font-anton text-black text-[clamp(4rem,12vw,100px)] uppercase leading-[0.9] tracking-[-2px] m-0 p-0 text-left">
                    WHAT I DO
                  </h2>
                </motion.div>

                {/* Services List */}
                <div className="flex flex-col border-t border-black/12" onMouseLeave={() => setHoveredServiceImage(null)}>
                  {SERVICES.map((srv, idx) => (
                    <motion.div
                      key={srv.id}
                      initial={{ opacity: 0, y: 40 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ duration: 1.4, delay: idx * 0.12 + 0.2, ease: [0.16, 1, 0.3, 1] }}
                      className="group flex flex-col lg:grid lg:grid-cols-12 items-start lg:items-center py-[40px] md:py-[55px] border-b border-black/12 transition-colors duration-700 hover:border-black/30 cursor-pointer gap-6 lg:gap-0 relative"
                      onMouseEnter={() => {
                        setCursorType("hover");
                        setHoveredServiceImage(srv.image);
                      }}
                      onMouseLeave={() => {
                        setCursorType("default");
                      }}
                    >
                      {/* Column 1: Number */}
                      <div className="lg:col-span-1 font-sans text-[26px] font-medium text-[#777777] self-start lg:self-center">
                        {srv.number}
                      </div>
                      
                      {/* Column 2: Title */}
                      <div className="lg:col-span-6 self-start lg:self-center transition-transform duration-700 ease-in-out group-hover:translate-x-[10px]">
                        <h3 className="font-anton text-[40px] md:text-[52px] text-[#111111] uppercase leading-[0.9] m-0 p-0">
                          {srv.title}
                        </h3>
                      </div>
                      
                      {/* Column 3: Description */}
                      <div className="lg:col-span-5 self-start lg:self-center">
                        <p className="font-sans text-[16px] md:text-[18px] text-[#666666] leading-[1.6] max-w-[400px] transition-opacity duration-700 opacity-90 group-hover:opacity-100 m-0">
                          {srv.description}
                        </p>
                      </div>
                    </motion.div>"""

new_content = """              <div className="w-full max-w-[1600px] mx-auto px-6 md:px-[120px] py-[40px] md:py-[60px]">
                {/* Header */}
                <motion.div
                  initial={{ opacity: 0, y: 40 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 1.4, ease: [0.22, 1, 0.36, 1] }}
                  className="mb-8 md:mb-[40px]"
                >
                  <span className="font-sans font-bold text-[11px] md:text-sm tracking-widest uppercase text-black mb-[15px] block">
                    SERVICES
                  </span>
                  <h2 className="font-anton text-black text-[clamp(3rem,8vw,80px)] uppercase leading-[0.9] tracking-[-2px] m-0 p-0 text-left">
                    WHAT I DO
                  </h2>
                </motion.div>

                {/* Services List */}
                <div className="flex flex-col border-t border-black/12" onMouseLeave={() => setHoveredServiceImage(null)}>
                  {SERVICES.map((srv, idx) => (
                    <motion.div
                      key={srv.id}
                      initial={{ opacity: 0, y: 40 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ duration: 1.4, delay: idx * 0.12 + 0.2, ease: [0.16, 1, 0.3, 1] }}
                      className="group flex flex-col lg:grid lg:grid-cols-12 items-start lg:items-center py-[20px] md:py-[30px] border-b border-black/12 transition-colors duration-700 hover:border-black/30 cursor-pointer gap-4 lg:gap-0 relative"
                      onMouseEnter={() => {
                        setCursorType("hover");
                        setHoveredServiceImage(srv.image);
                      }}
                      onMouseLeave={() => {
                        setCursorType("default");
                      }}
                    >
                      {/* Column 1: Number */}
                      <div className="lg:col-span-1 font-sans text-[20px] font-medium text-[#777777] self-start lg:self-center">
                        {srv.number}
                      </div>
                      
                      {/* Column 2: Title */}
                      <div className="lg:col-span-6 self-start lg:self-center transition-transform duration-700 ease-in-out group-hover:translate-x-[10px]">
                        <h3 className="font-anton text-[28px] md:text-[36px] text-[#111111] uppercase leading-[0.9] m-0 p-0">
                          {srv.title}
                        </h3>
                      </div>
                      
                      {/* Column 3: Description */}
                      <div className="lg:col-span-5 self-start lg:self-center">
                        <p className="font-sans text-[14px] md:text-[16px] text-[#666666] leading-[1.6] max-w-[400px] transition-opacity duration-700 opacity-90 group-hover:opacity-100 m-0">
                          {srv.description}
                        </p>
                      </div>
                    </motion.div>"""

content = content.replace(old_content, new_content)

with open('src/App.tsx', 'w') as f:
    f.write(content)
