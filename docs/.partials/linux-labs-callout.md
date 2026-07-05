<style>
  .sleek-callout {
    margin: 2.5rem 0;
    padding: 2rem;
    background: linear-gradient(145deg, #ffffff, #f8fafc);
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.05);
    position: relative;
    overflow: hidden;
  }
  .sleek-callout::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, #10b981, #3b82f6);
  }
  .sleek-callout-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 1rem;
  }
  .sleek-icon-box {
    width: 48px;
    height: 48px;
    background: #ecfdf5;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    box-shadow: 0 4px 10px rgba(16, 185, 129, 0.1);
  }
  .sleek-callout h3 {
    margin: 0;
    font-size: 1.3rem;
    font-weight: 800;
    color: #1e293b;
    letter-spacing: -0.02em;
  }
  .sleek-callout p {
    margin: 0 0 1.5rem 0;
    font-size: 0.95rem;
    line-height: 1.6;
    color: #475569;
  }
  .sleek-btn-group {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
  }
  .sleek-btn {
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
  .sleek-btn-primary {
    background: #10b981;
    color: white !important;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.25);
  }
  .sleek-btn-primary:hover {
    background: #059669;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(16, 185, 129, 0.35);
  }
  .sleek-btn-secondary {
    background: white;
    color: #334155 !important;
    border: 1px solid #cbd5e1;
  }
  .sleek-btn-secondary:hover {
    background: #f8fafc;
    border-color: #94a3b8;
    transform: translateY(-2px);
  }
  .sleek-promo {
    margin-top: 1.5rem;
    padding-top: 1rem;
    border-top: 1px solid #f1f5f9;
    font-size: 0.8rem;
    color: #64748b;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .sleek-promo-badge {
    background: #fef3c7;
    color: #d97706;
    padding: 2px 8px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 0.7rem;
    letter-spacing: 0.05em;
  }
</style>

<div class="sleek-callout">
  <div class="sleek-callout-header">
    <div class="sleek-icon-box">🚀</div>
    <h3>Practice Live in Your Browser</h3>
  </div>
  
  <p>
    Stop reading and start doing! Launch a fully-configured, secure Linux sandbox directly in your browser. Practice commands, debug broken servers, and complete timed challenges with instant task validation.
  </p>

  <div class="sleek-btn-group">
    <a href="https://www.devopspilot.com/lab/linux" target="_blank" class="sleek-btn sleek-btn-primary">
      ▶ Start Guided Lab
    </a>
    <a href="https://www.devopspilot.com/lab/linux?tab=troubleshooting" target="_blank" class="sleek-btn sleek-btn-secondary">
      🛠️ Troubleshooting Lab →
    </a>
    <a href="https://www.devopspilot.com/lab/linux?tab=challenge" target="_blank" class="sleek-btn sleek-btn-secondary">
      🏆 Challenge Lab →
    </a>
  </div>

  <div class="sleek-promo">
    <span class="sleek-promo-badge">FREE LAUNCH OFFER</span>
    <span><strong>Get all premium Linux labs for FREE until July 31st!</strong> (No Credit Card Required)</span>
  </div>
</div>
