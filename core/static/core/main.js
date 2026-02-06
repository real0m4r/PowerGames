document.addEventListener('DOMContentLoaded', function () {
    const blackout = document.querySelector('#blackout');
    const blackoutBtn = document.querySelector('#show-blackout');

    if (blackout) {
        blackout.style.display = 'none';
    }

    if (blackout && blackoutBtn) {
        blackoutBtn.addEventListener('click', function () {
            blackout.style.display = 'block';
        });
    }
});
