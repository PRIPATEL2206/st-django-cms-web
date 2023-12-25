const navBar = document.querySelector(".navigation")
const hamb_menu = document.querySelector(".hamb-menu")
const footer = document.querySelector(".footer")

navBar.innerHTML = `
    <div class="container">
        <div class="navigation-box">
            <a href="/" class="logo">
                <img src="/assets/images/icons/logo.svg" alt="" class="logo-image">
            </a>
            <div class="navigation-links">
                <a href="/admin.html" class="link">Admin</a>
                <a href="/addProduct.html" class="link">Add Product</a>
                <a href="/addEmployee.html" class="link">Add Emp</a>
                <a href="/allOrder.html" class="link">All Order</a>
                <a href="/myOrder.html" class="link">My Order</a>
                <a href="/userDisplay.html" class="link">Users</a>
            </div>
        </div>
        <div class="navigation-box">
            <a href="/cart.html" class="link cart-link">Cart <img src="./assets/images/icons/cart.svg" alt=""></a>
            <a href="/login.html" class="link sign-in">
            Sign In <img src="./assets/images/icons/right-arrow.svg" alt="arrow" class="icon">
            </a>
            <a href="/profile.html" class="link profile-link">
                <figure> <img src="./assets/images/icons/user.svg" alt=""> </figure> Profile
            </a>
        </div>
        <button class="hamb-btn">
            <div class="divider"></div>
            <div class="divider"></div>
        </button>
    </div>
`

hamb_menu.innerHTML = `
        <ul class="hamb-list">
            <a href="/profile.html" class="hamb-link">Profile</a>
            <a href="/admin.html" class="hamb-link">Admin</a>
            <a href="/cart.html" class="link cart-link">Cart <img src="./assets/images/icons/cart.svg" alt=""></a>
            <a href="/login.html" class="hamb-link sign-in">
                Sign In <img src="./assets/images/icons/right-arrow.svg" alt="arrow" class="icon">
            </a>
        </ul>
`

footer.innerHTML = `
                <div class="container">
                    <div class="footer-content">
                        <div class="footer-box">
                            <a href="/" class="logo">
                                <img src="./assets/images/icons/logo.svg" alt="logo" class="logo-image">
                            </a>
                            <div class="footer-box-content">
                                <p class="paragraph-md"><a href="tel:+01 292 4411" class="animated-link">T: 01 292
                                        4411</a></p>
                                <p class="paragraph-md"><a href="mailto:info@newkey.ie" class="animated-link">E:
                                        info@newkey.ie</a></p>
                                <p class="paragraph-sm">Unit 29, Southgate, Dublin road, <br />
                                    Drogheda, Co.Meath</p>
                            </div>
                        </div>
                        <div class="footer-box-2">
                            <div class="footer-list">
                                <a href="/about.html" class="link">About</a>
                                <a href="/projects.html" class="link">Projects</a>
                                <a href="/investor.html" class="link">Investing</a>
                                <a href="/contact.html" class="link">Contact</a>
                            </div>
                            <div class="footer-list">
                                <a href="./login.html" class="link sign-in">Sign In <img
                                        src="./assets/images/icons/right-arrow.svg" alt="arrow" class="icon"></a>
                            </div>
                        </div>
                    </div>
                    <div class="footer-panel">
                        <p class="paragraph-xs">
                            copyright 2023 NewKey Homes | All rights Reserved | <a href="/privacy.html"
                                class="animated-link">Privacy&nbsp;Policy</a>
                        </p>
                        <p class="paragraph-xs">
                            <a href="/" class="animated-link">Crafted</a>
                        </p>
                    </div>
                </div>
`

// new Textify(
//     {
//         el: ".paragraph, .title-2_5xl",
//         splitType: "lines",
//         largeText: true,
//         animation: {
//             by: "lines",
//             stagger: 0.1,
//             duration: 0.7,
//             ease: "expo.inOut",
//             transformOrigin: "left top",
//             animateProps: { y: "0", opacity: 0 },
//         },
//     },
//     gsap
// )

// new Textify(
//     {
//         el: ".title-5xl, .title-3xl:not(.not-animate)",
//         animation: {
//             stagger: 0.01,
//             duration: 0.5,
//             ease: "ease.inOut",
//             animateProps: { opacity: 0, y: 100 },
//         },
//     },
//     gsap
// )
