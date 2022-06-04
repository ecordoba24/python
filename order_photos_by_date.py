import os
import glob
import shutil

from PIL import Image
from PIL.ExifTags import TAGS

os.chdir('./')

if os.path.exists( 'fotos' ) == True:
    pass
else:
    os.mkdir( 'fotos' )

if os.path.exists( 'videos' ) == True:
    pass
else:
    os.mkdir( 'videos' )

while(True):
    JPG = glob.glob("*.JPG")
    JPEG = glob.glob("*.JPEG")

    for i in (JPG):
        print ( i )
        imagename = i
        image = Image.open(imagename)
        exifdata = image.getexif()
        image.close()

        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            if tag == 'DateTime' and data != "" :
                tiempo = data
                nueva_carpeta = tiempo[0:10]
                nueva_carpeta = nueva_carpeta.replace(":", "_")

                if os.path.exists( 'fotos/' + nueva_carpeta ) == True:
                    pass
                else:
                    os.mkdir( 'fotos/' + nueva_carpeta )
                    print( 'se creo la carpeta fotos/' + nueva_carpeta )

                if os.path.exists( 'fotos/' + nueva_carpeta + '/' + i ) == True:
                    pass
                else:
                    shutil.move( i, 'fotos/' + nueva_carpeta )
                    print('Se movio a fotos/' + nueva_carpeta + '/' + i )

            if isinstance(data, bytes):
                data = data.decode()

    for i in (JPEG):
        print ( i )
        imagename = i
        image = Image.open(imagename)
        exifdata = image.getexif()
        image.close()
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            if tag == 'DateTime' and data != "" :
                tiempo = data
                nueva_carpeta = tiempo[0:10]
                nueva_carpeta = nueva_carpeta.replace(":", "_")

                if os.path.exists( 'fotos/' + nueva_carpeta ) == True:
                    pass
                else:
                    os.mkdir( 'fotos/' + nueva_carpeta )
                    print( 'se creo la carpeta fotos/' + nueva_carpeta )

                if os.path.exists( 'fotos/' + nueva_carpeta + '/' + i ) == True:
                    pass
                else:

                    shutil.move( i, 'fotos/' + nueva_carpeta )
                    print('Se movio a fotos/' + nueva_carpeta + '/' + i )