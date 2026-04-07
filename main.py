from src.edu_assist.assistant import create_response

# Prepare prompt for LLM
INPUT_PROMPT = input()

# Call assistant
response = create_response(
    llm_key="api",
    role="math_tutor",
    template="tutor_quick_answer",
    prompt=INPUT_PROMPT,
)

print(response)
