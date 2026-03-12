import os
import shutil
import locale

# 1. Configuração de Idioma
# Tenta detectar o idioma do sistema (ex: 'pt_BR' ou 'en_US')
idioma_sistema = locale.getdefaultlocale()[0]
lang = "pt" if idioma_sistema and idioma_sistema.startswith("pt") else "en"

# Dicionário de tradução
texts = {
    "pt": {
        "photos": "Fotos",
        "videos": "Videos",
        "audio": "Audio",
        "cleaning": "Limpando a pasta",
        "done": "--- Tudo limpo! ---",
        "photo_msg": "Foto organizada",
        "video_msg": "Vídeo organizado",
        "audio_msg": "Áudio organizado"
    },
    "en": {
        "photos": "Photos",
        "videos": "Videos",
        "audio": "Audio",
        "cleaning": "Cleaning folder",
        "done": "--- All done! ---",
        "photo_msg": "Photo organized",
        "video_msg": "Video organized",
        "audio_msg": "Audio organized"
    }
}

# 2. Definição de Caminhos
user = os.getlogin()
downloads_folder = f"C:/Users/{user}/Downloads"

# Pastas usando o idioma detectado
photos_folder = os.path.join(downloads_folder, texts[lang]["photos"])
videos_folder = os.path.join(downloads_folder, texts[lang]["videos"])
audio_folder = os.path.join(downloads_folder, texts[lang]["audio"])

# Extensões
photo_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
video_extensions = [".mp4", ".mkv", ".mov", ".avi", ".wmv"]
audio_extensions = [".mp3", ".wav"]

def organize_downloads():
    # Criar pastas se não existirem
    for folder in [photos_folder, videos_folder, audio_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    print(f"{texts[lang]['cleaning']}: {downloads_folder}...")
    
    for file_name in os.listdir(downloads_folder):
        old_path = os.path.join(downloads_folder, file_name)
        
        if os.path.isdir(old_path):
            continue
            
        extension = os.path.splitext(file_name)[1].lower()

        # Lógica de movimentação com mensagens traduzidas
        if extension in photo_extensions:
            shutil.move(old_path, os.path.join(photos_folder, file_name))
            print(f"{texts[lang]['photo_msg']}: {file_name}")

        elif extension in video_extensions:
            shutil.move(old_path, os.path.join(videos_folder, file_name))
            print(f"{texts[lang]['video_msg']}: {file_name}")

        elif extension in audio_extensions:
            shutil.move(old_path, os.path.join(audio_folder, file_name))
            print(f"{texts[lang]['audio_msg']}: {file_name}")

if __name__ == "__main__":
    organize_downloads()
    print(texts[lang]["done"])
