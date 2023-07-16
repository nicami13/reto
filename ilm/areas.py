import os
import core
import detalles
diccPersona={'data':[]}
diccArea={'data':[]}





def cargar_persona():
    global diccPersona

    if (core.checkFile("personas.json")):
        diccPersona = core.LoadInfo("personas.json")
    else:
        core.crearInfo("personas.json",diccPersona)
def cargar_area():

    global diccArea

    if (core.checkFile('areas.json')):
        diccArea = core.LoadInfo('areas.json')
    else:
        core.crearInfo('areas.json',diccArea)

def mainMenu():
    global area
    area = {
      'id': '',
      'nombre': '',
      'salones':[]
      
    }
    
    while True:
        os.system('clear')
        print("╔═══════════════════════════════════╗")
        print("║            MENÚ AREAS             ║")
        print("╠═══════════════════════════════════╣")
        print("║ 1.INGRESAR NOMBRE E ID DE AREA    ║")
        print("║═══════════════════════════════════║")
        print("║ 2.INGRESAR SALON(ES) DEL AREA     ║")
        print("║═══════════════════════════════════║")
        print("║ 0.REGRESAR AL MENU PRINCIPAL      ║")
        print("╚═══════════════════════════════════╝")
       
            
        op=input('SELECCION:')

        if(int(op)==1):
         os.system('clear')
        
         area['nombre']=input('ingresa el nombre del area:')
         area['id']=input('ingresa el ID del area: ')
         os.system('pause')
         os.system('clear')
        if(int(op)==2):
            os.system('clear')


            can=input(f'ingresar la cantidad de salones actuales en el area {area["nombre"]}: ')

            for _ in range(int(can)):
                os.system('clear')
                print("╔═══════════════════════════════════╗")
                print("║            MENÚ SALONES           ║")
                print("╚═══════════════════════════════════╝")
                salon= {
                'ids': '',
                'nom': '',
                'trainer':'',
                'ma':[]}
                salon['ids']=input('ingresar el ID del salon: ')
                salon['nom']=input('ingresar nombre del salon: ')
                for i,item in enumerate(diccPersona['data']):
                    if item['tipo']=='Trainer':
                        print(i,'.','NOMBRE DEL TRAINER:',item['nombre'],' C.C:',item['id'])
                se=input('ingrese la numeracion del trainer deseado: ')
                trainer_seleccionado=diccPersona['data'][int(se)]
                salon['trainer']=trainer_seleccionado
                area['salones'].append(salon)
            diccArea['data'].append(area)
            core.crearInfo('areas.json',area)
        if(int(op)==0):
            os.system('clear')
            
            detalles.pantalla_carga()
            break
        
    
                
                




    




      
