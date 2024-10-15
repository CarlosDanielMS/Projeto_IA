import tkinter as tk
from tkinter import messagebox, filedialog
from text_generator import TextGenerator
from image_describer import ImageDescriber
from image_generator import ImageGenerator
from video_generator import VideoGenerator
from audio_transcriber import transcribe_audio, select_audio_file  # Importa as funções

class App:
    def __init__(self, master):
        self.master = master
        master.title("Interface Gráfica para Geração de Conteúdo")
        master.configure(bg='#f0f0f0')  # Cor de fundo

        # Campo de entrada para texto (apenas para gerar texto, imagem e vídeo)
        self.input_frame = tk.Frame(master, bg='#f0f0f0')
        self.input_frame.pack(pady=10)

        self.input_label = tk.Label(self.input_frame, text="Digite seu prompt:", bg='#f0f0f0', font=('Arial', 12))
        self.input_label.pack(side=tk.LEFT, padx=5)

        self.input_entry = tk.Entry(self.input_frame, width=50, font=('Arial', 12), bd=2, relief='groove')
        self.input_entry.pack(side=tk.LEFT, padx=5)

        # Botões com melhorias
        self.text_button = tk.Button(master, text="Gerar Texto", command=self.generate_text, bg='#4CAF50', fg='white', font=('Arial', 12))
        self.text_button.pack(pady=10)

        self.image_button = tk.Button(master, text="Gerar Imagem", command=self.generate_image, bg='#FFC107', fg='white', font=('Arial', 12))
        self.image_button.pack(pady=10)

        self.video_button = tk.Button(master, text="Gerar Vídeo", command=self.generate_video, bg='#FF5722', fg='white', font=('Arial', 12))
        self.video_button.pack(pady=10)

        # Botões para descrever imagem e transcrever áudio (sem campo de entrada)
        self.describe_button = tk.Button(master, text="Descrever Imagem", command=self.describe_image, bg='#2196F3', fg='white', font=('Arial', 12))
        self.describe_button.pack(pady=10)

        self.audio_button = tk.Button(master, text="Transcrever Áudio", command=self.audio_to_text, bg='#673AB7', fg='white', font=('Arial', 12))
        self.audio_button.pack(pady=10)

        # Barra de status
        self.status_bar = tk.Label(master, text="Pronto", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg='#f0f0f0')
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def generate_text(self):
        text_prompt = self.input_entry.get()  # Obtém o texto do campo de entrada
        if text_prompt.strip():  # Verifica se o campo não está vazio
            text_gen = TextGenerator()
            generated_text = text_gen.generate_text(text_prompt)
            messagebox.showinfo("Texto Gerado", generated_text)
            self.status_bar.config(text="Texto gerado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Por favor, digite um prompt válido.")

    def describe_image(self):
        image_path = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Arquivos de Imagem", "*.jpg;*.jpeg;*.png")])
        if image_path:
            describer = ImageDescriber()
            descricao_traduzida = describer.process_image(image_path)
            messagebox.showinfo("Descrição da Imagem", descricao_traduzida)
            self.status_bar.config(text="Imagem descrita com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Nenhuma imagem selecionada.")

    def generate_image(self):
        image_prompt = self.input_entry.get()  # Obtém o texto do campo de entrada
        if image_prompt.strip():  # Verifica se o campo não está vazio
            image_gen = ImageGenerator()
            image_gen.process_image(image_prompt)
            messagebox.showinfo("Imagem Gerada", "A imagem foi gerada e salva com sucesso!")
            self.status_bar.config(text="Imagem gerada com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Por favor, digite um prompt válido.")

    def generate_video(self):
        video_texts = self.input_entry.get().split(",")  # Obtém o texto do campo de entrada e divide em uma lista
        if any(video_texts):  # Verifica se a lista não está vazia
            video_filename = "video_gerado.mp4"
            video_gen = VideoGenerator()
            video_gen.process_video(video_texts, video_filename)
            messagebox.showinfo("Vídeo Gerado", "O vídeo foi gerado com sucesso!")
            self.status_bar.config(text="Vídeo gerado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Por favor, insira pelo menos um texto para o vídeo.")

    def audio_to_text(self):
        audio_file_path = select_audio_file()  # Seleciona o arquivo de áudio
        if audio_file_path:  # Verifica se um arquivo foi selecionado
            try:
                transcribed_text = transcribe_audio(audio_file_path)  # Transcreve o áudio
                messagebox.showinfo("Texto Transcrito", transcribed_text)  # Exibe o texto transcrito
                self.status_bar.config(text="Áudio transcrito com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro na transcrição: {e}")
        else:
            messagebox.showwarning("Atenção", "Nenhum arquivo de áudio selecionado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

