function events(x) {
    if (typeof selectUser != "undefined") {
        selectUser.style.display = "none"
        selectUser = document.getElementById("balloon"+x)
        selectUser.style.display = "block"
    } else {
        selectUser = document.getElementById("balloon"+x)
        selectUser.style.display = "block"
    }
}