import os
import shutil
from tkinter import filedialog, Tk

#Rutas donde estas los archivos y carpetas
# ruta_archivos = "C:/Users/PC/Documents"
# Crear carpetas en destino sino existen
# tipos=["Imagenes","PDFs","Videos","Documentos_Word","Documentos_Excel"]
extensiones={
    ".jpg":"Imagenes",
    ".png":"Imagenes",
    ".pdf":"PDFs",
    ".mp4":"Videos",
    ".docx":"Documentos_Word",
    ".xlsx":"Documentos_Excel",
    ".xls":"Documentos_Excel",
}
Ventana = Tk()
Ventana.withdraw()
ruta_archivos=filedialog.askdirectory(title="Selecciona la carpeta donde están los archivos")
for carpeta in set(extensiones.values()):
        ruta_carpeta = os.path.join(ruta_archivos, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)

for  archivo in os.listdir(ruta_archivos):
    ruta_archivo = os.path.join(ruta_archivos, archivo)
    if os.path.isfile(ruta_archivo):
        _, extension = os.path.splitext(archivo)
        extension = extension.lower()
        if extension in extensiones:
            carpeta_destino = extensiones[extension]
            ruta_destino = os.path.join(ruta_archivos, carpeta_destino, archivo)
            shutil.move(ruta_archivo, ruta_destino)
            print(f"Moviendo {archivo} a {carpeta_destino}")
        else:
            print(f"No se encontró la extensión de {archivo}")