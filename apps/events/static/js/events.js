// Sidebar Toggle Functionality
document.addEventListener('DOMContentLoaded', function() {
    const sidebarTogglers = document.querySelectorAll('.sidebar-toggler');
    const sidebar = document.querySelector('.sidebar');
    const main = document.querySelector('.main');

    sidebarTogglers.forEach(toggler => {
        toggler.addEventListener('click', function() {
            sidebar.classList.toggle('collapsed');
            main.classList.toggle('expanded');
            
            // Store the state in localStorage
            const isCollapsed = sidebar.classList.contains('collapsed');
            localStorage.setItem('sidebarCollapsed', isCollapsed);
        });
    });

    // Restore sidebar state from localStorage
    const isCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
    if (isCollapsed) {
        sidebar.classList.add('collapsed');
        main.classList.add('expanded');
    }
});
