// profile picture change
const img = document.querySelector(".profile-img")
const imgInput = document.querySelector(".profile-img-input")

imgInput.addEventListener("change", () => {
    img.src = URL.createObjectURL(imgInput.files[0])
})

// edit input
const inputContainers = document.querySelectorAll(".profile-info .input-container")

inputContainers.forEach((inpContainer) => {
    const inp = inpContainer.querySelector("input")
    const editBtn = inpContainer.querySelector(".edit-btn:not(.add-btn)")

    if (editBtn) {
        if (inp.value != "") {
            inp.setAttribute("readonly", true)
        }

        editBtn.addEventListener("click", () => {
            inp.removeAttribute("readonly")
            inp.focus()
        })

        inp.addEventListener("blur", () => {
            if (inp.value != "") {
                inp.setAttribute("readonly", true)
            }
        })
    }
})
