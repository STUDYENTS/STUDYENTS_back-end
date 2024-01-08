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
	const sourceLesson = 'http://127.0.0.1:8000/lessons/' + lessonId + '/';
	let res = await fetch(sourceLesson);
    const lesson = await res.json();
	lessonTitle.innerText = lesson.title;
	
	const video = document.getElementById('video');
	video.src = lesson.video;
	
	const file = document.querySelector('.additional-text');
	console.log(file);
	file.innerHTML = `<p>Дополнительная информация о текущем уроке или задания для студентов.</p><p>${lesson.theory}</p><a href=${lesson.file} target="_blank"><button>Скачать</button></a>`;

	const testField = document.querySelector('.tests');
	testField.innerText = '';
	
	res = await fetch('http://127.0.0.1:8000/tests/');
	const tests = await res.json();
	tests.forEach(async function(item) {	
		let optCount = '1';
		let questCount = '1';
		if (item.lesson == sourceLesson) {
			//Заголовок теста
			const header = document.createElement('h2');
			testField.appendChild(header);
			header.innerText = item.title;	
			
			const testForm = document.createElement('form');
			testField.appendChild(testForm);
			
			res = await fetch('http://127.0.0.1:8000/tasks/');
			const tasks = await res.json();
			const sourceTest = 'http://127.0.0.1:8000/tests/' + item.id + '/';
			tasks.forEach(async function(item) {
				if (item.test == sourceTest) {
					//Заголовок задания					
					const taskHeader = document.createElement('p');
					testForm.appendChild(taskHeader);
					taskHeader.innerText = item.question;	
					
					const answersBlock = document.createElement('div');	
					testForm.appendChild(answersBlock);
	
					res = await fetch('http://127.0.0.1:8000/answers/');
					const answers = await res.json();
					const sourceTask = 'http://127.0.0.1:8000/tasks/' + item.id + '/';
					
					answers.forEach(function(item) {
						if (item.task == sourceTask) {
							//Варианты ответов										
							answersBlock.innerHTML += `<input type="radio" id="option${optCount}" name="question${questCount}" value="option${optCount}">
							<label for="option${optCount}">${item.answer}</label><br>`;
							optCount++;							
						}
						
					})
				questCount++;
				}
			});
			
			testForm.appendChild(document.createElement('br'));
			const testButton = document.createElement('button');
			testButton.innerText = 'Отправить ответы';
			testButton.type = 'submit';
			testForm.appendChild(testButton);
		}
	})
};

window.addEventListener('load', async function () {
        const res = await fetch('http://127.0.0.1:8000/lessons/');
        const lessonList = await res.json();
		lessonList.sort(function(a, b) { return a.id - b.id;});
        lessonList.map((item) => {
            var newListItem = document.createElement('li');
            var newListItemA = document.createElement('div');
			newListItemA.id = item.id;
			newListItemA.setAttribute('onclick', 'changeLesson(' + item.id + ')');
            var newListItemA = document.createElement('div');
			newListItemA.id = item.id;
			newListItemA.setAttribute('onclick', 'changeLesson(' + item.id + ')');
            newListItemA.textContent = item.title;
            newListItem.appendChild(newListItemA);
            lessonsList.appendChild(newListItem);
        })		
		
		changeLesson(lessonList[0].id);
})