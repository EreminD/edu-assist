from src.edu_assist.api import app
from fastapi.testclient import TestClient


client = TestClient(app)



response = client.post(
    "/ask",
    json={
        "role": "math_tutor",
        "template": "tutor_quick_answer",
        "question": "Что такое число Пи?",
    },
)

print(response.text)
