import React, { useRef, useEffect } from "react";

interface ScrollLockerProps {
  children: React.ReactNode;
  onNext: () => void;
  onPrev: () => void;
  className?: string;
  id?: string;
}

export const ScrollLocker = ({ children, onNext, onPrev, className = "", id }: ScrollLockerProps) => {
  const ref = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    
    let isLocked = false;
    let touchStartY = 0;
    
    const handleNext = () => {
      if (!isLocked) {
        isLocked = true;
        onNext();
        setTimeout(() => { isLocked = false }, 1000);
      }
    };
    
    const handlePrev = () => {
      if (!isLocked) {
        isLocked = true;
        onPrev();
        setTimeout(() => { isLocked = false }, 1000);
      }
    };
    
    const handleWheel = (e: WheelEvent) => {
      const scrollableHeight = el.scrollHeight - el.clientHeight;
      const isAtTop = el.scrollTop <= 8;
      const isAtBottom = scrollableHeight <= 10 || el.scrollTop >= scrollableHeight - 8;

      if (e.deltaY > 0 && isAtBottom) {
        handleNext();
        e.preventDefault();
        e.stopPropagation();
        return;
      }
      
      if (e.deltaY < 0 && isAtTop) {
        handlePrev();
        e.preventDefault();
        e.stopPropagation();
        return;
      }
      
      if (scrollableHeight > 10) {
        e.stopPropagation();
      }
    };
    
    const handleTouchStart = (e: TouchEvent) => {
      touchStartY = e.touches[0].clientY;
    };
    
    const handleTouchMove = (e: TouchEvent) => {
      const touchY = e.touches[0].clientY;
      const deltaY = touchStartY - touchY;
      
      const scrollableHeight = el.scrollHeight - el.clientHeight;
      const isAtTop = el.scrollTop <= 8;
      const isAtBottom = scrollableHeight <= 10 || el.scrollTop >= scrollableHeight - 8;

      if (deltaY > 15 && isAtBottom) {
        handleNext();
        e.preventDefault();
        e.stopPropagation();
        return;
      }
      if (deltaY < -15 && isAtTop) {
        handlePrev();
        e.preventDefault();
        e.stopPropagation();
        return;
      }
      
      if (scrollableHeight > 10) {
        e.stopPropagation();
      }
    };
    
    el.addEventListener("wheel", handleWheel, { passive: false });
    el.addEventListener("touchstart", handleTouchStart, { passive: true });
    el.addEventListener("touchmove", handleTouchMove, { passive: false });
    
    return () => {
      el.removeEventListener("wheel", handleWheel);
      el.removeEventListener("touchstart", handleTouchStart);
      el.removeEventListener("touchmove", handleTouchMove);
    };
  }, [onNext, onPrev]);
  
  return (
    <div 
      ref={ref} 
      className={`overflow-y-auto overflow-x-hidden ${className}`} 
      id={id}
      data-lenis-prevent="true"
    >
      {children}
    </div>
  );
};
