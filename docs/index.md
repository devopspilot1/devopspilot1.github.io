---
title: Welcome to DevopsPilot
hide:
  - navigation
  - toc
---

<style>
  :root {
    /* Use the MkDocs Material theme primary color variable (defined in extra.css as #0f790e) */
    --primary-color: #0f790e;
    --secondary-color: #4ade80; /* Light Green to match Primary */
    --accent-color: #0f790e;
    --text-dark: #1f2937;
    --text-light: #6b7280;
  }
  
  /* Hero Section */
  .hero {
    padding: 0.5rem 1.5rem 2.5rem 1.5rem;
    margin-top: -1.5rem;
    text-align: center;
    margin-bottom: 2.5rem;
    background: transparent;
  }
  .hero h1 {
    font-size: 3.2rem !important;
    font-weight: 900;
    margin: 0 0 1.2rem 0;
    background: linear-gradient(135deg, #0f790e, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.15;
    letter-spacing: -0.02em;
  }
  .hero p {
    font-size: 1.2rem;
    max-width: 720px;
    margin: 0 auto 2.5rem auto;
    opacity: 0.85;
    line-height: 1.6;
    color: var(--md-typeset-color, #374151);
  }
  .hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }
  .btn {
    padding: 0.8rem 2.2rem;
    border-radius: 50px;
    font-weight: 700;
    text-decoration: none !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    display: inline-block;
  }
  .btn-primary {
    background: #0f790e;
    color: white !important;
    box-shadow: 0 4px 15px rgba(15, 121, 14, 0.3);
    border: 2px solid #0f790e;
  }
  .btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(15, 121, 14, 0.4);
    background: #0d660c;
    border-color: #0d660c;
  }
  .btn-secondary {
    background: rgba(15, 121, 14, 0.05);
    color: #0f790e !important;
    border: 2px solid rgba(15, 121, 14, 0.2);
  }
  .btn-secondary:hover {
    background: rgba(15, 121, 14, 0.1);
    border-color: #0f790e;
    transform: translateY(-3px);
  }

  /* Grid Layouts */
  .grid-3 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
  }
  .topic-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
  }
  
  /* Feature Cards */
  .card {
    background: white;
    border-radius: 12px;
    padding: 2rem;
    border: 1px solid #eaeaea;
    transition: all 0.3s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.08);
    border-color: var(--primary-color);
  }
  .card-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    display: block;
  }
  .card h3 {
    margin-top: 0;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-dark);
  }
  .card p {
    color: var(--text-light);
    line-height: 1.6;
    margin-bottom: 0;
  }

  /* Learning Path */
  .path-container {
    background: #f8fafc;
    border-radius: 16px;
    padding: 2rem;
    border: 1px solid #e2e8f0;
  }
  .step-item {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }
  .step-item:last-child { margin-bottom: 0; }
  .step-num {
    background: var(--primary-color);
    color: white;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    flex-shrink: 0;
    font-size: 1.2rem;
  }
  .step-info h4 {
    margin: 0 0 0.5rem 0;
    color: var(--text-dark);
    font-size: 1.2rem;
  }
  .step-info p {
    margin: 0 0 0.5rem 0;
    color: var(--text-light);
  }
  .step-link {
    color: var(--primary-color);
    font-weight: 600;
    text-decoration: none;
    font-size: 0.95rem;
  }
  .step-link:hover { text-decoration: underline; }

  /* Topic Cards */
  .topic-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: white;
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid #eaeaea;
    text-decoration: none !important;
    transition: all 0.3s ease;
    color: var(--text-dark) !important;
  }
  .topic-card:hover {
    border-color: var(--primary-color);
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.05);
  }
  .topic-icon { font-size: 3rem; margin-bottom: 0.5rem; }
  .topic-name { font-weight: 700; font-size: 1.1rem; }

  /* Utilities */
  .text-center { text-align: center; }
  .section-title { font-size: 2rem; font-weight: 800; text-align: center; margin: 4rem 0 2rem 0; color: var(--text-dark); }
  .newsletter {
    margin-top: 4rem;
    padding: 2rem;
    background: #f0fdf4; /* Light green */
    border-radius: 12px;
    text-align: center;
    border: 1px solid #bbf7d0;
  }
