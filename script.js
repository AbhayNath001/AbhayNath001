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
	var services_box = document.querySelectorAll('.services-container .services-box');
	var inputFields = document.querySelectorAll('.input-box input, textarea');
	var headings = document.querySelectorAll('.mywork-layer h4');
	var paragraphs = document.querySelectorAll('.mywork-layer p');

    if (isBackgroundColorWhite) {
        // Change from white to var(--bg-color)
        body.style.backgroundColor = 'var(--bg-color)';
		nav.style.backgroundColor = 'var(--bg-color)';
        body.style.color = 'var(--text-color)';
		header_span.style.color = '#0ef';
		services_box.forEach(box => {
            box.style.backgroundColor = '#1f242d';
        });
		inputFields.forEach(field => {
			field.style.backgroundColor = '#1f242d';
			field.style.color = 'white';
		});
		headings.forEach(heading => {
			heading.style.color = 'black';
		});
		paragraphs.forEach(paragraph => {
			paragraph.style.color = 'black';
		});
        button.style.color = 'var(--text-color)';
        button.style.backgroundColor = 'var(--bg-color)';
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
		services_box.forEach(box => {
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
        button.style.color = 'black';
        button.style.backgroundColor = '#c9c6c5';
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
