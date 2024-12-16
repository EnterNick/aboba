const modal = document.querySelector('.products__filters')
const btn = document.querySelector('.form__btn')
const closeBtn = document.querySelector('.products__filters-close')
const body = document.querySelector('body')

modal.style.display = 'none'

btn.onclick = function () {
    modal.style.display = 'flex'
    body.style.overflow = 'hidden'
}

closeBtn.onclick = function () {
    modal.style.display = 'none'
    body.style.overflow = 'scroll'
}