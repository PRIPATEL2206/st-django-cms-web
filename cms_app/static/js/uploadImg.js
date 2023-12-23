// profile picture change
const img = document.querySelector(".profile-img")
const imgInput = document.querySelector(".profile-img-input")

imgInput.addEventListener("change", () => {
    img.src = URL.createObjectURL(imgInput.files[0])
})
