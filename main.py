import customtkinter as ctk
import tkinter as tk
import webbrowser as wb
import pyautogui as pt
import time

class EscreverRedação():
    def __init__(self, master):
        super().__init__()
        time.sleep(1)
        pt.keyDown("alt")
        pt.press("tab")
        pt.keyUp("alt")
        time.sleep(0.5)
        pt.click(master.coord_x, master.coord_y)
        time.sleep(0.2)
        pt.write(master.textbox.textbox.get("0.0", "end-1c"), interval=0.01)

class LocalParaPorTexto(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.textbox = ctk.CTkTextbox(
            self,
            width=500,
            height=300, 
        )
        self.textbox.insert("0.0","Digite sua redação aqui... (Apague isso antes de escrever.)")
        self.textbox.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

class PegarMira(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.largura = 300
        self.altura = 300

        self.title("Posicionar Mira")
        self.geometry(f"{self.largura}x{self.altura}")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.wm_attributes("-alpha", 0.85)

        # Centraliza em relação à janela principal
        master.update_idletasks()
        x = master.winfo_x() + (master.winfo_width() // 2) - (self.largura // 2)
        y = master.winfo_y() + (master.winfo_height() // 2) - (self.altura // 2)
        self.geometry(f"{self.largura}x{self.altura}+{x}+{y}")

        # Canvas (Tkinter puro funciona melhor pra desenho)
        self.canvas = tk.Canvas(
            self,
            width=self.largura,
            height=self.altura,
            bg="#1e1e1e",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        # Centro
        self.cx = self.largura // 2
        self.cy = self.altura // 2

        # Desenha o X
        self.canvas.create_line(
            self.cx - 25, self.cy,
            self.cx + 25, self.cy,
            fill="red", width=2
        )
        self.canvas.create_line(
            self.cx, self.cy - 25,
            self.cx, self.cy + 25,
            fill="red", width=2
        )
        self.canvas.create_oval(
            self.cx - 6, self.cy - 6,
            self.cx + 6, self.cy + 6,
            outline="red", width=2
        )

        # Botão confirmar
        self.btn_confirmar = ctk.CTkButton(
            self,
            text="CONFIRMAR",
            command=self.confirmar
        )
        self.btn_confirmar.place(relx=0.5, rely=0.9, anchor="center")

    def confirmar(self):
        # Coordenadas reais da tela
        self.master.coord_x = self.winfo_rootx() + self.cx
        self.master.coord_y = self.winfo_rooty() + self.cy

        print(
            f"Coordenadas salvas: "
            f"X={self.master.coord_x}, "
            f"Y={self.master.coord_y}"
        )

        self.destroy()


class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.btn_open_Gpt = ctk.CTkButton(self, text="Abrir ChatGPT", command=lambda: wb.open("https://chat.openai.com"))
        self.btn_open_Gpt.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.btn_open_quilbo = ctk.CTkButton(self, text="Abrir QuillBot", command=lambda: wb.open("https://quillbot.com"))
        self.btn_open_quilbo.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.btn_Selecionar_local = ctk.CTkButton(
            self,
            text="local de digitação",
            command=self.abrir_mira
        )
        self.btn_Selecionar_local.grid(
            row=2, column=0, padx=10, pady=(10, 0), sticky="w"
        )

        self.btn_Escrever = ctk.CTkButton(
            self,
            text="Escrever Redação",
            command=lambda: EscreverRedação(self.master)
        )
        self.btn_Escrever.grid(
            row=3, column=0, padx=10, pady=(10, 10), sticky="w"
        )

    def abrir_mira(self):
        PegarMira(self.master)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bot de Redação")
        self.geometry("700x325")
        self.resizable(False, False)
        self._set_appearance_mode("system")

        # Coordenadas globais do app
        self.coord_x = None
        self.coord_y = None

        self.grid_columnconfigure(0, weight=1)

        self.button_frame = ButtonFrame(self)
        self.button_frame.grid(
            row=0, column=0, padx=10, pady=(10, 0), sticky="nsw"
        )
        self.textbox = LocalParaPorTexto(self)
        self.textbox.grid(
            row=0, column=1, padx=10, pady=(10, 0), sticky="nsw"
        )


app = App()
app.mainloop()
