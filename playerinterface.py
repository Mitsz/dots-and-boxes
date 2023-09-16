from tkinter import *

class PlayerInterface():
    def __init__(self):
        self.main_window = Tk()
        self.fill_main_window()
        self.main_window.mainloop()


    def fill_main_window(self):
        self.main_window.title("Jogo dos Pontinhos")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(False, False)
        self.main_window["bg"] = "#282828"

        self.logo = PhotoImage(file="img/logo.png")

        # Criação do Menu
        self.menubar = Menu(self.main_window)
        self.menubar.option_add('*tearOff', 0)
        self.main_window['menu'] = self.menubar

        # Adicionar menu(s) à barra de menu:
        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label='Help')

        # Frame da esquerda
        self.left_frame = Frame(self.main_window, pady=10, bg="#282828")
        self.left_frame.pack(side="left")

        self.logo_label = Label(self.left_frame, bd=0, image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.jogador_label = Label(self.left_frame, 
                                   bd=0, 
                                   text="VEZ DO JOGADOR 1", 
                                   bg="#282828", 
                                   font=("comic sans", 30),
                                   pady=50, padx=50)
        self.jogador_label.grid(row=1, column=0)

        self.pontuacao_label = Label(self.left_frame, 
                                   bd=0, 
                                   text="PONTUAÇÃO:\n\nJOGADOR 1 = x\nJOGADOR 2 = y", 
                                   bg="#282828", 
                                   font=("comic sans", 30),
                                   pady=50)
        self.pontuacao_label.grid(row=2, column=0)


        # Frame do tabuleiro
        self.board_frame = Frame(self.main_window, padx=20, pady=10, bg="#282828")
        self.board_frame.pack(side="left")
        # Gerando o tabuleiro
        self.create_board(self.board_frame)

    # Função para criar o tabuleiro de "Dots and Boxes"
    def create_board(self, board_frame):
        rows = 7
        cols = 7
        cell_size = 100  # Tamanho do espaço entre cada ponto
        off_set = 50

        self.board = Canvas(board_frame, width=700, height=700, bg="#282828")
        self.board.pack()

        # Desenhar os pontos
        for row in range(rows):
            for col in range(cols):
                x = col * cell_size + off_set
                y = row * cell_size + off_set
                self.board.bind("<Button-1>", lambda event: self.click(event))
                self.board.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")  
                
    def click(self, event):
        print('CLICK')

