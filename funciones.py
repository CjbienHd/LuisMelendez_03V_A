import random as rd
import statistics as st
trabajadores = ["Juan Pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","MiguelSánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = {}
sueldos_menores_800000 = {}
sueldos_entre_800000_2000000 = {}
sueldos_mayores_2000000 = {}
sueldo = []

def asignar_sueldos_trabajadores(trabajadores):
    for trabajador in trabajadores:
        sueldos[trabajador] = rd.randint(300000, 2500000)
    return sueldos

def clasificar_sueldos(sueldos):
    for trabajador in sueldos:
        if sueldos[trabajador] < 800000:
            sueldos_menores_800000[trabajador] = sueldos[trabajador]
        elif sueldos[trabajador] >= 800000 and sueldos[trabajador] <= 2000000:
            sueldos_entre_800000_2000000[trabajador] = sueldos[trabajador]
        else:
            sueldos_mayores_2000000[trabajador] = sueldos[trabajador]
    print("SUELDOS MENORES A 800.000 :",len(sueldos_menores_800000))
    print(sueldos_menores_800000)
    print("SUELDOS ENTRE 800.000 Y 2.000.000 :", len(sueldos_entre_800000_2000000))
    print(sueldos_entre_800000_2000000)
    print("SUELDOS MAYORES A 2.000.000 :", len(sueldos_mayores_2000000))
    print(sueldos_mayores_2000000)


def ver_estadisticas():
    sueldo = list(sueldos.values())
    sueldo_bajo = min(sueldo)
    sueldo_alto = max(sueldo)
    promedio = sum(sueldo) / len(sueldo)
    media_geometrica = st.mean(sueldo)
    print("el sueldo mas bajo es:", sueldo_bajo)
    print("el sueldo mas alto es:" , sueldo_alto)
    print("el promedio es:", promedio)
    print("La media geometrica es:", media_geometrica)
    return sueldo


def reporte_sueldos(sueldo):
    for i in sueldo:
        sueldo_liquido = (i * 0.12) - (i * 0.07)
    for trabajador in sueldos:
        sueldos[trabajador] = sueldo_liquido
        print(f"El sueldo liquido de {trabajador} es ${sueldo_liquido}")








    














    


