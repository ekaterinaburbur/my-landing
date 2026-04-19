from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key.startswith("sk-..."):
    print("Ошибка: укажи настоящий OPENAI_API_KEY в файле .env")
    raise SystemExit(1)

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": (
                "Придумай 3 креативных названия для моего проекта: "
                "дашборд для отслеживания дедлайнов по сделкам с партнёрами, "
                "который формирует дайджест для отправки в Telegram."
            ),
        }
    ],
)

print(response.choices[0].message.content)
