document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("toggle-qa");
  if (!btn) return;

  // Initial state: assume collapsed
  let expanded = false;

  btn.addEventListener("click", () => {
    // Get all details elements on the page
    const allDetails = document.querySelectorAll("details");
    
    // Toggle state
    expanded = !expanded;

    // Apply new state to all details elements
    allDetails.forEach(d => {
      d.open = expanded;
    });

    // Update button text
    btn.textContent = expanded
      ? "Collapse all answers"
      : "Expand all answers";
  });
});
