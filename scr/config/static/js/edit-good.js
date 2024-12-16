const price = document.querySelector('#price')
const prePrice = document.querySelector('.product-page__price-value')
const prePrices = document.querySelector('.products__product__price-value')

const description = document.querySelector('#description')
const preDesc = document.querySelector('.product-page__details_description')
const preDescs = document.querySelector('.products__product__description')

const title = document.querySelector('#title')
const preTitle = document.querySelector('.product-page__title')
const preTitles = document.querySelector('.products__product__title')

const quanity = document.querySelector('#value')
const preQuanity = document.querySelector('.product-page__quantity-value')
const preQuanity_second = document.querySelector('.products__product__quanity-value')

const category = document.querySelector('#category')
const preCategory = document.querySelector('.product-page__category-value')
const preCategories = document.querySelector('.products__product__category-value')

const preImage = document.querySelector('.product-page__image-img')
const preImages = document.querySelector('.products__product__image')

price.addEventListener('change', function () {
        prePrice.textContent = price.value + ' руб.'
        prePrices.textContent = price.value + ' руб.'
    }
)
title.addEventListener('change', function () {
        preTitle.textContent = title.value
        preTitles.textContent = title.value
    }
)
description.addEventListener('change', function () {
        preDesc.textContent = description.value
        preDescs.textContent = description.value
    }
)
quanity.addEventListener('change', function () {
        preQuanity.textContent = quanity.value
        preQuanity_second.textContent = quanity.value
    }
)
category.addEventListener('change', function () {
        preCategory.textContent = category.value
        preCategories.textContent = category.value
    }
)

function imagePreview () {
    const image = document.querySelector("#image").files[0];
    const reader = new FileReader();

    reader.addEventListener(
        'load',
        function () {
            preImage.src = reader.result;
            preImages.src = reader.result;
        }
    )
    if (image) {
        reader.readAsDataURL(image);
    }
}

prePrice.textContent = price.value + ' руб.'
prePrices.textContent = price.value + ' руб.'
preTitle.textContent = title.value
preTitles.textContent = title.value
preDesc.textContent = description.value
preDescs.textContent = description.value
preQuanity.textContent = quanity.value
preQuanity_second.textContent = quanity.value
preCategory.textContent = category.value
preCategories.textContent = category.value


const modal = document.querySelector('.modal')
const modalBtn = document.querySelector('#modal-delete-btn')
const modalBtnClose = document.querySelector('#modal-delete-btn-close')
const body = document.querySelector('body')

modal.style.display = 'none'

modalBtn.onclick = function () {
    modal.style.display = 'flex'
    body.style.overflow = 'hidden'
}

modalBtnClose.onclick = function () {
    modal.style.display = 'none'
    body.style.overflow = 'scroll'
}