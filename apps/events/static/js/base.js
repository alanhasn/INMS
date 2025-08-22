document.addEventListener('DOMContentLoaded', function() {
    // Toggle sidebar on mobile
    const toggleSidebar = document.querySelector('.toggle-sidebar');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.querySelector('.overlay');
    const mainContent = document.querySelector('.main');

    if (toggleSidebar) {
        toggleSidebar.addEventListener('click', function() {
            sidebar.classList.toggle('active');
            overlay.classList.toggle('active');
        });
    }

    // Close sidebar when clicking overlay
    if (overlay) {
        overlay.addEventListener('click', function() {
            sidebar.classList.remove('active');
            overlay.classList.remove('active');
        });
    }

    // Handle active navigation states
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // Handle responsive design
    function handleResize() {
        if (window.innerWidth > 768) {
            sidebar.classList.remove('active');
            overlay.classList.remove('active');
        }
    }

    window.addEventListener('resize', handleResize);
});
