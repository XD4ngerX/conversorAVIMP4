import os

def convert_avi_to_mp4(avi_file_path, nome):
    
     
    # converter um arquivo avi para mp4 usando o FFmpeg

    # aqui os parametros
    # avi_file_path:  caminho do arquivo avi que será convertido
    # nome: nome do arquivo que será dado após a conversão

    # retorno:
    # bool: Retorna True após completar a conversão
    
    command = f'ffmpeg -i "{avi_file_path}" -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 "{nome}.mp4"'
    os.system(command)  # Usando os.system para ver o resultado no terminal
    return True

print(f"Diretório atual: {os.getcwd()}")
path = 'videos'

for arquivo in os.listdir(path) : # vê os arquivos dentro da pasta videos
    if arquivo.endswith (".avi"):# se o arquivo terminar com .avi, ele converte
        full_path = os.path.join(path, arquivo) # pega o nome do caminho completo, sendo videos/arquivo 
        nomeArquivo = os.path.splitext(os.path.basename(full_path))[0] #retira a extensão do arquivo, no caso o .avi
        convert_avi_to_mp4(full_path, os.path.join(path,nomeArquivo)) #converte :)

print("operação concluida")