const skillsMain = document.querySelectorAll(".skills-main");
const skillsSection = document.querySelectorAll(".skills-section");

skillsMain.forEach((skill, index) => {
  // Show the skill section when hovering over the skill main item
  skill.addEventListener('mouseenter', () => {
    skillsSection[index].style.display = 'flex';
    skillsSection[index].style.flexDirection = 'column';
    skillsSection[index].style.opacity = '100%';
  });

  // Hide the skill section when the mouse leaves the skill main item
  skill.addEventListener('mouseleave', () => {
    skillsSection[index].style.opacity = '0%';

  });
});