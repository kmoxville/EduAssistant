from yaml import safe_load


def load_config(file_path: str):
    with open(file_path, 'r') as file:
        config_data = safe_load(file)
    
    return config_data