</style>

<div class="hero">
  <!-- Launch Offer Top Micro-Badge -->
  <a href="https://www.devopspilot.com" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; padding: 6px 16px; background: rgba(15, 121, 14, 0.05); border: 1px solid rgba(15, 121, 14, 0.2); border-radius: 50px; font-size: 0.72rem; font-weight: 800; color: #0f790e; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: 0.04em; text-decoration: none !important; transition: all 0.3s ease; cursor: pointer;" onmouseover="this.style.background='rgba(15, 121, 14, 0.1)'; this.style.borderColor='#0f790e'; this.style.transform='translateY(-2px)'" onmouseout="this.style.background='rgba(15, 121, 14, 0.05)'; this.style.borderColor='rgba(15, 121, 14, 0.2)'; this.style.transform='translateY(0)'">
    🚀 FREE LAUNCH SPECIAL: Get all premium Linux and Docker labs for FREE until July 31st! (No Credit Card Required)
  </a>
  <h1>Your Co-Pilot for DevOps Mastery</h1>
  <p>Stop watching endless videos. Practice live in real browser-based sandboxes with secure environments, real-world troubleshooting, and instant task validation.</p>
  <div class="hero-buttons">
    <a href="https://www.devopspilot.com/lab/linux" target="_blank" class="btn btn-primary">💻 Start Free Browser Labs</a>
    <a href="linux-commands/basic-linux-commands/" class="btn btn-secondary">📖 Read Tutorials</a>
    <a href="quiz/" class="btn btn-secondary">📝 Practice Quizzes</a>
  </div>
</div>

<h2 class="section-title">🗺️ Recommended Learning Path</h2>
<p class="text-center" style="max-width: 700px; margin: 0 auto 3rem auto; color: var(--text-light); line-height: 1.6;">
  Follow our expert-curated DevOps roadmaps to build solid engineering foundations. Kick off your journey with our interactive, browser-based Linux and Docker sandboxes!
</p>

<div class="path-container" style="max-width: 800px; margin: 0 auto 4rem auto;">
  <div class="step-item">
    <div class="step-num">1</div>
    <div class="step-info">
      <h4 style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 6px;">
        Master Linux Fundamentals
        <span style="padding: 2px 8px; background: rgba(15, 121, 14, 0.1); border: 1px solid rgba(15, 121, 14, 0.2); border-radius: 4px; font-size: 0.7rem; font-weight: 700; color: #0f790e; text-transform: uppercase; letter-spacing: 0.05em; display: inline-flex; align-items: center; gap: 4px;">💻 Live Labs Available</span>
      </h4>
      <p>The operating system of the cloud. Learn navigation, file permissions, users, and service management.</p>
      <a href="linux-commands/basic-linux-commands/" class="step-link">Start Linux Track →</a>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">2</div>
    <div class="step-info">
      <h4>Version Control with Git</h4>
      <p>Essential for every modern engineer. Learn branching strategies, merging, and remote repository integration.</p>
      <a href="git/" class="step-link">Learn Git →</a>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">3</div>
    <div class="step-info">
      <h4>Shell Scripting</h4>
      <p>Automate repetitive administrative tasks and build powerful command-line tools.</p>
      <a href="shellscript/" class="step-link">Start Scripting →</a>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">4</div>
    <div class="step-info">
      <h4 style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 6px;">
        Docker & Containers
        <span style="padding: 2px 8px; background: rgba(15, 121, 14, 0.1); border: 1px solid rgba(15, 121, 14, 0.2); border-radius: 4px; font-size: 0.7rem; font-weight: 700; color: #0f790e; text-transform: uppercase; letter-spacing: 0.05em; display: inline-flex; align-items: center; gap: 4px;">🐳 Live Labs Available</span>
      </h4>
      <p>Package applications for consistency. Learn multi-stage builds, volumes, networking, and compose stacks.</p>
      <a href="docker/" class="step-link">Explore Docker →</a>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">5</div>
    <div class="step-info">
      <h4>Kubernetes Orchestration</h4>
      <p>Manage containerized workloads at scale. Learn Pods, Deployments, Services, and Ingress routing.</p>
      <a href="kubernetes/" class="step-link">Master Kubernetes →</a>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">6</div>
    <div class="step-info">
      <h4>AWS Cloud Mastery</h4>
      <p>Validate your expertise with role-based quizzes from Cloud Engineer to Security Specialist.</p>
      <a href="quiz/aws/" class="step-link">Start AWS Track →</a>
    </div>
  </div>
