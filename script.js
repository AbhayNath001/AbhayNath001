// Initialize logic AFTER content is loaded
// Since we are using synchronous JS scripts at the bottom of the body, 
// or async scripts that we wait for, we can just run this logic.
// However, to be safe, we wrap it in a short timeout or check if elements exist.

window.addEventListener('load', () => {

    // Custom Cursor Logic
    const cursorDot = document.querySelector('.cursor-dot');
    const cursorOutline = document.querySelector('.cursor-outline');

    window.addEventListener('mousemove', (e) => {
        const posX = e.clientX;
        const posY = e.clientY;

        // Dot follows instantly
        cursorDot.style.left = `${posX}px`;
        cursorDot.style.top = `${posY}px`;

        // Outline follows with slight delay (animation is handled by CSS transition usually, 
        // but explicit animate() is smoother for trailing effect)
        cursorOutline.animate({
            left: `${posX}px`,
            top: `${posY}px`
        }, { duration: 500, fill: "forwards" });
    });

    // Ripple Effect on Click
    window.addEventListener('click', (e) => {
        const ripple = document.createElement('div');
        ripple.classList.add('cursor-ripple');
        ripple.style.left = `${e.clientX}px`;
        ripple.style.top = `${e.clientY}px`;
        document.body.appendChild(ripple);

        // Remove ripple after animation
        ripple.addEventListener('animationend', () => {
            ripple.remove();
        });
    });

    // Hamburger Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            // Animate hamburger lines
            const bars = document.querySelectorAll('.bar');
            bars.forEach(bar => bar.classList.toggle('active-bar'));
        });

        // Close mobile menu when a link is clicked
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
            });
        });
    }

    // Generic Tab Filtering Logic (Works for Projects, Experience, etc.)
    const tabContainers = document.querySelectorAll('.tabs');

    tabContainers.forEach(container => {
        const tabBtns = container.querySelectorAll('.tab-btn');
        // Find the grid/content container relative to the tabs. 
        // Assuming the common structure: container -> [tabs, grid]
        // or finding the next sibling that contains cards.
        // Let's use a more robust approach: find the parent section/container and search within it.
        const sectionContainer = container.closest('.container');

        if (sectionContainer) {
            tabBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // ... existing click logic ...
                    // (We will just keep the existing logic, but I am replacing the block to append the init logic after)
                    // Remove active class from all buttons IN THIS CONTAINER
                    tabBtns.forEach(b => b.classList.remove('active'));
                    // Add active class to clicked button
                    btn.classList.add('active');

                    const category = btn.getAttribute('data-tab');

                    // Find all filterable items in this section
                    // We look for items with 'data-category' attribute
                    const filterItems = sectionContainer.querySelectorAll('[data-category]');

                    filterItems.forEach(card => {
                        const cardCategory = card.getAttribute('data-category');

                        if (category === 'all' || cardCategory === category) {
                            card.style.display = 'flex';
                            setTimeout(() => {
                                card.style.opacity = '1';
                                card.style.transform = 'translateY(0)';
                            }, 100);
                        } else {
                            card.style.opacity = '0';
                            card.style.transform = 'translateY(20px)';
                            setTimeout(() => {
                                card.style.display = 'none';
                            }, 300);
                        }
                    });
                });
            });

            // Trigger the active tab on load to ensure state consistency
            const activeBtn = container.querySelector('.tab-btn.active');
            if (activeBtn && activeBtn.getAttribute('data-tab') !== 'all') {
                // We don't want to trigger the animation on load, just ensure display property is correct if inline styles failed
                // But inline styles are fastest. 
                // actually, let's just leave it, but making sure the 'all' logic doesn't override it if we had 'all' active by default.
                // The user wants 'Work' active. I set 'Work' as active in HTML.
            }
        }
    });

    // Scroll Animations (Intersection Observer)
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    const sections = document.querySelectorAll('.section, .hero');
    sections.forEach(section => {
        section.classList.add('fade-in');
        observer.observe(section);
    });

    // Add explicit fade-in class to elements we want to animate individually
    const animatedElements = document.querySelectorAll('.skill-card, .pub-item, .project-card, .timeline-item');
    animatedElements.forEach((el, index) => {
        el.classList.add('fade-in');
        el.style.transitionDelay = `${(index % 5) * 50}ms`; // Stagger effect
        observer.observe(el);
    });

    // Scroll Spy for Navbar
    const navLinksItems = document.querySelectorAll('.nav-links a');

    // Create a specific observer for scroll spy with different options
    // Using a simpler threshold and margin that works better for varying section heights
    const scrollSpyOptions = {
        threshold: [0.1, 0.3, 0.5, 0.7],
        rootMargin: "-20% 0px -50% 0px"
    };

    const scrollSpy = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // Check if the entry is significantly visible
            if (entry.isIntersecting && entry.intersectionRatio > 0.1) {
                // Remove active class from all links
                navLinksItems.forEach(link => link.classList.remove('active'));

                // Add active class to corresponding link
                const id = entry.target.getAttribute('id');
                const activeLink = document.querySelector(`.nav-links a[href="#${id}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    }, scrollSpyOptions);

    // Reuse the 'sections' variable defined earlier
    sections.forEach(section => {
        scrollSpy.observe(section);
    });

});
