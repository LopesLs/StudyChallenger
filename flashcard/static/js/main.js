function show_awnser(id) {
    card = document.getElementById(id)

    if (card.style.display == '') {
        card.style.display = "block"
    } else {
        card.style.display = 'none'
    }
}