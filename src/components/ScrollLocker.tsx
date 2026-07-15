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
      const isAtTop = el.scrollTop <= 0;
      const isAtBottom = Math.ceil(el.scrollTop + el.clientHeight) >= el.scrollHeight - 2;

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
      
      e.stopPropagation();
    };
    
    const handleTouchStart = (e: TouchEvent) => {
      touchStartY = e.touches[0].clientY;
    };
    
    const handleTouchMove = (e: TouchEvent) => {
      const touchY = e.touches[0].clientY;
      const deltaY = touchStartY - touchY;
      
      const isAtTop = el.scrollTop <= 0;
      const isAtBottom = Math.ceil(el.scrollTop + el.clientHeight) >= el.scrollHeight - 2;

      // Only trigger onNext/onPrev if there's significant movement to avoid accidental triggers
      if (deltaY > 10 && isAtBottom) {
        handleNext();
        e.preventDefault();
        e.stopPropagation();
        return;
      }
      if (deltaY < -10 && isAtTop) {
        handlePrev();
        e.preventDefault();
        e.stopPropagation();
        return;
      }
      
      e.stopPropagation();
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
