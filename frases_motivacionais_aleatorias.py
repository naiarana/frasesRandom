import random
import tkinter as tk
import this
import codecs



def RandomFrases():
    frases = ["Persista, mesmo quando parecer difícil, pois é nas dificuldades que encontramos nossa força interior.",
    "Cada novo dia é uma oportunidade para recomeçar e fazer melhor.",
    "Acredite no seu potencial e nada será impossível de alcançar.",
    "Pequenos passos podem levar a grandes conquistas, então siga em frente, um passo de cada vez.",
    "Seja a mudança que você deseja ver no mundo, comece por você mesmo.",
    "Não espere por circunstâncias ideais; crie-as. A mudança começa dentro de você.",
    "Os obstáculos são apenas degraus para o sucesso. Suba-os com determinação e fé.",
    "O segredo do progresso é começar, então não espere, faça acontecer agora.",
    "Nunca duvide da sua capacidade de superar desafios. Você é mais forte do que imagina.",
    "O único limite que existe está na sua mente. Liberte-se e alcance o impossível."]

    rdm = random.randrange(0,len(frases))
    label.config(text= frases[rdm],bg="black",width=30,height=5,fg="white", wraplength=200)
   
   
# # Função para sair
def close_window():
    janela.destroy()
    
# Criar uma janela
janela = tk.Tk()
janela.title("FRASES MOTIVACIONAIS")
#janela.grid()

## Criar uma label
label = tk.Label(janela, text="Frases",bg="#48b8d8",width=5,height=2,fg="#f42aea")
label.grid(column=1,row=2,padx=5, pady=5)


# Criar o botão para mudar texto
mudar_button = tk.Button(janela, text="FRASE SURPRESA!", command=RandomFrases, fg="#8A2BE2", width=30)
mudar_button.grid(column=1,row=4,padx=5, pady=5)


# # Criar o botão de fechar janela
close_button = tk.Button(janela, text="FECHAR", command= close_window, fg="red",width=30)
close_button.grid(column=1,row=6,padx=5, pady=5)

# # Executar em loop
janela.mainloop()