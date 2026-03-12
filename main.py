import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma pasta')

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "audios": [".mp3", ".wav", ".ogg"],
    "documentos": [".docx", ".txt"],
    "planilhas": [".xlsx"],
    "pdf": [".pdf"],
    "csv": [".csv"],
    "executáveis": [".exe"]
} 

for arquivo in lista_arquivos:
    # 01. Arquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.makedirs(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")