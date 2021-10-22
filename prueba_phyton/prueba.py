import PyPDF2, shutil, os, time
from os import path
from datetime import datetime
Dicc={                                                                          #DICCIONARIO DE PALABRAS CLAVE
                "Epicrisis":        ["EPICRISIS"],
                "Facturas":         ["FACT"],
                "Historia_Clinica": ["HIST"],
                "Notas_de_Credito": ["CREDIT"],
                "Notas_de_Debito":  ["DEBIT"],
                "Orden_de_Remision":["REMIS"],
                "Orden_de_pedido":  ["PEDID"]
                }
nombre_archivo = 'prueba.py'                                                    #OBTENCIÓN DE RUTA PRINCIPAL
ruta = path.abspath(nombre_archivo)
x = ruta.split("\\")
x.pop()
ruta_final = "/".join(x)
while True:                                                                     #Inicio ciclo busqueda de Indices
    tiem=datetime.now().strftime('%Y%m%d_%H%M%S_')                              #Importar Hora local del sistema
    for filename in os.listdir(ruta_final+r'/REPOST'):                          
        if filename.endswith(("pdf")):                                          #Filtro de archivo por la extensión
            pdfFileObj=open(ruta_final+'\\REPOST\\'+filename, 'rb')             #Apertura del archivo
            pdfReader=PyPDF2.PdfFileReader(pdfFileObj)                          #Lectura del archivo
            pageObj=pdfReader.getPage(0)                                        #Extraer primera pagina del archivo
            var=pageObj.extractText()                                           #Asignacion del texto extraido a la variable
            var =var.upper()                                                    #Conversion del texto a mayuscula
            var=var.replace('\n',"")                                            #Eliminar los saltos de linea del texto
            pdfFileObj.close()                                                  #Cierre del documento pdf
            for x in Dicc:                                                      #Inicio del ciclo de busqueda de palabras clave
                estado = False
                for v in Dicc[x]:                                               #Busqueda de indice de acuerdo la palabra clave
                    indice=var.find(v)                                          #Busqueda de ubicacion de palabra clave
                    if (indice!=-1):                                            
                        index=v                                                 # Asignacion de nombre de carpeta 
                        src_path= ruta_final+r"\\REPOST\\"+filename             # ruta de carpeta de Origen de repositorio con el nombre del archivo
                        dst_path =ruta_final+r"\\GDOC\\"+x+"\\"+tiem+filename   # ruta de carpeta de destino 
                        shutil.move(src_path, dst_path)                         # Funcion de traslado de carpera de origen a carpeta de destino
                        estado= True
                        break                                                   # detencion de ciclo interno
                if (estado==True):
                    break                                                       #detencion de ciclo externo
            if (estado == False):                                               # Si el archivo no puede ser leido es enviado a la carpeta de documentos no reconocibles    
                src_path = ruta_final+r"\\REPOST\\"+filename
                dst_path = ruta_final+r"\\GDOC\\No Recocnocibles\\"+tiem+filename
                shutil.move(src_path, dst_path) 
        else:                                                                   #Si el archivo no tiene la extension .pdf es enviado a la carpeta de Documentos no admitidos
            src_path = ruta_final+r"\\REPOST\\"+filename
            dst_path = ruta_final+r"\\GDOC\\Documento no Admitido\\"+tiem+filename
            shutil.move(src_path, dst_path)
    time.sleep(5)                                                               # Duracion del ciclo