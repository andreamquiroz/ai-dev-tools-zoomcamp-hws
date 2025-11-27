# todos/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_create_todo(self):
        response = self.client.post(reverse("home"), {
            "title": "Test Todo",
            "description": "Test Desc"
        })
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertEqual(Todo.objects.count(), 1)

    def test_toggle_complete(self):
        todo = Todo.objects.create(title="Test")
        response = self.client.get(reverse("toggle_complete", args=[todo.id]))
        todo.refresh_from_db()
        self.assertTrue(todo.is_completed)

    def test_delete_todo(self):
        todo = Todo.objects.create(title="Test")
        response = self.client.get(reverse("delete_todo", args=[todo.id]))
        self.assertEqual(Todo.objects.count(), 0)
