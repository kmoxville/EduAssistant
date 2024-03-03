import yaml

def load_config(file_path: str):
    with open(file_path, 'r') as file:
        config_data = yaml.safe_load(file)
    
    return config_data