const price = document.querySelector('#price')
const prePrice = document.querySelector('.product-page__price-value')

const description = document.querySelector('#description')
const preDesc = document.querySelector('.product-page__details_description')

const title = document.querySelector('#title')
const preTitle = document.querySelector('.product-page__title')

const quanity = document.querySelector('#value')
const preQuanity = document.querySelector('.product-page__quantity-value')

const category = document.querySelector('#category')
const preCategory = document.querySelector('.product-page__category-value')

const preImage = document.querySelector('.product-page__image-img')

price.addEventListener('change', function () {
        prePrice.textContent = price.value + ' руб.'
    }
)
title.addEventListener('change', function () {
        preTitle.textContent = title.value
    }
)
description.addEventListener('change', function () {
        preDesc.textContent = description.value
    }
)
quanity.addEventListener('change', function () {
        preQuanity.textContent = quanity.value
    }
)
category.addEventListener('change', function () {
        preCategory.textContent = category.value
    }
)

function imagePreview () {
    const image = document.querySelector("#image").files[0];
    const reader = new FileReader();

    reader.addEventListener(
        'load',
        function () {
            preImage.src = reader.result;
        }
    )
    if (image) {
        reader.readAsDataURL(image);
    }
}

prePrice.textContent = price.value + ' руб.'
preTitle.textContent = title.value
preDesc.textContent = description.value
preQuanity.textContent = quanity.value
preCategory.textContent = category.value


const modal = document.querySelector('.modal')
const modalBtn = document.querySelector('#modal-delete-btn')
const modalBtnClose = document.querySelector('#modal-delete-btn-close')
const body = document.querySelector('body')

const preview = document.querySelector('.preview')

preview.addEventListener('click', function () {
    preview.classList.toggle('preview__activate-full')
})

preview.addEventListener('mouseover', function () {
    preview.classList.add('preview__activate')
})

preview.addEventListener('mouseout', function () {
    preview.classList.remove('preview__activate')
})
