const grocerySlider = new Swiper(".grocery-slider", {
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

const mobileGrocerySlider = new Swiper(".mobile-grocery-slider", {
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
