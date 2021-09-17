# Course Notes
![](img/icon.png)<br>
A app for managing lessons with Django

Some Ideas for this app:
----
- [ ] Share Lessons
- [ ] Exam Generator

Installation:
----
Clone:

    git clone https://github.com/motahharm/course-notes.git
  
Go To Dir:

    cd course-notes

Django Initilize:

    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser #For Creat Super User

Use Whitenoise When Debug Is False:

    pip install whitenoise

- In Settings.py Uncommand Two Line For Whitenoise
- In Settings.py Find:

        debug = True

- Replace With:

        debug = False

You Are Success 😎

Run:
----
Run On Localhost:

    python3 manage.py runserver

Run On Other Port:

    python manage.py runserver <Your Port>

Run On All Ips:

    python3 manage.py runserver 0.0.0.0

Run On All Ips With Custom Port:

    python3 manage.py runserver 0.0.0.0:<Your Port>

I Will Be Happy😊:
----
Star This Project 🤩<br><br>
Thanks 🙏