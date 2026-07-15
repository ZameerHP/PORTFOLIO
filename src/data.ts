export interface ServiceItem {
  id: string;
  number: string;
  title: string;
  description: string;
  image: string;
}

export interface ProjectItem {
  id: string;
  title: string;
  description: string;
  image: string;
  tag: string;
}

export interface StepItem {
  number: string;
  title: string;
  description: string;
}

export interface TestimonialItem {
  name: string;
  role: string;
  text: string;
  image: string;
}

export interface FAQItem {
  question: string;
  answer: string;
}

export const PORTRAITS = {
  hero: "https://raw.githubusercontent.com/ZameerHP/PORTFOLIO/refs/heads/main/Remove_text_from_image_2K_202607120915.jpeg", // Custom high-end user background image
  gelPortrait: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=1200&auto=format&fit=crop", // Colorful gel/teal tone light portrait
  storytelling: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=1200&auto=format&fit=crop", // Elegant woman, glasses
  innovation: "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?q=80&w=1200&auto=format&fit=crop", // Studio dramatic portrait
  uiux: "https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=1200&auto=format&fit=crop", // Platinum hair elegant model
  faqLady: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=1200&auto=format&fit=crop", // High fashion clean portrait with red lipstick
  ctaModel: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=800&auto=format&fit=crop" // Beanie glasses modern male portrait
};

export const SERVICES: ServiceItem[] = [
  {
    id: "website-design",
    number: "01",
    title: "Website Design",
    description: "Crafting timeless digital experiences with exceptional design, clarity, and purpose.",
    image: "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=600&q=80&auto=format&fit=crop"
  },
  {
    id: "web-development",
    number: "02",
    title: "Full-Stack Development",
    description: "Engineering high-performance websites that are fast, scalable, and built for the future.",
    image: "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=600&q=80&auto=format&fit=crop"
  },
  {
    id: "ui-ux",
    number: "03",
    title: "UI/UX Experience",
    description: "Creating intuitive interfaces that combine beauty, usability, and seamless interaction.",
    image: "https://images.unsplash.com/photo-1558655146-d09347e92766?w=600&q=80&auto=format&fit=crop"
  },
  {
    id: "seo-perf",
    number: "04",
    title: "Performance & SEO",
    description: "Optimizing every detail for speed, visibility, accessibility, and long-term growth.",
    image: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80&auto=format&fit=crop"
  }
];

export const PROJECTS: ProjectItem[] = [
  {
    id: "project-1",
    title: "VISUAL STORYTELLING",
    description: "Through creative visuals and design, we turn ideas into compelling stories that connect with audiences.",
    image: PORTRAITS.storytelling,
    tag: "Art Direction"
  },
  {
    id: "project-2",
    title: "DIGITAL INNOVATION",
    description: "We explore new ideas and technologies to create digital experiences that are bold, meaningful, and memorable.",
    image: PORTRAITS.innovation,
    tag: "Creative Tech"
  },
  {
    id: "project-3",
    title: "UI / UX EXPERIENCES",
    description: "We design intuitive user interfaces and seamless user experiences that make digital products easy, engaging, and enjoyable to use.",
    image: PORTRAITS.uiux,
    tag: "Design System"
  }
];

export const STEPS: StepItem[] = [
  {
    number: "01",
    title: "STRATEGY FIRST",
    description: "We align on goals, audience, and creative direction before anything goes live."
  },
  {
    number: "02",
    title: "CREATE & MANAGE",
    description: "We handle planning, execution, and delivery across all essential platforms."
  },
  {
    number: "03",
    title: "REVIEW & REFINE",
    description: "We track performance, refine details, and optimize results continuously."
  }
];

export const TESTIMONIALS: TestimonialItem[] = [
  {
    name: "Sarah Lim",
    role: "Marketing Manager",
    text: "They completely elevated our brand presence. The new website feels modern and truly exceeded expectations!",
    image: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=150&auto=format&fit=crop"
  },
  {
    name: "Monali Sen",
    role: "Founder",
    text: "The team delivered more than we expected. The experience feels premium, thoughtful, and built for real impact!",
    image: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=150&auto=format&fit=crop"
  },
  {
    name: "Emily Ross",
    role: "Product Manager",
    text: "Working with Luxfolio was smooth and professional. The design quality and attention to detail truly stood out!",
    image: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=150&auto=format&fit=crop"
  },
  {
    name: "Olivia Emma",
    role: "Marketing Manager",
    text: "Luxfolio understood our vision from day one. The final result feels clean, confident, and perfectly executed!",
    image: "https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=150&auto=format&fit=crop"
  }
];

export const FAQS: FAQItem[] = [
  {
    question: "WHAT SERVICES DO YOU OFFER?",
    answer: "We do minimal only when needed, but always aim for impact when required. Craft digital experiences that are intuitive, fast, and unforgettable — built to convert and impress. Only purpose-driven design."
  },
  {
    question: "HOW DO I KNOW WHICH PLAN IS RIGHT FOR ME?",
    answer: "We offer clear, transparent collaboration tiers. The Standard plan is best for startups needing rapid asset and page design, while our Premium tier offers a comprehensive end-to-end strategy, customized high-fidelity design systems, and dedicated support."
  },
  {
    question: "HOW SOON CAN I EXPECT RESULTS?",
    answer: "Initial strategy alignment and layouts are presented within the first week. Standard page builds take 2-3 weeks, while comprehensive premium plans are fully executed, refined, and delivered within 4-6 weeks."
  },
  {
    question: "DO YOU OFFER CUSTOM PACKAGES?",
    answer: "Absolutely. We understand unique project parameters. Get in touch directly, and we can define a tailor-made engagement scale, scope, and delivery schedule that fits your exact ambitions."
  }
];
