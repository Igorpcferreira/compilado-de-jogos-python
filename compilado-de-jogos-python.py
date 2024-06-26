import tkinter as tk
from tkinter import messagebox
import random

class MenuPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Menu Principal")
        self.master.configure(bg="lightblue")
        
        self.label = tk.Label(self.master, text="Escolha um jogo:", bg="lightblue", fg="darkblue", font=("Helvetica", 14, "bold"))
        self.label.pack(pady=10)
        
        self.botao1 = tk.Button(self.master, text="Jogo da Adivinhação", command=self.jogar_jogo_adivinhacao, bg="green", fg="white", font=("Helvetica", 12, "bold"))
        self.botao1.pack(pady=5, ipadx=10, ipady=5)
        
        self.botao2 = tk.Button(self.master, text="Jogo da Forca", command=self.jogar_forca, bg="green", fg="white", font=("Helvetica", 12, "bold"))
        self.botao2.pack(pady=5, ipadx=10, ipady=5)
        
        self.botao3 = tk.Button(self.master, text="Jogo da Velha", command=self.jogar_velha, bg="green", fg="white", font=("Helvetica", 12, "bold"))
        self.botao3.pack(pady=5, ipadx=10, ipady=5)
        
        self.botao4 = tk.Button(self.master, text="Jogo Snake", command=self.jogar_snake, bg="green", fg="white", font=("Helvetica", 12, "bold"))
        self.botao4.pack(pady=5, ipadx=10, ipady=5)
        
        self.master.update_idletasks()
        self.master.geometry(f"{self.master.winfo_reqwidth()}x{self.master.winfo_reqheight()}")  # Ajusta a geometria da janela ao tamanho dos componentes
        
    def jogar_jogo_adivinhacao(self):
        self.iniciar_jogo(JogoAdivinhacao)
        
    def jogar_forca(self):
        self.iniciar_jogo(JogoForca)
        
    def jogar_velha(self):
        self.iniciar_jogo(JogoDaVelha)
        
    def jogar_snake(self):
        self.iniciar_jogo(JogoSnake)
        
    def iniciar_jogo(self, Jogo):
        self.master.withdraw()
        root = tk.Toplevel(self.master)
        jogo = Jogo(root, self.master)
        root.protocol("WM_DELETE_WINDOW", self.voltar_para_menu)
        root.mainloop()
        
    def voltar_para_menu(self):
        self.master.deiconify()


