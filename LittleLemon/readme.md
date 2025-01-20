# Little Lemon

Little Lemon is a Django-based web application designed to manage and display restaurant menus, reservations, and customer reviews.

## Features

- Menu management
- Reservation system
- Customer reviews
- User authentication

## Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/LittleLemon.git
  ```
2. Navigate to the project directory:
  ```bash
  cd LittleLemon
  ```
3. Create and activate a virtual environment:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
4. Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
5. Apply migrations:
  ```bash
  python manage.py migrate
  ```
6. Create a superuser:
  ```bash
  python manage.py createsuperuser
  ```
7. Run the development server:
  ```bash
  python manage.py runserver
  ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Log in to the admin panel at `http://127.0.0.1:8000/admin/` to manage menus, reservations, and reviews.

## Contributing

1. Fork the repository.
2. Create a new branch:
  ```bash
  git checkout -b feature-branch
  ```
3. Make your changes and commit them:
  ```bash
  git commit -m "Description of changes"
  ```
4. Push to the branch:
  ```bash
  git push origin feature-branch
  ```
5. Create a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact [iyadicy@gmail.com](mailto:iyadicy@gmail.com).