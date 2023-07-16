import json
import os

def crearInfo(*args):
    if checkFile(args[0]) == False:
        with open('data/' + args[0], "w") as write_file:
            json.dump(args[1], write_file, indent=4)
    else:
        with open('data/' + args[0], 'r+') as file:
            file_data = json.load(file)
            file_data["data"].append(args[1])
            file.seek(0)
            json.dump(file_data, file, indent=4)
            file.truncate()

def editarInfo(fileName, newData):
    if checkFile(fileName):
        with open('data/' + fileName, 'r+') as file:
            file_data = json.load(file)
            # Realiza la edición en el archivo data
            # Puedes modificar el código según tus necesidades para editar los datos existentes

            # Aquí hay un ejemplo que actualiza la clave "data" con los nuevos datos
            file_data["data"] = newData

            file.seek(0)
            json.dump(file_data, file, indent=4)
            file.truncate()
        return True
    else:
        return False

def LoadInfo(fileName):
    if checkFile(fileName):
        with open('data/' + fileName, "r") as read_file:
            dicc = json.load(read_file)
        return dicc

def checkFile(fileName):
    try:
        with open('data/' + fileName, 'r') as f:
            return True
    except FileNotFoundError as e:
        print("Error: El archivo no existe")
        return False
    except IOError as e:
        return False
