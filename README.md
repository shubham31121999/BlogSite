# BlogSite
This is a replica of social media website using Django


### Project Requirements:

1. **User Authentication:**
    - Implement user registration, login, and logout functionality using Django's built-in authentication system.
2. **Blog Post Model:**
    - Create a model `Post` with the following fields:
        - `title`: CharField
        - `content`: TextField
        - `author`: ForeignKey to User
        - `created_at`: DateTimeField (auto_now_add=True)
        - `updated_at`: DateTimeField (auto_now=True)
        - `status`: ChoiceField (Draft, Published)
3. **Views and Templates:**
    - Create views and corresponding templates for the following actions:
        - List all blog posts.
        - Create a new blog post.
        - Update an existing blog post.
        - Delete a blog post.
        - View a single blog post.
4. **Comment Model:**
    - Create a model `Comment` with the following fields:
        - `post`: ForeignKey to Post
        - `author`: ForeignKey to User
        - `content`: TextField
        - `created_at`: DateTimeField (auto_now_add=True)
5. **Views and Templates for Comments:**
    - Allow users to add comments to a blog post.
    - Display comments under each blog post.
6. **Like Functionality:**
    - Implement a like button for each blog post.
    - Track the number of likes for each post.

Login Page taken form net --> https://codepen.io/technext/pen/PoprgzP

1.Created a python virtual enviroment for setup which help's in clean development and deployement and to create a requirements.txt file --> python -m venv venv
2.Activate venv using --> venv\Scripts\activate
3.Create a project dir using command --> django-admin startproject Blog
4.Change Direcrtory to the project Blog --> cd Blog
5.Create an web app for the project Blog -->python manage.py startapp socialsite
6.Rename the Blog directory as config and also add django for setting and settings directory for using third party packages like celery.
7.Resturcuted the file from the normal setup to development setup. --> django directory in config is used for development level base ,local,production and also to use testcase we keep it in tests.py .
8.Changes in wsgi and asgi for naming in patha and also in manage.py change project name for running the server.
9.Created a login page and signup page using slider effect.
10.Fields for signup are firstname ,lastname ,password,date of birth, email a unique id is also assigned in the models and is generated through the package of uuid.