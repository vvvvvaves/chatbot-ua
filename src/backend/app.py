from typing import Any
from fastapi import FastAPI
from src.backend.objects.chat import LLMRequest
from config import get_api


app = FastAPI()

custom_api = get_api(run="deploy")


def build_request(query: str) -> LLMRequest:
    llm_request = LLMRequest([{"role": "user", "content": query}])
    return llm_request


@app.post("/new_chat")
def send_request(query: str) -> Any:
    # llm_request = build_request(query)
    # response = llm_request.send_request()
    response = custom_api.completion([{"role": "user", "content": query}], max_tokens=100)
    print(type(response))
    print(response)
    print(type(response.json()))
    print(response.json())

