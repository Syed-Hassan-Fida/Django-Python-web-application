(function ($) {
  "use strict";
  /*----------------------------------------*/
  /*  Check if element exists
/*----------------------------------------*/
  $.fn.elExists = function () {
    return this.length > 0;
  };

  /*--
        Custom script to call Background
        Image & Color from html data attribute
    -----------------------------------*/
  $("[data-bg-image]").each(function () {
    var $this = $(this),
      $image = $this.data("bg-image");
    $this.css("background-image", "url(" + $image + ")");
  });
  $("[data-bg-color]").each(function () {
    var $this = $(this),
      $color = $this.data("bg-color");
    $this.css("background-color", $color);
  });

  /*----------------------------------------*/
  /*  WOW
/*----------------------------------------*/
  new WOW().init();

  /*---------------------------------------
		Header Sticky
---------------------------------*/
  $(window).on("scroll", function () {
    if ($(this).scrollTop() > 300) {
      $(".header-sticky").addClass("sticky");
    } else {
      $(".header-sticky").removeClass("sticky");
    }
  });

  /*----------------------------------------*/
  /*  HasSub Item
/*----------------------------------------*/
  $(".hassub-item li.hassub a").on("click", function () {
    $(this).removeAttr("href");
    var element = $(this).parent("li");
    if (element.hasClass("open")) {
      element.removeClass("open");
      element.find("li").removeClass("open");
      element.find("ul").slideUp();
    } else {
      element.addClass("open");
      element.children("ul").slideDown();
      element.siblings("li").children("ul").slideUp();
      element.siblings("li").removeClass("open");
      element.siblings("li").find("li").removeClass("open");
      element.siblings("li").find("ul").slideUp();
    }
  });

  /*---------------------------------------
		Swiper All Slider
---------------------------------*/
  /* ---Main Slider--- */
  if ($(".main-slider").elExists()) {
    var swiper = new Swiper(".main-slider", {
      loop: true,
      slidesPerView: 1,
      speed: 750,
      autoplay: {
        disableOnInteraction: false,
        delay: 7000,
      },
      effect: "fade",
      fadeEffect: {
        crossFade: true,
      },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
        type: "bullets",
      },
    });
  }

  /* ---Project Slider--- */
  if ($(".project-slider").elExists()) {
    var mySwiper = new Swiper(".project-slider", {
      loop: true,
      slidesPerView: 4,
      effect: "slide",
      navigation: {
        prevEl: ".project-button-prev",
        nextEl: ".project-button-next",
      },
      pagination: {
        el: ".project-pagination",
        clickable: true,
        type: "custom",
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
        },
        576: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 2,
        },
        992: {
          slidesPerView: 3,
        },
        1200: {
          slidesPerView: 4,
        },
      },
    });
  }

  /* ---Project Slider--- */
  if ($(".project-slider-2").elExists()) {
    var mySwiper = new Swiper(".project-slider-2", {
      loop: true,
      spaceBetween: 30,
      effect: "slide",
      navigation: {
        nextEl: ".custom-button-next",
        prevEl: ".custom-button-prev",
      },
      pagination: {
        el: ".project-pagination",
        clickable: true,
        type: "custom",
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
        },
        576: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 2,
        },
        992: {
          slidesPerView: 3,
        },
        1200: {
          slidesPerView: 3,
        },
      },
    });
  }

  /* ---Brand Slider--- */
  if ($(".brand-slider").elExists()) {
    var mySwiper = new Swiper(".brand-slider", {
      loop: false,
      effect: "slide",
      navigation: {
        nextEl: ".brand-button-next",
        prevEl: ".brand-button-prev",
      },
      pagination: {
        el: ".brand-pagination",
        clickable: true,
        type: "custom",
      },
      breakpoints: {
        320: {
          slidesPerView: 2,
          slidesPerColumn: 1,
          slidesPerGroup: 1,
          slidesPerColumnFill: "column",
          spaceBetween: 50,
        },
        768: {
          slidesPerView: 4,
          slidesPerColumn: 2,
          slidesPerGroup: 1,
          slidesPerColumnFill: "row",
          spaceBetween: 100,
        },
        992: {
          slidesPerView: 5,
          slidesPerColumn: 2,
          slidesPerGroup: 1,
          slidesPerColumnFill: "row",
          spaceBetween: 100,
        },
      },
    });
  }

  /* ---Service Slider--- */
  if ($(".service-slider").elExists()) {
    var mySwiper = new Swiper(".service-slider", {
      loop: true,
      slidesPerView: 3,
      spaceBetween: 30,
      effect: "slide",
      navigation: {
        nextEl: ".custom-button-next",
        prevEl: ".custom-button-prev",
      },
      pagination: {
        el: ".service-pagination",
        clickable: true,
        type: "custom",
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 2,
        },
        992: {
          slidesPerView: 3,
        },
      },
    });
  }

  /* ---Service Slider Two--- */
  if ($(".service-slider-2").elExists()) {
    var mySwiper = new Swiper(".service-slider-2", {
      loop: false,
      slidesPerView: 3,
      slidesPerColumn: 2,
      slidesPerGroup: 1,
      slidesPerColumnFill: "row",
      spaceBetween: 30,
      effect: "slide",
      navigation: {
        nextEl: ".service-button-next",
        prevEl: ".service-button-prev",
      },
      pagination: {
        el: ".service-pagination",
        clickable: true,
        type: "custom",
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 2,
        },
        992: {
          slidesPerView: 3,
        },
      },
    });
  }

  /* ---Team Member Slider--- */
  if ($(".team-member-slider").elExists()) {
    var mySwiper = new Swiper(".team-member-slider", {
      loop: true,
      slidesPerView: 4,
      spaceBetween: 30,
      effect: "slide",
      navigation: {
        nextEl: ".team-button-next",
        prevEl: ".team-button-prev",
      },
      pagination: {
        el: ".team-pagination",
        clickable: true,
        type: "custom",
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
        },
        480: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 2,
        },
        1200: {
          slidesPerView: 4,
        },
      },
    });
  }

  /* ---Team Member Slider--- */
  if ($(".team-member-slider-2").elExists()) {
    var mySwiper = new Swiper(".team-member-slider-2", {
      loop: false,
      spaceBetween: 30,
      effect: "slide",
      navigation: {
        nextEl: ".team-button-next",
        prevEl: ".team-button-prev",
      },
      pagination: {
        el: ".team-pagination",
        clickable: true,
        type: "custom",
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
          slidesPerColumn: 1,
          slidesPerGroup: 1,
          slidesPerColumnFill: "column",
        },
        480: {
          slidesPerView: 2,
          slidesPerColumn: 1,
          slidesPerGroup: 1,
          slidesPerColumnFill: "column",
        },
        768: {
          slidesPerView: 3,
          slidesPerColumn: 1,
          slidesPerGroup: 1,
          slidesPerColumnFill: "column",
        },
        992: {
          slidesPerView: 4,
          slidesPerColumn: 2,
          slidesPerGroup: 1,
          slidesPerColumnFill: "row",
        },
      },
    });
  }

  /* ---Testimonial Slider--- */
  if ($(".testimonial-slider").elExists()) {
    var mySwiper = new Swiper(".testimonial-slider", {
      loop: false,
      spaceBetween: 40,
      effect: "slide",
      navigation: {
        nextEl: ".testimonial-button-next",
        prevEl: ".testimonial-button-prev",
      },
      pagination: {
        el: ".testimonial-pagination",
        clickable: true,
        type: "custom",
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 2,
          slidesPerColumn: 1,
          slidesPerGroup: 1,
          slidesPerColumnFill: "column",
        },
        992: {
          slidesPerView: 1,
          slidesPerColumn: 2,
          slidesPerGroup: 1,
          slidesPerColumnFill: "row",
        },
        1200: {
          slidesPerView: 2,
          slidesPerColumn: 1,
          slidesPerGroup: 1,
          slidesPerColumnFill: "column",
        },
      },
    });
  }

  /* ---Blog Slider--- */
  if ($(".blog-slider").elExists()) {
    var mySwiper = new Swiper(".blog-slider", {
      loop: true,
      slidesPerView: 3,
      spaceBetween: 30,
      effect: "slide",
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
        type: "bullets",
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 2,
        },
        1200: {
          slidesPerView: 3,
        },
      },
    });
  }

  /* ---Blog Slider--- */
  if ($(".product-detail-slider").elExists()) {
    var mySwiper = new Swiper(".product-detail-slider", {
      loop: true,
      slidesPerView: 1,
      // spaceBetween: 30,
      effect: "slide",
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });
  }

  /* ---Product Detail Horizontal Slider--- */
  if ($(".gallery-top").elExists()) {
    var galleryTop = new Swiper(".gallery-top", {
      spaceBetween: 3,
      loop: true,
      loopedSlides: 3,
    });
    var galleryThumbs = new Swiper(".gallery-thumbs", {
      spaceBetween: 10,
      slidesPerView: 3,
      touchRatio: 0.2,
      slideToClickedSlide: true,
      loop: true,
      loopedSlides: 3,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });
    galleryTop.controller.control = galleryThumbs;
    galleryThumbs.controller.control = galleryTop;
  }

  /*----------------------------------------*/
  /*  jQuery Zoom
/*----------------------------------------*/
  if ($(".zoom").elExists()) {
    $(".zoom").zoom();
  }

  /*------------------------------------
	Toolbar Button
	------------------------------------- */
  var $overlay = $(".global-overlay");
  $(".toolbar-btn").on("click", function (e) {
    e.preventDefault();
    e.stopPropagation();
    var $this = $(this);
    var target = $this.attr("href");
    var prevTarget = $this
      .parent()
      .siblings()
      .children(".toolbar-btn")
      .attr("href");
    $(target).toggleClass("open");
    $(prevTarget).removeClass("open");
    $($overlay).addClass("overlay-open");
  });

  /*----------------------------------------*/
  /*  Click on Documnet
/*----------------------------------------*/
  var $body = $(".global-overlay");

  $body.on("click", function (e) {
    var $target = e.target;
    var dom = $(".main-wrapper").children();

    if (!$($target).is(".toolbar-btn") && !$($target).parents().is(".open")) {
      dom.removeClass("open");
      dom.find(".open").removeClass("open");
      $overlay.removeClass("overlay-open");
    }
  });

  /*----------------------------------------*/
  /*  Close Button Actions
/*----------------------------------------*/
  $(".button-close").on("click", function (e) {
    var dom = $(".main-wrapper").children();
    e.preventDefault();
    var $this = $(this);
    $this.parents(".open").removeClass("open");
    dom.find(".global-overlay").removeClass("overlay-open");
  });

  /*----------------------------------------*/
  /*  Offcanvas
/*----------------------------------------*/
  var $offcanvasNav = $(".mobile-menu, .offcanvas-minicart_menu"),
    $offcanvasNavWrap = $(".mobile-menu_wrapper, .offcanvas-minicart_wrapper"),
    $offcanvasNavSubMenu = $offcanvasNav.find(".sub-menu"),
    $menuToggle = $(".menu-btn"),
    $menuClose = $(".button-close");

  $offcanvasNavSubMenu.slideUp();

  $offcanvasNav.on("click", "li a, li .menu-expand", function (e) {
    var $this = $(this);
    if (
      $this
        .parent()
        .attr("class")
        .match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/) &&
      ($this.attr("href") === "#" ||
        $this.attr("href") === "" ||
        $this.hasClass("menu-expand"))
    ) {
      e.preventDefault();
      if ($this.siblings("ul:visible").length) {
        $this.siblings("ul").slideUp("slow");
      } else {
        $this.closest("li").siblings("li").find("ul:visible").slideUp("slow");
        $this.closest("li").siblings("li").removeClass("menu-open");
        $this.siblings("ul").slideDown("slow");
        $this.parent().siblings().children("ul").slideUp();
      }
    }
    if (
      $this.is("a") ||
      $this.is("span") ||
      $this.attr("class").match(/\b(menu-expand)\b/)
    ) {
      $this.parent().toggleClass("menu-open");
    } else if (
      $this.is("li") &&
      $this.attr("class").match(/\b('menu-item-has-children')\b/)
    ) {
      $this.toggleClass("menu-open");
    }
  });

  $(".button-close").on("click", function (e) {
    e.preventDefault();
    $(".mobile-menu .sub-menu").slideUp();
    $(".mobile-menu .menu-item-has-children").removeClass("menu-open");
  });

  /*----------------------------------------*/
  /*  Slider Range
/*----------------------------------------*/
  var sliderrange = $("#slider-range");
  var amountprice = $("#amount");
  $(function () {
    sliderrange.slider({
      range: true,
      min: 10,
      max: 850,
      step: 10,
      values: [0, 1000],
      slide: function (event, ui) {
        amountprice.val("$" + ui.values[0] + " - $" + ui.values[1]);
      },
    });
    amountprice.val(
      "$" +
        sliderrange.slider("values", 0) +
        " - $" +
        sliderrange.slider("values", 1)
    );
  });

  /*----------------------------------------*/
  /*  QTY Button
/*----------------------------------------*/
  $(".cart-plus-minus").append(
    '<div class="dec qtybutton"><i class="ion-ios-arrow-down"></i></div><div class="inc qtybutton"><i class="ion-ios-arrow-up"></i></div>'
  );
  $(".qtybutton").on("click", function () {
    var $button = $(this);
    var oldValue = $button.parent().find("input").val();
    if ($button.hasClass("inc")) {
      var newVal = parseFloat(oldValue) + 1;
    } else {
      // Don't allow decrementing below zero
      if (oldValue > 1) {
        var newVal = parseFloat(oldValue) - 1;
      } else {
        newVal = 1;
      }
    }
    $button.parent().find("input").val(newVal);
  });

  /*----------------------------------------*/
  /*  Nice Select
/*----------------------------------------*/
  if ($(".nice-select").elExists()) {
    $(".nice-select").niceSelect();
  }
  /*----------------------------------------*/
  /*  JS Tilt
/*----------------------------------------*/
  if ($("[data-aos]").length) {
    AOS.init({
      once: true,
    });
  }

  /*--------------------------------
    Ajax Contact Form
-------------------------------- */
  $(function () {
    // Get the form.
    var form = $("#contact-form");
    // Get the messages div.
    var formMessages = $(".form-messege");
    // Set up an event listener for the contact form.
    $(form).submit(function (e) {
      // Stop the browser from submitting the form.
      e.preventDefault();
      // Serialize the form data.
      var formData = $(form).serialize();
      // Submit the form using AJAX.
      $.ajax({
        type: "POST",
        url: $(form).attr("action"),
        data: formData,
      })
        .done(function (response) {
          // Make sure that the formMessages div has the 'success' class.
          $(formMessages).removeClass("error");
          $(formMessages).addClass("success");

          // Set the message text.
          $(formMessages).text(response);

          // Clear the form.
          $("#contact-form input,#contact-form textarea").val("");
        })
        .fail(function (data) {
          // Make sure that the formMessages div has the 'error' class.
          $(formMessages).removeClass("success");
          $(formMessages).addClass("error");

          // Set the message text.
          if (data.responseText !== "") {
            $(formMessages).text(data.responseText);
          } else {
            $(formMessages).text(
              "Oops! An error occured and your message could not be sent."
            );
          }
        });
    });
  });

  /*----------------------------------------*/
  /*  Toggle Function Active
/*----------------------------------------*/
  // showlogin toggle
  $("#showlogin").on("click", function () {
    $("#checkout-login").slideToggle(900);
  });
  // showlogin toggle
  $("#showcoupon").on("click", function () {
    $("#checkout_coupon").slideToggle(900);
  });
  // showlogin toggle
  $("#cbox").on("click", function () {
    $("#cbox-info").slideToggle(900);
  });

  // showlogin toggle
  $("#ship-box").on("click", function () {
    $("#ship-box-info").slideToggle(1000);
  });

  /*----------------------------------------*/
  /*  CounterUp
/*----------------------------------------*/
  if ($(".count").elExists()) {
    $(".count").counterUp({
      delay: 10,
      time: 1000,
    });
  }

  /*--------------------------------
    Scroll To Top
-------------------------------- */
  function scrollToTop() {
    var $scrollUp = $(".scroll-to-top"),
      $lastScrollTop = 0,
      $window = $(window);

    $window.on("scroll", function () {
      var topPos = $(this).scrollTop();
      if (topPos > $lastScrollTop) {
        $scrollUp.removeClass("show");
      } else {
        if ($window.scrollTop() > 200) {
          $scrollUp.addClass("show");
        } else {
          $scrollUp.removeClass("show");
        }
      }
      $lastScrollTop = topPos;
    });

    $scrollUp.on("click", function (evt) {
      $("html, body").animate(
        {
          scrollTop: 0,
        },
        600
      );
      evt.preventDefault();
    });
  }

  scrollToTop();

  /*--------------------------------
    MailChimp
-------------------------------- */
  $("#mc-form").ajaxChimp({
    language: "en",
    callback: mailChimpResponse,
    url: "https://devitems.us11.list-manage.com/subscribe/post?u=6bbb9b6f5827bd842d9640c82&amp;id=05d85f18ef",
  });
  function mailChimpResponse(resp) {
    if (resp.result === "success") {
      $(".mailchimp-success").addClass("active");
      $(".mailchimp-success")
        .html("" + resp.msg)
        .fadeIn(900);
      $(".mailchimp-error").fadeOut(400);
    } else if (resp.result === "error") {
      $(".mailchimp-error")
        .html("" + resp.msg)
        .fadeIn(900);
    }
  }

  /*--------------------------------
    Hash Link Scroll To Top Prevent
-------------------------------- */
  $('a[href="#"]').on("click", function (e) {
    e.preventDefault ? e.preventDefault() : (e.returnValue = false);
  });
})(jQuery);
