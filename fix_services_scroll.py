import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Fix Slide 2 wrapper to use ScrollLocker
old_services = '''          {currentSlide === 2 && (
            <motion.div
              key="services-slide"
              custom={{ index: 2, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 2 }}
              className="absolute inset-0 w-full h-[100dvh] bg-[#F6EEDC] overflow-y-auto"
              id="services-slide-screen"
            >
              {/* Floating Image Preview */}
              <motion.div
                className="fixed top-0 left-0 pointer-events-none z-[100] hidden md:block"'''

new_services = '''          {currentSlide === 2 && (
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
              >
              {/* Floating Image Preview */}
              <motion.div
                className="fixed top-0 left-0 pointer-events-none z-[100] hidden md:block"'''

# Also add the closing tag for ScrollLocker
old_services_end = '''                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
            </motion.div>
          )}

                    
          {currentSlide === 3 && ('''

new_services_end = '''                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
              </ScrollLocker>
            </motion.div>
          )}

                    
          {currentSlide === 3 && ('''

content = content.replace(old_services, new_services)
content = content.replace(old_services_end, new_services_end)

with open('src/App.tsx', 'w') as f:
    f.write(content)
