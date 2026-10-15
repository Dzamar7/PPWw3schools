import re
import os

with open("original_howto.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Original length:", len(html))

# 1. Remove FastCMP and GTM scripts
# FastCMP
html = re.sub(r'<script[^>]*>\s*window\.FAST_CMP_OPTIONS.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<script[^>]*src=[\'"][^\'"]*fastcmp\.com[^\'"]*[\'"][^>]*>\s*</script>', '', html, flags=re.DOTALL)
# GTM
html = re.sub(r'<script[^>]*>\s*\(function\(w,d,s,l,i\)\{w\[l\]=w\[l\]\|\|\[\].*?googletagmanager\.com/gtm\.js.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<noscript><iframe src="https://www\.googletagmanager\.com/ns\.html[^"]*".*?</iframe></noscript>', '', html, flags=re.DOTALL)

# 2. Fix the logo in navbar and footer
# Official W3Schools SVG logo
svg_logo_green = '''<svg viewBox="0 0 54 50.8" style="width: 38px; height: 36px; vertical-align: middle; margin-right: 2px;" xmlns="http://www.w3.org/2000/svg">
  <defs><clipPath id="clip0"><rect width="37.2768" height="35" fill="white"/></clipPath></defs>
  <g clip-path="url(#clip0)" transform="matrix(1.451231, 0, 0, 1.451231, -0.05385, -2.645e-9)">
    <path d="M31.3987 7.36607C31.3987 7.36607 32.3362 8.37054 33.6458 8.37054C34.68 8.37054 35.4315 7.74554 35.4315 6.88988C35.4315 5.84077 34.4716 5.35714 33.4375 5.35714C32.186 5.35714 31.3323 6.00298 30.6033 6.9494C29.6238 8.22024 28.5609 9.87202 27.5189 11.6935C26.1747 14.0387 25.0494 16.494 24.1116 18.8244C23.5073 16.2917 22.4237 13.5923 21.0898 10.9851C19.7978 8.45536 18.2557 6.16667 16.5052 4.33631C14.8797 2.63393 12.8792 1.34524 10.6078 0.610119C8.33634 -0.125 5.81486 -0.160714 3.48089 0.446429C2.43891 0.717262 1.43862 1.14583 0.54254 1.70833L0 2.0506L1.50043 4.41369L2.04297 4.07143C2.689 3.66369 3.41838 3.35417 4.18944 3.15476C5.91909 2.70536 7.78426 2.73214 9.47225 3.27976C11.1602 3.82738 12.6502 4.79167 13.8693 6.06845C15.2447 7.5119 16.4533 9.30952 17.4745 11.3125C18.6623 13.6399 19.6418 16.1429 20.2045 18.5208C19.1417 20.9167 17.6829 23.5655 16.0884 26.2411C14.838 28.3363 13.4627 30.3423 12.0664 32.2232C11.8372 32.5327 11.5871 32.8125 11.337 33.1071L10.9828 33.5208L14.7755 35L15.0672 34.4643C15.5465 33.5833 16.1299 32.6101 16.7968 31.5714C18.6723 28.6488 20.9231 25.1399 22.8403 21.0625C24.0907 23.9405 25.6119 27.0655 27.5085 29.8988C29.4051 32.7321 31.7807 35.3214 34.6983 35.3214C35.5944 35.3214 36.4696 34.9643 36.9698 34.3393C37.3449 33.872 37.4907 33.3006 37.4491 32.7292C37.3866 31.9077 36.9281 31.2292 36.2612 30.7292C35.2193 29.9435 33.8439 29.6935 32.6561 30.0149C32.0934 30.1696 31.6141 30.4554 31.2807 30.8661C30.989 30.5804 30.6972 30.2768 30.4055 29.9554C28.7175 28.0982 27.2796 25.7768 26.1126 23.2381C25.4249 21.7381 24.8414 20.2024 24.3413 18.6667C25.3207 16.631 26.4669 14.4792 27.7589 12.3839C28.8425 10.6339 29.9887 8.95536 31.1486 7.52679L31.3987 7.36607Z" fill="#04AA6D"/>
  </g>
</svg>'''

