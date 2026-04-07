from src.edu_assist.config import Config


config = Config.from_yaml_file("config.yml")
print("Full config:", config)
print("LLM model:", config.llms["api"].model)

# Read file as text

system_prompt = config.render_system_instructions(role="history_tutor", template="tutor_quick_answer")
print("System prompt:", system_prompt)