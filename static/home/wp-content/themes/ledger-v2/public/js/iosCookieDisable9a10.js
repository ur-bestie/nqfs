(() => {
    function t(t, n) {
        return function(t) {
            if (Array.isArray(t)) return t
        }(t) || function(t, r) {
            var n = null == t ? null : "undefined" != typeof Symbol && t[Symbol.iterator] || t["@@iterator"];
            if (null == n) return;
            var e, o, a = [],
                l = !0,
                i = !1;
            try {
                for (n = n.call(t); !(l = (e = n.next()).done) && (a.push(e.value), !r || a.length !== r); l = !0);
            } catch (t) {
                i = !0, o = t
            } finally {
                try {
                    l || null == n.return || n.return()
                } finally {
                    if (i) throw o
                }
            }
            return a
        }(t, n) || function(t, n) {
            if (!t) return;
            if ("string" == typeof t) return r(t, n);
            var e = Object.prototype.toString.call(t).slice(8, -1);
            "Object" === e && t.constructor && (e = t.constructor.name);
            if ("Map" === e || "Set" === e) return Array.from(t);
            if ("Arguments" === e || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)) return r(t, n)
        }(t, n) || function() {
            throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
        }()
    }

    function r(t, r) {
        (null == r || r > t.length) && (r = t.length);
        for (var n = 0, e = new Array(r); n < r; n++) e[n] = t[n];
        return e
    }
    var n, e, o, a, l, i;
    o = "apptracking", a = window.location.search, l = new URLSearchParams(a).get(o), n = o, e = {}, new Date, document.cookie.split(";").forEach((function(r) {
        var n = t(r.split("="), 2),
            o = n[0],
            a = n[1];
        e[o.trim()] = a
    })), i = e[n], null !== l && (document.cookie = "".concat(o, "=").concat(l, "; path=/;")), "false" !== l && "false" !== i || document.head.insertAdjacentHTML("beforeend", "<style>#onetrust-consent-sdk{display:none;}</style>")
})();