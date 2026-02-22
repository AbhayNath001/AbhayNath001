document.getElementById('experience').innerHTML = `
    <div class="container">
        <h2 class="section-title">Experiences</h2>

        <div class="tabs">
            <!-- Removed 'All' tab as requested -->
            <button class="tab-btn active" data-tab="work">Works</button>
            <button class="tab-btn" data-tab="organization">Organisations / Contributions</button>
            <button class="tab-btn" data-tab="international">International Affairs</button>
        </div>

        <div class="timeline" style="margin-top: 2rem;">
            
            <!-- Work (formerly Internships) -->
            <div class="timeline-item" data-category="work">
                <div class="timeline-logo">
                    <!-- Placeholder for company logo -->
                    <img src="company_logo/ISI_Kolkata.jpg" alt="Indian Statistical Institute - Kolkata" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <div class="timeline-date">Jan 2025 - Mar 2025 · 3 months</div>
                    <div class="timeline-content">
                        <h4>Research Internship (Machine Learning)</h4>
                        <span class="company">Indian Statistical Institute (ISI), Kolkata, West Bengal, India</span>
                        <p>Project Title: Fusion-Based Deep Learning Model for Cross-Modality Calcium Detection in Echocardiography.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item" data-category="work">
                <div class="timeline-logo">
                    <!-- Placeholder for company logo -->
                    <img src="company_logo/WEBXELA.jpg" alt="WEBXELA" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <div class="timeline-date">Jun 2024 - Mar 2025 · 10 months</div>
                    <div class="timeline-content">
                        <h4>Tech Lead in AI/ML Department</h4>
                        <span class="company">WEBXELA, Ahmedabad, Gujarat, India</span>
                        <p>Led 85+ interns in AI and Machine Learning, overseeing real-time projects and delivering comprehensive training sessions from basic to advanced levels.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item" data-category="work">
                <div class="timeline-logo">
                    <!-- Placeholder for company logo -->
                    <img src="company_logo/Celebal Technologies.jpg" alt="Celebal Technologies" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <div class="timeline-date">Jun 2024 - Jul 2024 · 2 months</div>
                    <div class="timeline-content">
                        <h4>Data Science Internship</h4>
                        <span class="company">Celebal Technologies, Kolkata, West Bengal, India</span>
                        <p>Completed a 2-month internship at Celebal Technologies, implementing Latent Dirichlet Allocation (LDA) and K-Means for topic modeling and document clustering.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item" data-category="work">
                <div class="timeline-logo">
                    <!-- Placeholder for company logo -->
                    <img src="company_logo/CodeAlpha.jpg" alt="CodeAlpha" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <div class="timeline-date">May 2024 · 1 month</div>
                    <div class="timeline-content">
                        <h4>Machine Learning Internship</h4>
                        <span class="company">CodeAlpha, Lucknow, Uttar Pradesh, India</span>
                        <p>Completed a summer internship at CodeAlpha in Machine Learning, where I was recognized as the best intern for my work on projects like Emotion Recognition from Speech, Handwritten Character Recognition without deep learning modules, and Disease Prediction from Medical Data.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item" data-category="work">
                <div class="timeline-logo">
                    <!-- Placeholder for company logo -->
                    <img src="company_logo/CLUMOSS.jpg" alt="CLUMOSS" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <div class="timeline-date">Aug 2023 - Sep 2023 · 2 months</div>
                    <div class="timeline-content">
                        <h4>Head of AI/ML Department</h4>
                        <span class="company">CLUMOSS, Vadodara, Gujarat, India</span>
                        <p>CLUMOSS, a parent IT company, providing free training to college students worldwide, preparing them for the future. As the Head of AI & ML, I'm proud to contribute to this global initiative, offering valuable experiences to students and delivering diverse services across domains through technology.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item" data-category="work">
                <div class="timeline-logo">
                    <!-- Placeholder for company logo -->
                    <img src="company_logo/CodSoft.jpg" alt="CodSoft" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <div class="timeline-date">Aug 2023 · 1 month</div>
                    <div class="timeline-content">
                        <h4>Data Science Internship</h4>
                        <span class="company">CodSoft, Kolkata, West Bengal, India</span>
                        <p>I completed a summer internship at CodSoft in Data Science, where I implemented projects such as Titanic Survival Prediction, IRIS Flower Classification, and Sales Prediction using Python.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item" data-category="work">
                <div class="timeline-logo">
                    <!-- Placeholder for company logo -->
                    <img src="company_logo/CodeClause.jpg" alt="CodeClause" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <div class="timeline-date">Jul 2023 · 1 month</div>
                    <div class="timeline-content">
                        <h4>Data Science Internship</h4>
                        <span class="company">CodeClause, Pune, Maharashtra, India</span>
                        <p>I completed a summer internship at CodeClause in Data Science, where I implemented projects such as Breast Cancer Classification, Credit Card Fraud Detection, Movie Recommendation system and Sales Analysis.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item" data-category="work">
                <div class="timeline-logo">
                    <!-- Placeholder for company logo -->
                    <img src="company_logo/Oasis Infobyte.jpg" alt="Oasis Infobyte" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <div class="timeline-date">May 2023 · 1 month</div>
                    <div class="timeline-content">
                        <h4>Web Development and Designing Internship</h4>
                        <span class="company">Oasis Infobyte, Pune, Maharashtra, India</span>
                        <p>I completed a summer internship at Oasis Infobyte in Web Development and Design, where I implemented projects such as Landing Page, Personalize Portfolio and Temperature Converter.</p>
                    </div>
                </div>
            </div>

            <!-- Organisations -->
            <div class="timeline-item" data-category="organization" style="display:none;">
                <div class="timeline-logo">
                     <img src="company_logo/Club Gamma.jpg" alt="Club Gamma" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <!-- Added date placeholder here too for consistency if needed, or keep logic flexible -->
                    <div class="timeline-date">Oct-2023 - Sep-2024 · 1 Year</div>
                    <div class="timeline-content">
                        <h4>AI/ML Core Team Member</h4>
                        <span class="company">Club Gamma @CHARUSAT, Anand, Gujarat, India</span>
                        <p>Excited to join Club Gamma's AI/ML Team! We're on a mission to explore the cutting edge of Artificial Intelligence and Machine Learning, pushing the boundaries of technology together.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item" data-category="organization" style="display:none;">
                <div class="timeline-logo">
                     <img src="company_logo/GirlScript Summer of Code.jpg" alt="GirlScript Summer of Code" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <!-- Added date placeholder here too for consistency if needed, or keep logic flexible -->
                    <div class="timeline-date">May-2024 - Jul-2024 · 3 Months</div>
                    <div class="timeline-content">
                        <h4>GSSOC'24 Contributor</h4>
                        <span class="company">GirlScript Summer of Code, New Delhi, Delhi, India</span>
                        <p>Active contributor in Girl Script Summer of Code 2024, specializing in technical implementations, code reviews, and collaborative problem-solving.</p>
                    </div>
                </div>
            </div>

            <!-- International Affairs -->
            <div class="timeline-item" data-category="international" style="display:none;">
                <div class="timeline-logo">
                     <img src="company_logo/logo_placeholder.png" alt="Event Logo" onerror="this.style.display='none'; this.parentElement.style.background='#333'">
                </div>
                <div class="timeline-content-wrapper">
                    <div class="timeline-date">MM-YYYY - MM-YYYY</div>
                    <div class="timeline-content">
                        <h4>Speaker / Delegate</h4>
                        <span class="company">Event Name</span>
                        <p>Description of international engagement.</p>
                    </div>
                </div>
            </div>

        </div>

    </div>
`;
