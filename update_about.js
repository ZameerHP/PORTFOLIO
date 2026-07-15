const fs = require('fs');

let content = fs.readFileSync('src/App.tsx', 'utf8');

const startIdx = content.indexOf('{/* LEFT LABEL */}');
const endIdx = content.indexOf('{/* BUTTON */}', startIdx);
const btnEndIdx = content.indexOf('</motion.div>\n                </div>\n              </motion.div>', startIdx);

const replacement = `{/* LEFT LABEL */}
                <div className="lg:col-span-4 flex justify-start lg:justify-end lg:pr-16 lg:h-full lg:pt-[8vh]" id="about-left">
                  <motion.h3 
                    variants={{
                      initial: { opacity: 0, x: -20 },
                      animate: { opacity: 1, x: 0, transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } }
                    }}
                    className="font-anton text-black text-sm tracking-[0.1em] uppercase mt-2"
                  >
                    ABOUT US
                  </motion.h3>
                </div>

                {/* RIGHT CONTENT */}
                <div className="lg:col-span-8 flex flex-col items-start pt-[6vh]" id="about-right">
                  {/* MAIN HEADLINE */}
                  <div className="flex flex-col space-y-0 mb-6 w-full">
                    <div className="overflow-hidden">
                      <motion.h2 
                        variants={{
                          initial: { y: "120%" },
                          animate: { y: 0, transition: { duration: 0.9, ease: [0.16, 1, 0.3, 1] } }
                        }} 
                        className="font-anton text-white uppercase text-[12vw] md:text-[8vw] lg:text-[4.8vw] xl:text-[4.2vw] leading-[0.88] m-0 p-0 text-left"
                      >
                        WE BUILD
                      </motion.h2>
                    </div>
                    <div className="overflow-hidden">
                      <motion.h2 
                        variants={{
                          initial: { y: "120%" },
                          animate: { y: 0, transition: { duration: 0.9, ease: [0.16, 1, 0.3, 1] } }
                        }} 
                        className="font-anton text-white uppercase text-[12vw] md:text-[8vw] lg:text-[4.8vw] xl:text-[4.2vw] leading-[0.88] m-0 p-0 text-left"
                      >
                        PREMIUM DIGITAL
                      </motion.h2>
                    </div>
                    <div className="overflow-hidden">
                      <motion.h2 
                        variants={{
                          initial: { y: "120%" },
                          animate: { y: 0, transition: { duration: 0.9, ease: [0.16, 1, 0.3, 1] } }
                        }} 
                        className="font-anton text-white uppercase text-[12vw] md:text-[8vw] lg:text-[4.8vw] xl:text-[4.2vw] leading-[0.88] m-0 p-0 text-left"
                      >
                        EXPERIENCES
                      </motion.h2>
                    </div>
                  </div>

                  {/* DESCRIPTION */}
                  <motion.p 
                    variants={{
                      initial: { opacity: 0, y: 30 },
                      animate: { opacity: 1, y: 0, transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } }
                    }}
                    className="font-sans text-white/95 text-base md:text-[17px] max-w-[620px] leading-relaxed font-medium mb-10 text-left"
                  >
                    We design and develop premium websites, high-performance web applications, and digital experiences that help ambitious brands grow online through exceptional design, speed, and strategy.
                  </motion.p>

                  {/* STATISTICS CARDS */}
                  <motion.div 
                    variants={{
                      initial: {},
                      animate: { transition: { staggerChildren: 0.1 } }
                    }}
                    className="grid grid-cols-1 sm:grid-cols-3 gap-4 w-full mb-10"
                    style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(0, 1fr))', ...(typeof window !== 'undefined' && window.innerWidth >= 640 ? { gridTemplateColumns: '1fr 0.85fr 1fr' } : {}) }}
                  >
                    {/* Card 01 */}
                    <motion.div 
                      variants={{
                        initial: { opacity: 0, y: 40 },
                        animate: { opacity: 1, y: 0, transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } }
                      }}
                      whileHover={{ y: -8, scale: 1.02, boxShadow: "0 20px 40px rgba(0,0,0,0.15)" }}
                      className="bg-[#f2ece4] rounded-[16px] p-6 lg:p-7 flex flex-col justify-between shadow-sm cursor-default h-full min-h-[190px] transition-all duration-400"
                    >
                      <div className="flex items-end gap-2.5 mb-3">
                        <span className="font-anton text-black text-5xl md:text-5xl leading-[0.85] m-0 p-0">150+</span>
                        <span className="font-sans font-bold text-[11px] text-black uppercase tracking-widest pb-1">PROJECTS</span>
                      </div>
                      <p className="font-sans text-[#555555] text-[13px] font-medium leading-relaxed mt-auto">
                        Successfully delivered premium websites, landing pages, SaaS platforms, and custom digital solutions.
                      </p>
                    </motion.div>

                    {/* Card 02 */}
                    <motion.div 
                      variants={{
                        initial: { opacity: 0, y: 40 },
                        animate: { opacity: 1, y: 0, transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } }
                      }}
                      whileHover={{ y: -8, scale: 1.02, boxShadow: "0 20px 40px rgba(0,0,0,0.4)" }}
                      className="bg-[#111111] rounded-[16px] p-6 lg:p-7 flex flex-col justify-between shadow-sm cursor-default h-full min-h-[190px] transition-all duration-400"
                    >
                      <div className="flex items-end gap-3 mb-3">
                        <span className="font-anton text-white text-5xl md:text-5xl leading-[0.85] m-0 p-0">98%</span>
                      </div>
                      <p className="font-sans text-[#a0a0a0] text-[13px] font-medium leading-relaxed mt-auto">
                        Client satisfaction achieved through quality design, clean development, and fast communication.
                      </p>
                    </motion.div>

                    {/* Card 03 */}
                    <motion.div 
                      variants={{
                        initial: { opacity: 0, y: 40 },
                        animate: { opacity: 1, y: 0, transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } }
                      }}
                      whileHover={{ y: -8, scale: 1.02, boxShadow: "0 20px 40px rgba(0,0,0,0.15)" }}
                      className="bg-white rounded-[16px] p-6 lg:p-7 flex flex-col justify-between shadow-sm cursor-default h-full min-h-[190px] transition-all duration-400"
                    >
                      <div className="flex items-end gap-2.5 mb-3">
                        <span className="font-anton text-black text-5xl md:text-5xl leading-[0.85] m-0 p-0">5+</span>
                        <span className="font-sans font-bold text-[11px] text-black uppercase tracking-widest pb-1">YEARS</span>
                      </div>
                      <p className="font-sans text-[#555555] text-[13px] font-medium leading-relaxed mt-auto">
                        Years of creating modern websites with cutting-edge technology and exceptional user experiences.
                      </p>
                    </motion.div>
                  </motion.div>

                  {/* BUTTON */}
`;

content = content.substring(0, startIdx) + replacement + content.substring(endIdx + '{/* BUTTON */}'.length);
fs.writeFileSync('src/App.tsx', content);
