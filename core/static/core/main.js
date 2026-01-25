// Main JavaScript file
document.addEventListener('DOMContentLoaded', function() {
    console.log('Django app loaded successfully!');
    
    // Add active class to current nav link
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});
