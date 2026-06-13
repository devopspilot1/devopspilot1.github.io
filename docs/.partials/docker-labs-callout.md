<style>
  .sleek-callout-docker {
    margin: 2.5rem 0;
    padding: 2rem;
    background: linear-gradient(145deg, #ffffff, #f0f9ff);
    border: 1px solid #e0f2fe;
    border-radius: 16px;
    box-shadow: 0 10px 30px -5px rgba(14, 165, 233, 0.1);
    position: relative;
    overflow: hidden;
  }
  .sleek-callout-docker::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, #0ea5e9, #3b82f6);
  }
  .sleek-header-docker {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 1rem;
  }
  .sleek-icon-docker {
    width: 48px;
    height: 48px;
    background: #e0f2fe;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    box-shadow: 0 4px 10px rgba(14, 165, 233, 0.15);
  }
  .sleek-callout-docker h3 {
    margin: 0;
    font-size: 1.3rem;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.02em;
  }
  .sleek-callout-docker p {
    margin: 0 0 1.5rem 0;
    font-size: 0.95rem;
    line-height: 1.6;
    color: #475569;
  }
  .sleek-btn-group-docker {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
  }
  .sleek-btn-docker {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none !important;
    transition: all 0.2s ease;
  }
  .sleek-btn-primary-docker {
    background: #0ea5e9;
    color: white !important;
    box-shadow: 0 4px 12px rgba(14, 165, 233, 0.25);
  }
  .sleek-btn-primary-docker:hover {
    background: #0284c7;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(14, 165, 233, 0.35);
  }
  .sleek-btn-secondary-docker {
    background: white;
    color: #334155 !important;
    border: 1px solid #cbd5e1;
  }
  .sleek-btn-secondary-docker:hover {
    background: #f0f9ff;
    border-color: #94a3b8;
    transform: translateY(-2px);
  }
  .sleek-promo-docker {
    margin-top: 1.5rem;
    padding-top: 1rem;
    border-top: 1px solid #e0f2fe;
    font-size: 0.8rem;
    color: #64748b;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .sleek-badge-docker {
    background: #fef3c7;
    color: #d97706;
    padding: 2px 8px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 0.7rem;
    letter-spacing: 0.05em;
  }
</style>

<div class="sleek-callout-docker">
  <div class="sleek-header-docker">
    <div class="sleek-icon-docker">🐳</div>
    <h3>Practice Live in Your Browser</h3>
  </div>
  
  <p>
    Don't just read about Docker commands—execute them in real time! Launch a fully-configured, secure Docker sandbox directly in your browser. Practice commands, debug broken containers, and complete timed challenges with instant task validation.
  </p>

  <div class="sleek-btn-group-docker">
    <a href="https://www.devopspilot.com/lab/docker" target="_blank" class="sleek-btn-docker sleek-btn-primary-docker">
      ▶ Start Guided Lab
    </a>
    <a href="https://www.devopspilot.com/lab/docker?tab=troubleshooting" target="_blank" class="sleek-btn-docker sleek-btn-secondary-docker">
      🛠️ Troubleshooting Lab →
    </a>
    <a href="https://www.devopspilot.com/lab/docker?tab=challenge" target="_blank" class="sleek-btn-docker sleek-btn-secondary-docker">
      🏆 Challenge Lab →
    </a>
  </div>

  <div class="sleek-promo-docker">
    <span class="sleek-badge-docker">FREE LAUNCH OFFER</span>
    <span><strong>Get all premium Docker labs for FREE until June 30th!</strong> (No Credit Card Required)</span>
  </div>
</div>
