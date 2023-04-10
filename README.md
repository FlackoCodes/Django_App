Django Customer Relationship Management (CRM) App
This is a Django-based web application for managing customer relationships. Users can login, create an account, and add their customer records to the app. This app uses MySQL as the database and Bootstrap for styling.

Installation and Setup
To install and run this app locally, you need to have Python 3 and MySQL installed on your system. Here are the steps to set up this app:

Clone this repository to your local machine:

Create a virtual environment for the project:

Activate the virtual environment:

Create a MySQL database and update the database settings in the settings.py file:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Run database migrations after setting up your models.py file:

Create a superuser account:

python manage.py createsuperuser

Start the development server:
python manage.py runserver
Open your web browser and go to http://localhost:8000 to view the app.


Usage


Home Page
The home page displays a list of all customer records added to the app. Users can log in or create a new account to add or manage their records.

Login
Users can log in to the app using their username and password. Invalid login attempts will display an error message.

Logout
Users can log out of the app by clicking the logout button.

Register
Users can create a new account by providing their details in the registration form. After successful registration, users will be automatically logged in.

Customer Records
Clicking on a customer record on the home page will take users to a detailed view of that record.

Add Records
Users can add new customer records to the app by clicking the "Add Record" button on the home page and filling out the add record form.

Update Records
Users can update existing customer records by clicking the "Edit" button next to the record they want to update and filling out the update record form.

Delete Records
Users can delete existing customer records by clicking the "Delete" button next to the record they want to delete.

Contributing.
This project is open for contributions. If you find any bugs or want to add new features, feel free to create a pull request or submit an issue.
