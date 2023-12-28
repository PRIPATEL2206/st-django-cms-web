// const navBar = document.querySelector(".navigation")
// const hamb_menu = document.querySelector(".hamb-menu")
// const footer = document.querySelector(".footer")

// navBar.innerHTML = `
//     <div class="container">
//         <div class="navigation-box">
//             <a href="/" class="logo">
//                 <img src="/assets/images/icons/logo.svg" alt="" class="logo-image">
//             </a>
//             <div class="navigation-links">
//                 <a href="/admin.html" class="link">Admin</a>
//                 <a href="/addProduct.html" class="link">Add Product</a>
//                 <a href="/addEmployee.html" class="link">Add Emp</a>
//                 <a href="/allOrder.html" class="link">All Order</a>
//                 <a href="/myOrder.html" class="link">My Order</a>
//                 <a href="/userDisplay.html" class="link">Users</a>
//             </div>
//         </div>
//         <div class="navigation-box">
//             <a href="/cart.html" class="link link-with-img">Cart <img src="./assets/images/icons/cart.svg" alt=""></a>
//             <a href="/login.html" class="link link-with-img">
//                 Sign In <img src="./assets/images/icons/right-arrow.svg" alt="arrow" class="icon">
//             </a>
//             <a href="/profile.html" class="link link-with-img profile-link">
//                 <figure> <img src="./assets/images/icons/user.svg" alt=""> </figure> Profile
//             </a>
//         </div>
//         <button class="hamb-btn">
//             <div class="divider"></div>
//             <div class="divider"></div>
//         </button>
//     </div>
// `

// hamb_menu.innerHTML = `
//         <ul class="hamb-list">
//             <a href="/admin.html" class="link">Admin</a>
//             <a href="/addProduct.html" class="link">Add Product</a>
//             <a href="/addEmployee.html" class="link">Add Emp</a>
//             <a href="/allOrder.html" class="link">All Order</a>
//             <a href="/myOrder.html" class="link">My Order</a>
//             <a href="/userDisplay.html" class="link">Users</a>
//             <a href="/cart.html" class="link link-with-img">Cart <img src="./assets/images/icons/cart.svg" alt=""></a>
//             <a href="/login.html" class="link link-with-img">
//                 Sign In <img src="./assets/images/icons/right-arrow.svg" alt="arrow" class="icon">
//             </a>
//             <a href="/profile.html" class="link link-with-img profile-link">
//                 <figure> <img src="./assets/images/icons/user.svg" alt=""> </figure> Profile
//             </a>
//         </ul>
// `

// footer.innerHTML = `
//                 <div class="container">
//                     <div class="footer-content">
//                         <div class="footer-box">
//                             <a href="/" class="logo">
//                                 <img src="./assets/images/icons/logo.svg" alt="logo" class="logo-image">
//                             </a>
//                         </div>
//                         <div class="footer-box-2">
//                             <div class="footer-list admin">
//                                 <a href="/addEmployee.html" class="link">Add Employee</a>
//                                 <a href="/addProduct.html" class="link">Add Product</a>
//                                 <a href="/admin.html" class="link">Dashboard</a>
//                                 <a href="/userDisplay.html" class="link">Users</a>
//                             </div>
//                             <div class="footer-list employee">
//                                 <a href="/admin.html" class="link">Dashboard</a>
//                                 <a href="/allOrder.html" class="link">Orders</a>
//                             </div>
//                             <div class="footer-list user">
//                                 <a href="/cart.html" class="link link-with-img">Cart <img src="./assets/images/icons/cart.svg" alt=""></a>
//                                 <a href="/myOrder.html" class="link">My Orders</a>
//                             </div>

//                         </div>
//                         <div class="footer-box-3">
//                             <div class="footer-list login">
//                                 <a href="./login.html" class="link link-with-img">Sign In <img
//                                         src="./assets/images/icons/right-arrow.svg" alt="arrow" class="icon"></a>
//                             </div>
//                             <div class="footer-list logout">
//                                 <a href="/profile.html" class="link link-with-img profile-link">
//                                     <figure> <img src="./assets/images/icons/user.svg" alt=""> </figure> Profile
//                                 </a>
//                                 <a href="#" class="link">Log Out</a>
//                             </div>
//                         </div>
//                     </div>
//                     <div class="footer-panel">
//                         <p class="paragraph-xs">
//                             copyright 2023 SARC | Sales And Relationship with Customers | All rights Reserved | Privacy Policy
//                         </p>
//                         <p class="paragraph-xs">
//                             Crafted By |
//                             <a href="https://github.com/PRIPATEL2206" class="animated-link">PRIPATEL2206</a>
//                         </p>
//                     </div>
//                 </div>
// `

// Break repair
const body = document.querySelector("body")
body.innerHTML += `
    <p class="paragraph-md" style="opacity: 0; position: absolute; top: -100%">
        lorem100
    </p>
`

new Textify(
    {
        el: ".title-3xl,.title-5xl,.title-2xl",
        animation: {
            stagger: 0.007,
            duration: 0.5,
            ease: "ease.inOut",
            animateProps: { opacity: 0, y: 100 },
        },
    },
    gsap
)

new Textify(
    {
        el: ".paragraph-md,paragraph,.paragraph-sm",
        splitType: "lines",
        largeText: true,
        animation: {
            by: "lines",
            stagger: 0.1,
            duration: 0.5,
            ease: "circ.out",
            transformOrigin: "left top",
            animateProps: { y: "-100%", rotate: -30 },
        },
    },
    gsap
)
