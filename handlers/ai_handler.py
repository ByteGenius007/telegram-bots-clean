import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# память диалога (можно расширять)
dialog_memory = {}
MAX_HISTORY = 5

SYSTEM_PROMPT = (
    "Ты Марат Тайкешев — представитель компании my-robot-store. "
    "Отвечай дружелюбно и понятно, как живой человек. "
    "Говори простым языком. "
    "Если вопрос про ИИ, роботов или компанию — объясняй доступно."
)

def ask_openai(user_id: int, question: str) -> str:
    history = dialog_memory.get(user_id, [])
    history.append({"role": "user", "content": question})

    # обрезаем историю
    history = history[-MAX_HISTORY:]
    dialog_memory[user_id] = history

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )
        answer = response.choices[0].message.content.strip()
        dialog_memory[user_id].append({"role": "assistant", "content": answer})
        return answer
    except Exception as e:
        print("OpenAI ERROR:", e)
        return "Сейчас не могу ответить, попробуй позже 🙏"
