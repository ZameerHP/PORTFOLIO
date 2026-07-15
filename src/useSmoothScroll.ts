import { useEffect } from "react";

export function useSmoothScroll() {
  useEffect(() => {
    // Elegant frame-based smooth scroll logic to replicate Lenis behavior
    let targetScroll = window.scrollY;
    let currentScroll = window.scrollY;
    const ease = 0.085; // Luxuriously soft, weighted, fluid cinematic feel
    let animationFrameId: number;
    let isScrollActive = false;

    const onWheel = (e: WheelEvent) => {
      // Allow custom smooth scroll while preventing default janky browser jumps
      e.preventDefault();
      targetScroll += e.deltaY * 0.85;
      
      // Keep boundaries
      const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      targetScroll = Math.max(0, Math.min(targetScroll, maxScroll));
      
      if (!isScrollActive) {
        isScrollActive = true;
        animate();
      }
    };

    const animate = () => {
      currentScroll += (targetScroll - currentScroll) * ease;
      
      if (Math.abs(targetScroll - currentScroll) < 0.3) {
        currentScroll = targetScroll;
        window.scrollTo(0, currentScroll);
        isScrollActive = false;
        return;
      }
      
      window.scrollTo(0, currentScroll);
      animationFrameId = requestAnimationFrame(animate);
    };

    // Track standard native scroll triggers as well (so buttons, keyboard, etc. keep track of target)
    const onScroll = () => {
      if (!isScrollActive) {
        targetScroll = window.scrollY;
        currentScroll = window.scrollY;
      }
    };

    window.addEventListener("wheel", onWheel, { passive: false });
    window.addEventListener("scroll", onScroll);

    return () => {
      window.removeEventListener("wheel", onWheel);
      window.removeEventListener("scroll", onScroll);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);
}