</div>

<h2 class="section-title">Why DevopsPilot Interactive Labs?</h2>
<div class="grid-3" style="margin-bottom: 4rem;">
  <div class="card">
    <span class="card-icon">💻</span>
    <h3>Live Browser Sandboxes</h3>
    <p>Launch fully-isolated, live Linux and Docker environments directly in your browser. Practice commands, deploy containers, and write configurations in real time with secure tmux shells.</p>
  </div>
  <div class="card">
    <span class="card-icon">🛠️</span>
    <h3>Troubleshooting & Challenges</h3>
    <p>Debug pre-broken servers, lockdown active firewall attacks, and tackle custom scenarios designed by production engineers under pressure.</p>
  </div>
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>Smart Validation</h3>
    <p>Get instant, programmatic feedback on your tasks. Verify your configurations and resolve issues with automated scripts directly inside the interface.</p>
  </div>
</div>

<h2 class="section-title">Featured DevOps & Cloud Guides</h2>
<p class="text-center" style="max-width: 700px; margin: 0 auto 3rem auto; color: var(--text-light); line-height: 1.6;">
  Explore our in-depth, step-by-step tutorials designed for real-world DevOps and Cloud use cases. 
  These practical guides help you master complex deployments and pipelines with ease.
</p>

<div class="grid-3" style="margin-bottom: 4rem;">
  <a href="cloud/gcp/projects/apigee-psc-cloudrun/" class="card" style="text-decoration: none;">
    <span class="card-icon">☁️</span>
    <h3>Apigee X with PSC</h3>
    <p>Securely connect Apigee X to Cloud Run using Private Service Connect in Google Cloud.</p>
  </a>
  <a href="jenkins/tutorials/write-jenkinsfile/" class="card" style="text-decoration: none;">
    <span class="card-icon">📜</span>
    <h3>Master Jenkinsfile</h3>
    <p>A comprehensive guide to writing Declarative Pipelines for robust CI/CD automation.</p>
  </a>
  <a href="cloud/aws/tutorials/deploy-fastapi-lambda/" class="card" style="text-decoration: none;">
    <span class="card-icon">⚡</span>
    <h3>FastAPI on Lambda</h3>
    <p>Deploy a high-performance FastAPI application to AWS Lambda using Docker containers.</p>
  </a>
</div>

<h2 class="section-title">📚 Explore Topics</h2>

<div class="topic-grid">
  <a href="linux-commands/basic-linux-commands/" class="topic-card">
    <span class="topic-icon">🐧</span>
    <span class="topic-name">Linux</span>
  </a>
  <a href="git/" class="topic-card">
    <span class="topic-icon">🐙</span>
    <span class="topic-name">Git</span>
  </a>
  <a href="docker/" class="topic-card">
    <span class="topic-icon">🐳</span>
    <span class="topic-name">Docker</span>
  </a>
  <a href="kubernetes/" class="topic-card">
    <span class="topic-icon">☸️</span>
    <span class="topic-name">Kubernetes</span>
  </a>
  <a href="jenkins/" class="topic-card">
    <span class="topic-icon">⚙️</span>
    <span class="topic-name">Jenkins</span>
  </a>
  <a href="cloud/" class="topic-card">
    <span class="topic-icon">☁️</span>
    <span class="topic-name">Cloud</span>
  </a>
  <a href="terraform/" class="topic-card">
    <span class="topic-icon">🏗️</span>
    <span class="topic-name">Terraform</span>
  </a>
  <a href="quiz/" class="topic-card">
    <span class="topic-icon">📝</span>
    <span class="topic-name">Quizzes</span>
  </a>
</div>

<div class="newsletter">
  <h3>🚀 Join the DevOps Revolution</h3>
  <p>DevOpsPilot is constantly adding new content. Stay tuned for updates!</p>
  <div style="margin-top: 1rem;">
    <iframe src="https://devopspilot.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>
  </div>
</div>
