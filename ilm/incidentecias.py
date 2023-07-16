import os
import core
import detalles

diccInc = {'data': []}
diccArea = core.LoadInfo('areas.json')
diccPersonas = core.LoadInfo('personas.json')


def cargar_incidencias():
    global diccInc

    if core.checkFile("incidencias.json"):
        diccInc = core.LoadInfo("incidencias.json")
    else:
        core.crearInfo("incidencias.json", diccInc)


def mainMenu():
    inci = {
        'trainer': '',
        'categoria': '',
        'area': {'noma': '', 'ida': ''},
        'salon': {'s1': '', 's2': '', 's3': ''},
        'descripcion': '',
        'maquina': {'m1': '', 'm2': '', 'm3': ''}
    }
    print("╔═══════════════════════════════════╗")
    print("║       VERIFICACION DE TRAINER     ║")
    print("╚═══════════════════════════════════╝")
    nombre = input('NOMBRE:')
    id = input('ID:')
    os.system('clear')
    for item in diccPersonas['data']:
        if item['nombre'] == nombre and item['id'] == id and item['tipo'] == 'Trainer':
            inci['trainer'] = nombre
            for i, item in enumerate(diccArea['data']):
                print("╔═══════════════════════════════════╗")
                print("║        SELECCION DE AREA          ║")
                print("╚═══════════════════════════════════╝")
                print(i, '. NOMBRE:', diccArea['nombre'], ' IDENTIFICADOR:', diccArea['id'])
            op = input('SELECION:')
            os.system('clear')
              
            op = input('SELECCION:')
            if i == int(op):
                area_seleccionada = diccArea['data'][int(op)]
                inci['area']['noma'] = area_seleccionada['nombre']
                inci['area']['ida'] = area_seleccionada['id']
                os.system('clear')
                print("╔═══════════════════════════════════╗")
                print("║         SELECCION DE SALON        ║")
                print("╚═══════════════════════════════════╝")
                for a, t in enumerate(area_seleccionada['salones']):
                    print(a, '.', 'NOMBRE:', t['nom'], ' ID:', t['ids'])
                o = input('SELECCION:')
                salon_seleccionado = area_seleccionada['salones'][int(o)]
                inci['salon']['s1'] = salon_seleccionado['nom']
                inci['salon']['s2'] = salon_seleccionado['ids']
                inci['salon']['s3'] = salon_seleccionado['trainer']
                os.system('clear')
                print("╔═══════════════════════════════════╗")
                print("║        SELECCION DE EQUIPO        ║")
                print("╚═══════════════════════════════════╝")
                for n, m in enumerate(salon_seleccionado['ma']):
                    print(n, '.', 'NOMBRE:', m['nomm'], ' ID:', m['idm'], '   MARCA:', m['marca'])
                c = input('SELECCIO: ')
                maquina_seleccionada = salon_seleccionado['ma'][int(c)]
                inci['maquina']['m1'] = maquina_seleccionada['nomm']
                inci['maquina']['m2'] = maquina_seleccionada['idm']
                inci['maquina']['m3'] = maquina_seleccionada['marca']
                os.system('clear')
                print("╔═══════════════════════════════════╗")
                print("║       SELECCION DE CATEGORIA      ║")
                print("╚═══════════════════════════════════╝")
                print('¿De qué categoría es la incidencia?')
                a = 'Software'
                b = 'Hardware'
                print('1.', a)
                print('2.', b)
                op = input('SELECCION:')
                if int(op) == 1:
                    inci['categoria'] = a
                    print("╔═══════════════════════════════════╗")
                    print("║       SELECCION DE CATEGORIA      ║")
                    print("╚═══════════════════════════════════╝")
                    print('Ingresa una pequeña descripción del problema\nque se presenta en el equipo\n')
                    inci['descripcion'] = input(':')

                if int(op) == 2:
                    inci['categoria'] = b
                    print("╔═══════════════════════════════════╗")
                    print("║       SELECCION DE CATEGORIA      ║")
                    print("╚═══════════════════════════════════╝")
                    print('Ingresa una pequeña descripción del problema\nque se presenta en el equipo\n')
                    inci['descripcion'] = input(':')

    diccInc['data'].append(inci)
    core.crearInfo('incidencias.json', diccInc)
    detalles.pantalla_carga()

                    

                         
                
