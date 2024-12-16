const prices = Array.from(document.querySelectorAll('.cart__item-price-value'))
const total = document.querySelector('.cart__total-value')
const values = Array.from(document.querySelectorAll('.cart__item-val-value'))

let sum = 0

for (i = 0; i < prices.length; i++) {
    sum += +prices[i].textContent * +values[i].textContent
}

total.textContent = sum + ' руб.'
