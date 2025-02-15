(() => {
    var e = jQuery(".item:first").height() / 3 * 2;
    jQuery(window).resize((function() {
        e = jQuery(".item:first").height() / 3 * 2
    }));
    var r = jQuery(".item"),
        i = jQuery(r.get().reverse()),
        a = jQuery(".fixed-area > div");
    firstImgPreview = jQuery(".scroll-fixed-zone .item:first").data("img"), a.css("background-image", "url(" + firstImgPreview + ")").addClass("fadeIn"), jQuery(".scroll-fixed-zone .fixed-area-text").scroll((function(t) {
        var s = jQuery(t.target).scrollTop();
        i.each((function() {
            var i = jQuery(this);
            return i.position().top + s > e + s || (i.hasClass("active") || (r.filter(".active").removeClass("active"), i.addClass("active"), a.css("background-image", "url(" + i.data("img") + ")")), !1)
        }))
    })), navigator.userAgent.match(/iPad|iPhone/) && jQuery(".cover").addClass("for-ios")
})();