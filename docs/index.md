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
    --accent-color: #10b981;
    --text-dark: #1f2937;
    --text-light: #6b7280;
  }
  
  /* Hero Section */
  .hero {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    padding: 4rem 2rem;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 3rem;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  }
  .hero h1 {
    font-size: 3rem !important;
    font-weight: 800;
    margin: 0 0 1rem 0;
    color: white !important;
    line-height: 1.2;
  }
  .hero p {
    font-size: 1.25rem;
    max-width: 700px;
    margin: 0 auto 2.5rem auto;
    opacity: 0.95;
    line-height: 1.6;
    color: rgba(255,255,255,0.9);
  }
  .hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }
  .btn {
    padding: 0.8rem 2rem;
    border-radius: 50px;
    font-weight: 700;
    text-decoration: none !important;
    transition: all 0.3s ease;
    display: inline-block;
  }
  .btn-primary {
    background: white;
    color: var(--primary-color) !important;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  }
  .btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    color: var(--primary-color) !important;
  }
  .btn-secondary {
    background: rgba(255,255,255,0.2);
    color: white !important;
    border: 2px solid rgba(255,255,255,0.4);
    backdrop-filter: blur(5px);
  }
  .btn-secondary:hover {
    background: rgba(255,255,255,0.3);
    border-color: white;
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
  <h1>Your Co-Pilot for DevOps Mastery</h1>
  <p>Stop watching endless videos. Start learning by doing with our step-by-step guides, real-world examples, and interactive quizzes.</p>
  <div class="hero-buttons">
    <a href="linux-commands/basic-linux-commands/" class="btn btn-primary">🚀 Start Learning Linux</a>
    <a href="quiz/" class="btn btn-secondary">📝 Practice Quizzes</a>
  </div>
</div>

<h2 class="section-title">Why DevopsPilot?</h2>

<div class="grid-3">
  <div class="card">
    <span class="card-icon">🛠️</span>
    <h3>Practical Approach</h3>
    <p>We believe in "Learning by Doing". Every tutorial comes with commands you can run and real scenarios to solve, not just theory.</p>
  </div>
  <div class="card">
    <span class="card-icon">🎯</span>
    <h3>Interview Focused</h3>
    <p>Curated content that targets the most common questions in DevOps interviews. We prepare you for the job, not just the certification.</p>
  </div>
  <div class="card">
    <span class="card-icon">⚡</span>
    <h3>Beginner Friendly</h3>
    <p>Complex topics broken down into simple, bite-sized lessons. No jargon overload—just clear, actionable engineering advice.</p>
  </div>
</div>

<h2 class="section-title">🗺️ Recommended Learning Path</h2>

<div class="path-container">
  <div class="step-item">
    <div class="step-num">1</div>
    <div class="step-info">
      <h4>Master Linux Fundamentals</h4>
      <p>The operating system of the cloud. Learn permissions, shell, and file systems.</p>
      <a href="linux-commands/basic-linux-commands/" class="step-link">Start Linux Track →</a>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">2</div>
    <div class="step-info">
      <h4>Version Control with Git</h4>
      <p>Essential for every engineer. Learn branching, merging, and collaboration.</p>
      <a href="git/" class="step-link">Learn Git →</a>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">3</div>
    <div class="step-info">
      <h4>Shell Scripting</h4>
      <p>Automate repetitive tasks and build powerful tools.</p>
      <a href="shellscript/part-1/" class="step-link">Start Scripting →</a>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">4</div>
    <div class="step-info">
      <h4>Docker & Containers</h4>
      <p>Package applications for consistency across environments.</p>
      <a href="docker/" class="step-link">Explore Docker →</a>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">5</div>
    <div class="step-info">
      <h4>Kubernetes Orchestration</h4>
      <p>Manage containerized applications at scale.</p>
      <a href="kubernetes/" class="step-link">Master Kubernetes →</a>
    </div>
  </div>
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
  <a href="cloud/on-premise-cloud/" class="topic-card">
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
  <p>We are constantly adding new content. Stay tuned for updates!</p>
  <div style="margin-top: 1rem;">
    <iframe src="https://devopspilot.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>
  </div>
</div>
