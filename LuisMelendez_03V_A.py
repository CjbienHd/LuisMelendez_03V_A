import funciones as fn
sueldo = []

trabajadores = ["Juan Pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","MiguelSánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
while True:
    print("----MENU PRINCIPAL----")
    print("1. Asignar sueldos aletorios\n 2. Clasificar sueldos\n 3. Ver estadisticas\n 4.Reporte de sueldos\n 5. Salir ")
    while True:
        try:
            opcion = int(input("Ingrese eleccion :"))
            break
        except:
            print("Ingrese solo valores numericos")
    
    if opcion == 1:
        fn.asignar_sueldos_trabajadores(trabajadores)
    elif opcion == 2:
        fn.clasificar_sueldos(fn.asignar_sueldos_trabajadores(trabajadores))
    elif opcion == 3:
        fn.ver_estadisticas()
    elif opcion == 4:
        fn.reporte_sueldos(fn.ver_estadisticas())
    else:
        print("Finalizando programa\n Desarrollado por Luis Melendez\n RUT 21.302.168-0")
        break


