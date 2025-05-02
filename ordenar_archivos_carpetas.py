import os
import shutil

#Rutas donde estas los archivos y carpetas
ruta_archivos = "C:/Users/PC/Documents"
# Crear carpetas en destino sino existen
tipos=["Imagenes","PDFs","Videos","Documentos_Word","Documentos_Excel"]

for carpeta in tipos:
        if not os.path.exists(os.path.join(ruta_archivos,carpeta)):
            os.makedirs(os.path.join(ruta_archivos,carpeta))
        
# Obtener la lista de archivos en la ruta
for archivo in os.listdir(ruta_archivos):
    # Verificar si es un archivo
    if os.path.isfile(os.path.join(ruta_archivos, archivo)):
        # Obtener la extensión del archivo
        extension = archivo.split(".")[-1].lower()
        
        # Mover el archivo a la carpeta correspondiente según su extensión
        if extension in ["jpg", "jpeg", "png", "gif"]:
            shutil.move(os.path.join(ruta_archivos, archivo), os.path.join(ruta_archivos, "Imagenes", archivo))
        elif extension in ["pdf"]:
            shutil.move(os.path.join(ruta_archivos, archivo), os.path.join(ruta_archivos, "PDFs", archivo))
        elif extension in ["docx"  , "doc"]:
            shutil.move(os.path.join(ruta_archivos, archivo), os.path.join(ruta_archivos, "Documentos_Word", archivo))
        elif extension in ["xlsx"  , "xls"]:
            shutil.move(os.path.join(ruta_archivos, archivo), os.path.join(ruta_archivos, "Documentos_Excel", archivo))