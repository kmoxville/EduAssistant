from dataclasses import dataclass

@dataclass
class Config:
    def __init__(self, token: str):
        self.token = token
    token: str
    api_url: str = 'https://api.telegram.org/bot'