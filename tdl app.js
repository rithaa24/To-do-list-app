document.addEventListener("DOMContentLoaded", function () {
    // Get references to HTML elements
    const taskInput = document.getElementById("task-input");
    const addTaskButton = document.getElementById("add-task-button");
    const taskList = document.getElementById("task-list");

    // Event listener for adding a new task
    addTaskButton.addEventListener("click", function () {
        const taskText = taskInput.value.trim();

        if (taskText !== "") {
            addTask(taskText);
            taskInput.value = "";
        }
    });

    // Function to add a new task to the list
    function addTask(taskText) {
        const taskItem = document.createElement("li");
        taskItem.className = "task-item";

        const taskDetails = document.createElement("div");
        taskDetails.className = "task-details";
        taskDetails.textContent = taskText;

        const taskButtons = document.createElement("div");
        taskButtons.className = "task-buttons";

        const completeButton = document.createElement("button");
        completeButton.className = "complete-button";
        completeButton.textContent = "Complete";
        completeButton.addEventListener("click", function () {
            // You can implement logic for marking a task as complete here
            taskItem.classList.toggle("completed");
        });

        const deleteButton = document.createElement("button");
        deleteButton.className = "delete-button";
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", function () {
            // You can implement logic for deleting a task here
            taskList.removeChild(taskItem);
        });

        taskButtons.appendChild(completeButton);
        taskButtons.appendChild(deleteButton);

        taskItem.appendChild(taskDetails);
        taskItem.appendChild(taskButtons);

        taskList.appendChild(taskItem);
    }
});
