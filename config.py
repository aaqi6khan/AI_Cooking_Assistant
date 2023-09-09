import openai

class Config:
    openai_key = "enter_your_api_keys_here"
    serpapi_key = "enter_your_api_keys_here"
    
    @staticmethod
    def get_openai_key():
        return Config.openai_key
    
    @staticmethod
    def get_serpapi_key():
        return Config.serpapi_key


