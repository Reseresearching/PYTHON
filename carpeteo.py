
#Import os Library
import os
s=1
while s==1:
    USERS=input("Como te llamas para crearte una carpeta de usuario")
    print(os.getcwd())


    #EXISTE? LA CARPETA?
    condicion=os.path.exists(USERS)
    if condicion:  #si el usuario que han creado existe....
        print("el nombre de usuario ya existe de antes")
 #       break
    else:
        #USERS="NOMBREDELACARPETA"
        #coge el actual directorio donde este y crea ahi despue
        os.getcwd()
        # Create Directory
        os.mkdir(USERS)
        #entra en el directorio
        os.chdir(USERS)
        #qué tipo de archivo quieres crear
        archivosQueQuieroCreartxt=input("introduce el nombre del archivo ejemplo: a.txt")
        
        #existe un archivo con ese nombre?
        condicion2=os.path.exists(archivosQueQuieroCreartxt)
        #comprueba que no se repita
        if condicion2:   #si existe 
            print("el nombre de usuario ya existe de antes")
            break
        else:
            #crea un txt
            with open(archivosQueQuieroCreartxt,"w")as f:   #w o a para agregar
                f.write("hola")
            #archivosQueQuieroCrear=input("introduce los archivos que quieres crear  ejemplo a.txt,b.txt,c.txt")
            
        #sal de la carpeta que has entrado:        
            os.chdir("..")
