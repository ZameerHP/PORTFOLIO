import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Fix Lenis RAF to clear properly
old_raf = '''    function raf(time: number) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);'''
new_raf = '''    let rafId: number;
    function raf(time: number) {
      lenis.raf(time);
      rafId = requestAnimationFrame(raf);
    }
    rafId = requestAnimationFrame(raf);'''
content = content.replace(old_raf, new_raf)

old_cleanup = '''    return () => {
      lenis.destroy();
      clearTimeout(snapTimeout);
    };'''
new_cleanup = '''    return () => {
      lenis.destroy();
      clearTimeout(snapTimeout);
      cancelAnimationFrame(rafId);
    };'''
content = content.replace(old_cleanup, new_cleanup)

# Replace ScrollLocker in Services Slide
old_services = '''          {currentSlide === 2 && (
            <motion.div
              key="services-slide"
              custom={{ index: 2, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 2 }}
              className="absolute inset-0 w-full h-[100dvh] bg-[#F6EEDC]"
            >
              <ScrollLocker
                id="services-slide-screen"
                className="absolute inset-0 w-full h-[100dvh] pt-24 custom-scrollbar"
                onNext={() => changeSlide("next")}
                onPrev={() => changeSlide("prev")}
              >'''
new_services = '''          {currentSlide === 2 && (
            <motion.div
              key="services-slide"
              custom={{ index: 2, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 2 }}
              className="absolute inset-0 w-full h-[100dvh] bg-[#F6EEDC] flex flex-col justify-center"
              id="services-slide-screen"
            >'''
content = content.replace(old_services, new_services)

old_services_end = '''                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
              </ScrollLocker>
            </motion.div>
          )}'''
new_services_end = '''                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
            </motion.div>
          )}'''
content = content.replace(old_services_end, new_services_end)

# Also make the text even smaller for Services so it fits without scrolling
old_service_padding = 'py-[20px] md:py-[30px]'
new_service_padding = 'py-[15px] md:py-[20px]'
content = content.replace(old_service_padding, new_service_padding)

old_service_heading = 'text-[28px] md:text-[36px]'
new_service_heading = 'text-[22px] md:text-[28px]'
content = content.replace(old_service_heading, new_service_heading)

old_service_desc = 'text-[14px] md:text-[16px]'
new_service_desc = 'text-[13px] md:text-[14px]'
content = content.replace(old_service_desc, new_service_desc)

with open('src/App.tsx', 'w') as f:
    f.write(content)

