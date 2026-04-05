import openai
import os

def get_car_ai_bio(model, brand, year):
    # Obtém a API Key do ambiente para segurança
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return "Biografia não gerada. Por favor, configure a chave da API OpenAI."

    client = openai.OpenAI(api_key=api_key)
    
    prompt = f"Crie uma descrição de venda curta e atrativa para um carro {brand} {model} ano {year}. " \
             f"Destaque pontos fortes do modelo. Máximo 250 caracteres."

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return f"Carro {brand} {model} {year}. Um excelente veículo para quem busca qualidade e conforto."
