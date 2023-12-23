// fix safari and all browser size (vh) issues
let vh = window.innerHeight * 0.01
document.documentElement.style.setProperty("--vh", `${vh}px`)

// add smooth scroll
const wrapper = document.querySelector(".wrapper")
const scrollContainer = document.querySelector(".scroll-container")
const nav = document.querySelector(".navigation")

const lenis = new Lenis({
    wrapper: wrapper,
    content: scrollContainer,
})
lenis.on("scroll", ({ direction, scroll }) => {
    if (scroll > 50) {
        if (direction === -1) {
            nav.classList.remove("hide")
        } else {
            nav.classList.add("hide")
        }
    } else {
        nav.classList.remove("hide")
    }
})
function raf(time) {
    lenis.raf(time)
    requestAnimationFrame(raf)
}
requestAnimationFrame(raf)

const hambBtn = document.querySelector(".hamb-btn")
const hambMenu = document.querySelector(".hamb-menu")
let isActive = false

if (hambBtn || hambMenu) {
    hambMenu.style = ""

    hambBtn.addEventListener("click", () => {
        isActive = !isActive
        hambBtn.classList.toggle("active")
        hambMenu.classList.toggle("active")
        if (isActive) {
            lenis.stop()
        } else {
            lenis.start()
        }
        nav.classList.remove("hide")
    })
}

const accordion = document.querySelector(".accordian-content")
const trigger = document.querySelector(".accordian-trigger")

if (trigger) {
    trigger.addEventListener("click", () => {
        if (accordion.classList.contains("active")) {
            accordion.classList.remove("active")
            accordion.style.maxHeight = 0
        } else {
            accordion.classList.add("active")
            accordion.style.maxHeight = accordion.scrollHeight + "px"
        }
    })
}

// scroll to
const anchor = document.querySelector("#anchor")
if (anchor) {
    const scrollTo = anchor.getAttribute("href")

    anchor.addEventListener("click", () => {
        lenis.scrollTo(scrollTo, {
            duration: 2,
        })
    })
}
