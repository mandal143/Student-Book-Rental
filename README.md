# Student Book Rental Application

## Overview
This application allows students to rent books for free for the first month. After the first month, the student will be charged a fee based on the page count of the book, calculated as `(page_count // 100)` per month.

### Features:
- Admin interface for managing users, books, and rentals.
- Automatic fee calculation after the first month.
- Integration with OpenLibrary API to fetch book details by title.
- View all rentals and fees for each student.
- Prolong rentals and apply additional fees automatically.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mandal143/Student-Book-Rental.git
    cd book-rental-app
    ```
2. Set up the Python environment:
    ```bash
    python3 -m venv vitual
    source vitual/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser for the admin interface:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the admin panel at:
    ```
    http://127.0.0.1:8000/admin
    ```

## Admin Features
- **Start a New Rental**: Navigate to the **Rental** section, click on “Add Rental,” select the student and book, and save.
- **Prolong a Rental**: In the **Rental** section, select the rental(s) you wish to prolong, and choose the "Prolong selected rentals by one month" action.
- **View Student Rentals**: Navigate to the **Users** section, select a user, and scroll down to see all books they have rented, along with the corresponding fees.

## Configuration
### OpenLibrary API
Ensure the application can connect to OpenLibrary by modifying settings in `views.py`. The `fetch_book_details` function uses the OpenLibrary API to retrieve book data.

```python
OPEN_LIBRARY_API = 'https://openlibrary.org/search.json?title='
