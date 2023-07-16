import os 
import core

diccPersona={'data':[]}
def cargar_persona():
    global diccPersona

    if (core.checkFile("personas.json")):
        diccPersona = core.LoadInfo("personas.json")
    else:
        core.crearInfo("personas.json",diccPersona)

def mainMenu():

    run =True
    while run:
        os.system('clear')
        print("╔═══════════════════════════════════╗")
        print("║          MENU DE USUARIO          ║")
        print("╠═══════════════════════════════════╣")
        print("║ 1.INGRESAR USUARIO                ║")
        print("║═══════════════════════════════════║ ")
        print("║ 0.REGRESAR AL MENU PRINCIPAL      ║")
        print("╚═══════════════════════════════════╝")
        
        op=input(':')
        os.system('clear')
        if(int(op)==1):
            persona={
                'id':'',
                'nombre':'',
                'email':'',
                'tel':'',
                'tipo':''
                }
            print('elige el tipo de usuario que eres.')
            print(' 1.Trainer.\n','2.Camper.\n','3.Abministrador.\n','4.Tutor Review.')
            o=input(':')
            os.system('clear')
            if(int(o)==1):
                persona['tipo']='Trainer'
            if(int(o)==2):
                persona['tipo']='Camper'
            if(int(o)==3):
                persona['tipo']='Administrador'
            if(int(o)==4):
                persona['tipo']='Tutor review'
            if(int(o)>4 or int(o)== str):
                print('Tipo de usuario no valido.')
                os.system('clear')
                print('elige el tipo de usuario que eres.')
                print('1.Trainer.\n','2.Camper.\n','3.Abministrador.\n','4.Tutor Review.')
                o=input(':')  
                os.system('clear')    
                if(int(o)==1):
                    persona['tipo']='Trainer'
                if(int(o)==2):
                    persona['tipo']='Camper'
                if(int(o)==3):
                    persona['tipo']='Administrador'
                if(int(o)==4):
                    persona['tipo']='Tutor review' 
            x1=f'ingresar su nombre {persona["tipo"]} :'
            x2=f'ingresar su c.c {persona["tipo"]} :'
            x3=f'ingresar su EMAIL {persona["tipo"]} :'
            x4=f'ingresar su numero telefonico {persona["tipo"]} :'
            persona['nombre']=input(x1)
            persona['id']=input(x2)   
            persona['email']=input(x3)   
            persona['tel']=input(x4)   
            diccPersona['data'].append(persona)
            core.crearInfo('personas.json',persona)
            os.system('clear')
        elif (int(op) == 0):
            break
        if(int(op)>1 or int(op)== str):
            print('opcion invalida :(')
            break
        