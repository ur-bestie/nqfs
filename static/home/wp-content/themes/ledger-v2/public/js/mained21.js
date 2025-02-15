(() => {
    jQuery(".textwidget").each((function() {
        jQuery(this).replaceWith(jQuery(this).contents())
    }));
    for (var e = document.querySelectorAll(".fields-container input"), t = 0, i = e.length; t < i; t++) e[t].addEventListener("focus", (function(e) {
        var t, i = e.target.id;
        (i && (t = document.querySelector("label[for=" + i + "]")), t) && t.closest("div").classList.add("is-active")
    }), !1), e[t].addEventListener("blur", (function(e) {
        if (!e.target.value) {
            var t, i = e.target.id;
            if (i && (t = document.querySelector("label[for=" + i + "]")), t) t.closest("div").classList.remove("is-active")
        }
    }), !1);
    jQuery(e).each((function() {
        "" != jQuery(this).val() && jQuery(this).parent().addClass("is-active")
    }));
    var r = document.getElementById("main-navigation");
    if (r) {
        var o = function() {
                r.classList.toggle("is-open"), n.classList.toggle("is-open")
            },
            n = document.getElementById("mobile-menu"),
            a = document.getElementById("bg-menu-mobile");
        n.addEventListener("click", o, !1), a.addEventListener("click", o, !1)
    }
    jQuery("body").click((function() {
        jQuery(".fb_lightbox-overlay-fixed,.preloaded_lightbox").remove(), jQuery("body, html").removeClass("fb_lightbox-lock"), jQuery("body").css("overflow", "auto")
    }));
    var l = jQuery(".guide-playlist-tab");
    if (l.length) {
        var c = jQuery(".guide-playlist-tab > .active").offset().left - 30;
        l.scrollLeft(c)
    }
    var s = "https://www.ledgerwallet.com",
        u = p("ledger.affiliate_uuid"),
        d = p("ledger.affiliate_tracker"),
        f = window.location.href.slice(window.location.href.indexOf("?") + 1).split("&"),
        y = {};
    for (t = 0; t < f.length; t++) {
        var h = f[t].split("=");
        y[h[0]] = h[1]
    }
    var v = y.r,
        j = y.tracker;
    if (null != v && (null == u || u != v || d != j)) {
        u = v, d = j;
        var Q = document.referrer;
        document.cookie = "ledger.affiliate_uuid=" + u + ";path=/;domain=" + ".ledger.com;", document.cookie = "ledger.affiliate_tracker=" + d + ";path=/;domain=" + ".ledger.com;", document.cookie = "ledger.referrer=" + Q + ";path=/;domain=" + ".ledger.com;",
            function(e, t) {
                jQuery.ajax({
                    type: "POST",
                    url: s + "/api/shopify/affiliate_hit",
                    data: {
                        affiliate_uuid: e,
                        referrer: t
                    },
                    success: function() {},
                    fail: function() {}
                })
            }(u, Q)
    }

    function p(e) {
        for (var t = e + "=", i = decodeURIComponent(document.cookie).split(";"), r = 0; r < i.length; r++) {
            for (var o = i[r];
                " " == o.charAt(0);) o = o.substring(1);
            if (0 == o.indexOf(t)) return o.substring(t.length, o.length)
        }
        return null
    }
    if (jQuery("body").click((function() {
            jQuery("html").removeClass(), jQuery("body").css("overflow-y", "visible"), jQuery(".fb_digioh-overlay, .fb_lightbox-overlay, .fb_lightbox-overlay-fixed, .preloaded_lightbox, .preloaded_lightbox iframe").hide()
        })), document.addEventListener("DOMContentLoaded", (function() {
            var e;
            if ("IntersectionObserver" in window) {
                e = document.querySelectorAll(".lazy");
                for (var t = new IntersectionObserver((function(e, i) {
                        for (var r = 0, o = e.length; r < o; r++)
                            if (e[r].isIntersecting) {
                                var n = e[r].target;
                                n.src = n.dataset.src, n.classList.remove("lazy"), t.unobserve(n)
                            }
                    })), i = 0, r = e.length; i < r; i++) t.observe(e[i])
            } else {
                var o, n = function() {
                    o && clearTimeout(o), o = setTimeout((function() {
                        var t = jQuery(window).scrollTop();
                        e.each((function() {
                            var i = jQuery(this);
                            if (i.offset().top < window.innerHeight + t + 500) {
                                var r = i.attr("data-src");
                                i.attr("src", r), i.removeClass("lazy"), e = jQuery(".lazy")
                            }
                        })), 0 == e.length && (jQuery(document).off("scroll"), jQuery(window).off("resize"))
                    }), 20)
                };
                e = jQuery(".lazy"), jQuery(document).on("scroll", n), jQuery(window).on("resize", n)
            }
        })), document.addEventListener("DOMContentLoaded", (function(e) {
            new Swiper(".testimonial-swiper", {
                slidesPerView: "auto",
                centeredSlides: !0,
                spaceBetween: 25,
                navigation: {
                    nextEl: ".swiper-button-next",
                    prevEl: ".swiper-button-prev"
                },
                pagination: {
                    el: ".swiper-pagination",
                    clickable: !0
                }
            });
            jQuery(window).on("scroll", (function() {
                var e = jQuery(".fadin-blocks");
                if (e.length > 0) {
                    jQuery(".fadin-blocks").offset().top;
                    var t = jQuery(window).scrollTop();
                    jQuery(e).each((function() {
                        jQuery(this).offset().top - 460 < t && (jQuery(this).css("transform", "translate(0,0)"), jQuery(this).css("opacity", "1"))
                    }))
                }
            })), jQuery(".open-pop-modal").each((function(e) {
                jQuery(this).on("click", (function() {
                    var e = jQuery(this).data("modal");
                    jQuery(".pop-modal#" + e).addClass("active")
                }))
            })), jQuery(".close-pop-modal").on("click", (function() {
                var e = jQuery(this).parent().attr("id"),
                    t = jQuery("#" + e + " iframe").attr("src");
                jQuery("#" + e + " iframe").attr("src", t), jQuery("#" + e).removeClass("active").removeAttr("style")
            }));
            var t = 52;
            jQuery(window).scroll((function(e) {
                jQuery(window).width() <= 992 && (t = 35), jQuery(".scroll-fixed-content .item").removeClass("active");
                var i, r = window.innerHeight,
                    o = jQuery(e.target).scrollTop(),
                    n = Math.round(o + r * t / 100);
                jQuery(".scroll-fixed-content .item").each((function(e, t) {
                    var r = jQuery(t);
                    r.offset().top < n && (i = r)
                })), i || (i = jQuery(".scroll-fixed-content .item:eq(0)")), idElement = i.data("id"), jQuery(".scroll-fixed-content .item[data-id=" + idElement + "]").addClass("active")
            }))
        })), jQuery("#main").hasClass("changing-header")) {
        jQuery("#header").offset().top;
        var g = jQuery("#hero").outerHeight();
        jQuery(window).scroll((function(e) {
            jQuery(this).scrollTop() >= g ? jQuery("#header").fadeIn(40).addClass("out-of-top") : jQuery("#header").removeClass("out-of-top")
        }))
    }
    jQuery(document).ready((function() {
        function e(e) {
            window.location.href = e
        }
        jQuery(".all-clickable").each((function() {
            var t = jQuery(this).find("a:first-of-type").attr("href");
            jQuery(this).on("click", (function() {
                var i = jQuery(this).find("input"),
                    r = jQuery(this).find(".no-all-clickable");
                "undefined" != typeof inputOfCar ? jQuery(event.target).closest(i).length || e(t) : void 0 !== r && jQuery(event.target).closest(r).length || e(t)
            }))
        })), 0 !== jQuery("#download-button").length && jQuery(".download-button").click((function() {
            jQuery(this).toggleClass("is-open"), jQuery(this).siblings(".list-app").toggleClass("is-hidden").fadeIn(100)
        })), winWidth = jQuery(window).width(), 0 !== jQuery("#on-click-block").length && winWidth >= 768 && (activeIllustration = jQuery("#on-click-block .swiper-container").find(".active").find("img").attr("src"), jQuery("#on-click-block-illustration").html('<img src="' + activeIllustration + '" alt="">'), jQuery("#on-click-block .swiper-container .swiper-slide").click((function() {
            jQuery("#on-click-block .swiper-container .swiper-slide").removeClass("active"), jQuery(this).addClass("active"), activeIllustration = jQuery("#on-click-block .swiper-container").find(".active").find("img").attr("src"), console.log(activeIllustration), jQuery("#on-click-block-illustration img").attr("src", activeIllustration)
        }))), jQuery(window).scroll((function(e) {
            winWidth = jQuery(window).width();
            var t = jQuery("#header").outerHeight(),
                i = jQuery(this).scrollTop();
            jQuery("#top-of-the-pop") && winWidth > 860 && (i >= t ? jQuery("#top-of-the-pop").fadeIn(40) : jQuery("#top-of-the-pop").fadeOut(40))
        }))
    }))
})();