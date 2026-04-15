from dotenv import load_dotenv
from edu_assist.tools.formula import extract_and_solve_trailing_formula
from loguru import logger

from edu_assist.config import Config, RoleType, TemplateType
from edu_assist.llm_client import get_llm_client

# Load environment variables from .env file
load_dotenv()


def create_response(
    llm_key: str,
    role: RoleType,
    template: TemplateType,
    prompt: str,
) -> str:
    config = Config.from_yaml_file("config.yml")
    llm_сonfig = config.llms[llm_key]
    client = get_llm_client(llm_сonfig)

    instructions = config.render_system_instructions(role=role, template=template)
   
    
    if role == "math_tutor":
        solution = extract_and_solve_trailing_formula(prompt)
        if solution:
            instructions += f"\n\nНе пытайся считать формулу, используй уже посчитанный результат: {solution}"
   
    
    
    logger.debug(f"LLM instructions: {instructions}")
    
    response = client.responses.create(
        model=llm_сonfig.model,
        instructions=instructions,
        input=prompt,
        max_output_tokens=llm_сonfig.max_output_tokens,
    )

    return response.output_text
    