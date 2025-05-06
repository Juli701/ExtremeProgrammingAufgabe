'''
Extreme Programming Aufgabe
FSST-Labor
Zahlenraten-Gui
Julian Lengauer & Manuel Margreiter
'''

import customtkinter as ctk
import random
from tkinter import Menu
import CTkMessagebox


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class NumberGuessApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Zahlenraten")
        self.geometry("400x230")

        self.random_number = random.randint(0, 100)

        menu_bar = Menu(self)

        game_menu = Menu(menu_bar, tearoff=0)
        game_menu.add_command(label="Neues Spiel", command = self.reset_game)
        game_menu.add_separator()
        game_menu.add_command(label="Beenden", command=self.quit)
        menu_bar.add_cascade(label="Spiel", menu=game_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="So wird gespielt", command=self.show_info)
        menu_bar.add_cascade(label="Hilfe", menu=help_menu)

        self.config(menu=menu_bar)


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.title_text = ctk.CTkLabel(self, text="Zahlenraten-Spiel", font=("Arial", 25))
        self.title_text.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="nsew")

        self.label_info = ctk.CTkLabel(self, text="Gib eine Zahl zwischen 0 und 100 ein!")
        self.label_info.grid(row=1, column=0, columnspan=2, pady=5)

        self.entry = ctk.CTkEntry(self, placeholder_text="Deine Zahl hier")
        self.entry.grid(row=2, column=0, columnspan=2, pady=5, padx=20, sticky="nsew")

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)

        self.button = ctk.CTkButton(self, text="Raten", command=self.check_guess)
        self.button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")


    def ask_player_new_game(self):
        self.msg = CTkMessagebox.CTkMessagebox(title="Info", message="Nochmal spielen?", corner_radius=3,
                                               option_1="Ja", option_2="Nein", icon="question")
        self.response = self.msg.get()

        if self.response == "Ja":
            self.reset_game()

        elif self.response == "Nein":
            self.quit()

    def check_guess(self):
        try:
            self.guess = int(self.entry.get())
            if self.guess < 0 or self.guess > 100:
                self.result_label.configure(text="Bitte gib eine Zahl von 0 bis 100 ein!")
            elif self.guess < self.random_number:
                self.result_label.configure(text="Zahl ist zu klein!")
            elif self.guess > self.random_number:
                self.result_label.configure(text="Zahl ist zu groß!")
            else:
                self.result_label.configure(text="Richtig geraten!")
                self.ask_player_new_game()
        except ValueError:
            self.result_label.configure(text="Bitte gib eine gültige Zahl ein!")

    def reset_game(self):
        self.random_number = random.randint(0,100)
        self.entry.delete(0,"end")
        self.result_label.configure(text="")

    def show_info(self):
        CTkMessagebox.CTkMessagebox(title="Hilfe", message="Der User soll eine Zahl von 0-100 raten."
                                                           "Wenn die Zahl richtig eingegeben wurde, hat der User gewonnen."
                                    ,corner_radius=3)




if __name__ == "__main__":
    app = NumberGuessApp()
    app.mainloop()
