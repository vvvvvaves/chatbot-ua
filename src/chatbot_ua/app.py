from typing import Any

from fastapi import FastAPI
from src.chatbot_ua.objects.chat import LLMRequest
from src.chatbot_ua.llm.api.custom_api import custom_api
app = FastAPI()


def build_request(query: str) -> LLMRequest:
    llm_request = LLMRequest([{"role": "user", "content": query}])
    return llm_request


@app.post("/new_chat")
def send_request(query: str) -> Any:
    # llm_request = build_request(query)
    # response = llm_request.send_request()
    response = custom_api.completion([{"role": "user", "content": query}])
    print(type(response))
    print(response)
    print(response.json())

