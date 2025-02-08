# Smart Task and Reminder Management System

#### Video Demo: <https://youtu.be/A9xMnFzm_T8?si=qC4qeqpg8YznU857>

#### Description:

The Smart Task and Reminder Management System is a Python-based application designed to help users effectively manage their tasks and set reminders. This project provides an intuitive command-line interface that allows users to add tasks, list them, update their statuses, and send reminders for upcoming deadlines. It aims to enhance productivity by ensuring that important tasks are not overlooked. 

### Project Features

1. **Task Management**: Users can add new tasks with a name, description, and due date. Each task is assigned a unique ID, making it easy to reference and update them later.

2. **Task Listing**: The system provides a feature to list all tasks along with their current statuses, due dates, and the number of days remaining until the due date. This overview helps users prioritize their tasks efficiently.

3. **Status Updates**: Users can update the status of tasks (e.g., completed, pending, or canceled). This functionality allows users to keep track of their progress and manage their workload effectively.

4. **Reminders**: The system can send reminders for tasks that are due today or in the coming days. This feature is crucial for users to stay on top of their responsibilities.

### File Structure

- `project.py`: This is the main file containing the application's logic. It includes functions for adding tasks, listing tasks, updating their statuses, and sending reminders. The `main` function serves as the entry point for the application, providing a menu-driven interface.

- `test_project.py`: This file contains unit tests for the functions defined in `project.py`. It uses the `pytest` framework to verify that the application behaves as expected. The tests cover adding tasks, updating statuses, and sending reminders, ensuring the reliability of the system.

- `requirements.txt`: This file lists the dependencies required for the project. Currently, it includes `pytest`, which is used for testing the application.

### Design Choices

During the development of this project, several design choices were made to enhance functionality and user experience. For instance, the command-line interface was chosen to keep the application lightweight and easy to use. This approach allows for quick interactions without the overhead of a graphical user interface.

Additionally, the decision to implement task reminders was influenced by the need for users to stay organized and avoid missing deadlines. The system calculates the number of days remaining for each task, providing relevant feedback when reminders are triggered.

### Future Improvements

While this project serves as a robust task management system, there are several potential enhancements that could be implemented in future versions:

- **User Authentication**: Implementing a user authentication system could allow multiple users to manage their tasks independently.

- **Graphical User Interface (GUI)**: Developing a GUI could make the application more user-friendly and visually appealing.

- **Data Persistence**: Currently, the tasks are stored in memory. Adding functionality to save tasks to a file or database would enable users to retain their tasks between sessions.

In conclusion, the Smart Task and Reminder Management System is a practical tool for anyone looking to improve their task management and productivity. The project showcases the fundamental concepts of Python programming and offers opportunities for further development and complexity.
