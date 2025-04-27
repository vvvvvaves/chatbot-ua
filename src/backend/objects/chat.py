from typing import Any, Optional

from litellm.types.utils import ModelResponse
from pydantic import BaseModel
from litellm import completion

class LLMRequest(BaseModel):
    request: Optional[list[dict]] = None

    def __init__(self, request: Optional[list[dict]] = None, **data: Any):
        super().__init__(**data)
        if request is None:
            self.request = [{"role": "user", "content": "hello from litellm"}]
        else:
            self.request = request

    def send_request(self, stream: bool = False) -> ModelResponse:
        response = completion(
            model="deepseek/deepseek-v3-base:free",
            messages=self.request,
            stream=stream
        )
        return response

    def __repr__(self):
        self.model_dump_json(indent=4)


class LLMResponse(BaseModel):
    response: dict

    def __repr__(self):
        self.model_dump_json(indent=4)


class Chat(BaseModel):
    chat: list[tuple[LLMRequest, LLMResponse]]

    def __repr__(self):
        self.model_dump_json(indent=4)
