const inputLike = document.getElementById('input-like');
const log = document.getElementById('log');

inputLike.addEventListener('change', calculateVipLikeOnLikeChange);

function calculateVipLikeOnLikeChange(e) {
    console.log (e.target.value)
    log.textContent = e.target.value * 32;
}