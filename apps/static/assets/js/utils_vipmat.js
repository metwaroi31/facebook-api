const inputLike = document.getElementById('input-like');
const inputTime = document.getElementById('input-time');

const log = document.getElementById('log');

inputLike.addEventListener('change', calculateVipLikeOnLikeChange);
inputTime.addEventListener('change', calculateVipLikeOnTimeChange);
function calculateVipLikeOnLikeChange(e) {
    log.textContent = e.target.value * inputTime.value * 1200;
}

function calculateVipLikeOnTimeChange(e) {
    log.textContent = e.target.value * inputLike.value * 1200;
}