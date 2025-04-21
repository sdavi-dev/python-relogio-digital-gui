import tkinter as tk
from datetime import datetime

def relogio():

    texto_relogio.config(text=datetime.now().strftime("%H:%M:%S"))
    janela.after(1000, relogio)
        


janela = tk.Tk()
janela.title("Projeto de Relógio Digital")
janela.geometry("300x200")

texto_relogio = tk.Label(janela, text=f"{datetime.now().strftime('%H:%M:%S')}", font=("Verdana", 30))
texto_relogio.pack(pady="50")

#Rodar o programa com a janela
relogio()
janela.mainloop()
