# Treinamento de IA para Aprendizado de Máquina

Este projeto é uma implementação de um sistema de inteligência artificial que utiliza várias APIs e bibliotecas para processar texto, áudio e imagens. O objetivo é treinar uma IA para aprender e gerar conteúdo específico de forma eficiente.

## Tecnologias Utilizadas

1. **API Gemini**:
   - Utilizada para a geração de texto e áudio, proporcionando uma maneira eficaz de gerar conteúdo a partir de prompts específicos.

2. **Transformers**:
   - A biblioteca [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) foi utilizada para processamento e geração de descrições de imagens.
   - Código:
     ```python
     from transformers import BlipProcessor, BlipForConditionalGeneration
     ```

3. **Google Translate**:
   - A biblioteca `googletrans` foi utilizada para traduzir descrições geradas para o português.
   - Código:
     ```python
     from googletrans import Translator
     ```

4. **MoviePy**:
   - A biblioteca `moviepy.editor` foi utilizada para a geração de vídeos a partir de sequências de imagens.
   - Código:
     ```python
     from moviepy.editor import ImageSequenceClip
     ```

5. **Diffusers**:
   - A biblioteca `diffusers` foi utilizada para a geração de imagens com base em prompts de texto.
   - Código:
     ```python
     from diffusers import StableDiffusionPipeline
     ```

6. **Pillow**:
   - A biblioteca `PIL` (Python Imaging Library) foi utilizada para manipulação de imagens.
   - Código:
     ```python
     from PIL import Image
     ```

## Funcionalidades

- **Geração de Texto**: Utiliza a API Gemini para criar conteúdo textual com base em prompts fornecidos pelo usuário.
- **Transcrição de Áudio**: Processa arquivos de áudio e converte-os em texto utilizando google.generativeai.
- **Descrição de Imagens**: Gera descrições para imagens usando o modelo BLIP e traduz para o português.
- **Geração de Imagens**: Cria imagens a partir de descrições textuais utilizando a biblioteca Diffusers.
- **Criação de Vídeos**: Gera vídeos a partir de sequências de imagens utilizando a biblioteca MoviePy.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/MrRastro/Projeto_IA.git
