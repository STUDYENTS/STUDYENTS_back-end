// script.js
// A function to create a new lesson element
function createLesson() {
    // Create a div element for the lesson
    var lesson = document.createElement("div");
    lesson.className = "lesson";
  
    // Create an input element for the lesson name
    var input = document.createElement("input");
    input.type = "text";
    input.placeholder = "e.g. Lesson 1: HTML Basics";
  
    // Create a button element for adding content
    var button = document.createElement("button");
    button.textContent = "Add Content";
  
    // Create a div element for the content
    var content = document.createElement("div");
    content.className = "content";
  
    // Create a label and an input element for the video
    var videoLabel = document.createElement("label");
    videoLabel.textContent = "Video:";
    var videoInput = document.createElement("input");
    videoInput.type = "file";
    videoInput.accept = "video/*";
  
    // Create a label and an input element for the file
    var fileLabel = document.createElement("label");
    fileLabel.textContent = "File:";
    var fileInput = document.createElement("input");
    fileInput.type = "file";
    fileInput.accept = ".pdf,.doc,.ppt";
  
    // Create a label and an input element for the test
    var testLabel = document.createElement("label");
    testLabel.textContent = "Test:";
    var testInput = document.createElement("input");
    testInput.type = "text";
    testInput.placeholder = "e.g. https://www.example.com/test-1";
  
    // Create a button element for finishing the content
    var doneButton = document.createElement("button");
    doneButton.textContent = "Done";
  
    // Append the elements to the lesson div
    lesson.appendChild(input);
    lesson.appendChild(button);
    content.appendChild(videoLabel);
    content.appendChild(videoInput);
    content.appendChild(fileLabel);
    content.appendChild(fileInput);
    content.appendChild(testLabel);
    content.appendChild(testInput);
    content.appendChild(doneButton);
    lesson.appendChild(content);
  
    // Add an event listener to the add content button
    button.addEventListener("click", function() {
      // Show the content div
      content.classList.add("active");
    });
  
    // Add an event listener to the done button
    doneButton.addEventListener("click", function() {
      // Hide the content div
      content.classList.remove("active");
    });
  
    // Return the lesson div
    return lesson;
  }
  
  // Get the lessons div
  var lessons = document.getElementById("lessons");
  
  // Get the add lesson button
  var addLesson = document.getElementById("add-lesson");
  
  // Add an event listener to the add lesson button
  addLesson.addEventListener("click", function() {
    // Create a new lesson and append it to the lessons div
    var lesson = createLesson();
    lessons.appendChild(lesson);
  });