class JogoForca:
    def __init__(self, master, menu_master):
        self.master = master
        self.menu_master = menu_master
        self.master.title("Jogo da Forca")
        self.master.configure(bg="lightblue")
        
        self.palavras = ['python', 'java', 'javascript', 'html', 'css', 'ruby', 'php', 'swift']
        self.palavra_secreta = random.choice(self.palavras)
        self.letras_tentadas = []
        self.max_tentativas = 6
        self.tentativas = 0
        
        self.rotulo_palavra = tk.Label(self.master, text=self.exibir_palavra(), bg="lightblue", fg="darkblue", font=("Helvetica", 14, "bold"))
        self.rotulo_palavra.pack(pady=10)
        
        self.rotulo_tentativas = tk.Label(self.master, text=f"Tentativas restantes: {self.max_tentativas}", bg="lightblue", fg="darkblue")
        self.rotulo_tentativas.pack(pady=5)
        
        self.rotulo_entrada = tk.Label(self.master, text="Tente uma letra:", bg="lightblue", fg="darkblue")
        self.rotulo_entrada.pack(pady=5)
        
        self.entrada = tk.Entry(self.master)
        self.entrada.pack(pady=5)
        
        self.botao_tentar = tk.Button(self.master, text="Tentar", command=self.verificar_letra, bg="green", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_tentar.pack(pady=5, ipadx=10, ipady=5)
        
        self.botao_menu = tk.Button(self.master, text="Voltar para o Menu", command=self.voltar_para_menu, bg="red", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_menu.pack(pady=5, ipadx=10, ipady=5)
        
        self.master.update_idletasks()
        self.master.geometry("")  # Ajusta a geometria da janela ao tamanho dos componentes
        
    def exibir_palavra(self):
        palavra_exibida = ""
        for letra in self.palavra_secreta:
            if letra in self.letras_tentadas:
                palavra_exibida += letra + " "
            else:
                palavra_exibida += "_ "
        return palavra_exibida.strip()
    
    def verificar_letra(self):
        letra = self.entrada.get().lower()
        self.entrada.delete(0, tk.END)
        
        if len(letra) != 1 or not letra.isalpha():
            messagebox.showerror("Entrada Inválida", "Por favor, digite apenas uma letra.")
            return
        
        if letra in self.letras_tentadas:
            messagebox.showwarning("Letra Já Tentada", "Você já tentou essa letra.")
            return
        
        self.letras_tentadas.append(letra)
        if letra not in self.palavra_secreta:
            self.tentativas += 1
            self.rotulo_tentativas.config(text=f"Tentativas restantes: {self.max_tentativas - self.tentativas}")
        
        self.rotulo_palavra.config(text=self.exibir_palavra())
        
        if self.tentativas >= self.max_tentativas:
            messagebox.showinfo("Fim de Jogo", f"Você perdeu! A palavra era '{self.palavra_secreta}'.")
            self.voltar_para_menu()
        elif "_" not in self.exibir_palavra():
            messagebox.showinfo("Parabéns!", "Você venceu!")
            self.voltar_para_menu()
            
    def voltar_para_menu(self):
        self.master.destroy()
        self.menu_master.deiconify()

class JogoAdivinhacao:
    def __init__(self, master, menu_master):
        self.master = master
        self.menu_master = menu_master
        self.master.title("Jogo de Adivinhação")
        self.master.configure(bg="lightblue")
        
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        
        self.rotulo = tk.Label(self.master, text="Digite um número entre 1 e 100:", bg="lightblue", fg="darkblue", font=("Helvetica", 14, "bold"))
        self.rotulo.pack(pady=10)
        
        self.entrada = tk.Entry(self.master)
        self.entrada.pack(pady=5)
        
        self.botao = tk.Button(self.master, text="Adivinhar", command=self.verificar_palpite, bg="green", fg="white", font=("Helvetica", 12, "bold"))
        self.botao.pack(pady=5, ipadx=10, ipady=5)
        
        self.botao_menu = tk.Button(self.master, text="Voltar para o Menu", command=self.voltar_para_menu, bg="red", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_menu.pack(pady=5, ipadx=10, ipady=5)
        
        self.master.update_idletasks()
        self.master.geometry("")  
        
    def verificar_palpite(self):
        palpite = self.entrada.get()
        self.tentativas += 1
        
        try:
            palpite = int(palpite)
            if palpite == self.numero_secreto:
                messagebox.showinfo("Parabéns!", f"Você acertou em {self.tentativas} tentativas!")
                self.voltar_para_menu()
            elif palpite < self.numero_secreto:
                messagebox.showinfo("Tente novamente", "Tente um número maior.")
            else:
                messagebox.showinfo("Tente novamente", "Tente um número menor.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite apenas números.")

    def voltar_para_menu(self):
        self.master.destroy()
        self.menu_master.deiconify()

class JogoDaVelha:
    def __init__(self, master, menu_master):
        self.master = master
        self.menu_master = menu_master
        self.master.title("Jogo da Velha")
        self.master.configure(bg="lightblue")
        
        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(self.master, text="", width=10, height=3, command=lambda i=i, j=j: self.clicar(i, j), bg="green", fg="white", font=("Helvetica", 12, "bold"))
                self.botoes[i][j].grid(row=i, column=j)
                
        self.botao_menu = tk.Button(self.master, text="Voltar para o Menu", command=self.voltar_para_menu, bg="red", fg="white", font=("Helvetica", 12, "bold"))
        self.botao_menu.grid(row=3, columnspan=3, pady=10)
        
        self.master.update_idletasks()
        self.master.geometry("")  
        
    def clicar(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == "":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogador_atual)
            
            if self.verificar_vencedor():
                messagebox.showinfo("Vitória", f"O jogador {self.jogador_atual} venceu!")
                self.reiniciar_tabuleiro()
            elif self.verificar_empate():
                messagebox.showinfo("Empate", "O jogo terminou em empate!")
                self.reiniciar_tabuleiro()
            else:
                self.trocar_jogador()
        
    def trocar_jogador(self):
        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
        
    def verificar_vencedor(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != "":
                return True
        for j in range(3):
            if self.tabuleiro[0][j] == self.tabuleiro[1][j] == self.tabuleiro[2][j] != "":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != "":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != "":
            return True
        return False
    
    def verificar_empate(self):
        for linha in self.tabuleiro:
            for celula in linha:
                if celula == "":
                    return False
        return True
    
    def reiniciar_tabuleiro(self):
        for i in range(3):
            for j in range(3):
                self.tabuleiro[i][j] = ""
                self.botoes[i][j].config(text="")
        self.jogador_atual = "X"
        
    def voltar_para_menu(self):
        self.master.destroy()
        self.menu_master.deiconify()

class JogoSnake:
    def __init__(self, master, menu_master):
        self.master = master
        self.menu_master = menu_master
        self.master.title("Snake Eater")
        self.master.configure(bg="black")
        
        self.canvas = tk.Canvas(self.master, bg="black", width=400, height=400)
        self.canvas.pack()
        
        self.canvas.bind("<KeyPress>", self.mover_cobra)
        self.canvas.focus_set()  
        
        self.tamanho_celula = 20
        self.largura_canvas = 400
        self.altura_canvas = 400
        
        self.cobra = [(100, 100), (80, 100), (60, 100)]
        self.direcao = "Direita"
        
        self.comida = self.criar_comida()
        
        self.velocidade = 100  
        
        self.jogo_ativo = False  
        self.pontos = 0
        
        self.desenhar_cobra()
        self.desenhar_comida()

        # Countdown
        self.countdown_label = tk.Label(self.master, text="", font=("Helvetica", 48), fg="white", bg="black")
        self.countdown_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Inicia o countdown
        self.iniciar_countdown(5)  

    def iniciar_countdown(self, segundos):
        if segundos > 0:
            self.countdown_label.config(text=str(segundos))
            self.master.after(1000, lambda: self.iniciar_countdown(segundos - 1))
        else:
            self.countdown_label.config(text="GO!")
            self.master.after(1000, self.iniciar_jogo)

    def iniciar_jogo(self):
        self.countdown_label.destroy()  
        self.jogo_ativo = True
        self.master.after(self.velocidade, self.atualizar_jogo)
        
    def desenhar_cobra(self):
        self.canvas.delete("cobra")
        for x, y in self.cobra:
            self.canvas.create_rectangle(x, y, x + self.tamanho_celula, y + self.tamanho_celula, fill="green", tag="cobra")
    
    def desenhar_comida(self):
        x, y = self.comida
        self.canvas.create_oval(x, y, x + self.tamanho_celula, y + self.tamanho_celula, fill="red", tag="comida")
    
    def mover_cobra(self, event):
        key = event.keysym
        if key == "Left" and self.direcao != "Direita":
            self.direcao = "Esquerda"
        elif key == "Right" and self.direcao != "Esquerda":
            self.direcao = "Direita"
        elif key == "Up" and self.direcao != "Baixo":
            self.direcao = "Cima"
        elif key == "Down" and self.direcao != "Cima":
            self.direcao = "Baixo"
    
    
    def atualizar_jogo(self):
        if self.jogo_ativo:
            self.mover()
            self.verificar_colisao()
            self.desenhar_cobra()
            
            if self.verificar_comida():
                self.pontos += 10
                self.master.title(f"Snake Eater - Pontos: {self.pontos}")
                self.canvas.delete("comida")  # Adicione essa linha
                self.comida = self.criar_comida()
                self.desenhar_comida()
            
            self.master.after(self.velocidade, self.atualizar_jogo)
        else:
            messagebox.showinfo("Fim de Jogo", f"Você perdeu! Pontuação: {self.pontos}")
            self.voltar_para_menu()
    
    def mover(self):
        cabeca_x, cabeca_y = self.cobra[0]
        
        if self.direcao == "Direita":
            nova_cabeca = (cabeca_x + self.tamanho_celula, cabeca_y)
        elif self.direcao == "Esquerda":
            nova_cabeca = (cabeca_x - self.tamanho_celula, cabeca_y)
        elif self.direcao == "Cima":
            nova_cabeca = (cabeca_x, cabeca_y - self.tamanho_celula)
        elif self.direcao == "Baixo":
            nova_cabeca = (cabeca_x, cabeca_y + self.tamanho_celula)
        
        self.cobra.insert(0, nova_cabeca)
        if not self.verificar_comida_atingida():
            self.cobra.pop()
    
    def verificar_colisao(self):
        cabeca_x, cabeca_y = self.cobra[0]
        
        if cabeca_x < 0 or cabeca_x >= self.largura_canvas or cabeca_y < 0 or cabeca_y >= self.altura_canvas:
            self.jogo_ativo = False
        
        for segmento in self.cobra[1:]:
            if cabeca_x == segmento[0] and cabeca_y == segmento[1]:
                self.jogo_ativo = False
    
    def verificar_comida(self):
        cabeca_x, cabeca_y = self.cobra[0]
        comida_x, comida_y = self.comida
        return cabeca_x == comida_x and cabeca_y == comida_y
    
    def verificar_comida_atingida(self):
        cabeca_x, cabeca_y = self.cobra[0]
        comida_x, comida_y = self.comida
        return cabeca_x == comida_x and cabeca_y == comida_y
    
    def criar_comida(self):
        comida_x = random.randint(0, (self.largura_canvas - self.tamanho_celula) // self.tamanho_celula) * self.tamanho_celula
        comida_y = random.randint(0, (self.altura_canvas - self.tamanho_celula) // self.tamanho_celula) * self.tamanho_celula
        return comida_x, comida_y
    
    def voltar_para_menu(self):
        self.master.destroy()
        self.menu_master.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    menu = MenuPrincipal(root)
    root.mainloop()
