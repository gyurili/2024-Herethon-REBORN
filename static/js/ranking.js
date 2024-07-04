// Select the button element
const btn = document.getElementById("show-more-btn");

// Function to toggle visibility of elements with 'extra' class under .allRanks
function toggleRankings() {
    const elements = document.querySelectorAll('.allRanks .post-container.extra');
    elements.forEach(element => {
        element.classList.toggle('hidden'); // Assuming you have a CSS class 'hidden' to hide elements
    });
}

// Add event listener to the button
btn.addEventListener('click', toggleRankings);
