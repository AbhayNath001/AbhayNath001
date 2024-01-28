/*------------------------------------------toggle icon navbar-------------------------------------------------*/
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');
menuIcon.onclick = () => {
	menuIcon.classList.toggle('bx-x');
	navbar.classList.toggle('active');
};

// Global variable to store the background color state
var isBackgroundColorWhite = false;

function changeBackgroundColor() {
    var body = document.body;
    var button = document.querySelector('.navbar i');
	var nav = document.querySelector('.header');
	var header_span = document.querySelector('.header span');
	var publications_box = document.querySelectorAll('.publications-container .publications-box');
	var inputFields = document.querySelectorAll('.input-box input, textarea');
	var headings = document.querySelectorAll('.mywork-layer h4');
	var paragraphs = document.querySelectorAll('.mywork-layer p');
	var experience = document.querySelectorAll('.experience h4, .certification h4');
	var experience_link = document.querySelectorAll('.experience .exp a h3, .certification .cert a h3');
	var exp_h4 = document.querySelectorAll('.exp h4 span');
	var follow = document.querySelector('.follow p');

    if (isBackgroundColorWhite) {
        // Change from white to var(--bg-color)
        body.style.backgroundColor = '#1f242d';
		nav.style.backgroundColor = '#1f242d';
        body.style.color = '#fff';
		header_span.style.color = '#0ef';
		publications_box.forEach(box => {
            box.style.backgroundColor = '#1f242d';
        });
		inputFields.forEach(field => {
			field.style.backgroundColor = '#1f242d';
			field.style.color = 'white';
		});
		headings.forEach(heading => {
			heading.style.color = 'white';
		});
		paragraphs.forEach(paragraph => {
			paragraph.style.color = 'white';
		});
		experience.forEach(experience => {
			experience.style.color = 'white';
		});
		experience_link.forEach(experience_link => {
			experience_link.style.color = 'white';
		});
		exp_h4.forEach(exp_h4 => {
			exp_h4.style.color = 'aqua';
		});
        button.style.color = 'var(--text-color)';
        button.style.backgroundColor = 'var(--bg-color)';
        follow.style.color = 'aqua';
        document.documentElement.style.setProperty('--second-bg-color', '#323946');
        document.documentElement.style.setProperty('--text-color', '#fff');
        document.documentElement.style.setProperty('--main-color', '#0ef');
        isBackgroundColorWhite = false;
    } else {
        // Change from var(--bg-color) to white
        body.style.backgroundColor = '#edebeb';
		nav.style.backgroundColor = '#edebeb';
        body.style.color = 'black';
		header_span.style.color = '#f24005';
		publications_box.forEach(box => {
            box.style.backgroundColor = '#ccc9c8';
        });
		inputFields.forEach(field => {
			field.style.backgroundColor = '#ccc9c8';
			field.style.color = '#1f242d';
		});
		headings.forEach(heading => {
			heading.style.color = 'white';
		});
		paragraphs.forEach(paragraph => {
			paragraph.style.color = 'white';
		});
		experience.forEach(experience => {
			experience.style.color = 'black';
		});
		experience_link.forEach(experience_link => {
			experience_link.style.color = 'black';
		});
		exp_h4.forEach(exp_h4 => {
			exp_h4.style.color = '#f24005';
		});
        button.style.color = 'black';
        button.style.backgroundColor = '#c9c6c5';
		follow.style.color = '#f24005';
		follow.style.filter = 'drop-shadow(0 0 0.1rem #f24005)';
        document.documentElement.style.setProperty('--second-bg-color', '#e3e3e3');
        document.documentElement.style.setProperty('--text-color', 'black');
        document.documentElement.style.setProperty('--main-color', '#f24005');
        isBackgroundColorWhite = true;
    }
}


/*------------------------------------------scroll section active link-------------------------------------------------*/

let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');
window.onscroll = () => {
	sections.forEach(sec => {
		let top = window.scrollY;
		let offset = sec.offsetTop - 150;
		let height = sec.offsetHeight;
		let id = sec.getAttribute('id');
		if(top >= offset && top <offset + height){
			navLinks.forEach(links => {
				links.classList.remove('active');
				document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
			});
		};
	});

/*------------------------------------------sticky navbar-------------------------------------------------*/

	let header = document.querySelector('header');
	header.classList.toggle('sticky', window.scrollY > 100);
	
/*------------------------remove toggle icon and navbar when click navbar link (scroll)-------------------*/
	menuIcon.classList.remove('bx-x');
	navbar.classList.remove('active');
	};
/*-------------------------------------------scroll reveal------------------------------------------------*/
// ScrollReveal({ 
	//reset: true,
	// distance: '80px',
	// duration: 1500,
	// delay: 200
	// });
// ScrollReveal().reveal('.home-content, .heading, .checkbox-list, .skills', { origin: 'top' });
// ScrollReveal().reveal('.home-img, .services-container, .mywork-box, .show_more', { origin: 'bottom' });
// ScrollReveal().reveal('.home-content h1, .about-img', { origin: 'left' });
// ScrollReveal().reveal('.home-content p, .about-content', { origin: 'right' });