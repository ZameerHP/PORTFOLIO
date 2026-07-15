import React, { useState } from "react";
import { motion, AnimatePresence } from "motion/react";
import { Check, ArrowRight } from "lucide-react";

interface ContactModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export function ContactModal({ isOpen, onClose }: ContactModalProps) {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
    plan: "Standard",
  });
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitted(true);
    setTimeout(() => {
      setIsSubmitted(false);
      setFormData({ name: "", email: "", message: "", plan: "Standard" });
      onClose();
    }, 2800);
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          {/* Backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="absolute inset-0 bg-black/80 backdrop-blur-md"
            id="modal-backdrop"
          />

          {/* Modal Content */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 20 }}
            transition={{ type: "spring", damping: 30, stiffness: 300 }}
            className="relative w-full max-w-lg overflow-hidden rounded-2xl border border-white/10 bg-[#141414] p-8 md:p-10 shadow-2xl"
            id="modal-container"
          >
            <button
              onClick={onClose}
              className="absolute top-4 right-4 p-3 text-white/50 transition-colors hover:text-white text-xl font-light"
              id="modal-close-btn"
            >
              ✕
            </button>

            {!isSubmitted ? (
              <form onSubmit={handleSubmit} className="space-y-6" id="modal-form">
                <div className="space-y-2">
                  <span className="text-xs font-mono tracking-widest text-[#ff4f1d] uppercase">
                    Start a project
                  </span>
                  <h3 className="font-display text-2xl font-semibold tracking-tight text-white">
                    LET'S CREATE SOMETHING LUXURIOUS
                  </h3>
                  <p className="text-base text-white/60">
                    Brief us on your vision. We will follow up within 24 hours.
                  </p>
                </div>

                <div className="space-y-4">
                  <div>
                    <label className="block text-xs font-mono text-white/50 uppercase tracking-wider mb-2">
                      Full Name
                    </label>
                    <input
                      type="text"
                      required
                      value={formData.name}
                      onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                      className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 text-base text-white focus:outline-none focus:border-[#ff4f1d] transition-colors"
                      placeholder="e.g. John Doe"
                      id="input-name"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-mono text-white/50 uppercase tracking-wider mb-2">
                      Email Address
                    </label>
                    <input
                      type="email"
                      required
                      value={formData.email}
                      onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                      className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 text-base text-white focus:outline-none focus:border-[#ff4f1d] transition-colors"
                      placeholder="john@example.com"
                      id="input-email"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-mono text-white/50 uppercase tracking-wider mb-2">
                      Preferred Scale
                    </label>
                    <select
                      value={formData.plan}
                      onChange={(e) => setFormData({ ...formData, plan: e.target.value })}
                      className="w-full bg-[#181818] border border-white/10 rounded-lg px-4 py-3 text-base text-white focus:outline-none focus:border-[#ff4f1d] transition-colors"
                      id="select-plan"
                    >
                      <option value="Standard">Standard Plan ($500/mo)</option>
                      <option value="Premium">Premium Plan (Starting at $1000)</option>
                      <option value="Enterprise">Enterprise Design System (Custom)</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-xs font-mono text-white/50 uppercase tracking-wider mb-2">
                      Your Ambition / Brief
                    </label>
                    <textarea
                      required
                      rows={4}
                      value={formData.message}
                      onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                      className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 text-base text-white focus:outline-none focus:border-[#ff4f1d] transition-colors resize-none"
                      placeholder="Tell us about your brand..."
                      id="textarea-msg"
                    />
                  </div>
                </div>

                <button
                  type="submit"
                  className="w-full bg-[#ff4f1d] text-white font-medium px-6 py-4 rounded-xl flex items-center justify-center gap-2 hover:bg-[#e04318] transition-all hover:translate-y-[-2px] shadow-lg shadow-[#ff4f1d]/20 group"
                  id="modal-submit-btn"
                >
                  <span>Submit Creative Brief</span>
                  <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
                </button>
              </form>
            ) : (
              <motion.div
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                className="py-12 text-center space-y-4"
                id="modal-success"
              >
                <div className="w-16 h-16 bg-[#ff4f1d]/10 border border-[#ff4f1d]/30 rounded-full flex items-center justify-center mx-auto" id="success-icon-wrap">
                  <Check className="w-8 h-8 text-[#ff4f1d]" />
                </div>
                <h3 className="font-display text-xl font-bold tracking-tight text-white">
                  CREATIVE BRIEF RECEIVED
                </h3>
                <p className="text-base text-white/60 max-w-sm mx-auto">
                  Thank you, <span className="text-white font-medium">{formData.name}</span>! Our Senior Art Director will reach out to you shortly.
                </p>
              </motion.div>
            )}
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
}
