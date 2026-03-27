function filterGames() {
    var input = document.getElementById('search-input');
    if (!input) return;
    var filter = input.value.toLowerCase();
    var cards = document.querySelectorAll('.game-card');
    cards.forEach(function(card) {
        var title = card.getAttribute('data-title') || '';
        card.style.display = title.includes(filter) ? '' : 'none';
    });
}
