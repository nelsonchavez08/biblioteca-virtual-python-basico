def buscar_libro(codigo,lista):
    for i,j in lista.items():
        if i==codigo:
            return j["titulo"], j["autor"], j["estado"]
    return False
        
def duplicados(codigo,lista):
    contador=0
    for i,j in lista.items():
        if codigo==i:
            contador+=1
    if contador>=1:
        return False
    if contador==0:
        return True

def cambiar_estado_libro(codigo,lista):
    for i,j in lista.items():
        if i==codigo:
            if j["estado"]=="Disponible":
                j["estado"]="Prestado"
                return False
            elif j["estado"]=="Prestado":
                j["estado"]="Disponible"
                return True

def eliminar_libro(codigo,lista):
    lista.pop(codigo)

def libros_disponibles(lista):
    disponibles=[]
    for i,j in lista.items():
        if j["estado"]=="Disponible":
            disponibles.append((i,j["titulo"]))
    return disponibles

def libros_prestados(lista):
    disponibles=[]
    for i,j in lista.items():
        if j["estado"]=="Prestado":
            disponibles.append((i,j["titulo"]))
    return disponibles

def validar_codigo(codigo):
    if len(codigo)!=7:
        return 0
    letras=codigo[:2]
    numeros=codigo[3:]
    separador=codigo[2]
    if letras.isalpha() and numeros.isdigit() and separador=="-":
        return 1
    elif letras.isalpha() and numeros.isdigit():
        return 2

def validacion_texto(texto):
    if len(texto)==0:
        return False
    contador=0
    for i in texto:
        if i.isalpha():
            contador+=1
    if contador>=1:
        return True
    else:
        return False
    
def exportar_libros(ruta):
    libros={}
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea=linea.strip()
                if not linea:
                    continue
                partes=linea.split(",")
                if len(partes) < 4:
                    continue
                try:
                    codigo_libro=partes[0]
                    libros[codigo_libro]={
                        "titulo":partes[1],
                        "autor":partes[2],
                        "estado":partes[3]
                    }
                except ValueError:
                    continue
    except FileNotFoundError:
        return{}
    except Exception as e:
        print(f"error al leer {ruta}:{e}")
    return libros

def actualizar_archivo(ruta, lista):
    with open(ruta, "w", encoding="utf-8") as archivo:
        for codigo, datos in lista.items():
            archivo.write(f"{codigo},{datos['titulo']},{datos['autor']},{datos['estado']}\n")