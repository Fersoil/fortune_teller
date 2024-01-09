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
