import yaml
import os
from yaml.loader import SafeLoader
from src.chatbot_ua.llm.api.custom_api import CustomAPI

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(PROJECT_ROOT, 'config.yaml')
LLM_PATH = os.path.join(PROJECT_ROOT, 'llm.yaml')


def get_api(run: str) -> CustomAPI:
    with open(CONFIG_PATH, 'r') as f:
        config_data = list(yaml.load_all(f, Loader=SafeLoader))[0]

    with open(LLM_PATH, 'r') as f:
        llm_data = list(yaml.load_all(f, Loader=SafeLoader))[0]

    for model in llm_data['llm_apis']:
        if model['model'] == config_data[run]["model"]:
            return CustomAPI(**model)

    raise ValueError(f"No model named \"{config_data[run]['model']}\"")