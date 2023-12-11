from PIL import Image
import os
direccion ="C:/Users/sara alcala/Pictures/fotos/"
imagenes = "C:/Users/sara alcala/Pictures/orden/"
if __name__ == "__main__":
    for nombre in os.listdir(direccion):
        archivo ,extencion = os.path.splitext(direccion + nombre)

        if extencion in[".jpg",".png",".jpeg", ".PNG"]:
            picture = Image.open(direccion + nombre)
            picture.save(imagenes + "comprimir_" + nombre , optimize=True , quality=60)
            os.remove(direccion + nombre)
            print(archivo +":" + extencion)

        if extencion in [".xlsx"]:  
            excel  = "C:/Users/sara alcala/Pictures/ecxel/"
            os.rename(direccion + nombre, excel + nombre)
