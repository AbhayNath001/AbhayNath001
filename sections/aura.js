// Ultra Instinct Aura Effect
const canvas = document.getElementById('aura-canvas');
const ctx = canvas.getContext('2d');

let width, height;
let particles = [];
const particleCount = 60; // Adjust density

function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
}

window.addEventListener('resize', resize);
resize();

class Particle {
    constructor() {
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.vx = (Math.random() - 0.5) * 0.5; // Slow horizontal movement
        this.vy = (Math.random() - 0.5) * 0.5; // Slow vertical movement
        this.size = Math.random() * 2 + 1; // Varied size
        this.alpha = Math.random() * 0.5 + 0.1; // Varied opacity
        // Ultra Instinct Colors: Silver/White with hints of Blue/Purple
        const colors = ['255, 255, 255', '192, 192, 192', '173, 216, 230', '255, 255, 255'];
        this.color = colors[Math.floor(Math.random() * colors.length)];
        this.pulseSpeed = Math.random() * 0.02 + 0.005;
        this.pulseDir = 1;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;

        // Wrap around screen
        if (this.x < 0) this.x = width;
        if (this.x > width) this.x = 0;
        if (this.y < 0) this.y = height;
        if (this.y > height) this.y = 0;

        // Pulse opacity
        this.alpha += this.pulseSpeed * this.pulseDir;
        if (this.alpha > 0.6 || this.alpha < 0.1) {
            this.pulseDir *= -1;
        }
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${this.color}, ${this.alpha})`;
        ctx.shadowBlur = 10;
        ctx.shadowColor = `rgba(${this.color}, 0.8)`; // Glow effect
        ctx.fill();
    }
}

function init() {
    particles = [];
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
}

function animate() {
    ctx.clearRect(0, 0, width, height);

    // Optional: Draw a subtle connecting line between close particles for a "constellation" feel
    // or just keep it as independent flowing energy. Let's do independent for "Aura" feel.

    particles.forEach(p => {
        p.update();
        p.draw();
    });

    requestAnimationFrame(animate);
}

init();
animate();
