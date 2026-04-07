from openai import OpenAI

from edu_assist.config import LLMConfig


def get_llm_client(llm_config: LLMConfig) -> OpenAI:
    return OpenAI(
        base_url=llm_config.base_url,
        timeout=llm_config.timeout,
    )
