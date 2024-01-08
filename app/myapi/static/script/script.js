var data = [
  {
    title: "Курс по Web-программированию для начинающих",
    image: "image/curse_img.jpg",
    tests: "10",
    tasks: "20",
    skillPer: "49"
  }
];

let item = data[0];
for (let i = 0; i < 20; i++) {
  data.push(item);
}

async function GetCourse() {
    let dataCourse = [];
    const res = await fetch("http://127.0.0.1:8000/courses");
    const courseList = await res.json();

    // Use courseList directly, it's an array
    courseList.forEach((item) => {
        let course = {
            title: item.title,
            image: item.img,
            tests: item.number_of_tests,
            tasks: item.number_of_lessons,
            skillPer: (item.number_of_completed_tests / item.number_of_tests) * 100,
        };
        dataCourse.push(course);
    });
    return dataCourse;
}


// Функция для создания HTML-кода для элемента данных
function createContentItem(data) {
  return `
    <a class="content-item" href="CursePage.html" >
      <div>
        <img src="${data.image}">
        <h3>${data.title}</h3>
      </div>
      <div>
        <p class="test">Кол-во тестов: ${data.tests}</p>
        <p class="task">Кол-во заданий: ${data.tasks}</p>
      </div>
      <div class="skill-main">
        <div class="skill-wrrap">
          <div class="skill-name"></div>
          <div class="skill-bar">
            <div class="skill-per" per="${data.skillPer}"></div>
          </div>
        </div>
      </div>
    </a>
   
  `;
}

// Добавление каждого элемента данных в блок `content`
var content = document.querySelector(".content");
async function fetchDataAndRender() {
    let datas = await GetCourse(); // Wait for the promise to resolve
    console.log('ds', datas);

    // Use datas in the loop
    datas.forEach(function (item) {
        content.innerHTML += createContentItem(item);
    });

    // Update progress bars after adding new elements
    updateProgressBars();
}

// Call the async function
fetchDataAndRender();

// Обновление полос прогресса
function updateProgressBars() {
    var skillPers = document.querySelectorAll(".skill-per");
    skillPers.forEach(function (skillPer) {
        var per = parseFloat(skillPer.getAttribute("per"));

        var animatedValue = 0;
        var startTime = null;

        function animate(timestamp) {
            if (!startTime) startTime = timestamp;
            var progress = timestamp - startTime;
            var stepPercentage = progress / 1000; // Dividing by duration in milliseconds (1000ms = 1s)

            if (stepPercentage < 1) {
                animatedValue = per * stepPercentage;
                skillPer.style.width = Math.floor(animatedValue) + "%";
                skillPer.setAttribute("per", Math.floor(animatedValue) + "%");
                requestAnimationFrame(animate);
            } else {
                animatedValue = per;
                skillPer.style.width = Math.floor(animatedValue) + "%";
                skillPer.setAttribute("per", Math.floor(animatedValue) + "%");
            }
        }

        requestAnimationFrame(animate);
    });
}

// Вызовите эту функцию после добавления новых элементов
updateProgressBars();

document.getElementById('toggleButton').addEventListener('click', function () {
    GetCourse()
    var topic = document.querySelector('.topic');
    var button = document.getElementById('toggleButton');
    topic.classList.toggle('hidden');
    button.classList.toggle('hidden');
});