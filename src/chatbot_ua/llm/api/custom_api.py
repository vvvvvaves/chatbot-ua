from typing import Optional

import requests
import json
from pydantic import BaseModel
import litellm
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

    def completion(self, messages: list[dict], *args, **kwargs): # -> litellm.ModelResponse:

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
              "stream": False, # https://openrouter.ai/docs/api-reference/streaming
              "max_tokens": 100,
              "temperature": 1.,
              "presence_penalty": 0,
              "frequency_penalty": 0
            })
          )


        response.raise_for_status()
        return response


custom_api = CustomAPI(api_base="https://openrouter.ai/api/v1/chat/completions",
                       api_key_env_var='OPENROUTER_DEEPSEEK_V3_BASE_FREE_API_KEY',
                       model="deepseek/deepseek-v3-base:free")


litellm.custom_provider_map = [ # 👈 KEY STEP - REGISTER HANDLER
        {"provider": "custom_api", "custom_handler": custom_api}
    ]

