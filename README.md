# Django Store App
This project is a basic store website built with Django. It allows users to register, log in, and view a list of products. Admins can add new products through a Django form. Product images, categories, and details are stored and displayed dynamically.

## Features

- User registration and login with session management
- Product listing with images, categories, and prices
- Add new products via Django form
- Bootstrap for styling and responsive layout
- Basic admin interface
- File/image upload support

## Technologies Used

- Python
- Django
- postgreSQL
- HTML5 / CSS3
- Bootstrap

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment and activate it:
  ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Run the server:
   ```
   python manage.py runserver
   ```

## Notes
- Product images are uploaded and stored in the media/ folder.
- Bootstrap is used for styling and is included via static files.
- The user session is used to manage login status.

## License
This project is for educational purposes. You may use or modify it freely.
