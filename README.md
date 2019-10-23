An asynchronous Django server with a Celery worker and Redis as a broker.

Installation:

To install this project it will require Python >= 3.7.3. Once installed you will need to install virtualenv via pip
by using the commmand sudo -H pip install. Using the -H flag along with the sudo command will make sure virualenv is installed
system wide. 

Next is activating the virtualenv by navigating into the directory which includes /async_django, /lib, /bin, and /include.
Activate the virtualenv with the command source bin/activate. If all goes well you should see the name of the project in 
parentheses (django_async) behind you computer name in the terminal. To deactivate the virtualenv use the command deactivate
and the virtualenv will no onger be active.

For the rest of this installation it will be assumed that you have succesfully installed Python3 with virtualenv and it is 
activated. If you are stuggling then please contact me at wesley.k.r1993@gmail.com and I'll help you get it working.

Installing dependencies:

This can be tricky or easy. Fortunately it has been made easy with the requirements.txt file via pip freezre one directory 
down. This file is in the async_django directory which has /async_django, /feedback, /templates, db.sqlite3, manage.py,
and requirements.txt. We will install the dependencies with a simple command pip install -r requirements.txt. The -r flag is 
used to indicate that pip should do this operation recursively. If all goes well you should see eleven packages and all their
dependencies installed directly into the virtualenv (not system wide).

Usage:

From this point forward we will be operating exclusively in this directory and only using the one file manage.py. To run the
server it is a simple command python manage.py runserver and you are done. 

This project is far from complete so there is not much to do. This readme was created as a template to make my life easier.
Happy coding!
