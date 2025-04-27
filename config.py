import yaml
from yaml.loader import SafeLoader
from src.chatbot_ua.llm.api.custom_api import CustomAPI


def get_api(run: str = "test") -> CustomAPI:
    with open('config.yaml', 'r') as f:
        config_data = list(yaml.load_all(f, Loader=SafeLoader))[0]

    with open('llm.yaml', 'r') as f:
        llm_data = list(yaml.load_all(f, Loader=SafeLoader))[0]

    for model in llm_data['llm_apis'][run]:
        if model['model'] == config_data[run]["model"]:
            return CustomAPI(**model)

    raise ValueError(f"No model named \"{config_data[run]['model']}\" in run \"{run}\"")