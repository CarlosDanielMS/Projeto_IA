from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip
import os

class VideoGenerator:
    def __init__(self, img_size=(640, 480), bg_color=(255, 255, 255), text_color=(0, 0, 0)):
        self.img_size = img_size
        self.bg_color = bg_color
        self.text_color = text_color
        self.image_files = []

    def create_image_with_text(self, text, filename):
        # Criar uma nova imagem
        img = Image.new('RGB', self.img_size, self.bg_color)
        draw = ImageDraw.Draw(img)

        # Definir fonte (pode ser necessário ajustar o caminho da fonte)
        font = ImageFont.load_default()

        # Calcular a posição do texto
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Centralizar o texto na imagem
        text_x = (self.img_size[0] - text_width) // 2
        text_y = (self.img_size[1] - text_height) // 2

        # Adicionar o texto à imagem
        draw.text((text_x, text_y), text, fill=self.text_color, font=font)

        # Salvar a imagem
        img.save(filename)

    def generate_images(self, texts):
        # Gerar imagens a partir do texto
        for i, text in enumerate(texts):
            filename = f"text_image_{i}.png"
            self.create_image_with_text(text, filename)
            self.image_files.append(filename)

    def create_video(self, video_filename, fps=1):
        # Criar um vídeo a partir das imagens
        clip = ImageSequenceClip(self.image_files, fps=fps)
        clip.write_videofile(video_filename, codec="libx264")

    def clean_up(self):
        # Limpar as imagens geradas
        for image_file in self.image_files:
            os.remove(image_file)
        self.image_files.clear()

    def process_video(self, texts, video_filename, fps=1):
        # Gerar imagens e vídeo
        self.generate_images(texts)
        self.create_video(video_filename, fps)
        self.clean_up()
