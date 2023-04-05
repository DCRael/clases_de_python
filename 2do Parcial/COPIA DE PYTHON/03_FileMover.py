from PIL import Image
import os

downloadsFolder = r"/Users/garci/OneDrive/Documentos/Universidad_Oriente/Cuatrimestre 2/Programación 1/2do Parcial/COPIA DE PYTHON/FDownloads/"
files = os.listdir(downloadsFolder)

picturesFolder = r"/Users/garci/OneDrive/Documentos/Universidad_Oriente/Cuatrimestre 2/Programación 1/2do Parcial/COPIA DE PYTHON/FDownloads/Pictures/"
videoFolder = r"/Users/garci/OneDrive/Documentos/Universidad_Oriente/Cuatrimestre 2/Programación 1/2do Parcial/COPIA DE PYTHON/FDownloads/Video/"
audioFolder = r"/Users/garci/OneDrive/Documentos/Universidad_Oriente/Cuatrimestre 2/Programación 1/2do Parcial/COPIA DE PYTHON/FDownloads/Audio/"

if __name__ == "__main__":
    for filename in files:
        name,extension = os.path.splitext(downloadsFolder+filename)
        if extension in[".jpg",".png",".jpeg"]:
            picture=Image.open(downloadsFolder+filename)
            picture.save(downloadsFolder+'compressed_'+filename, optimize=True, quality=60)
            os.remove(downloadsFolder+filename)

        if extension in [".mp3"]:
            os.rename(downloadsFolder + filename, audioFolder + filename)

        if extension in [".mp4"]:
            os.rename(downloadsFolder + filename, videoFolder + filename)