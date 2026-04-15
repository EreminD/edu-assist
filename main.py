# from src.edu_assist.api import app
# from fastapi.testclient import TestClient


# client = TestClient(app)



# response = client.post(
#     "/ask",
#     json={
#         "role": "math_tutor",
#         "template": "tutor_quick_answer",
#         "question": "Что такое число Пи?",
#     },
# )

# print(response.text)

from src.edu_assist.tools.formula import extract_and_solve_trailing_formula


PROMPT = "Посчитай 1+1/2-0,5-(3/2-3/6)"
# PROMPT = "Упрости выражение: x^2-x(x+1)+2(0.5x-1)+2"

solution = extract_and_solve_trailing_formula(PROMPT)
print("Решение формулы: " + solution)