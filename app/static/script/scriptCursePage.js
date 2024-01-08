document.getElementById('toggleButton').addEventListener('click', function () {
    var topic = document.querySelector('.topic');
    var button = document.getElementById('toggleButton');
    topic.classList.toggle('hidden');
    button.classList.toggle('hidden');
});

// Предположим, что у вас есть следующий объект данных с сервера
let data = {
    courseTitle: "Курс по Web-программированию для начинающих ",
    courseDescription: "Прекрасный текст с описанием курса да да я сама креативность",
    modules: [
        {
            moduleName: "Название модуля",
            lessons: ["Урок 1", "Урок 2", "Урок 3"]
        },
        {
            moduleName: "Название модуля",
            lessons: ["Урок 1", "Урок 2", "Урок 3", "Урок 3", "Урок 3", "Урок 3", "Урок 3", "Урок 3"]
        },
        {
            moduleName: "Название модуля",
            lessons: ["Урок 1", "Урок 2", "Урок 3"]
        },
        {
            moduleName: "Название модуля",
            lessons: ["Урок 1", "Урок 2", "Урок 3"]
        },
        {
            moduleName: "Название модуля",
            lessons: ["Урок 1", "Урок 2", "Урок 3"]
        },
        {
            moduleName: "Название модуля",
            lessons: ["Урок 1", "Урок 2", "Урок 3"]
        },
        {
            moduleName: "Название модуля",
            lessons: ["Урок 1", "Урок 2", "Урок 3"]
        },
        {
            moduleName: "Название модуля",
            lessons: ["Урок 1", "Урок 2", "Урок 3"]
        },
        {
            moduleName: "Название модуля",
            lessons: ["Урок 1", "Урок 2", "Урок 3"]
        },
    ]


};

// Вставляем название курса и его описание в блок класса 'content'
let content = document.querySelector('.content');
content.querySelector('h1').textContent = data.courseTitle;
content.querySelector('p').textContent = data.courseDescription;

// Вставляем модули и уроки в блок класса 'container'
let container = document.querySelector('.container');

// Очищаем контейнер
container.innerHTML = '';

data.modules.forEach(module => {
    // Создаем новый элемент 'container-item'
    let containerItem = document.createElement('div');
    containerItem.className = 'container-item';

    // Добавляем название модуля
    let h3 = document.createElement('h3');
    h3.textContent = module.moduleName;
    containerItem.appendChild(h3);

    // Добавляем уроки
    module.lessons.forEach(lesson => {
        let lessonBox = document.createElement('a');
        lessonBox.className = 'lesson-box';
        lessonBox.textContent = lesson;
        lessonBox.href="course_menu.html"
        containerItem.appendChild(lessonBox);
    });

    // Добавляем 'container-item' в 'container'
    container.appendChild(containerItem);
});
