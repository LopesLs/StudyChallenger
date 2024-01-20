function toggleAwnserDisplay(id) {
    let awnser = document.getElementById(id);
    let cardContainer = document.getElementById('flashcard-container');

    if (cardContainer.classList.contains('op2')) {
        return;
    }
    
    if (awnser.style.display === 'none' || awnser.style.display === '') {
        awnser.style.display = 'block';
    } else {
        awnser.style.display = "none";
    }
}