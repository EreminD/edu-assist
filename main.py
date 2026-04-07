from dotenv import load_dotenv

from src.edu_assist.config import Config
from src.edu_assist.llm import get_llm_client

load_dotenv()

INPUT_PROMPT = "Кто ты?"

config = Config.from_yaml_file("config.yml")
llmConfig = config.llms["ollama"]
client = get_llm_client(llmConfig)

response = client.responses.create(
  model=llmConfig.model,
  input=INPUT_PROMPT
)

print(response)

print(response.output_text)