svg_logo_footer = '''<svg viewBox="0 0 54 50.8" style="width: 48px; height: 45px; vertical-align: middle;" xmlns="http://www.w3.org/2000/svg">
  <defs><clipPath id="clip0f"><rect width="37.2768" height="35" fill="white"/></clipPath></defs>
  <g clip-path="url(#clip0f)" transform="matrix(1.451231, 0, 0, 1.451231, -0.05385, -2.645e-9)">
    <path d="M31.3987 7.36607C31.3987 7.36607 32.3362 8.37054 33.6458 8.37054C34.68 8.37054 35.4315 7.74554 35.4315 6.88988C35.4315 5.84077 34.4716 5.35714 33.4375 5.35714C32.186 5.35714 31.3323 6.00298 30.6033 6.9494C29.6238 8.22024 28.5609 9.87202 27.5189 11.6935C26.1747 14.0387 25.0494 16.494 24.1116 18.8244C23.5073 16.2917 22.4237 13.5923 21.0898 10.9851C19.7978 8.45536 18.2557 6.16667 16.5052 4.33631C14.8797 2.63393 12.8792 1.34524 10.6078 0.610119C8.33634 -0.125 5.81486 -0.160714 3.48089 0.446429C2.43891 0.717262 1.43862 1.14583 0.54254 1.70833L0 2.0506L1.50043 4.41369L2.04297 4.07143C2.689 3.66369 3.41838 3.35417 4.18944 3.15476C5.91909 2.70536 7.78426 2.73214 9.47225 3.27976C11.1602 3.82738 12.6502 4.79167 13.8693 6.06845C15.2447 7.5119 16.4533 9.30952 17.4745 11.3125C18.6623 13.6399 19.6418 16.1429 20.2045 18.5208C19.1417 20.9167 17.6829 23.5655 16.0884 26.2411C14.838 28.3363 13.4627 30.3423 12.0664 32.2232C11.8372 32.5327 11.5871 32.8125 11.337 33.1071L10.9828 33.5208L14.7755 35L15.0672 34.4643C15.5465 33.5833 16.1299 32.6101 16.7968 31.5714C18.6723 28.6488 20.9231 25.1399 22.8403 21.0625C24.0907 23.9405 25.6119 27.0655 27.5085 29.8988C29.4051 32.7321 31.7807 35.3214 34.6983 35.3214C35.5944 35.3214 36.4696 34.9643 36.9698 34.3393C37.3449 33.872 37.4907 33.3006 37.4491 32.7292C37.3866 31.9077 36.9281 31.2292 36.2612 30.7292C35.2193 29.9435 33.8439 29.6935 32.6561 30.0149C32.0934 30.1696 31.6141 30.4554 31.2807 30.8661C30.989 30.5804 30.6972 30.2768 30.4055 29.9554C28.7175 28.0982 27.2796 25.7768 26.1126 23.2381C25.4249 21.7381 24.8414 20.2024 24.3413 18.6667C25.3207 16.631 26.4669 14.4792 27.7589 12.3839C28.8425 10.6339 29.9887 8.95536 31.1486 7.52679L31.3987 7.36607Z" fill="#04AA6D"/>
  </g>
</svg>'''

# Replace top navbar logo:
html = re.sub(
    r'<i\s+class="fa fa-logo ws-hover-text-green"[^>]*>.*?</i>',
    svg_logo_green,
    html,
    flags=re.DOTALL
)

# Replace footer logo:
html = re.sub(
    r'<i\s+class="fa fa-logo"[^>]*>.*?</i>',
    svg_logo_footer,
    html,
    flags=re.DOTALL
)

# 3. Fix footer social icons
# Replace &#59398; etc with real Font Awesome icons
html = html.replace('&#59398;', '<i class="fa fa-facebook-official" style="font-size:22px;"></i>')
html = html.replace('&#59399;', '<i class="fa fa-instagram" style="font-size:22px;"></i>')
html = html.replace('&#59400;', '<i class="fa fa-linkedin-square" style="font-size:22px;"></i>')
html = html.replace('&#59401;', '<i class="fa fa-youtube-play" style="font-size:22px;"></i>')
html = html.replace('&#59402;', '<i class="fa fa-comments" style="font-size:22px;"></i>')

# Also ensure FontAwesome 4.7 is linked in head
if "font-awesome/4.7.0" not in html:
    html = html.replace(
        '</head>',
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n</head>'
    )

