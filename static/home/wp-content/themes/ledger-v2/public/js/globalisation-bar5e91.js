window.ledgerGlobalisationBar = function() {
    var e = {
            "": "English",
            fr: "French",
            de: "German",
            ru: "Russian",
            es: "Spanish",
            ar: "Arabic",
            "zh-hans": "Chinese",
            tr: "Turkish",
            ja: "Japanese",
            ko: "Korean",
            "pt-br": "Portuguese"
        },
        n = document.body.classList.contains("logged-in"),
        t = document.location.origin,
        a = document.location.pathname,
        o = a.split("/")[1],
        i = Object.keys(e).reduce((function(e, n) {
            return n === o ? n : e
        }), ""),
        r = document.querySelector('link[rel="shortlink"]'),
        c = !1;
    if (r) {
        var l = r.href;
        c = new URL(l).searchParams.get("p")
    }
    var d, s, u = '\n    <div class="row flexbox" id="languageBar" style="align-items: flex-start; '.concat(n ? "" : "background-color: orange", "\">\n      <div class=\"flexbox\">\n        <div>\n          <a id='submitEditDiv' style='display:none;margin-right: 2em;' href=\"").concat((d = t, s = c, s ? "".concat(d, "/wp-admin/post.php?post=").concat(s, "&action=edit") : ""), '" target="_blank" style=\'cursor:pointer\'>Edit the current page</a>\n        </div>\n        <div>\n          <select id=\'languageSelector\' style="width:150px;padding:0;border-radius:0; font-size: 13px;">\n            <option value="empty">Select a language</option>\n            ').concat(Object.keys(e).filter((function(e) {
            return e !== i
        })).map((function(n) {
            return '<option value="'.concat(n, '">').concat(e[n], "</option>")
        })).join(""), '\n          </select>\n        </div>\n        <div id="redirectLink" style="margin-left: 1em;">\n        </div>\n      </div>\n      <div class="flexbox"></div>\n    </div>\n  '),
        g = document.createElement("div");
    g.classList.add("bg", "bg-carbon"), g.style.paddingTop = "10px", g.style.paddingBottom = "10px", g.style.position = "sticky", g.style.top = 0, g.style.zIndex = 1e3, g.innerHTML = u;
    var p = document.getElementById("languageBar");
    p && p.parentElement.remove(), document.body.prepend(g), document.querySelector("#header").style.top = "45px", document.body.scrollTo(), c && (document.getElementById("submitEditDiv").style.display = "block");
    var m = document.querySelector("#redirectLink");
    document.querySelector("#languageSelector").addEventListener("change", (function(n) {
        var o = n.target.value,
            r = e[o];
        if (r) {
            var c = function(e) {
                    return "".concat(t).concat(e.length ? "/".concat(e) : "").concat(i.length ? a.slice(i.length + 1) : a)
                }(o),
                l = (new Date).getTime();
            m.innerHTML = '<a href="'.concat(c, "?").concat(l, '" target="_blank">View this page in ').concat(r, "</a>")
        } else m.innerHTML = ""
    }))
};