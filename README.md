# idea_pot

The aim of this prioject is to create an idea management platform. It is currently implemented using Django, the future plan is a Django REST + ANgular implementation.

# Basic features:
1. User registration
2. Idea creation
3. Team creation
4. One to many association between idea and team

# Extended features(this may have more entries as the project advances):
1. Comment/like ideas
2. Using NLP for organizing related ideas, keyword extraction, summerization.

Currently its in a crude stage with a little extension from the Django seed. Basic models for idea, team and user profile are in place. The front end for users is currently under development. Planning to use Django Comments framework to implement comments and like features.

# To sart the app:
1. Clone this repository to your local machine (or just download the zip)
2. Extract the files into a new forlder (name it whatever you like)
3. Open up a command prompt at this derectory (in windows: shift + right click -> Open command window here)
4. In the command prompt, type python manage.py migrate
5. Once migrations are complete, type python manage.py runserver and you should be able to browse the site at 127.0.0.1:8000
6. You should be able to access the admin site at 127.0.0.1:8000/admin
7. This is at a very crude stage right now, so don't expect anything magical ;)
8. Please feel free to pull, fork and comment.
