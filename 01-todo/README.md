# Django TODO App – AI Dev Tools Zoomcamp HW1

This is a simple TODO application built with **Django**, as part of the **AI Dev Tools Zoomcamp (2025)** homework on AI-assisted development.

The goal of the assignment was to build a full CRUD TODO app using an AI assistant (ChatGPT) *without needing prior Django experience*.

![My To-Do App site](todo_app.png)

---

## Features

- Create TODO items with:
  - Title (required)
  - Optional description
  - Optional due date
- View a list of all TODOs
- Mark TODOs as **done / not done**
- Delete TODOs
- Basic, clean UI using HTML + inline CSS (no extra frontend framework)

---

## Tech Stack

- Python 3.12 (local)
- Django 5.x
- SQLite (default Django DB)

---

## Project Structure

Inside this repo, the project for HW1 lives in the `01-todo` folder:

```text
01-todo/
├── manage.py
├── requirements.txt
├── todo_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todos/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── templates/
    ├── base.html
    └── home.html
