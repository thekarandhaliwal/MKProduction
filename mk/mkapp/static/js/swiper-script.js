$(function () {
    var swiperPartner = new Swiper('.swiper.swiperPartner', {
        autoplay: {
            delay: 3000
        },
        speed: 2000,
        slidesPerView: 5,
        slidesPerGroup: 1,
        spaceBetween: 10,
        initialSlide: 1,
        loop: false,
        grabCursor: true,
        breakpoints: {
            // when window width is >= 360px
            360: {
                slidesPerView: 2,
                slidesPerGroup: 1,
            },
            // when window width is >= 768px
            768: {
                slidesPerView: 2,
                slidesPerGroup: 1,
            },
            // when window width is >= 1024px
            1024: {
                slidesPerView: 5,
                slidesPerGroup: 1,
            }
        },
        // If we need pagination
        pagination: {
            enabled: false,
            el: '.swiper-pagination',
            type: 'bullets',
            clickable: true,
        },
    });

});

$(function () {
    var swiperTestimonials = new Swiper('.swiper.swiperTestimonials', {
        autoplay: {
            delay: 3000
        },
        speed: 2000,
        slidesPerView: 4,
        slidesPerGroup: 2,
        initialSlide: 2,
        spaceBetween: 10,
        loop: false,
        grabCursor: true,
        breakpoints: {
            // when window width is >= 360px
            360: {
                slidesPerView: 1,
            },
            // when window width is >= 768px
            768: {
                slidesPerView: 4,
            },
            // when window width is >= 1024px
            1024: {
                slidesPerView: 4,
            }
        },
        // If we need pagination
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
            renderBullet: function (index, className) {
                return '<span class="' + className + '"></span>';
            },
        },
    });

});

$(function () {
    var swiperImage = new Swiper('.swiper.swiperImage', {
        speed: 2000,
        slidesPerView: 4,
        slidesPerGroup: 1,
        spaceBetween: 20,
        loop: false,
        grabCursor: true,
        breakpoints: {
            // when window width is >= 360px
            360: {
                slidesPerView: 1,
            },
            // when window width is >= 768px
            768: {
                slidesPerView: 4,
            },
            // when window width is >= 1024px
            1024: {
                slidesPerView: 4,
            }
        },
        // If we need pagination
        pagination: {
            enabled: false,
            el: '.swiper-pagination',
            type: 'bullets',
            clickable: true,
        },
    });

});

const mySwiper = new Swiper('.mySwiper', {
    direction: 'horizontal',
    slidesPerView: 4, // Jumlah slide yang ditampilkan
    spaceBetween: 20, // Jarak antar slide
    breakpoints: {
        // when window width is >= 360px
        360: {
            slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
            slidesPerView: 3,
        },
        // when window width is >= 1024px
        1024: {
            slidesPerView: 4,
        }
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    }
});


