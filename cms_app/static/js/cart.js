const likeBtns = document.querySelectorAll(".like-btn")

likeBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
        btn.classList.toggle("liked")
    })
})
