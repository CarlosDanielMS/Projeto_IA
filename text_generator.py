import google.generativeai as genai

API_KEY = "AIzaSyCJQXgoOd3DBBnXGkV0BVZbklo6jrjnsaQ"

class TextGenerator:
    def __init__(self):
        # Configura a API
        genai.configure(api_key=API_KEY)

    def generate_text(self, prompt):
        # Definir o modelo e gerar a resposta
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
