import core
import detalles
import os

diccArea = {'data': []}


def cargar_machine():
    global diccArea
    if core.checkFile("areas.json"):
        diccArea = core.LoadInfo('areas.json')
    else:
        core.crearInfo('areas.json', diccArea)


def mainMenu():
    os.system('clear')
    global area
    area = {
        'id': '',
        'nombre': '',
        'salones': [],
    }
    conl = 0
    while True:

        print("╔═══════════════════════════════════╗")
        print("║            INVENTARIO             ║")
        print("╠═══════════════════════════════════╣")
        print("║ 1.INGRESAR MAQUINA                ║")
        print("║═══════════════════════════════════║ ")
        print("║ 0.REGRESAR AL MENU PRINCIPAL      ║")
        print("╚═══════════════════════════════════╝")
        op = input('SELECCION:')
        os.system('clear')

        if int(op) == 1:
            maquinas_ingresadas = []

            maquina = {
                'idm': '',
                'nomm': '',
                'marca': ''
            }
            for i, item in enumerate(diccArea['data']):
                print("╔═══════════════════════════════════╗")
                print("║        SELECCION DE AREA          ║")
                print("╚═══════════════════════════════════╝")
                print(i, '. NOMBRE:', item['nombre'], ' IDENTIFICADOR:', item['id'])
            o = input('SELECION:')
            os.system('clear')
            if int(o) == i:
                area_seleccionada = diccArea['data'][int(o)]
                area['nombre'] = area_seleccionada['nombre']
                area['id'] = area_seleccionada['id']
                print("╔═══════════════════════════════════╗")
                print("║        SELECCION DE SALON         ║")
                print("╚═══════════════════════════════════╝")
                for i, it in enumerate(area_seleccionada['salones']):
                    print(i, '.', 'IDENTIFICADOR:', it['ids'], '  NOMBRE:', it['nom'], '  TRAINER:', it['trainer']['nombre'])

                p = input('SELECCION:')

                os.system('clear')
                salon_seleccionado = area_seleccionada['salones'][int(p)]
                for i, it in enumerate(area_seleccionada['salones']):
                    if (it != salon_seleccionado):
                        area['salones'].append(it)
                print("╔═══════════════════════════════════╗")
                print("║       INGRESO DE MAQUINAS         ║")
                print("╚═══════════════════════════════════╝")
                cantidad = input('ingresar la cantidad de maquinas que se ingresaran: ')
                os.system('clear')
                for _ in range(int(cantidad)):
                    print("╔═══════════════════════════════════╗")
                    print("║       INGRESO DE MAQUINAS         ║")
                    print("╚═══════════════════════════════════╝")
                    maquina['idm'] = input('ingresa el id del equipo: ')
                    maquina['nomm'] = input('ingresar el nombre del equipo: ')
                    maquina['marca'] = input('ingresar la marca del equipo: ')
                    maquinas_ingresadas.append(maquina.copy())
                salon_seleccionado['ma'].extend(maquinas_ingresadas)
                os.system('clear')
            area['salones'].append(salon_seleccionado)
            diccArea['data'] = area.copy()
            core.editarInfo('areas.json', area)

            conl += 1
            global ver
            ver = len(diccArea) - conl

        if ver == 0:
            detalles.pantalla_carga()
            break

        elif int(op) == 0:
            detalles.pantalla_carga()
            break
