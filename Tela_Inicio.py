import tkinter as tk
from tkinter import messagebox

class ExpandableMenu:
    def __init__(self, root):
        self.root = root
        self.is_expanded = False
        self.menu_width_expanded = 250
        self.menu_width_collapsed = 50
        self.create_menu()

    def create_menu(self):
        # Frame principal do menu
        self.menu_frame = tk.Frame(self.root, width=self.menu_width_collapsed, bg='#2c3e50')
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.menu_frame.pack_propagate(False)

        # Botão de toggle (hamburger menu)
        self.toggle_button = tk.Button(
            self.menu_frame,
            text="☰",
            command=self.toggle_menu,
            bg='#34495e',
            fg='white',
            font=("Arial", 16),
            relief='flat',
            bd=0,
            cursor='hand2'
        )
        self.toggle_button.pack(pady=20, padx=5, fill=tk.X)

        # Container para os botões do menu (inicialmente vazio)
        self.menu_content_frame = tk.Frame(self.menu_frame, bg='#2c3e50')

        # Lista de itens do menu
        self.menu_items = [
            ("🏠", "Início", self.show_home),
            ("📅", "Agenda", self.show_agenda),
            ("📚", "Atividades", self.show_activities),
            ("📊", "Notas", self.show_grades),
            ("💬", "Chat", self.show_chat),
            ("⚙️", "Config", self.show_settings)
        ]

        # Criar botões do menu (inicialmente escondidos)
        self.create_menu_buttons()

    def create_menu_buttons(self):
        for icon, text, command in self.menu_items:
            # Frame para cada botão
            btn_frame = tk.Frame(self.menu_content_frame, bg='#2c3e50', height=45)
            btn_frame.pack(fill=tk.X, pady=2)
            btn_frame.pack_propagate(False)

            # Botão do menu
            btn = tk.Button(
                btn_frame,
                text=f" {icon}",
                command=command,
                bg='#2c3e50',
                fg='white',
                font=("Arial", 14),
                anchor='w',
                relief='flat',
                bd=0,
                width=3
            )
            btn.pack(side=tk.LEFT, fill=tk.Y)

            # Label com texto (inicialmente escondido)
            text_label = tk.Label(
                btn_frame,
                text=text,
                bg='#2c3e50',
                fg='white',
                font=("Arial", 11),
                anchor='w'
            )

            # Armazenar referências
            btn.text_label = text_label
            btn.icon_text = f" {icon}  {text}"
            btn.normal_text = f" {icon}"

            # Efeitos hover
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover_enter(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_hover_leave(b))

    def toggle_menu(self):
        if self.is_expanded:
            self.collapse_menu()
        else:
            self.expand_menu()
        self.is_expanded = not self.is_expanded

    def expand_menu(self):
        # Expandir o frame
        self.menu_frame.config(width=self.menu_width_expanded)

        # Mostrar conteúdo do menu
        self.menu_content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 20))

        # Atualizar textos dos botões
        for widget in self.menu_content_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Button):
                        child.config(text=child.icon_text, width=20, anchor='w')
                    elif isinstance(child, tk.Label):
                        child.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Atualizar botão toggle
        self.toggle_button.config(text="Fercha")

    def collapse_menu(self):
        # Recolher o frame
        self.menu_frame.config(width=self.menu_width_collapsed)

        # Esconder conteúdo do menu
        self.menu_content_frame.pack_forget()

        # Restaurar textos dos botões
        for widget in self.menu_content_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Button):
                        child.config(text=child.normal_text, width=3, anchor='center')
                    elif isinstance(child, tk.Label):
                        child.pack_forget()

        # Atualizar botão toggle
        self.toggle_button.config(text="☰")

    def on_hover_enter(self, button):
        button.config(bg='#34495e')

    def on_hover_leave(self, button):
        button.config(bg='#2c3e50')

    # Métodos de exemplo para os botões
    def show_home(self):
        messagebox.showinfo("Menu", "Página Inicial")

    def show_agenda(self):
        messagebox.showinfo("Menu", "Agenda")

    def show_activities(self):
        messagebox.showinfo("Menu", "Atividades")

    def show_grades(self):
        messagebox.showinfo("Menu", "Notas")

    def show_chat(self):
        messagebox.showinfo("Menu", "Chat")

    def show_settings(self):
        messagebox.showinfo("Menu", "Configurações")

# Exemplo de uso com interface completa
class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu Expansível")
        self.root.geometry("900x600")
        self.root.configure(bg='#ecf0f1')

        self.setup_ui()

    def setup_ui(self):
        # Criar menu expansível
        self.menu = ExpandableMenu(self.root)

        # Frame de conteúdo principal
        self.content_frame = tk.Frame(self.root, bg='white')
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Conteúdo exemplo
        self.create_content()

    def create_content(self):
        # Título
        frame = tk.Label(
            self.content_frame,
            text="EducaMais+",
            font=("Arial", 24, "bold"),
            bg='white',
            fg='#2c3e50'
        )
        frame.pack(pady=50)


# Executar aplicação
if __name__ == "__main__":
    app = Application()
    app.root.mainloop()
