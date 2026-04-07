from fastapi import FastAPI
from pydantic import BaseModel
from edu_assist.assistant import create_response
from edu_assist.config import RoleType, TemplateType


class AskBody(BaseModel):
      role: RoleType
      template: TemplateType
      question: str
    

app = FastAPI()


@app.post('/ask')
def ask(body: AskBody) -> str:
    response = create_response(
        llm_key="api",
        role=body["role"],
        template=body["template"],
        prompt=body["question"],
    )
    return response
