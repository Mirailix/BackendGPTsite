from openai import OpenAI
from config import Config


class GPTClient:
    def __init__(self):
        if not Config.chatgpt_key:
            raise ValueError("OPENAI_API_KEY не найден")

        self.client = OpenAI(api_key=Config.chatgpt_key)

    def get_answer_from_gpt(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content
    