# 4. Make all image src attributes robust:
# If image is local (e.g. img_nature_wide.jpg), it works as img_nature_wide.jpg
# We also have <base href="https://www.w3schools.com/howto/"> or direct paths.
# Let's ensure <base href="https://www.w3schools.com/howto/"> is in head if not already
if '<base ' not in html:
    html = html.replace('<head>', '<head>\n<base href="https://www.w3schools.com/howto/">')

# 5. Fix init_pagination to ensure it works on localhost/index.html
pagination_js_fix = '''
<script>
// Robust Pagination Init for Page 1
function init_pagination() {
  var pagescount = 8, i, txt = "", able = " pagdisabled";
  var prevPage = "default.asp";
  var nextPage = "default_page2.asp";
  
  for (i = 1; i <= pagescount; i++) {
    var defPage = (i === 1) ? "default.asp" : ("default_page" + i + ".asp");
    if (i === 1) {
      txt += "<a class='howtopag_item" + able + "' href='" + prevPage + "'>&#10094;</a>";
    }
    var activeClass = (i === 1) ? " pagactive" : "";
    txt += "<a class='howtopag_item" + activeClass + "' href='" + defPage + "'>" + i + "</a>";
    if (i === pagescount) {
      txt += "<a class='howtopag_item' href='" + nextPage + "'>&#10095;</a>";
    }
  }
  var x = document.getElementsByClassName("howtopag");
  for (i = 0; i < x.length; i++) {
    x[i].innerHTML = txt;
  }
}
</script>
'''

html = html.replace('</head>', pagination_js_fix + '\n</head>')

# 6. Add topnav menu handlers and modal outside click handlers
extra_interactivity = '''
<script>
document.addEventListener("DOMContentLoaded", function() {
  // 1. Initialize pagination
  try { init_pagination(); } catch(e) { console.error(e); }

  // 2. Topnav menu toggles (Tutorials, References, Exercises, Certified, Services)
  var navButtons = document.querySelectorAll('[data-tnb-action="openNavItem"]');
  navButtons.forEach(function(btn) {
    btn.addEventListener("click", function(e) {
      e.preventDefault();
      var navId = btn.getAttribute("data-tnb-nav-id");
      var target = document.getElementById("nav_" + navId);
      if (!target) return;
      var isVisible = (target.style.display === "block");
      // Close all other dropdown navs
      document.querySelectorAll(".dropdown-nav").forEach(function(nav) {
        nav.style.display = "none";
      });
      target.style.display = isVisible ? "none" : "block";
    });
  });

  // Topnav close buttons
  var closeNavButtons = document.querySelectorAll('[data-tnb-action="closeNavItem"], [data-tnb-action="closeNavItemBackdrop"]');
  closeNavButtons.forEach(function(btn) {
    btn.addEventListener("click", function(e) {
      var navId = btn.getAttribute("data-tnb-nav-id");
      if (navId) {
        var target = document.getElementById("nav_" + navId);
        if (target) target.style.display = "none";
      } else {
        document.querySelectorAll(".dropdown-nav").forEach(function(nav) {
          nav.style.display = "none";
        });
      }
    });
  });

  // 3. Dark Theme toggle
  var themeToggles = document.querySelectorAll('[data-tnb-action="toggleUserPreferredTheme"]');
  themeToggles.forEach(function(toggle) {
    toggle.addEventListener("click", function(e) {
      document.body.classList.toggle("darktheme");
      document.body.classList.toggle("darkpagetheme");
    });
  });

  // 4. Modal outside click listener for all modals
  window.addEventListener("click", function(event) {
    // Login modal
    var loginModal = document.getElementById("loginModal");
    if (event.target === loginModal) {
      loginModal.style.display = "none";
    }
    // W3 Modal Box (id01)
    var modalBox = document.getElementById("id01");
    if (event.target === modalBox) {
      modalBox.style.display = "none";
    }
    // Modal Image (myModal2)
    var modalImg = document.getElementById("myModal2");
    if (event.target === modalImg) {
      modalImg.style.display = "none";
    }
    // Lightbox Modal
    var lightbox = document.getElementById("myModalLightbox");
    if (event.target === lightbox) {
      lightbox.style.display = "none";
    }
  });
});
</script>
'''

html = html.replace('</body>', extra_interactivity + '\n</body>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Generated new index.html! Length:", len(html))
