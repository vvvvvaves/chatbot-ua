from typing import Optional
import requests
import json
from litellm import CustomLLM
import os
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class CustomAPI(CustomLLM):
    api_base: str
    api_key_env_var: str
    model: Optional[str] = None

    def __init__(self, api_base: str, api_key_env_var: str, model: Optional[str] = None):
        super().__init__()
        self.api_base = api_base
        self.api_key_env_var = api_key_env_var
        self.model = model

    def completion(self,
                   messages: list[dict],
                   *args: dict,
                   stream: bool = False,
                   max_tokens: int = 4096,
                   temperature: float = 1.,
                   presence_penalty: float = 0.,
                   frequency_penalty: float = 0.,
                   **kwargs: dict): # -> litellm.ModelResponse:

        response = requests.post(
            url=self.api_base,
            headers={
              "Authorization": f"Bearer {os.environ[self.api_key_env_var]}",
              # "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
              # "X-Title": "<YOUR_SITE_NAME>",  # Optional. Site title for rankings on openrouter.ai.
            },
            data=json.dumps({
              "model": self.model,  # Optional
              "messages": messages,
              "stream": stream, # https://openrouter.ai/docs/api-reference/streaming
              "max_tokens": max_tokens,
              "temperature": temperature,
              "presence_penalty": presence_penalty,
              "frequency_penalty": frequency_penalty
            })
          )

        response.raise_for_status()
        return response

