/*! For license information please see language.js.LICENSE.txt */
(() => {
    "use strict";

    function e(e) {
        for (var t = 1; t < arguments.length; t++) {
            var n = arguments[t];
            for (var r in n) e[r] = n[r]
        }
        return e
    }
    var t = function t(n, r) {
        function o(t, o, i) {
            if ("undefined" != typeof document) {
                "number" == typeof(i = e({}, r, i)).expires && (i.expires = new Date(Date.now() + 864e5 * i.expires)), i.expires && (i.expires = i.expires.toUTCString()), t = encodeURIComponent(t).replace(/%(2[346B]|5E|60|7C)/g, decodeURIComponent).replace(/[()]/g, escape);
                var c = "";
                for (var a in i) i[a] && (c += "; " + a, !0 !== i[a] && (c += "=" + i[a].split(";")[0]));
                return document.cookie = t + "=" + n.write(o, t) + c
            }
        }
        return Object.create({
            set: o,
            get: function(e) {
                if ("undefined" != typeof document && (!arguments.length || e)) {
                    for (var t = document.cookie ? document.cookie.split("; ") : [], r = {}, o = 0; o < t.length; o++) {
                        var i = t[o].split("="),
                            c = i.slice(1).join("=");
                        try {
                            var a = decodeURIComponent(i[0]);
                            if (r[a] = n.read(c, a), e === a) break
                        } catch (e) {}
                    }
                    return e ? r[e] : r
                }
            },
            remove: function(t, n) {
                o(t, "", e({}, n, {
                    expires: -1
                }))
            },
            withAttributes: function(n) {
                return t(this.converter, e({}, this.attributes, n))
            },
            withConverter: function(n) {
                return t(e({}, this.converter, n), this.attributes)
            }
        }, {
            attributes: {
                value: Object.freeze(r)
            },
            converter: {
                value: Object.freeze(n)
            }
        })
    }({
        read: function(e) {
            return '"' === e[0] && (e = e.slice(1, -1)), e.replace(/(%[\dA-F]{2})+/gi, decodeURIComponent)
        },
        write: function(e) {
            return encodeURIComponent(e).replace(/%(2[346BF]|3[AC-F]|40|5[BDE]|60|7[BCD])/g, decodeURIComponent)
        }
    }, {
        path: "/"
    });
    const n = t;

    function r(e, t) {
        var n = "undefined" != typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
        if (!n) {
            if (Array.isArray(e) || (n = function(e, t) {
                    if (!e) return;
                    if ("string" == typeof e) return o(e, t);
                    var n = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === n && e.constructor && (n = e.constructor.name);
                    if ("Map" === n || "Set" === n) return Array.from(e);
                    if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return o(e, t)
                }(e)) || t && e && "number" == typeof e.length) {
                n && (e = n);
                var r = 0,
                    i = function() {};
                return {
                    s: i,
                    n: function() {
                        return r >= e.length ? {
                            done: !0
                        } : {
                            done: !1,
                            value: e[r++]
                        }
                    },
                    e: function(e) {
                        throw e
                    },
                    f: i
                }
            }
            throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
        }
        var c, a = !0,
            u = !1;
        return {
            s: function() {
                n = n.call(e)
            },
            n: function() {
                var e = n.next();
                return a = e.done, e
            },
            e: function(e) {
                u = !0, c = e
            },
            f: function() {
                try {
                    a || null == n.return || n.return()
                } finally {
                    if (u) throw c
                }
            }
        }
    }

    function o(e, t) {
        (null == t || t > e.length) && (t = e.length);
        for (var n = 0, r = new Array(t); n < t; n++) r[n] = e[n];
        return r
    }

    function i(e, t) {
        var n = Object.keys(e);
        if (Object.getOwnPropertySymbols) {
            var r = Object.getOwnPropertySymbols(e);
            t && (r = r.filter((function(t) {
                return Object.getOwnPropertyDescriptor(e, t).enumerable
            }))), n.push.apply(n, r)
        }
        return n
    }

    function c(e) {
        for (var t = 1; t < arguments.length; t++) {
            var n = null != arguments[t] ? arguments[t] : {};
            t % 2 ? i(Object(n), !0).forEach((function(t) {
                a(e, t, n[t])
            })) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n)) : i(Object(n)).forEach((function(t) {
                Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(n, t))
            }))
        }
        return e
    }

    function a(e, t, n) {
        return t in e ? Object.defineProperty(e, t, {
            value: n,
            enumerable: !0,
            configurable: !0,
            writable: !0
        }) : e[t] = n, e
    }
    var u = "userLanguage",
        d = {};
    document.location.hostname.endsWith(".ledger.com") && (d.domain = ".ledger.com");
    var l = function() {
            return n.get(u) || navigator.language.slice(0, 2) || ""
        },
        s = function(e) {
            n.set(u, e, c(c({}, d), {}, {
                expires: 365
            }))
        };
    window.addEventListener("load", (function() {
        var e, t = [document.querySelector("#language-popup"), document.querySelector("#language-popup-no"), document.querySelector("#language-popup-set-default"), document.querySelector(".activeLanguage"), document.querySelectorAll(".localeItem"), document.querySelector("#user-language"), document.querySelector("#language-popup-close")],
            o = t[0],
            i = t[1],
            c = t[2],
            a = t[3],
            u = t[4],
            d = t[5],
            f = t[6],
            p = [],
            g = r(u);
        try {
            var v = function() {
                var t = e.value;
                p.find((function(e) {
                    return e.isoCode === t.getAttribute("data-isocode")
                })) || p.push({
                    isoCode: t.getAttribute("data-isocode"),
                    name: t.getAttribute("data-name"),
                    url: t.getAttribute("href")
                })
            };
            for (g.s(); !(e = g.n()).done;) v()
        } catch (e) {
            g.e(e)
        } finally {
            g.f()
        }
        var m, b = r(u);
        try {
            for (b.s(); !(m = b.n()).done;) {
                m.value.addEventListener("click", (function(e) {
                    e.preventDefault(), s(e.target.getAttribute("data-isocode")), window.location.href = e.target.getAttribute("href")
                }))
            }
        } catch (e) {
            b.e(e)
        } finally {
            b.f()
        }
        var y = a.getAttribute("data-isocode"),
            h = l();
        h !== y && p.some((function(e) {
            return e.isoCode === h
        })) && !n.get("userLanguage") && (d.textContent = p.find((function(e) {
            return e.isoCode === h
        })).name, o.classList.remove("is-hidden"), i.addEventListener("click", (function() {
            s(y), o.classList.add("is-hidden")
        })), f.addEventListener("click", (function() {
            s(y), o.classList.add("is-hidden")
        })), c.addEventListener("click", (function() {
            o.classList.add("is-hidden"), window.location.href = p.find((function(e) {
                return e.isoCode === h
            })).url
        })))
    }))
})();