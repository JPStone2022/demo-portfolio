// theme-toggle.js

// Icons
const sunIcon = document.getElementById('theme-toggle-sun-icon');
const moonIcon = document.getElementById('theme-toggle-moon-icon');
const themeToggleBtn = document.getElementById('theme-toggle');

// Theme variables
const userTheme = localStorage.getItem('color-theme');
const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches;

// Function to toggle theme
const toggleTheme = (isDark) => {
    if (isDark) {
        document.documentElement.classList.add('dark');
        if (moonIcon) moonIcon.classList.remove('hidden');
        if (sunIcon) sunIcon.classList.add('hidden');
        localStorage.setItem('color-theme', 'dark');
    } else {
        document.documentElement.classList.remove('dark');
        if (sunIcon) sunIcon.classList.remove('hidden');
        if (moonIcon) moonIcon.classList.add('hidden');
        localStorage.setItem('color-theme', 'light');
    }
};

// Initial theme check and icon display
const initialThemeCheck = () => {
    if (userTheme === 'dark' || (!userTheme && systemTheme)) {
        if (moonIcon) moonIcon.classList.remove('hidden');
        if (sunIcon) sunIcon.classList.add('hidden');
        document.documentElement.classList.add('dark');
    } else {
        if (sunIcon) sunIcon.classList.remove('hidden');
        if (moonIcon) moonIcon.classList.add('hidden');
        document.documentElement.classList.remove('dark'); // Ensure light if not dark
    }
};

// Call the initial check once the DOM is ready
document.addEventListener('DOMContentLoaded', initialThemeCheck);


// Event listener for the toggle button
if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
        // Check if dark mode is currently enabled
        const isDarkMode = document.documentElement.classList.contains('dark');
        toggleTheme(!isDarkMode); // Toggle to the opposite theme
    });
}

// Listen for changes in system preference (optional, but good for UX)
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    // Only change if no theme is explicitly set by the user
    if (!localStorage.getItem('color-theme')) {
        toggleTheme(e.matches);
    }
});
