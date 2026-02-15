document.addEventListener('DOMContentLoaded', function () {
    const blackout = document.querySelector('#blackout');
    const showBtn = document.querySelector('#show-blackout');
    const hideBtn = document.querySelector('#hide-blackout');

    if (!blackout || !showBtn || !hideBtn) return;

    // Initial state
    blackout.style.display = 'none';
    hideBtn.style.display = 'none';

    showBtn.addEventListener('click', () => {
        blackout.style.display = 'block';
        hideBtn.style.display = 'block';
    });

    hideBtn.addEventListener('click', () => {
        blackout.style.display = 'none';
        hideBtn.style.display = 'block';
    });
});
