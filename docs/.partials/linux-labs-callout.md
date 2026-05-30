<style>
  .lab-card-link {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    cursor: pointer !important;
    display: block !important;
  }
  .lab-card-link:hover {
    transform: translateY(-4px) !important;
  }
  
  /* Guided Labs Card Hover */
  .lab-card-link.guided {
    background: rgba(16, 185, 129, 0.04) !important;
    border: 1px solid rgba(16, 185, 129, 0.15) !important;
  }
  .lab-card-link.guided:hover {
    background: rgba(16, 185, 129, 0.12) !important;
    border-color: rgba(16, 185, 129, 0.8) !important;
    box-shadow: 0 8px 20px rgba(16, 185, 129, 0.18) !important;
  }

  /* Troubleshooting Card Hover */
  .lab-card-link.troubleshoot {
    background: rgba(59, 130, 246, 0.04) !important;
    border: 1px solid rgba(59, 130, 246, 0.15) !important;
  }
  .lab-card-link.troubleshoot:hover {
    background: rgba(59, 130, 246, 0.12) !important;
    border-color: rgba(59, 130, 246, 0.8) !important;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.18) !important;
  }

  /* Challenge Labs Card Hover */
  .lab-card-link.challenge {
    background: rgba(245, 158, 11, 0.04) !important;
    border: 1px solid rgba(245, 158, 11, 0.15) !important;
  }
  .lab-card-link.challenge:hover {
    background: rgba(245, 158, 11, 0.12) !important;
    border-color: rgba(245, 158, 11, 0.8) !important;
    box-shadow: 0 8px 20px rgba(245, 158, 11, 0.18) !important;
  }
</style>

<div style="margin: 2rem 0; padding: 1.5rem; background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 12px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
    <span style="font-size: 24px; line-height: 1;">🚀</span>
    <h3 style="margin: 0; font-size: 1.1rem; font-weight: 800; color: var(--md-typeset-color, #10b981); letter-spacing: -0.01em;">
      Practice Live inside your Browser!
    </h3>
  </div>
  
  <p style="margin: 0 0 16px 0; font-size: 0.9rem; line-height: 1.5; opacity: 0.85;">
    Don't just read about these commands—execute them in real time! We have prepared fully-configured, secure sandbox environments with automated task validation ready for you.
  </p>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
    <!-- Guided Mode -->
    <a href="https://www.devopspilot.com/lab/linux" target="_blank" class="lab-card-link guided" style="text-decoration: none; padding: 12px; border-radius: 8px; display: block; text-align: center;">
      <div style="font-size: 1.25rem; margin-bottom: 4px;">🎯</div>
      <strong style="display: block; font-size: 0.85rem; color: #10b981; margin-bottom: 2px;">Guided Labs</strong>
      <span style="font-size: 0.75rem; opacity: 0.7; display: block; line-height: 1.2;">Step-by-step interactive command practice</span>
    </a>

    <!-- Troubleshooting Mode -->
    <a href="https://www.devopspilot.com/lab/linux?tab=troubleshooting" target="_blank" class="lab-card-link troubleshoot" style="text-decoration: none; padding: 12px; border-radius: 8px; display: block; text-align: center;">
      <div style="font-size: 1.25rem; margin-bottom: 4px;">🛠️</div>
      <strong style="display: block; font-size: 0.85rem; color: #3b82f6; margin-bottom: 2px;">Troubleshooting</strong>
      <span style="font-size: 0.75rem; opacity: 0.7; display: block; line-height: 1.2;">Debug & fix pre-broken live Linux servers</span>
    </a>

    <!-- Challenge Mode -->
    <a href="https://www.devopspilot.com/lab/linux?tab=challenge" target="_blank" class="lab-card-link challenge" style="text-decoration: none; padding: 12px; border-radius: 8px; display: block; text-align: center;">
      <div style="font-size: 1.25rem; margin-bottom: 4px;">🏆</div>
      <strong style="display: block; font-size: 0.85rem; color: #f59e0b; margin-bottom: 2px;">Challenge Labs</strong>
      <span style="font-size: 0.75rem; opacity: 0.7; display: block; line-height: 1.2;">Test your skills against custom timers</span>
    </a>
  </div>

  <div style="margin-top: 14px; text-align: center; font-size: 0.75rem; opacity: 0.85; font-weight: bold;">
    ⚡ <span style="color: #10b981; text-transform: uppercase; letter-spacing: 0.05em;">Free Launch Offer:</span> Get all premium Linux labs for <span style="color: #10b981;">FREE</span> until June 30th! (No Credit Card Required)
  </div>
</div>
