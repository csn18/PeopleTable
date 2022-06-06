const sortNameButton = document.querySelector('.sort__name')
const sortAgeButton = document.querySelector('.sort__age')
const allSortButtons = document.querySelectorAll('.table__col-sort')
const searchNameField = document.querySelector('.search__name')
const searchAgeField = document.querySelector('.search__age')
let allSearchFields = document.querySelectorAll('.table__search-field')
const getDataButton = document.querySelector('.get__data')

getDataButton.addEventListener('click', (event) => {
    event.preventDefault()
    axios.get(`${document.URL}get/data`).then((response) => {
        if (response.data.status === 'ok') {
            axios.get(`${document.URL}get/peoples`).then((response) => {
                updateDateTable(response.data)
            })
        }
    })
})

const updateDateTable = (data) => {
    let tableItems = document.querySelector('.table__items')
    let allTableItems = document.querySelectorAll('.table__item')

    // Удаление всех старых элементов таблицы
    if (allTableItems) {
        allTableItems.forEach(item => {
            item.classList.add('animate__animated')
            item.classList.add('animate__faster')
        })
        allTableItems.forEach(item => {
            item.classList.add('animate__fadeOut')
        })
        setTimeout(() => {
            allTableItems.forEach(item => item.remove())
            data.forEach(item => {
                // Создание элемента таблицы и добавление классов
                let newTabItem = document.createElement('div')
                newTabItem.classList.add('table__item')
                newTabItem.classList.add('table__grid')
                newTabItem.classList.add('animate__animated')
                newTabItem.classList.add('animate__fadeIn')
                newTabItem.classList.add('animate__faster')

                // Создание ячеек в элементе таблицы, добавление классов и текста
                let newSpanName = document.createElement('span')
                let newSpanAge = document.createElement('span')
                let newSpanGroup = document.createElement('span')

                newSpanName.classList.add('table__item-content')
                newSpanName.classList.add('table__item-name')
                newSpanAge.classList.add('table__item-content')
                newSpanAge.classList.add('table__item-age')
                newSpanGroup.classList.add('table__item-content')
                newSpanGroup.classList.add('table__item-group')

                newSpanName.innerText = item.name
                newSpanAge.innerText = item.age
                newSpanGroup.innerText = item.group

                // Добавление ячеек в элемент таблицы
                newTabItem.appendChild(newSpanName)
                newTabItem.appendChild(newSpanAge)
                newTabItem.appendChild(newSpanGroup)

                // Добавление элемента таблицы на экран
                tableItems.appendChild(newTabItem)
            })
        }, 500)
    }
}

sortNameButton.addEventListener('click', () => {
    if (sortNameButton.classList.contains('active')) {
        sortNameButton.classList.remove('active')
    } else {
        allSortButtons.forEach(item => item.classList.remove('active'))
        allSearchFields = document.querySelectorAll('.table__search-field')
        allSearchFields.forEach(item => item.value = '')
        sortNameButton.classList.add('active')
        axios.get(`${document.URL}filter/name`).then((response) => {
            updateDateTable(response.data)
        })
    }
})

sortAgeButton.addEventListener('click', () => {
    if (sortAgeButton.classList.contains('active')) {
        sortAgeButton.classList.remove('active')
    } else {
        allSortButtons.forEach(item => item.classList.remove('active'))
        allSearchFields = document.querySelectorAll('.table__search-field')
        allSearchFields.forEach(item => item.value = '')
        sortAgeButton.classList.add('active')
        axios.get(`${document.URL}filter/age`).then((response) => {
            updateDateTable(response.data)
        })
    }
})

searchNameField.addEventListener('input', () => {
    let data = new FormData()
    data.append('name', searchNameField.value)

    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    axios.post(`${document.URL}search/name`, data).then((response) => {
        updateDateTable(response.data)
    })
})


searchAgeField.addEventListener('input', () => {
    let data = new FormData()
    data.append('age', searchAgeField.value)

    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    axios.post(`${document.URL}search/age`, data).then((response) => {
        updateDateTable(response.data)
    })
})