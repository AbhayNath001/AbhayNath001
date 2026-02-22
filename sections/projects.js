
const projectsData = [
    {
        category: "dissertation",
        html: `
            <div class="project-card" data-category="dissertation">
                <div class="project-content">
                    <span class="project-tag">B.Tech Thesis</span>
                    <h3 class="project-title">Advancing Oncology Diagnostics and Therapeutics with Deep Learning and Generative AI</h3>
                    <p class="project-desc">A deep dive into advanced AI methodologies.</p>
                    <div class="contributors">
                        <span>Principal Investigator:</span>
                        <div class="contributor-avatars">
                            <div class="avatar-placeholder contributor-chintal_raval" title="Dr. Chintal Raval"></div>
                        </div>
                    </div>
                </div>
            </div>`
    },
    {
        category: "research",
        html: `
            <div class="project-card" data-category="research">
                <div class="project-content">
                    <span class="project-tag">Research</span>
                    <h3 class="project-title">Protein-Ligand Binding Affinity using AI-ML and Enhanced Docking Techniques</h3>
                    <p class="project-desc">Innovative study on [Topic] leading to publication/findings.</p>
                        <div class="contributors">
                        <span>Contributors:</span>
                        <div class="contributor-avatars">
                            <div class="avatar-placeholder contributor-drashti" title="Drashti Shah"></div>
                            <div class="avatar-placeholder contributor-ashish" title="Dr. Ashish Patel"></div>
                            <div class="avatar-placeholder contributor-arya" title="Arya Patel"></div>
                        </div>
                    </div>
                </div>
            </div>`
    },
    {
        category: "research",
        html: `
            <div class="project-card" data-category="research">
                <div class="project-content">
                    <span class="project-tag">Research</span>
                    <h3 class="project-title">RUDRA - India's Own Artificial Intelligent Based Voice Assistant</h3>
                    <p class="project-desc">Innovative study on [Topic] leading to publication/findings.</p>
                        <div class="contributors">
                        <span>Contributors:</span>
                        <div class="contributor-avatars">
                            <div class="avatar-placeholder contributor-####" title="####"></div>
                        </div>
                    </div>
                </div>
            </div>`
    },
    {
        category: "research",
        html: `
            <div class="project-card" data-category="research">
                <div class="project-content">
                    <span class="project-tag">Research</span>
                    <h3 class="project-title">Leveraging Artificial Intelligence for Anticancer Drug Discovery: Identifying Compounds with Range Threshold Adjustments and Validating via Biological Studies</h3>
                    <p class="project-desc">Innovative study on [Topic] leading to publication/findings.</p>
                        <div class="contributors">
                        <span>Contributors:</span>
                        <div class="contributor-avatars">
                            <div class="avatar-placeholder contributor-####" title="####"></div>
                        </div>
                    </div>
                </div>
            </div>`
    },
    {
        category: "research",
        html: `
            <div class="project-card" data-category="research">
                <div class="project-content">
                    <span class="project-tag">Research</span>
                    <h3 class="project-title">MedYOLO: An Enhanced Object Detection Model for Hospital Environments with Improved Precision and Real-Time Performance</h3>
                    <p class="project-desc">Innovative study on [Topic] leading to publication/findings.</p>
                        <div class="contributors">
                        <span>Contributors:</span>
                        <div class="contributor-avatars">
                            <div class="avatar-placeholder contributor-####" title="####"></div>
                        </div>
                    </div>
                </div>
            </div>`
    },
    {
        category: "research",
        html: `
            <div class="project-card" data-category="research">
                <div class="project-content">
                    <span class="project-tag">Research</span>
                    <h3 class="project-title">Enhanced YOLOv8 for Road Object Detection with Advanced AI-based Real-Time Precision Algorithm</h3>
                    <p class="project-desc">Innovative study on [Topic] leading to publication/findings.</p>
                        <div class="contributors">
                        <span>Contributors:</span>
                        <div class="contributor-avatars">
                            <div class="avatar-placeholder contributor-####" title="####"></div>
                        </div>
                    </div>
                </div>
            </div>`
    },
    {
        category: "research",
        html: `
            <div class="project-card" data-category="research">
                <div class="project-content">
                    <span class="project-tag">Research</span>
                    <h3 class="project-title">Lime Diseases Classification using Machine Learning and Spectrometry</h3>
                    <p class="project-desc">Innovative study on [Topic] leading to publication/findings.</p>
                        <div class="contributors">
                        <span>Contributors:</span>
                        <div class="contributor-avatars">
                            <div class="avatar-placeholder contributor-pratishtha" title="Pratishtha Makhijani"></div>
                        </div>
                    </div>
                </div>
            </div>`
    },
    {
        category: "research",
        html: `
            <div class="project-card" data-category="research">
                <div class="project-content">
                    <span class="project-tag">Research</span>
                    <h3 class="project-title">Cancer Histology Detection and Masking using Deep Learning</h3>
                    <p class="project-desc">Innovative study on [Topic] leading to publication/findings.</p>
                        <div class="contributors">
                        <span>Contributors:</span>
                        <div class="contributor-avatars">
                            <div class="avatar-placeholder contributor-alkesh" title="Dr. Alkesh Patel"></div>
                        </div>
                    </div>
                </div>
            </div>`
    },
    {
        category: "poc",
        html: `
            <div class="project-card" data-category="poc">
                <div class="project-content">
                    <span class="project-tag">Proof of Concept</span>
                    <h3 class="project-title">Medicinal Plant Identification using Machine Learning (Android Application)</h3>
                    <p class="project-desc">Innovative study on [Topic] leading to publication/findings.</p>
                        <div class="contributors">
                        <span>Contributors:</span>
                        <div class="contributor-avatars">
                            <div class="avatar-placeholder contributor-rishi" title="Rishi Vachhani"></div>
                            <div class="avatar-placeholder contributor-urvesh" title="Urvesh Bhesdadiya"></div>
                            <div class="avatar-placeholder contributor-goldi" title="Goldi Ladani"></div>
                            <div class="avatar-placeholder contributor-mann" title="Mann Mendapara"></div>
                        </div>
                    </div>
                </div>
            </div>`
    },
    {
        category: "poc",
        html: `
            <div class="project-card" data-category="poc">
                <div class="project-content">
                    <span class="project-tag">Proof of Concept</span>
                    <h3 class="project-title">AI Powered Platformer (Super Mario) Game with Dynamic Level Generation and AI-Powered Adaptive Difficulty</h3>
                    <p class="project-desc">Innovative study on [Topic] leading to publication/findings.</p>
                        <div class="contributors">
                        <span>Contributors:</span>
                        <div class="contributor-avatars">
                            <div class="avatar-placeholder contributor-sneha" title="Sneha Das"></div>
                        </div>
                    </div>
                </div>
            </div>`
    }
];

