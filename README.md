# Cyber Cafe Management System (Cyber-Cafe-MS)
Cyber Cafe Management System (Cyber-Cafe-MS) is an efficient software for managing cyber cafe operations. It tracks user sessions, handles billing, manages inventory, and ensures security. With a user-friendly interface and detailed reporting.This project is a Django-based web application designed to manage cyber users. The system allows for the creation, updating, viewing, and deletion of user records. The project is built using Django, Bootstrap for the frontend, and includes functionalities such as user authentication, search, and responsive table management.

## Features

- **User Authentication**: Login required to access user management functionalities.
- **Manage Users**: Create, update, view, and delete user records.
- **Search Users**: Search users by entry ID.
- **Responsive Design**: Uses Bootstrap for a responsive and user-friendly interface.
- **Modals for Actions**: Confirm deletion using Bootstrap modals.

## Requirements

- Python 3.x
- Django 3.x or later
- Bootstrap 4.x or later
- Font Awesome (for icons)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/kavinandan18/cyber-cafe-ms.git
    cd cyber-user-management
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the Application**:
    Open your browser and go to `http://127.0.0.1:8000`.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss changes.
