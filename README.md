# API for "Yatube"

## Tecnhologies

- Python 3.9.10
- Django 3.2.16
- djangorestframework 3.12.4
- SQLite3

## Description

The REST API for the "Yatube" project.
Implemented API functionality for the project https://github.com/Zulusssss/hw05_final.

## Functional

- Subscription and unsubscription from an authorized user;
- An authorized user views posts, creates new ones deletes and modifies them;
- View communities;
- Commenting, viewing, deleting and updating comments;
- Filtering by fields;
- Authentication using a JWT token.

## Installation

1. Clone a repository:

   ```python
   git clone git@github.com:Zulusssss/api_final_yatube.git
   ```

2. Go to the project folder:

   ```python
   cd api_final_yatube/
   ```

3. Install a virtual environment for the project:

   ```python
   python -m venv venv
   ```

4. Activate the virtual environment for the project:

   ```python
   # for OS Linux and macOS
   source venv/bin/activate

   # for OS Windows
   source venv/Scripts/activate
   ```

5. Install dependencies:

   ```python
   python3 -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Perform migrations at the project level:

   ```python
   cd yatube
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

7. Fill in the env-file like it
   ```text
   SECRET_KEY=<Your_some_long_string>
   DEBUG=False
   ```

8. Run the project:

   `python manage.py runserver`

## Request examples

Getting a token

Send a POST request to the address `api/v1/jwt/create/` и передать 2 поля в `data`:

1. `username`
2. `password`

Creating a post

Send a POST request to the address `api/v1/posts/` and pass the required `text` field, specify `Authorization` in the header:`Bearer <token>`.

1. Request example:

   ```json
   {
     "text": "My first post."
   }
   ```

2. Response example:

   ```json
   {
     "id": 2,
     "author": "user1",
     "text": "My first post.",
     "pub_date": "2022-05-22T13:00:32.021094Z",
     "image": null,
     "group": null
   }
   ```

Commenting on a user's post

Send a POST request to the address `api/v1/posts/{post_id}/comments/` and pass the required fields `post` and `text`, specify `Authorization` in the header:`Bearer <token>`.

1. Request example:

   ```json
   {
     "post": 1,
     "text": "Test"
   }
   ```

2. Response example:

   ```json
   {
     "id": 1,
     "author": "user1",
     "text": "Test",
     "created": "2022-04-22T12:06:13.146875Z",
     "post": 1
   }
   ```

## Resources

```python
# Project documentation
http://127.0.0.1:8000/redoc/
```

```python
# API testing software, Postman
https://www.postman.com/
```
