let lessonsList = document.getElementById('lessons');
let toggleButton = document.getElementById('toggle-button');
let lessonsBar = document.querySelector('.lessons-bar');
let mainContent = document.querySelector('.main-content');
let lessonTitle = document.getElementById('lesson-title');

toggleButton.addEventListener('click', function () {
    if (lessonsBar.classList.contains('collapsed')) {
        lessonsBar.classList.remove('collapsed');
        mainContent.classList.remove('expanded');
    } else {
        lessonsBar.classList.add('collapsed');
        mainContent.classList.add('expanded');
    }
});

toggleButton.addEventListener('click', function () {
    if (lessonsBar.style.display === "none") {
        lessonsBar.style.display = "block";
        mainContent.style.width = "80%";
        toggleButton.style.left = "20%";
    } else {
        lessonsBar.style.display = "none";
        mainContent.style.width = "100%";
        toggleButton.style.left = "0%";
    }
});

async function changeLesson(lessonId) {
    try {
        const sourceLesson = 'http://127.0.0.1:8000/lessons/' + lessonId;
        const res = await fetch(sourceLesson);

        if (!res.ok) {
            console.error('Failed to fetch lesson:', res.status, res.statusText);
            return;
        }

        const lesson = await res.json();
        lessonTitle.innerText = lesson.title;

        const video = document.getElementById('video');
        video.src = "http://127.0.0.1:8000/video/%D0%B4%D1%80_%D0%BC%D0%B0%D0%BC%D0%B0.mp4";
        video.load();
        video.play();
    } catch (error) {
        console.error('An error occurred:', error);
    }
}


window.addEventListener('load', async function () {
        const res = await fetch('http://127.0.0.1:8000/lessons/');
        console.log('re',res)
        const lessonList = await res.json();
		lessonList.sort(function(a, b) { return a.id - b.id;});
        lessonList.map((item) => {
            var newListItem = document.createElement('li');
            var newListItemA = document.createElement('div');
			newListItemA.id = item.id;
			newListItemA.setAttribute('onclick', 'changeLesson(' + item.id + ')');
            newListItemA.textContent = item.title;
            newListItem.appendChild(newListItemA);
            lessonsList.appendChild(newListItem);
        })
		changeLesson(lessonList[0].id);
})