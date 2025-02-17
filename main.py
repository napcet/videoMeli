import os
import subprocess

def download_video(m3u8_url, output_path):
    print(f"Baixando o vídeo de: {m3u8_url}")

    # Verifica se ffmpeg está instalado
    if subprocess.run(["ffmpeg", "-version"], capture_output=True).returncode != 0:
        raise Exception("ffmpeg não está instalado ou não está no PATH.")

    command = [
        "ffmpeg",
        "-i", m3u8_url,
        "-c", "copy",
        output_path
    ]
    
    subprocess.run(command, check=True)
    print(f"Vídeo salvo em: {output_path}")

def main():
    m3u8_url = input("Digite o link do índice .m3u8: ").strip()
    anuncio_codigo = input("Digite o código do anúncio: ").strip()

    # Formata o nome do arquivo de saída
    output_path = f"MLB{anuncio_codigo}.mp4"

    try:
        download_video(m3u8_url, output_path)
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
