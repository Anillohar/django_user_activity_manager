# django_user_activity_manager
Simple Repository which maintains the record of a user's activities in database.
**http://anillohar03.pythonanywhere.com/**

**INSTALLATION**:<br>
Python 3 is required to run this
1. Install virtualenv if it doesn't exist.
2. make virtual environment using command:<br>
    `virtualenv --python=python3 venv`
3. clone repository using <br>
    `git clone https://github.com/Anillohar/django_user_activity_manager`
4. activate virtualenv using `source venv/bin/activate` and 
    navigate to folder django_user_activity_manager
5. install requirements using: <br>
    `pip install -r requirements.txt`

**HOW TO USE**
1. create database tables using<br>
    1. `python manage.py makemigrations`<br>
    2. `python manage.py migrate`
2. Configure static files:<br>
    1. `python manage.py collectstatic`
3. To create dummy data run:<br>
    1. `python manage.py auto_populate_database`
4. Run the server using <br>
    1. `python manage.py runserver`
5. Go to url:<br>
    `http://anillohar03.pythonanywhere.com/api/v1/get-members-list/` to see members list
    
**What have been done?**
1. Override django user model and maintain the user activity by tracking user 
    start and end time from login and logout views.
2. Use Credentials <br>
    Url: 'http://anillohar03.pythonanywhere.com'<br>
    Username: `test`<br>
    Password: `Welcome@123`<br>
    To sign in to admin console.
3. Use <br>
    Url: http://anillohar03.pythonanywhere.com/api/v1/get-members-list/<br>
    to see all member activities