# Personal Portfolio Website with Django

This is a Django website to show your work and skills. It lets you share your experience, projects, and blog posts.

## What's Inside

The website has these main parts:
- A home page with your skills and experience  
- A portfolio section to show your projects  
- A blog where you can write posts  
- A contact form for people to reach you  
- A testimonials section for feedback from others  

## How to Set It Up

1. **Create a Python environment:**  
   Run these commands in your terminal:  
   ```bash 
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate ```
## Install the Requirements

Use `pip` to install the dependencies listed in the `requirements.txt` file.

```pip install -r requirements.txt ```

## Apply Migrations

Set up the database by creating the necessary tables. Run the following commands:
 
``` python manage.py makemigrations ```
``` python manage.py migrate ```

## Run Server
``` python manage.py runserver ```
