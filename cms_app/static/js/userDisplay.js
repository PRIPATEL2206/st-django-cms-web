const userSlider = new Swiper(".users-slider", {
    slidesPerView: 1,
    spaceBetween: 50,
    grab: true,

    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        renderBullet: function (index, className) {
            return '<span class="' + className + '">' + (index + 1) + "</span>"
        },
    },
})

const mobileUserSlider = new Swiper(".mobile-users-slider", {
    slidesPerView: 1,
    spaceBetween: 50,
    grab: true,

    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        renderBullet: function (index, className) {
            return '<span class="' + className + '">' + (index + 1) + "</span>"
        },
    },
})
