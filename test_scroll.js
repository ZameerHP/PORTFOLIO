const PROJECTS = [1,2,3];
const numProjects = PROJECTS.length;
const workScrolls = numProjects; // 3
const workEndVh = 3 + workScrolls + 1; // 7

function test(scrollY) {
  let activeIndex = 0;
  let progress = 0;
  let vh = 1;

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
  return {activeIndex, progress};
}

console.log("0:", test(0));
console.log("1:", test(1));
console.log("2:", test(2));
console.log("3:", test(3)); // attached
console.log("3.5:", test(3.5)); // splitting
console.log("4:", test(4)); // p1
console.log("5:", test(5)); // p2
console.log("6:", test(6)); // p3
console.log("6.5:", test(6.5)); // p3 still visible? Yes! progress clamped to 300, activeIndex 3.
console.log("7:", test(7)); // Reviews!
console.log("8:", test(8)); // Pricing
console.log("9:", test(9)); // Contact
