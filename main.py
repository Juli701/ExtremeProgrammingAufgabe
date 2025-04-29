'''
Extreme Programming Aufgabe
FSST-Labor
Zahlenraten-Gui
'''

import customtkinter as ctk
import random

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class NumberGuessApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Zahlenraten")
        self.geometry("400x300")

        self.random_number = random.randint(0, 100)

        self.label_info = ctk.CTkLabel(self, text="Rate eine Zahl zwischen 0 und 100")
        self.label_info.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="Deine Zahl hier")
        self.entry.pack(pady=10)

        self.button = ctk.CTkButton(self, text="Raten")
        self.button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=10)

        self.reset_button = ctk.CTkButton(self, text="Neues Spiel")
        self.reset_button.pack(pady=10)


if __name__ == "__main__":
    app = NumberGuessApp()
    app.mainloop()