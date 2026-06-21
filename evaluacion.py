import funciones as fun
libro={}
libro=(fun.exportar_libros(ruta="libros.txt"))
while True:
    try:
        print("=====================================================================")
        print("Bienvenido a la biblioteca virtual")
        print("=====================================================================")
        print("Ingrese el valor numero según lo que necesite")
        print("1. Ingresar un nuevo libro")
        print("2. Buscar un libro")
        print("3. Cambiar el estado de un libro")
        print("4. Eliminar un libro")
        print("5. Imprimir los libros disponibles")
        print("6. Imprimir los libros prestados")
        print("7. Salir")
        opc=int(input())
        if opc==1:
            while True:
                ####################################SOLICITAR CODIGO+VALIDACION#############################################
                codigo_libro=input("ingresa el codigo del libro (AA-XXXX)(A es carácter alfabetico y X es digito)\n").lower()
                validacion=fun.validar_codigo(codigo_libro)
                validar_duplicados=fun.duplicados(codigo=codigo_libro,lista=libro)
                if validacion==0:
                    print("El dato ingresado no contiene 7 carácteres")
                elif validacion==1:
                    if validar_duplicados:
                        break
                    elif not validar_duplicados:
                        print("este codigo ya existe, intenta uno diferente")
                elif validacion==2:
                    print("""Debes ingresar "-" para separar caracter alfabetico de digito (AA-XXXX)""")
                else:
                    print("Codigo incorrecto, vuelve a intentar")
            while True:
                ##############################SOLICITAR TITULO+VALIDACION####################################
                titulo_libro=input("ingresa el titulo del libro\n").lower()
                validar_texto=fun.validacion_texto(titulo_libro)
                if validar_texto:
                    break
                else:
                    print("No deben haber espacios en blanco y debe haber 1 o mas carácteres alfabeticos")
            while True:
                ###############################SOLICITAR AUTOR+VALIDACION#########################
                autor_libro=input("Ingrese el nombre del autor de este libro\n")
                validar_texto=fun.validacion_texto(autor_libro)
                if validar_texto:
                    break
                else:
                    print("No deben haber espacios en blanco y debe haber 1 o mas carácteres alfabeticos")
            ######################################AGREGAR AL DICCIONARIO + AL DOCUMENTO##############################################
            libro[codigo_libro]={"titulo":titulo_libro,
                                "autor":autor_libro,
                                "estado":"Disponible"}
            with open("libros.txt","a",encoding="UTF=8") as archivo:
                archivo.write(f"{codigo_libro},{titulo_libro},{autor_libro},Disponible\n")
        elif opc==2:
            while True:
                codigo=input("Ingrese el codigo del libro que desea buscar\n").lower()
                validar_codigo=fun.validar_codigo(codigo)
                if validar_codigo==0:
                    print("El codigo debe tener 7 digitos")
                elif validar_codigo==2:
                    print("Recuerda que el formato de texto es AA-0000")
                elif validar_codigo==1:
                    libro_encontrado=fun.buscar_libro(codigo=codigo,lista=libro)
                    if not libro_encontrado:
                        print("Libro no encontrado, vuelve a intentar")
                    else:
                        titulo,autor,estado=libro_encontrado
                        print(f"El libro con codigo {codigo}, se llama {titulo}, su autor es {autor} y su estado es {estado}")
                        break
                else:
                    print("codigo incorrecto")
        elif opc==3:
            while True:
                codigo=input("Ingrese el codigo del libro que desea cambiar de estado\n").lower()
                cambiar_estado=fun.cambiar_estado_libro(codigo,libro)
                fun.actualizar_archivo("libros.txt",libro)
                if cambiar_estado:
                    print(f"El libro con codigo {codigo} se ha cambiado a Disponible")
                    break
                elif not cambiar_estado:
                    print(f"El libro con codigo {codigo} se ha cambiado a Prestado")
                    break
        elif opc==4:
            while True:
                codigo=input("Ingrese el codigo del libro que desea eliminar\n").lower()
                validar_codigo=fun.validar_codigo(codigo)
                if validar_codigo==0:
                    print("El codigo debe tener 7 digitos")
                elif validar_codigo==2:
                    print("Recuerda que el formato de texto es AA-0000")
                elif validar_codigo==1:
                    libro_encontrado=fun.buscar_libro(codigo=codigo,lista=libro)
                    if not libro_encontrado:
                        print("Libro no encontrado, vuelve a intentar")
                    else:
                        while True:
                            titulo,autor,estado=libro_encontrado
                            validar_eliminar=input(f"Estas seguro de eliminar el libro de codigo:{codigo} titulo:{titulo} del autor:{autor}? (si/no)\n").lower()
                            if validar_eliminar=="si":
                                fun.eliminar_libro(codigo=codigo,lista=libro)
                                fun.actualizar_archivo("libros.txt",libro)
                                print("Libro eliminado con exito")
                                break
                            elif validar_eliminar=="no":
                                print("El libro no se eliminó")
                                break
                        break
                else:
                    print("codigo incorrecto")
        elif opc==5:
            libros_disponibless=fun.libros_disponibles(libro)
            print(f"los libros que se encuentran disponibles son los siguientes:{libros_disponibless}")
        elif opc==6:
            libros_prestados=fun.libros_prestados(libro)
            print(f"los codigos+nombres de libros que se encuentran prestados son los siguientes:{libros_prestados}")
        elif opc==7:
            break
        else:
            print("Ingrese un valor dentro del rango")
    except ValueError:
        print(f"Ingrese valores numericos")