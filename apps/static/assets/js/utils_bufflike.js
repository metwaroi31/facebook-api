const inputLike = document.getElementById('input-like');
const inputType = document.getElementById('input-type');

const log = document.getElementById('log');

inputLike.addEventListener('change', calculateVipLikeOnLikeChange);
inputTime.addEventListener('change', calculateVipLikeOnTimeChange);
function calculateVipLikeOnLikeChange(e) {
    var valueType = inputType.value;
    console.log(valueType)
    if (valueType == 'like_v2') {
        log.textContent = e.target.value * 32;
    } else {
        log.textContent = e.target.value * 64;
    }
}

function calculateVipLikeOnTimeChange(e) {
    var valueType = e.target.value;
    if (valueType == 'like_v2') {
        log.textContent = inputLike.value * 32;
    } else {
        log.textContent = inputLike.value * 64;
    }
}