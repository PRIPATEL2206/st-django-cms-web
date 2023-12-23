const weeklyChart = document.getElementById("weekly-chart")
const salesChart = document.getElementById("sales-chart")

new Chart(weeklyChart, {
    type: "bar",
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [
            {
                label: "# of Votes",
                data: [12, 19, 3, 5, 2, 3],
                borderWidth: 1,
            },
        ],
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
    },
})

new Chart(salesChart, {
    type: "line",
    data: {
        labels: [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
        ],
        datasets: [
            {
                label: "# of Votes",
                data: [12, 19, 3, 5, 2, 3, 12, 19, 3, 5, 2, 3],
                borderWidth: 1,
            },
        ],
    },
    options: {
        scales: {
            y: {
                type: "linear",
                grace: "20%",
                beginAtZero: true,
            },
        },
        aspectRatio: 5 / 1,
    },
})
