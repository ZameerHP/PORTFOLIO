import React, { useState, useRef, useEffect } from "react";
import { motion, AnimatePresence, useMotionValue, useTransform, useMotionTemplate, useSpring } from "motion/react";
import { ArrowRight, ChevronDown, Check, Sparkles, Volume2, ArrowUpRight } from "lucide-react";
import { SERVICES, PROJECTS, STEPS, TESTIMONIALS, FAQS, PORTRAITS } from "./data";
import { Suspense, lazy } from "react";
const ContactModal = lazy(() => import('./components/ContactModal').then(module => ({ default: module.ContactModal })));
const SkillsSection = lazy(() => import('./components/SkillsSection').then(module => ({ default: module.SkillsSection })));
import { ScrollLocker } from "./components/ScrollLocker";

import Lenis from "lenis";


const ProjectCard = ({ project, idx, splitProgress }: any) => {
  const transform = useTransform(splitProgress, (v: number) => {
    if (idx === 0) {
      const p0 = Math.min(100, v) / 100;
      return `translateY(${(1 - p0) * 80}px) scale(${0.9 + p0 * 0.1})`;
    } else {
      const startProgress = idx * 100;
      const p = Math.min(100, Math.max(0, v - startProgress)) / 100;
      return `translateY(${(1 - p) * 100}vh)`;
    }
  });

  const opacity = useTransform(splitProgress, (v: number) => {
    if (idx === 0) return Math.min(100, v) / 100;
    return 1;
  });

  return (
    <motion.div 
      className="absolute inset-0 flex items-center justify-center will-change-transform pointer-events-none"
      style={{ transform, opacity, zIndex: 10 + idx }}
    >
      <div className="relative w-[90%] md:w-[85%] lg:w-[80%] h-[75vh] max-h-[800px] rounded-[18px] overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.2)] group transition-all duration-700 hover:scale-[1.01] hover:shadow-[0_30px_60px_rgba(0,0,0,0.3)] pointer-events-auto cursor-pointer">
        <img loading="lazy" decoding="async"
          src={project.image} 
          alt={project.title}
          className="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
          referrerPolicy="no-referrer"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent pointer-events-none transition-opacity duration-500 group-hover:opacity-90" />
        
        <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none z-20">
          <a 
            href="#" 
            target="_blank" 
            rel="noopener noreferrer"
            className="pointer-events-auto bg-black text-white px-[34px] py-[16px] rounded-full font-sans font-bold text-sm tracking-wider uppercase transform translate-y-4 group-hover:translate-y-0 transition-all duration-500 hover:scale-105"
          >
            VIEW PROJECT
          </a>
        </div>
        
        <div className="absolute bottom-0 left-0 w-full p-8 md:p-12 text-white flex justify-between items-end">
          <div>
            <div className="text-[10px] sm:text-xs font-mono mb-3 uppercase tracking-widest text-neutral-300">
              {project.category}
            </div>
            <h3 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-display font-medium leading-none tracking-tight">
              {project.title}
            </h3>
          </div>
          <div className="w-12 h-12 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center group-hover:bg-white group-hover:text-black transition-colors duration-500 pointer-events-auto cursor-pointer">
            <ArrowUpRight className="w-5 h-5" />
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export default function App() {
  const [activeTab, setActiveTab] = useState<string>("all");
  const [openFaqIndex, setOpenFaqIndex] = useState<number | null>(0);
  const [activeServiceImage, setActiveServiceImage] = useState<string>(SERVICES[0].image);
  const [hoveredServiceImage, setHoveredServiceImage] = useState<string | null>(null);
  const [isContactOpen, setIsContactOpen] = useState<boolean>(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState<boolean>(false);
  const [isCopied, setIsCopied] = useState<boolean>(false);

  // Loading Screen State
  const [loadingProgress, setLoadingProgress] = useState<number>(0);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  // Custom Cursor Coordinates & Type
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);
  const smoothX = useSpring(mouseX, { stiffness: 450, damping: 28, mass: 0.6 });
  const smoothY = useSpring(mouseY, { stiffness: 450, damping: 28, mass: 0.6 });
  const [cursorType, setCursorType] = useState<"default" | "hover" | "view">("default");

  // Page Snapping / Uplifting Slide system
  const [currentSlide, setCurrentSlide] = useState<number>(0);
  const [prevSlide, setPrevSlide] = useState<number>(0);
  const [isAnimating, setIsAnimating] = useState<boolean>(false);
  const splitProgress = useMotionValue(0);
  const woX = useTransform(splitProgress, (v: number) => `calc(-${(Math.min(100, v) / 100) * 80}vw)`);
  const rkX = useTransform(splitProgress, (v: number) => `calc(${(Math.min(100, v) / 100) * 80}vw)`);
  const slideCount = 11; // 0 to 8 slides
  const lenisRef = useRef<Lenis | null>(null);
  const isScrollingProgrammaticallyRef = useRef<boolean>(false);
  const snapTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  // Background Image Dynamic Fallback Loader
  const [heroImageSrc, setHeroImageSrc] = useState<string>(PORTRAITS.hero);
  const [imageRetryCount, setImageRetryCount] = useState<number>(0);

  const handleImageError = () => {
    if (imageRetryCount === 0) {
      // Fallback to beautiful Unsplash luxury dark abstract artwork if the GitHub link fails
      setHeroImageSrc("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1920&auto=format&fit=crop");
      setImageRetryCount(1);
    }
  };

  // Slide definitions for dynamic uplifting scroll system
  const slides = [
    { id: "hero", label: "00 // INTRO", name: "Intro" },
    { id: "about", label: "01 // VISION", name: "Vision" },
    { id: "services", label: "02 // CAPABILITIES", name: "Services" },
    { id: "works", label: "03 // SIGNATURE", name: "Works" },
    { id: "skills", label: "04 // EXPERTISE", name: "Skills" },
    { id: "testimonials", label: "05 // CLIENTS", name: "Reviews" },
    { id: "faq", label: "06 // INSIGHTS", name: "Contact & FAQ" }
  ];

  // Loader sequence
  useEffect(() => {
    let timer: any;
    if (loadingProgress < 100) {
      timer = setInterval(() => {
        setLoadingProgress((prev) => {
          const next = prev + Math.floor(Math.random() * 8) + 4;
          return next >= 100 ? 100 : next;
        });
      }, 80);
    } else {
      const exitTimer = setTimeout(() => {
        setIsLoading(false);
      }, 600);
      return () => clearTimeout(exitTimer);
    }
    return () => clearInterval(timer);
  }, [loadingProgress]);

  // Track Mouse movement for luxury lag cursor
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      mouseX.set(e.clientX);
      mouseY.set(e.clientY);
    };
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);

  // Handle slide change transition
  const [slideDirection, setSlideDirection] = useState<"next" | "prev">("next");

  const isUpliftActive = (currentSlide === 0 && prevSlide === 1) || (currentSlide === 1 && prevSlide === 0);

  // Uplift variants for Slide 0 and Slide 1
    const upliftVariants = {
    initial: (custom: { index: number; dir: "next" | "prev" }) => {
      if (custom.index === 0) {
        return { y: 0, scale: 0.9, opacity: 0.3 };
      } else {
        return { y: "100%", scale: 1, opacity: 1 };
      }
    },
    animate: {
      y: 0,
      scale: 1,
      opacity: 1,
      transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] }
    },
    exit: (custom: { index: number; dir: "next" | "prev" }) => {
      if (custom.index === 0) {
        return { y: 0, scale: 0.9, opacity: 0.3, transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] } };
      } else {
        return { y: "100%", scale: 1, opacity: 1, transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] } };
      }
    }
  };


  // Standard sequential sliding variants for all other slides (SAME LIKE BEFORE)
    const standardVariants = {
    initial: (custom: { index: number; dir: "next" | "prev" }) => ({
      y: custom.dir === "next" ? "100%" : "-100%",
      opacity: 0,
      scale: 0.95,
      
    }),
    animate: {
      y: 0,
      opacity: 1,
      scale: 1,
      
      transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] }
    },
    exit: (custom: { index: number; dir: "next" | "prev" }) => ({
      y: custom.dir === "next" ? "-100%" : "100%",
      opacity: 0,
      scale: 0.95,
      
      transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] }
    }),
  };


  const changeSlide = (direction: "next" | "prev" | number) => {
    if (!lenisRef.current) return;
    const vh = window.innerHeight || 800;
    const numProjects = PROJECTS.length; // 3
    const workEndVh = 3 + numProjects + 1; // 7

    let targetScroll = 0;

    if (typeof direction === "number") {
      if (direction < 3) targetScroll = direction * vh;
      else if (direction === 3) targetScroll = 3 * vh;
      else targetScroll = (workEndVh + direction - 4) * vh;
    } else if (direction === "next") {
      if (currentSlide === 3 && splitProgress.get() < numProjects * 100) {
        const currentPhase = Math.floor(splitProgress.get() / 100);
        targetScroll = (3 + currentPhase + 1) * vh;
      } else {
        const nextSlide = Math.min(6, currentSlide + 1);
        if (nextSlide < 3) targetScroll = nextSlide * vh;
        else if (nextSlide === 3) targetScroll = 3 * vh;
        else targetScroll = (workEndVh + nextSlide - 4) * vh;
      }
    } else {
      if (currentSlide === 3 && splitProgress.get() > 0) {
        const currentPhase = Math.ceil(splitProgress.get() / 100);
        targetScroll = (3 + currentPhase - 1) * vh;
      } else {
        const prevSlide = Math.max(0, currentSlide - 1);
        if (prevSlide < 3) targetScroll = prevSlide * vh;
        else if (prevSlide === 3) targetScroll = (workEndVh - 1) * vh;
        else targetScroll = (workEndVh + prevSlide - 4) * vh;
      }
    }

    // Determine the target slide index based on the target scroll
    let targetIndex = 0;
    if (targetScroll < 3 * vh) {
      targetIndex = Math.min(2, Math.floor(targetScroll / vh));
    } else if (targetScroll >= 3 * vh && targetScroll < workEndVh * vh) {
      targetIndex = 3;
    } else {
      targetIndex = Math.min(6, 4 + Math.floor((targetScroll - workEndVh * vh) / vh));
    }

    if (snapTimeoutRef.current) {
      clearTimeout(snapTimeoutRef.current);
    }

    if (targetIndex !== currentSlide) {
      isScrollingProgrammaticallyRef.current = true;
      setPrevSlide(currentSlide);
      setCurrentSlide(targetIndex);
      setSlideDirection(targetIndex > currentSlide ? "next" : "prev");
    }

    lenisRef.current.scrollTo(targetScroll, { 
      duration: 1.4,
      onComplete: () => {
        isScrollingProgrammaticallyRef.current = false;
      }
    });
  };

  // Initialize Lenis Smooth Scroll
  useEffect(() => {
    if (isLoading) return;

    if ('scrollRestoration' in history) { history.scrollRestoration = 'manual'; }
    window.scrollTo(0, 0);

    const lenis = new Lenis({
      duration: 1.4,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: "vertical",
      gestureOrientation: "vertical",
      smoothWheel: true,
      wheelMultiplier: 1.1,
      touchMultiplier: 1.5,
    });

    lenisRef.current = lenis;
    lenis.scrollTo(0, { immediate: true });

    let lastSlide = currentSlide;

    let rafId: number;
    function raf(time: number) {
      lenis.raf(time);
      rafId = requestAnimationFrame(raf);
    }
    rafId = requestAnimationFrame(raf);

    const handleScroll = () => {
      const scrollY = lenis.scroll;
      const vh = window.innerHeight || 800;

      let activeIndex = 0;
      let progress = 0;

      const numProjects = PROJECTS.length;
      const workScrolls = numProjects; // 3
      const workEndVh = 3 + workScrolls + 1; // 7

      if (scrollY < 3 * vh) {
        activeIndex = Math.min(2, Math.floor(scrollY / vh));
        progress = 0;
      } else if (scrollY >= 3 * vh && scrollY < workEndVh * vh) {
        activeIndex = 3;
        progress = Math.min(workScrolls * 100, Math.max(0, ((scrollY - 3 * vh) / vh) * 100));
      } else {
        activeIndex = Math.min(6, 4 + Math.floor((scrollY - workEndVh * vh) / vh));
        progress = workScrolls * 100;
      }

      splitProgress.set(progress);

      if (isScrollingProgrammaticallyRef.current) {
        lastSlide = activeIndex;
        return;
      }

      if (activeIndex !== lastSlide) {
        setPrevSlide(lastSlide);
        setCurrentSlide(activeIndex);
        setSlideDirection(activeIndex > lastSlide ? "next" : "prev");
        lastSlide = activeIndex;
      }
    };

    const handleScrollAndSnap = () => {
      handleScroll();

      if (snapTimeoutRef.current) {
        clearTimeout(snapTimeoutRef.current);
      }

      if (!isScrollingProgrammaticallyRef.current) {
        snapTimeoutRef.current = setTimeout(() => {
          if (isScrollingProgrammaticallyRef.current) return;
          const currentScroll = lenis.scroll;
          const vh = window.innerHeight || 800;
          const numProjects = PROJECTS.length;
          const workEndVh = 3 + numProjects + 1; // 7
          const maxScroll = (workEndVh + 3) * vh; // max scroll target is 10 * vh

          const snapTarget = Math.round(currentScroll / vh) * vh;
          const cappedSnapTarget = Math.min(maxScroll, Math.max(0, snapTarget));

          if (Math.abs(currentScroll - cappedSnapTarget) > 10) {
            let targetIndex = 0;
            if (cappedSnapTarget < 3 * vh) {
              targetIndex = Math.min(2, Math.floor(cappedSnapTarget / vh));
            } else if (cappedSnapTarget >= 3 * vh && cappedSnapTarget < workEndVh * vh) {
              targetIndex = 3;
            } else {
              targetIndex = Math.min(6, 4 + Math.floor((cappedSnapTarget - workEndVh * vh) / vh));
            }

            isScrollingProgrammaticallyRef.current = true;
            setPrevSlide(lastSlide);
            setCurrentSlide(targetIndex);
            setSlideDirection(targetIndex > lastSlide ? "next" : "prev");
            lastSlide = targetIndex;

            lenis.scrollTo(cappedSnapTarget, {
              duration: 1.0,
              easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
              onComplete: () => {
                isScrollingProgrammaticallyRef.current = false;
              }
            });
          }
        }, 300);
      }
    };

    lenis.on("scroll", handleScrollAndSnap);
    handleScroll();

    return () => {
      lenis.destroy();
      if (snapTimeoutRef.current) {
        clearTimeout(snapTimeoutRef.current);
      }
      cancelAnimationFrame(rafId);
    };
  }, [isLoading]);

  // Keyboard Navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      const activeEl = document.activeElement;
      const isTyping = activeEl && (
        activeEl.tagName === "INPUT" || 
        activeEl.tagName === "TEXTAREA" || 
        activeEl.tagName === "SELECT" ||
        activeEl.getAttribute("contenteditable") === "true"
      );

      if (isTyping || isContactOpen) return;

      const isDownKey = e.key === "ArrowDown" || e.key === "PageDown" || e.key === " ";
      const isUpKey = e.key === "ArrowUp" || e.key === "PageUp";

      if (isDownKey) {
        e.preventDefault();
        changeSlide("next");
      } else if (isUpKey) {
        e.preventDefault();
        changeSlide("prev");
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, [currentSlide, isContactOpen]);

  const handleCopyEmail = () => {
    navigator.clipboard.writeText("INFO@LUXFOLIO.COM");
    setIsCopied(true);
    setTimeout(() => setIsCopied(false), 2000);
  };

  return (
    <div 
      className="relative w-full text-white selection:bg-[#ff4f1d] selection:text-white font-sans antialiased cursor-none" 
      id="luxfolio-root"
      style={{ minHeight: "100dvh" }}
    >
      {/* FIXED VIEWPORT CONTAINER FOR ALL UI */}
      <div className="fixed inset-0 w-full h-full overflow-hidden bg-[#0d0d0d] z-10">
      {/* LUXURY LOADER OVERLAY */}
      <AnimatePresence>
        {isLoading && (
          <motion.div
            initial={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 1.4, ease: [0.22, 1, 0.36, 1] }}
            className="fixed inset-0 z-50 bg-[#0d0d0d] flex flex-col justify-between p-8 md:p-16"
            id="page-loader-screen"
          >
            <div className="flex justify-between items-center" id="loader-top">
              
              <span className="font-mono text-xs tracking-widest text-white/40">CREATIVE ARTS // AGENCY</span>
            </div>

            <div className="space-y-4" id="loader-center">
              <div className="overflow-hidden" id="loader-heading-frame">
                <motion.h2 
                  initial={{ y: 80 }}
                  animate={{ y: 0 }}
                  transition={{ duration: 1.4, ease: [0.22, 1, 0.36, 1] }}
                  className="font-display text-4xl sm:text-6xl md:text-8xl font-black tracking-tighter leading-none text-white uppercase"
                >
                  HIGH-END DIGITAL
                </motion.h2>
              </div>
              <div className="overflow-hidden" id="loader-heading-frame-2">
                <motion.h2 
                  initial={{ y: 80 }}
                  animate={{ y: 0 }}
                  transition={{ duration: 1.4, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
                  className="font-display text-4xl sm:text-6xl md:text-8xl font-black tracking-tighter leading-none text-stroke-white uppercase"
                >
                  CRAFTING
                </motion.h2>
              </div>
            </div>

            <div className="flex justify-between items-end" id="loader-bottom">
              <div className="space-y-1" id="loader-status">
                <span className="font-mono text-[10px] text-white/30 block uppercase tracking-widest">LOADING EXPERIENCE</span>
                <span className="font-mono text-xs tracking-widest uppercase">PLEASE WAIT</span>
              </div>
              <div className="font-display font-black text-6xl sm:text-9xl text-[#ff4f1d] leading-none select-none" id="loader-percent">
                {String(loadingProgress).padStart(3, "0")}%
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* LUXURY CUSTOM CURSOR */}
      <motion.div
        style={{
          x: smoothX,
          y: smoothY,
          marginLeft: cursorType === "view" ? -40 : -8,
          marginTop: cursorType === "view" ? -40 : -8,
          willChange: "transform"
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
      >
        {cursorType === "view" && "VIEW"}
      </motion.div>

      {/* HEADER / NAVIGATION */}
      <header className="fixed top-10 left-6 md:left-[60px] right-6 md:right-[60px] z-40 flex items-center justify-between pointer-events-none select-none" id="nav-header">
        {/* Left Logo */}
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
        </div>

        {/* Right Nav Links + CTA Button Group */}
        <div className="flex items-center gap-[12px] pointer-events-auto" id="nav-right-group">
          {/* Mobile Menu Toggle */}
          <button 
            className={`lg:hidden font-mono text-[11px] font-bold uppercase tracking-widest px-[16px] h-[44px] md:h-[44px] flex items-center justify-center rounded-full transition-all duration-300 ${currentSlide === 1 || currentSlide === 2 || currentSlide === 3 ? "text-black border border-black/20" : "text-white border border-white/20"}`}
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? "CLOSE" : "MENU"}
          </button>
          
          {/* Nav Links on the Right */}
          <div className="hidden lg:flex items-center gap-[8px]" id="nav-links">
            {[
              { name: "About", index: 1 },
              { name: "Services", index: 2 },
              { name: "Works", index: 3 },
              { name: "Skills", index: 4 }
            ].map((item) => {
              const isDarkText = currentSlide === 1 || currentSlide === 2;
              return (
              <button
                key={item.name}
                onClick={() => changeSlide(item.index)}
                onMouseEnter={() => setCursorType("hover")}
                onMouseLeave={() => setCursorType("default")}
                className={`h-[44px] px-[14px] rounded-full transition-all duration-700 text-[12px] font-[600] font-sans uppercase tracking-wider ${
                  currentSlide === item.index 
                    ? (isDarkText ? "bg-black/20 text-black" : "bg-white/20 text-white") 
                    : (isDarkText ? "bg-black/10 text-black hover:bg-black/[0.18]" : "bg-white/10 text-white hover:bg-white/[0.18]")
                }`}
                id={`nav-link-${item.name.toLowerCase()}`}
              >
                {item.name}
              </button>
            )})}
          </div>

          {/* Right CTA Button */}
          <button
            onClick={() => setIsContactOpen(true)}
            onMouseEnter={() => setCursorType("hover")}
            onMouseLeave={() => setCursorType("default")}
            className={`w-[185px] h-[44px] font-sans rounded-full flex items-center justify-between pl-4 pr-1 transition-all duration-700 shadow-xl shadow-black/20 group ${currentSlide === 1 || currentSlide === 2 ? "bg-black text-white hover:bg-neutral-800" : "bg-white text-[#111111] hover:bg-neutral-100"}`}
            id="nav-cta-btn"
          >
            <span className="text-[14px] font-[600] tracking-wide">Book a Free Call</span>
            <div 
              className="w-[36px] h-[44px] rounded-full bg-[#FF6A3A] flex items-center justify-center text-white transition-transform duration-700 group-hover:scale-105" 
              id="nav-cta-circle"
            >
              <ArrowUpRight className="w-4 h-4 stroke-[2.5]" />
            </div>
          </button>
        </div>
      </header>

      {/* DYNAMIC UPLIFTING SLIDE CONTAINER CONTAINER */}
      <div className="relative w-full h-full" id="uplifting-slides-master">
        <AnimatePresence mode={isUpliftActive ? undefined : "wait"}>
          {currentSlide === 0 && (
            <motion.div
              key="hero-slide"
              custom={{ index: 0, dir: slideDirection }}
              variants={isUpliftActive ? upliftVariants : standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 0, willChange: "transform, opacity" }}
              className="absolute inset-0 w-full h-full flex flex-col justify-between overflow-hidden bg-[#050505]"
              id="hero-slide-screen"
            >
              {/* Full-screen Cinematic Background Image with precise visual overlays */}
              <div className="absolute inset-0 w-full h-full z-0 overflow-hidden" id="hero-bg-wrapper">
                {/* 1. Base dark background */}
                <div 
                  className="absolute inset-0 w-full h-full z-0 bg-neutral-950" 
                />

                {/* 2. The main high-resolution portrait image, filling the full screen perfectly with clean, natural lighting */}
                <img
                  src={heroImageSrc}
                  onError={handleImageError}
                  alt="Zameer Studio Background"
                  className="w-full h-full object-cover z-20 select-none pointer-events-none filter brightness-[1.10] contrast-[1.05]"
                  style={{ 
                    objectPosition: "center 20%",
                  }}
                  referrerPolicy="no-referrer"
                  id="hero-bg-image"
                />

                {/* 2.5 Luxury Ambient Orange and Amber Light Glow overlay to make the background feel custom and match the brand theme */}
                <div 
                  className="absolute inset-0 z-25 pointer-events-none opacity-50 mix-blend-screen"
                  style={{
                    background: "radial-gradient(circle at 80% 30%, rgba(255, 106, 58, 0.35) 0%, rgba(255, 138, 61, 0.12) 40%, rgba(0, 0, 0, 0) 75%)"
                  }}
                  id="hero-ambient-orange-glow"
                />

                {/* 3. Subtle dark linear overlay for text legibility */}
                <div 
                  className="absolute inset-0 z-30 pointer-events-none"
                  style={{
                    background: "linear-gradient(180deg, rgba(0, 0, 0, 0.45) 0%, rgba(0, 0, 0, 0.5) 100%)"
                  }}
                />

                {/* 4. Soft Film Grain for elegant texture */}
                <div className="absolute inset-0 z-40 pointer-events-none film-grain opacity-[0.015]" />
              </div>

              {/* Absolute Content Layout above the hero background */}
              <div className="absolute inset-0 w-full h-full z-10 pointer-events-none" id="hero-content-wrapper">
                {/* Left Hero Content */}
                <div 
                  className="absolute left-6 md:left-[60px] top-[140px] md:top-[170px] max-w-[500px] flex flex-col items-start z-30 pointer-events-auto" 
                  id="hero-left-content"
                >
                  {/* Headline */}
                  <h1 
                    className="font-bebas font-[800] text-white text-[28px] uppercase tracking-normal leading-[1.05] text-left drop-shadow-[0_2px_8px_rgba(0,0,0,0.5)]"
                    style={{ maxWidth: "500px", letterSpacing: "0px" }}
                    id="hero-main-title"
                  >
                    WE DESIGN HIGH-CONVERTING WEBSITES THAT HELP BUSINESSES ATTRACT MORE CLIENTS, BUILD TRUST, AND GROW FASTER.
                  </h1>

                  {/* CTA Button (40px below the headline) */}
                  <button
                    onClick={() => setIsContactOpen(true)}
                    onMouseEnter={() => setCursorType("hover")}
                    onMouseLeave={() => setCursorType("default")}
                    className="mt-[40px] w-[210px] h-[48px] bg-white text-[#111111] font-sans font-[600] text-[16px] rounded-full flex items-center justify-between pl-5 pr-1 transition-all duration-700 hover:bg-neutral-100 shadow-xl shadow-black/30 group cursor-pointer"
                    id="hero-cta-btn"
                  >
                    <span className="select-none">Book a Free Call</span>
                    <div 
                      className="w-[40px] h-[40px] rounded-full bg-[#FF6A3A] flex items-center justify-center text-white transition-transform duration-700 group-hover:scale-105" 
                      id="hero-cta-circle"
                    >
                      <ArrowUpRight className="w-5 h-5 stroke-[2.5]" />
                    </div>
                  </button>
                </div>

                {/* Hero Title (Gigantic Typography positioned on the left with generous spacing) */}
                <div 
                  className="absolute left-12 md:left-[160px] bottom-[70px] z-20 select-none w-[calc(100%-96px)] md:w-[calc(100%-320px)] overflow-hidden"
                  id="hero-massive-title"
                >
                  <h1 className="font-display font-[800] leading-[0.9] text-white uppercase tracking-tighter text-[clamp(3rem,10vw,110px)] text-left drop-shadow-[0_4px_16px_rgba(0,0,0,0.4)]">
                    ZAMEER STUDIO
                  </h1>
                </div>

                {/* Bottom Right Scroll Text */}
                <div 
                  onClick={() => changeSlide(1)}
                  onMouseEnter={() => setCursorType("hover")}
                  onMouseLeave={() => setCursorType("default")}
                  className="absolute right-6 md:right-[70px] bottom-[30px] z-30 cursor-pointer font-sans text-[20px] font-[500] text-white/90 select-none pointer-events-auto flex items-center gap-2 hover:text-white transition-colors duration-700 drop-shadow-[0_1px_4px_rgba(0,0,0,0.5)] min-h-[44px] py-2"
                  id="hero-scroll-btn"
                >
                  <span>(Scroll down)</span>
                </div>
              </div>
            </motion.div>
          )}

          {currentSlide === 1 && (
            <motion.div
              key="about-slide"
              custom={{ index: 1, dir: slideDirection }}
              variants={isUpliftActive ? upliftVariants : standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 1, willChange: "transform, opacity" }}
              className="absolute inset-0 w-full h-full bg-[#ff4f1d] flex flex-col justify-center overflow-hidden"
              id="about-slide-screen"
            >
              <motion.div 
                className="max-w-[1500px] mx-auto px-6 md:px-12 w-full grid grid-cols-1 lg:grid-cols-12 gap-y-8 gap-x-8 pt-8 pb-8 lg:pt-0 lg:pb-0 h-full max-h-[900px] items-start" 
                id="about-grid"
                variants={{
                  initial: {},
                  animate: { transition: { staggerChildren: 0.1, delayChildren: 0.5 } },
                  exit: {}
                }}
              >
                {/* LEFT LABEL */}
                <div className="hidden lg:block lg:col-span-2" id="about-left">
                </div>

                {/* RIGHT CONTENT */}
                <div className="lg:col-span-10 flex flex-col items-start pt-24 lg:pt-[18vh]" id="about-right">
                  {/* MAIN HEADLINE */}
                  <div className="flex flex-col space-y-0 w-full">
                    <div className="overflow-hidden">
                      <motion.h2 
                        variants={{
                          initial: { y: "120%" },
                          animate: { y: 0, transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] } }
                        }} 
                        className="font-anton text-white uppercase text-[15vw] md:text-[11vw] lg:text-[7.5vw] xl:text-[7vw] leading-[0.9] m-0 p-0 text-left"
                      >
                        WE BUILD PREMIUM
                      </motion.h2>
                    </div>
                    <div className="overflow-hidden">
                      <motion.h2 
                        variants={{
                          initial: { y: "120%" },
                          animate: { y: 0, transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] } }
                        }} 
                        className="font-anton text-white uppercase text-[15vw] md:text-[11vw] lg:text-[7.5vw] xl:text-[7vw] leading-[0.9] m-0 p-0 text-left"
                      >
                        DIGITAL EXPERIENCES
                      </motion.h2>
                    </div>
                  </div>

                  {/* STATISTICS CARDS */}
                  <motion.div 
                    variants={{
                      initial: {},
                      animate: { transition: { staggerChildren: 0.1 } }
                    }}
                    className="grid grid-cols-1 lg:grid-cols-[1fr_0.85fr_1fr] gap-4 w-full mb-8 mt-4"
                  >
                    {/* Card 01 */}
                    <motion.div 
                      variants={{
                        initial: { opacity: 0, y: 40 },
                        animate: { opacity: 1, y: 0, transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] } }
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
                        animate: { opacity: 1, y: 0, transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] } }
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
                        animate: { opacity: 1, y: 0, transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] } }
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

                  <motion.div 
                    variants={{
                      initial: { opacity: 0, y: 20 },
                      animate: { opacity: 1, y: 0, transition: { duration: 1.4, ease: [0.22, 1, 0.36, 1] } }
                    }}
                  >
                    <button 
                      onClick={() => setIsContactOpen(true)}
                      onMouseEnter={() => setCursorType("hover")}
                      onMouseLeave={() => setCursorType("default")}
                      className="bg-white rounded-full flex items-center gap-6 pl-10 pr-2.5 py-2.5 shadow-sm hover:shadow-[0_12px_30px_rgba(0,0,0,0.15)] transition-all duration-400 group group-hover:scale-[1.02]"
                    >
                      <span className="font-sans font-bold text-[#111111] text-lg whitespace-nowrap tracking-tight">
                        Start Your Project
                      </span>
                      <div className="bg-[#ff4f1d] w-12 h-12 rounded-full flex items-center justify-center transition-colors duration-400 group-hover:bg-[#e04318]">
                        <ArrowRight className="w-5 h-5 text-white transform group-hover:translate-x-1 transition-transform duration-400" />
                      </div>
                    </button>
                  </motion.div>
                </div>
              </motion.div>
            </motion.div>
          )}

          {currentSlide === 2 && (
            <motion.div
              key="services-slide"
              custom={{ index: 2, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 2, willChange: "transform, opacity" }}
              className="absolute inset-0 w-full h-full bg-[#F6EEDC] overflow-y-auto"
              id="services-slide-screen"
            >
              {/* Floating Image Preview */}
              <motion.div
                className="fixed top-0 left-0 pointer-events-none z-[100] hidden md:block"
                style={{ x: smoothX, y: smoothY, marginLeft: 20, marginTop: 20, willChange: "transform" }}
                animate={{
                  opacity: hoveredServiceImage ? 1 : 0,
                  scale: hoveredServiceImage ? 1 : 0.95,
                }}
                transition={{
                  opacity: { duration: 0.3, ease: "easeOut" },
                  scale: { duration: 0.3, ease: "easeOut" }
                }}
              >
                {hoveredServiceImage && (
                  <img loading="lazy" decoding="async" 
                    src={hoveredServiceImage}
                    alt="Service Preview"
                    className="w-[220px] h-[300px] object-cover rounded-[12px] shadow-2xl shadow-black/30"
                  />
                )}
              </motion.div>

              <div className="w-full max-w-[1600px] mx-auto px-6 md:px-[120px] py-[40px] md:py-[60px]">
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
                      className="group flex flex-col lg:grid lg:grid-cols-12 items-start lg:items-center py-[25px] md:py-[32px] border-b border-black/12 transition-colors duration-700 hover:border-black/30 cursor-pointer gap-4 lg:gap-0 relative"
                      onMouseEnter={() => {
                        setCursorType("hover");
                        setHoveredServiceImage(srv.image);
                      }}
                      onMouseLeave={() => {
                        setCursorType("default");
                      }}
                    >
                      {/* Column 1: Number */}
                      <div className="lg:col-span-1 font-sans text-[22px] md:text-[26px] font-medium text-[#777777] self-start lg:self-center">
                        {srv.number}
                      </div>
                      
                      {/* Column 2: Title */}
                      <div className="lg:col-span-6 self-start lg:self-center transition-transform duration-700 ease-in-out group-hover:translate-x-[10px]">
                        <h3 className="font-anton text-[26px] md:text-[40px] text-[#111111] uppercase leading-[0.9] m-0 p-0">
                          {srv.title}
                        </h3>
                      </div>
                      
                      {/* Column 3: Description */}
                      <div className="lg:col-span-5 self-start lg:self-center">
                        <p className="font-sans text-[15px] md:text-[17px] text-[#666666] leading-[1.6] max-w-[500px] transition-opacity duration-700 opacity-90 group-hover:opacity-100 m-0">
                          {srv.description}
                        </p>
                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
            </motion.div>
          )}



          
                                        {currentSlide === 3 && (
            <motion.div
              key="reveal-slide"
              custom={{ index: 3, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 4, willChange: "transform, opacity" }}
              className="absolute inset-0 w-full h-full bg-[#F6EEDC] flex flex-col justify-center items-center overflow-hidden"
              id="reveal-slide-screen"
            >
              {/* Central text WORK perfectly together at 0, splits apart as scroll */}
              <div className="absolute inset-0 flex items-center justify-center pointer-events-none z-[5]">
                <div className="font-display font-black text-[22vw] leading-none text-[#111111] uppercase tracking-tighter flex items-center justify-center">
                  <motion.div style={{ x: woX }} className="will-change-transform flex items-center">
                    WO
                  </motion.div>
                  <motion.div style={{ x: rkX }} className="will-change-transform flex items-center">
                    RK
                  </motion.div>
                </div>
              </div>

              {/* The Full-Screen Projects */}
                            {PROJECTS.map((project, idx) => (
                <ProjectCard key={project.id} project={project} idx={idx} splitProgress={splitProgress} />
              ))}
            </motion.div>
          )}

          {currentSlide === 4 && (
            <motion.div
              key="skills-slide"
              custom={{ index: 4, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 5, willChange: "transform, opacity" }}
              className="absolute inset-0 w-full h-full bg-[#0d0d0d]"
              id="skills-slide-screen"
            >
              <Suspense fallback={null}><SkillsSection /></Suspense>
            </motion.div>
          )}
          {currentSlide === 5 && (
            <motion.div
              key="testimonials-slide"
              custom={{ index: 5, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 6, willChange: "transform, opacity" }}
              className="absolute inset-0 w-full h-full bg-[#121212] flex flex-col justify-center"
              id="testimonials-slide-screen"
            >
              <div className="max-w-7xl mx-auto px-6 md:px-12 w-full space-y-8" id="testimonials-container">
                
                <div className="text-center space-y-2" id="testimonials-header">
                  <span className="font-mono text-xs tracking-widest uppercase text-[#ff4f1d] block">
                    06 // CLIENT STORIES
                  </span>
                  <h2 className="font-display text-3xl sm:text-4xl font-black tracking-tight uppercase max-w-2xl mx-auto leading-none" id="testimonials-heading">
                    STORIES FROM OUR HAPPY CLIENTS
                  </h2>
                </div>

                {/* Testimonial Cards Layout */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6" id="testimonials-grid">
                  {TESTIMONIALS.map((t, idx) => (
                    <div 
                      key={idx}
                      className="bg-white/[0.02] border border-white/5 rounded-2xl p-6 flex flex-col justify-between gap-4 hover:border-white/15 transition-all duration-700"
                      id={`testimonial-card-${idx}`}
                    >
                      <p className="text-white/80 text-xs italic leading-relaxed" id={`testimonial-text-${idx}`}>
                        "{t.text}"
                      </p>

                      <div className="flex items-center gap-3" id={`testimonial-user-${idx}`}>
                        <div className="w-8 h-8 overflow-hidden rounded-full border border-white/10" id={`testimonial-avatar-wrap-${idx}`}>
                          <img loading="lazy" decoding="async" 
                            src={t.image} 
                            alt={t.name}
                            className="w-full h-full object-cover"
                            referrerPolicy="no-referrer"
                            id={`testimonial-avatar-${idx}`}
                          />
                        </div>
                        <div id={`testimonial-meta-${idx}`}>
                          <div className="font-display font-bold text-xs uppercase text-white" id={`testimonial-name-${idx}`}>{t.name}</div>
                          <div className="font-mono text-[9px] tracking-widest uppercase text-white/50" id={`testimonial-role-${idx}`}>{t.role}</div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>

              </div>
            </motion.div>
          )}

          {currentSlide === 6 && (
            <motion.div
              key="faq-contact-slide"
              custom={{ index: 7, dir: slideDirection }}
              variants={standardVariants}
              initial="initial"
              animate="animate"
              exit="exit"
              style={{ zIndex: 8, willChange: "transform, opacity" }}
              className="absolute inset-0 w-full h-full bg-[#121212]"
            >
              <ScrollLocker
                id="faq-contact-slide-screen"
                className="absolute inset-0 w-full h-full pt-24 pb-12 custom-scrollbar"
                onNext={() => changeSlide("next")}
                onPrev={() => changeSlide("prev")}
              >
              <div className="max-w-7xl mx-auto px-6 md:px-12 space-y-16" id="faq-contact-wrapper">
                
                {/* FAQ section */}
                <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center" id="faq-grid">
                  <div className="lg:col-span-5 space-y-4" id="faq-left">
                    <span className="font-mono text-xs tracking-widest uppercase text-[#ff4f1d] block">
                      08 // FAQ
                    </span>
                    <h2 className="font-display text-3xl sm:text-4xl font-black tracking-tight uppercase leading-none" id="faq-heading">
                      EVERYTHING YOU NEED TO KNOW
                    </h2>
                  </div>

                  <div className="lg:col-span-7 space-y-3" id="faq-right">
                    {FAQS.map((faq, idx) => {
                      const isOpen = openFaqIndex === idx;
                      return (
                        <div 
                          key={idx}
                          className="bg-white/[0.02] border border-white/5 rounded-xl overflow-hidden transition-all duration-700"
                          id={`faq-item-${idx}`}
                        >
                          <button
                            onClick={() => setOpenFaqIndex(isOpen ? null : idx)}
                            onMouseEnter={() => setCursorType("hover")}
                            onMouseLeave={() => setCursorType("default")}
                            className="w-full px-5 py-4 flex justify-between items-center text-left"
                            id={`faq-btn-${idx}`}
                          >
                            <span className="font-display font-bold text-xs tracking-wide text-white uppercase">
                              {faq.question}
                            </span>
                            <ChevronDown className={`w-4 h-4 text-white/50 transition-transform duration-700 ${isOpen ? "rotate-180 text-[#ff4f1d]" : ""}`} />
                          </button>

                          <AnimatePresence initial={false}>
                            {isOpen && (
                              <motion.div
                                initial={{ height: 0 }}
                                animate={{ height: "auto" }}
                                exit={{ height: 0 }}
                                transition={{ duration: 0.3, ease: "easeInOut" }}
                                className="overflow-hidden"
                                id={`faq-content-wrap-${idx}`}
                              >
                                <div className="px-5 pb-4 text-xs text-white/60 leading-relaxed border-t border-white/5 pt-3" id={`faq-answer-${idx}`}>
                                  {faq.answer}
                                </div>
                              </motion.div>
                            )}
                          </AnimatePresence>
                        </div>
                      );
                    })}
                  </div>
                </div>

                {/* Contact CTA Section */}
                <div className="bg-[#ff4f1d] text-white rounded-3xl p-8 md:p-12 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative overflow-hidden" id="cta-card">
                  <div className="lg:col-span-7 space-y-6 relative z-10" id="cta-footer-left">
                    <span className="font-mono text-xs tracking-widest uppercase text-white/70 block">
                      09 // CONTACT US
                    </span>
                    <h2 className="font-display text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight uppercase leading-none" id="cta-footer-heading">
                      LET'S CREATE TOGETHER
                    </h2>
                    <p className="text-white/80 text-sm max-w-lg font-light leading-relaxed" id="cta-footer-p">
                      We translate brand visions into striking digital products that stand out, scale, and deliver impact. Let's make something timeless.
                    </p>

                    <div className="flex flex-col sm:flex-row items-start sm:items-center gap-4" id="cta-footer-actions">
                      <button
                        onClick={() => setIsContactOpen(true)}
                        onMouseEnter={() => setCursorType("hover")}
                        onMouseLeave={() => setCursorType("default")}
                        className="bg-black text-white hover:bg-white hover:text-black font-mono text-xs tracking-widest font-semibold uppercase px-8 py-4 rounded-full transition-all duration-700 flex items-center gap-3"
                        id="cta-footer-btn"
                      >
                        <span>Start a project</span>
                        <ArrowRight className="w-4 h-4" />
                      </button>

                      <button
                        onClick={handleCopyEmail}
                        onMouseEnter={() => setCursorType("hover")}
                        onMouseLeave={() => setCursorType("default")}
                        className="bg-white/10 hover:bg-white/20 text-white font-mono text-xs tracking-widest font-semibold uppercase px-6 py-4 rounded-full transition-all duration-700 flex items-center gap-2"
                        id="cta-copy-btn"
                      >
                        <span>{isCopied ? "COPIED TO CLIPBOARD" : "INFO@LUXFOLIO.COM"}</span>
                      </button>
                    </div>
                  </div>

                  <div className="lg:col-span-5 flex justify-center" id="cta-footer-right">
                    <div className="relative w-full max-w-[240px] aspect-square overflow-hidden rounded-full border border-white/10 shadow-2xl group" id="cta-portrait-frame">
                      <img
                        src={PORTRAITS.ctaModel}
                        alt="Luxfolio Studio Representative"
                        className="w-full h-full object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                        referrerPolicy="no-referrer"
                        id="cta-portrait-img"
                      />
                      <div className="absolute inset-0 bg-[#ff4f1d]/20 mix-blend-overlay pointer-events-none" />
                    </div>
                  </div>

                  {/* Dynamic Loop accent bar inside the contact section */}
                  <div className="absolute bottom-0 left-0 right-0 py-3 bg-black overflow-hidden whitespace-nowrap select-none border-t border-white/10" id="marquee-bar">
                    <div className="inline-block animate-marquee font-display font-black text-[9px] tracking-widest uppercase text-white/50 space-x-12" id="marquee-text">
                      <span>DESIGN WITH PURPOSE</span>
                      <span>•</span>
                      <span>BRAND IDENTITY</span>
                      <span>•</span>
                      <span>UI UX DESIGN</span>
                      <span>•</span>
                      <span>WEB EXPERIENCES</span>
                      <span>•</span>
                      <span>VISUAL STORYTELLING</span>
                      <span>•</span>
                      <span>CREATIVE STUDIO</span>
                      <span>•</span>
                      <span>LET'S COLLABORATE</span>
                      <span>•</span>
                    </div>
                  </div>
                </div>

                {/* Footer Directories */}
                <footer className="pt-12 border-t border-white/5" id="main-footer">
                  <div className="grid grid-cols-1 md:grid-cols-12 gap-8" id="footer-grid">
                    <div className="md:col-span-6 space-y-4" id="footer-left">
                      <h3 className="font-display font-black tracking-widest text-lg text-white uppercase">
                        LUXFOLIO STUDIO
                      </h3>
                      <p className="text-white/40 text-xs max-w-sm leading-relaxed" id="footer-description">
                        A bespoke digital design and creative arts system engineered to craft bold luxury assets that elevate businesses and captivate audiences.
                      </p>
                    </div>

                    <div className="md:col-span-3 space-y-3" id="footer-links">
                      <h4 className="font-mono text-xs tracking-widest uppercase text-[#ff4f1d] font-semibold">
                        EXPLORE
                      </h4>
                      <div className="flex flex-col gap-1.5 text-xs font-mono tracking-widest uppercase text-white/50" id="footer-explore-links">
                        <button onClick={() => changeSlide(0)} className="hover:text-white text-left transition-colors py-2 block">Home</button>
                        <button onClick={() => changeSlide(1)} className="hover:text-white text-left transition-colors py-2 block">About</button>
                        <button onClick={() => changeSlide(2)} className="hover:text-white text-left transition-colors py-2 block">Services</button>
                        <button onClick={() => changeSlide(3)} className="hover:text-white text-left transition-colors py-2 block">Works</button>
                        <button onClick={() => changeSlide(4)} className="hover:text-white text-left transition-colors py-2 block">Skills</button>
                        <button onClick={() => changeSlide(5)} className="hover:text-white text-left transition-colors py-2 block">Reviews</button>
                        <button onClick={() => changeSlide(6)} className="hover:text-white text-left transition-colors py-2 block">Contact</button>
                      </div>
                    </div>

                    <div className="md:col-span-3 space-y-3" id="footer-contact-info">
                      <h4 className="font-mono text-xs tracking-widest uppercase text-[#ff4f1d] font-semibold">
                        OFFICE
                      </h4>
                      <p className="text-white/50 text-[11px] font-mono leading-relaxed uppercase" id="footer-address">
                        Los Angeles, California<br />
                        United States, Remote
                      </p>
                    </div>
                  </div>

                  <div className="mt-12 pt-6 border-t border-white/5 flex flex-col sm:flex-row justify-between items-center gap-4 text-[10px] font-mono tracking-wider text-white/30 uppercase" id="footer-credits">
                    <div id="footer-rights">© 2026 LUXFOLIO. All Rights Reserved.</div>
                    <div className="flex gap-4" id="footer-policies">
                      <a href="#" className="hover:text-white transition-colors">Privacy Policy</a>
                      <span>•</span>
                      <a href="#" className="hover:text-white transition-colors">Terms of Service</a>
                    </div>
                  </div>
                </footer>

              </div>
            </ScrollLocker>
            </motion.div>
          )}
        </AnimatePresence>

        
      </div>

      
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
                className="font-mono text-[11px] font-bold uppercase tracking-widest text-white px-[16px] h-[44px] flex items-center justify-center rounded-full border border-white/20"
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
                { name: "Skills", index: 4 }
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

      {/* CONTACT MODAL POPUP */}
      <Suspense fallback={null}><ContactModal isOpen={isContactOpen} onClose={() => setIsContactOpen(false)} /></Suspense>

      </div>

      {/* NATURAL SCROLL SPACER */}
      <div style={{ height: "1000dvh" }} className="pointer-events-none relative w-1 opacity-0 z-0" id="lenis-scroll-spacer" />
    </div>
  );
}
