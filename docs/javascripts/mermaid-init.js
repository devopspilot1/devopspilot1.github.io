/**
 * mermaid-init.js
 *
 * Initializes Mermaid with the "dark" theme so diagrams match the site's
 * dark mode. Uses startOnLoad:false + mermaid.run() so our config is applied
 * BEFORE Mermaid renders (avoids the race condition where the CDN auto-renders
 * with the wrong theme before this script's DOMContentLoaded fires).
 */

// Call initialize() synchronously — this script loads after mermaid.min.js so
// mermaid is already defined. Calling initialize() here overrides the CDN
// defaults before the DOMContentLoaded event fires.
if (typeof mermaid !== "undefined") {
  mermaid.initialize({
    startOnLoad: false, // prevent auto-render; we call mermaid.run() below
    theme: "dark",
    themeVariables: {
      // Edge label pill — use a slate-700 tone that reads as an intentional badge
      edgeLabelBackground: "#334155",
      // Overall diagram area
      background: "#1e293b",
      mainBkg: "#1e293b",
      // Connector lines
      lineColor: "#94a3b8",
    },
  });
}

// Once the DOM is ready, manually trigger rendering with our config applied
document.addEventListener("DOMContentLoaded", function () {
  if (typeof mermaid !== "undefined") {
    mermaid.run();
  }
});
