// main.js
document.addEventListener('DOMContentLoaded', () => {
    const consentBanner = document.getElementById('cookieConsentBanner');
    const acceptCookies = document.getElementById('acceptCookies');

    // Show banner if no consent cookie found
    if (!document.cookie.split('; ').find(row => row.startsWith('cookie_consent='))) {
        consentBanner.style.display = 'block';
    }

    // Set a cookie on acceptance and hide the banner
    acceptCookies.addEventListener('click', () => {
        document.cookie = "cookie_consent=accepted; path=/; max-age=31536000"; // Expires after 1 year
        consentBanner.style.display = 'none';
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.querySelector('.navbar-toggle');
    const menu = document.querySelector('.navbar-menu');

    toggle.addEventListener('click', function () {
        menu.style.display = menu.style.display === 'none' ? 'flex' : 'none';
    });

    window.addEventListener('resize', function () {
        if (window.innerWidth > 768) {
            menu.style.display = 'inline';
        } 
    });
});

function validatePassword() {
    var password = document.getElementById("id_password1").value;
    var message = "";

    if (password.length < 8) {
        message = "Password must be at least 8 characters";
    } else if (!password.match(/\d/)) {
        message = "Password must contain a number";
    } 

    document.getElementById("passwordMessage").innerText = message;
}


document.getElementById("id_password1").addEventListener("keyup", validatePassword);
