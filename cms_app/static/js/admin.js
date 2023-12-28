// const monthlyChart = document.getElementById("monthly-chart")
// const yearlyChart = document.getElementById("yearly-chart")
// const itemsChart = document.getElementById("items-chart")
// const customerChart = document.getElementById("customer-chart")

// const iChart = new Chart(itemsChart, {
//     type: "bar",
//     data: {
//         labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
//         datasets: [
//             {
//                 label: "# of Votes",
//                 data: [12, 19, 3, 5, 2, 3],
//                 borderWidth: 1,
//             },
//         ],
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true,
//             },
//         },
//         responsive: true,
//         maintainAspectRatio: false,
//     },
// })

// const cChart = new Chart(customerChart, {
//     type: "bar",
//     data: {
//         labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
//         datasets: [
//             {
//                 label: "# of Votes",
//                 data: [12, 19, 3, 5, 2, 3],
//                 borderWidth: 1,
//             },
//         ],
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true,
//             },
//         },

//         responsive: true,
//         maintainAspectRatio: false,
//     },
// })

// const mChart = new Chart(monthlyChart, {
//     type: "line",
//     data: {
//         labels: [
//             "January",
//             "February",
//             "March",
//             "April",
//             "May",
//             "June",
//             "January",
//             "February",
//             "March",
//             "April",
//             "May",
//             "June",
//         ],
//         datasets: [
//             {
//                 label: "",
//                 data: [12, 19, 3, 5, 2, 3, 12, 19, 3, 5, 2, 3],
//                 borderWidth: 1,
//             },
//         ],
//     },
//     options: {
//         scales: {
//             y: {
//                 type: "linear",
//                 grace: "20%",
//                 beginAtZero: true,
//             },
//         },
//         responsive: true,
//         maintainAspectRatio: false,
//     },
// })

// const yChart = new Chart(yearlyChart, {
//     type: "line",
//     data: {
//         labels: [2000, 2000, 2000, 2000, 2000, 2000],
//         datasets: [
//             {
//                 label: "",
//                 data: [12, 19, 3, 5, 2, 3],
//                 borderWidth: 1,
//             },
//         ],
//     },
//     options: {
//         scales: {
//             y: {
//                 type: "linear",
//                 grace: "20%",
//                 beginAtZero: true,
//             },
//         },
//         responsive: true,
//         maintainAspectRatio: false,
//     },
// })

// tab logic
const dashboards = document.querySelectorAll(".dashboard-item")
const tabs = document.querySelectorAll(".tab-btn")
const arr = [
    ["monthly", "yearly"],
    ["item", "customer"],
]

const mobile = window.innerWidth < 831

tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => {
        tab.classList.add("active")
        const num = Math.floor(index / 2)

        if (index == 0 || index == 2) {
            tabs[index + 1].classList.remove("active")
            dashboards[num].classList.add(arr[num][0])
            dashboards[num].classList.remove(arr[num][1])
            if (!mobile) {
                animateRight(dashboards[num])
            } else {
                mobileAnimationRight(dashboards[num])
            }
        } else if (index == 1 || index == 3) {
            tabs[index - 1].classList.remove("active")
            dashboards[num].classList.add(arr[num][1])
            dashboards[num].classList.remove(arr[num][0])
            if (!mobile) {
                animateLeft(dashboards[num])
            } else {
                mobileAnimationLeft(dashboards[num])
            }
        }
    })
})

function animateLeft(dashboard) {
    const leftCard = dashboard.querySelector(".big-card")
    const infoCard = dashboard.querySelector(".info-card")
    const rightCard = dashboard.querySelector(".small-card")
    const tl = gsap.timeline({ ease: "ease.Power2()" })

    tl.to(leftCard, {
        width: "25%",
        height: "50%",
    })
    tl.to(
        infoCard,
        {
            x: 0,
            delay: 0.1,
        },
        0
    )
    tl.to(
        rightCard,
        {
            width: "70%",
            height: "100%",
            delay: 0.15,
        },
        0
    )
}

function animateRight(dashboard) {
    const leftCard = dashboard.querySelector(".big-card")
    const infoCard = dashboard.querySelector(".info-card")
    const rightCard = dashboard.querySelector(".small-card")
    const tl = gsap.timeline({ ease: "ease.Power2()" })

    tl.to(rightCard, {
        width: "25%",
        height: "50%",
    })
    tl.to(
        infoCard,
        {
            x: "300%",
            delay: 0.1,
        },
        0
    )
    tl.to(
        leftCard,
        {
            width: "70%",
            height: "100%",
            delay: 0.15,
        },
        0
    )
}

function mobileAnimationLeft(dashboard) {
    const leftCard = dashboard.querySelector(".big-card")
    const rightCard = dashboard.querySelector(".small-card")
    const tl = gsap.timeline({ ease: "ease.Power2()" })

    tl.to(leftCard, {
        x: "-120%",
    })

    tl.to(
        rightCard,
        {
            x: 0,
        },
        0
    )
}

function mobileAnimationRight(dashboard) {
    const leftCard = dashboard.querySelector(".big-card")
    const rightCard = dashboard.querySelector(".small-card")
    const tl = gsap.timeline({ ease: "ease.Power2()" })

    tl.to(leftCard, {
        x: 0,
    })

    tl.to(
        rightCard,
        {
            x: "120%",
        },
        0
    )
}