// Generate HTML for Preview (First 4)
// Note: transforming class to 'project-card-preview' to avoid conflict with tab filtering in script.js
const previewHTML = projectsData.slice(0, 4).map(p => {
    return p.html.replace('class="project-card"', 'class="project-card-preview" style="display:flex; flex-direction:column; background:var(--card-bg); border-radius:15px; overflow:hidden; border:1px solid rgba(255,255,255,0.1); padding:2rem; position:relative;"');
}).join('');

// Generate HTML for Full View (All)
const fullHTML = projectsData.map(p => p.html).join('');

document.getElementById('projects').innerHTML = `
    <!-- MAIN VIEW (PREVIEW) -->
    <div class="container" id="projects-preview-container">
        <h2 class="section-title">Projects</h2>
        
        <div class="projects-grid">
            ${previewHTML}
        </div>

        <div style="text-align: center; margin-top: 3rem;">
            <button id="see-all-btn" class="btn btn-secondary" style="font-size: 1.1rem; padding: 1rem 3rem;">See All Projects</button>
        </div>
    </div>

    <!-- FULL VIEW (HIDDEN) -->
    <div class="container" id="projects-full-container" style="display: none; padding-top: 2rem;">
        <div style="margin-bottom: 2rem;">
            <button id="back-to-preview-btn" class="btn btn-secondary">
                <i class="fas fa-arrow-left"></i> Back to Main
            </button>
        </div>

        <h2 class="section-title">All Projects</h2>

        <div class="tabs">
            <button class="tab-btn active" data-tab="all">All</button>
            <button class="tab-btn" data-tab="research">Research</button>
            <button class="tab-btn" data-tab="poc">Proof of Concept</button>
            <button class="tab-btn" data-tab="dissertation">Thesis / Dissertation</button>
        </div>

        <div class="projects-grid">
            ${fullHTML}
        </div>
    </div>
`;

// Logic for switching views
document.getElementById('see-all-btn').addEventListener('click', () => {
    document.getElementById('projects-preview-container').style.display = 'none';
    document.getElementById('projects-full-container').style.display = 'block';
    // Scroll to top of section for better UX
    document.getElementById('projects').scrollIntoView({ behavior: 'smooth' });
});

document.getElementById('back-to-preview-btn').addEventListener('click', () => {
    document.getElementById('projects-full-container').style.display = 'none';
    document.getElementById('projects-preview-container').style.display = 'block';
    document.getElementById('projects').scrollIntoView({ behavior: 'smooth' });
});
