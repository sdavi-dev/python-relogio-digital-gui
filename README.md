# Projeto iniciante de um relógio digital utilizando o Tkinter no python para criação de GUIs
## Linguagem de programação
- Python

## Bibliotecas utilizadas
- tkinter
- datetime

## Funções do tkinter
```python
janela = tk.Tk()
janela.title("Projeto de Relógio Digital")
janela.geometry("300x200")

texto_relogio = tk.Label(janela, text=f"{datetime.now().strftime('%H:%M:%S')}", font=("Verdana", 30))
texto_relogio.pack(pady="50")
janela.mainloop()
```

- tk.Tk() : Inicializa a janela
- janela.title : Define um título para a janela
- janela.geometry : Define o tamanho da janela
- tk.Label : Insere um texto na janela (nesse caso servirá para apresentar o relógio na tela)
- texto_relogio.pack() : empacota os elementos um embaixo do outro (ou um ao lado do outro, se configurado).
- pady : Define a posição vertical.
- janela.mainloop() : Rodar o programa

# Função relogio()
Essa função é responsável pelo relógio.
```python
def relogio():

    texto_relogio.config(text=datetime.now().strftime("%H:%M:%S"))
    janela.after(1000, relogio)

```

- texto_relogio.config: Atualiza o texto do visor.
- janela.after(1000, relogio): Chama a função novamente a cada 1000 milissegundos (1 segundo).
