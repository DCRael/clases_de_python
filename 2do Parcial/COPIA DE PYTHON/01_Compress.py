#python3 -m pip install Pillow
from PIL import Image
import os 

downloadsFolder = r"C:/Users/garci/OneDrive/Documentos/Universidad_Oriente/Cuatrimestre 2/Programación 1/2do Parcial/COPIA DE PYTHON/FDownloads/"
files= os.listdir(downloadsFolder)

if __name__ == "__main__":
    for filename in files:
        name,extension = os.path.splitext(downloadsFolder+filename)
        if extension in[".jpg",".png",".jpeg"]:
            picture=Image.open(downloadsFolder+filename)
            picture.save(downloadsFolder+'compressed_'+filename, optimize=True, quality=60)