// const monthlyChart = document.getElementById("monthly-chart")
// const yearlyChart = document.getElementById("yearly-chart")
// const itemsChart = document.getElementById("items-chart")
// const customerChart = document.getElementById("customer-chart")

// const iChart = new Chart(itemsChart, {
//     type: "bar",
//     data: {
//         labels: {{itemWiseSalse.lable | safe}},
//         datasets: [
//             {
//                 label: "# of salse",
//                 data: {{itemWiseSalse.data }},
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
//         labels: {{customerWiseSalse.lable | safe}},
//         datasets: [
//             {
//                 label: "# of Buying",
//                 data:{{customerWiseSalse.data }},
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
//         labels:{{ monthlySalse.lable  }},
//         datasets: [
//             {
//                 label: "",
//                 data: {{monthlySalse.data}},
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
//         labels: {{ yearlySalse.lable  }},
//         datasets: [
//             {
//                 label: "",
//                 data:{{yearlySalse.data}},
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

tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => {
        tab.classList.add("active")
        const num = Math.floor(index / 2)
        let charts = []
        if (index < 2) {
            charts = [mChart, yChart]
        } else {
            charts = [iChart, cChart]
        }

        if (index == 0 || index == 2) {
            tabs[index + 1].classList.remove("active")
            dashboards[num].classList.add(arr[num][0])
            dashboards[num].classList.remove(arr[num][1])
            animateRight(dashboards[num], charts[0], charts[1])
        } else if (index == 1 || index == 3) {
            tabs[index - 1].classList.remove("active")
            dashboards[num].classList.add(arr[num][1])
            dashboards[num].classList.remove(arr[num][0])
            animateLeft(dashboards[num], charts[0], charts[1])
        }
    })
})

function animateLeft(dashboard, lChart, rChart) {
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

function animateRight(dashboard, lChart, rChart) {
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
